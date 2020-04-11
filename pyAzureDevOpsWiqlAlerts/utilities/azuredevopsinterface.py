#! python3
from msrest.authentication import BasicAuthentication
from azure.devops.connection import Connection
from azure.devops.v6_0.work_item_tracking.models import Wiql


class AzureDevopsInterface:

    def __init__(self, uri: str, personal_access_token: str) -> None:
        print(f'azure_devops_interface constructor called with uri={uri} and PAT={personal_access_token}')
        self._uri = uri
        self._personal_access_token = personal_access_token
        self._credentials = BasicAuthentication('', self._personal_access_token)
        self._connection = Connection(base_url=self._uri, creds=self._credentials)
        self._azure_devops_client = \
            self._connection.clients_v6_0.get_work_item_tracking_client()

    def get_azure_devops_work_items_from_query_id(self, query_id: str) -> []:
        query_result = self._azure_devops_client.query_by_id(id=query_id)
        return self.map_work_item_references_to_dtos(query_result)

    def get_azure_devops_work_items_from_wiql_query(self, wiql_query: str) -> []:
        query_wiql = Wiql(query=wiql_query)
        query_result = self._azure_devops_client.query_wiql(query_wiql).work_items
        return self.map_work_item_references_to_dtos(query_result)

    def map_work_item_references_to_dtos(self, query_result: []) -> []:
        if not query_result.work_items:
            return None

        print(f'Mapping {str(len(query_result.work_items))} items.')

        fields = []
        if query_result.columns:
            for field_ref in query_result.columns:
                fields.append(field_ref.reference_name)

        work_item_ids = []
        for work_item_ref in query_result.work_items:
            work_item_ids.append(work_item_ref.id)

        # for work_item_ref in query_result.work_items:
        work_items = self._azure_devops_client.get_work_items(ids=work_item_ids, as_of=query_result.as_of,
                                                              fields=fields)

        return work_items

        #         List<AzureDevOpsWorkItemDto> results = new List<AzureDevOpsWorkItemDto>();

        # //create instance of work item tracking http client
        # using (WorkItemTrackingHttpClient workItemTrackingHttpClient = new WorkItemTrackingHttpClient(_uri, _credentials))
        # {
        #     //execute the query to get the list of work items in the results 
        #     WorkItemQueryResult workItemQueryResult = workItemTrackingHttpClient.QueryByWiqlAsync(wiql).Result;

        #     _log.Info($"Found {workItemQueryResult.WorkItems.Count()} items.");

        #     //some error handling                
        #     if (workItemQueryResult.WorkItems.Count() != 0)
        #     {
        #         //need to get the list of our work item ids and put them into an array
        #         List<int> list = new List<int>();
        #         foreach (var item in workItemQueryResult.WorkItems)
        #         {
        #             list.Add(item.Id);
        #         }
        #         int[] arr = list.ToArray();

        #         //build a list of the fields we want to see
        #         var fields = new List<string>
        #         {
        #             "System.Id",
        #             "System.Title",
        #             "System.State",
        #             "RCA Summary",
        #             "System.History",
        #             "System.Reason",
        #             "System.AssignedTo",
        #             "System.AreaLevel2",
        #             "System.AreaPath",
        #             "System.CreatedDate", // Dates come down as UTC.
        #             "System.ChangedDate",
        #             "Microsoft.VSTS.Common.StateChangeDate",
        #             "Liazon.ProductLead",
        #             "Liazon.SeniorProductManager",
        #             "Liazon.ProjectManager"
        #         };

        #         //get work items for the ids found in query
        #         var workItems = await workItemTrackingHttpClient.GetWorkItemsAsync(arr, fields.ToArray(), workItemQueryResult.AsOf);

        #         // Map DTOs. Magic strings come from WIQL, easiest way to find them is: https://liazon.visualstudio.com/BrightChoices/_apps/hub/ottostreifel.wiql-editor.wiql-playground-hub
        #         foreach (var workItem in workItems)
        #         {
        #             _log.Info("Mapping WorkItem...");

        #             var impedimentDto = new AzureDevOpsWorkItemDto();
        #             impedimentDto.Id = workItem.Id.Value;
        #             impedimentDto.Title = workItem.Fields["System.Title"].ToString();

        #             if (workItem.Fields.ContainsKey("System.CreatedDate"))
        #             {
        #                 impedimentDto.CreatedDate = DateTime.Parse(workItem.Fields["System.CreatedDate"].ToString());
        #             }

        #             if (workItem.Fields.ContainsKey("System.State"))
        #             {
        #                 impedimentDto.State = workItem.Fields["System.State"].ToString();
        #             }

        #             if (workItem.Fields.ContainsKey("System.ChangedDate"))
        #             {
        #                 impedimentDto.LastChangedDate = DateTime.Parse(workItem.Fields["System.ChangedDate"].ToString());
        #             }

        #             if(workItem.Fields.ContainsKey("Microsoft.VSTS.Common.StateChangeDate"))
        #             {
        #                 impedimentDto.StateChangedDate = DateTime.Parse(workItem.Fields["Microsoft.VSTS.Common.StateChangeDate"].ToString());
        #             }

        #             if (workItem.Fields.ContainsKey("RCA Summary"))
        #             {
        #                 impedimentDto.RCA = workItem.Fields["RCA Summary"].ToString();
        #             }

        #             if (workItem.Fields.ContainsKey("System.Reason"))
        #             {
        #                 impedimentDto.Reason = workItem.Fields["System.Reason"].ToString();
        #             }

        #             if (workItem.Fields.ContainsKey("System.History"))
        #             {
        #                 impedimentDto.DiscussionHistory = workItem.Fields["System.History"].ToString();
        #             }

        #             if (workItem.Fields.ContainsKey("System.AssignedTo"))
        #             {
        #                 impedimentDto.AssignedTo = workItem.Fields["System.AssignedTo"].ToString();
        #             }

        #             if (workItem.Fields.ContainsKey("System.AreaLevel2"))
        #             {
        #                 impedimentDto.TeamName = workItem.Fields["System.AreaLevel2"].ToString().ToLower() == "brightchoices"
        #                     ? "Unassigned"
        #                     : workItem.Fields["System.AreaLevel2"].ToString();
        #             }

        #             if (workItem.Fields.ContainsKey("System.AreaPath"))
        #             {
        #                 impedimentDto.TeamName = workItem.Fields["System.AreaPath"].ToString().ToLower() == "brightchoices"
        #                     ? "Unassigned"
        #                     : workItem.Fields["System.AreaPath"].ToString();
        #             }

        #             if (workItem.Fields.ContainsKey("Liazon.ProductLead"))
        #             {
        #                 impedimentDto.ProductManager = string.IsNullOrEmpty(workItem.Fields["Liazon.ProductLead"].ToString())
        #                     ? "Unassigned"
        #                     : workItem.Fields["Liazon.ProductLead"].ToString().Substring(0, workItem.Fields["Liazon.ProductLead"].ToString().IndexOf("<") - 1);
        #             }

        #             if (workItem.Fields.ContainsKey("Liazon.SeniorProductManager"))
        #             {
        #                 impedimentDto.SeniorProductManager = string.IsNullOrEmpty(workItem.Fields["Liazon.SeniorProductManager"].ToString())
        #                     ? "Unassigned"
        #                     : workItem.Fields["Liazon.SeniorProductManager"].ToString().Substring(0, workItem.Fields["Liazon.SeniorProductManager"].ToString().IndexOf("<") - 1);
        #             }

        #             if (workItem.Fields.ContainsKey("Liazon.ProjectManager"))
        #             {
        #                 impedimentDto.LeadProjectManager = string.IsNullOrEmpty(workItem.Fields["Liazon.ProjectManager"].ToString())
        #                     ? "Unassigned"
        #                     : workItem.Fields["Liazon.ProjectManager"].ToString().Substring(0, workItem.Fields["Liazon.ProjectManager"].ToString().IndexOf("<") - 1);
        #             }

        #             results.Add(impedimentDto);

        #             _log.Info("... mapped WorkItem");
        #         }

        #         return results;
        #     }

        #     return new List<AzureDevOpsWorkItemDto>();
        # }
