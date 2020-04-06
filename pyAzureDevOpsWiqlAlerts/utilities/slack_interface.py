#! python3
import slack

class slack_interface:

    def __init__ (self, slack_api_uri):
        self._slack_api_uri = slack_api_uri
        self._client = slack.WebClient(token=self._slack_api_uri)
        pass

    def send_message(self, message, attachments, channel):
        self._client.chat_postMessage(channel=channel, text=message)
            # // If there are any announcement messages to print, do so here in italics. These are pulled from the 
            # //   ADDITIONAL_ANNOUCNEMENT_MESSAGE_TO_DISPLAY_PER_MESSAGE app setting in Azure Portal.
            # if (!string.IsNullOrEmpty(_additionalAnnouncementMessageToDisplayPerMessage))
            # {
            #     message += $"\n_{_additionalAnnouncementMessageToDisplayPerMessage}_";
            # }
            # else
            # {
            #     _log.Info("Failed to append announcement message");
            # }

            # var payload = new
            # {
            #     text = message,
            #     attachments,
            #     channel,
            #     _userName,
            # };

            # var serializedPayload = JsonConvert.SerializeObject(payload);
            # var response = await _httpClient.PostAsync(_webhookUrl, new StringContent(serializedPayload, Encoding.UTF8, "application/json"));

            # return response;

        pass

    def replace_html_with_markdown(self, str):

        str.replace('<div>', '')
        str.replace('</div>', '')
        str.replace('<div/>', '')

            #         //regex: \[(.*?)\]+\((.*?)\)
            # Regex vstsLinkRegex = new Regex(@"\[(.*?)\]+\((.*?)\)");
            # var matches = vstsLinkRegex.Matches(str);

            # while (matches.Count > 0)
            # {
            #     var match = matches[0];
            #     var occurrence = str.Substring(match.Index, match.Length);

            #     //  content within the brackets is the url text
            #     var bracketsMatch = Regex.Match(occurrence, @"\[(.*?)\]");

            #     // content within the parens is the actual url
            #     var parensMatch = Regex.Match(occurrence, @"\((.*?)\)");

            #     // offset by 1 on both sides to drop the actual brackets.
            #     var linkText = occurrence.Substring(bracketsMatch.Index + 1, bracketsMatch.Length - 2);
            #     var linkUrl = occurrence.Substring(parensMatch.Index + 1, parensMatch.Length - 2);

            #     var slackFormattedLink = GetSlackFormattedLink(linkText, linkUrl);

            #     str = str.Replace(match.Value, slackFormattedLink);

            #     matches = vstsLinkRegex.Matches(str);
            # }

            # return str;

        return str
    
    def get_link_from_work_item_id(self, base_url, id):
        pass

    def get_slack_formatted_link(self, url, text):
        pass

