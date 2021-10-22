from TrainRequest import *
from TestRequest import *


class Get_Norification():

    def __init__(self):

        pass

    def __update_notification(self, update_all_notifications_data: dict):

        """
        Handle the short polling response data and call corresponding functions

        Parameters:
         update_all_notifications_data - Dictionary.

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """

        unread_request_notification = update_all_notifications_data["unread request"]
        unread_match_id_notification = update_all_notifications_data["unread match id"]
        unread_situation_notification = update_all_notifications_data["unread situation"]
        unread_output_notification = update_all_notifications_data["unread output"]

        unread_test_request_notification = update_all_notifications_data["unread test request"]
        unread_test_match_id_notification = update_all_notifications_data["unread test match id"]
        unread_test_output_notification = update_all_notifications_data["unread test output"]

        console.log("unread_request_notification", unread_request_notification,
                    unread_request_notification["check_dict"])
        console.log("unread_match_id_notification", unread_match_id_notification,
                    unread_match_id_notification["check_dict"])
        console.log("unread_situation_notification", unread_situation_notification,
                    unread_situation_notification["check_dict"])
        console.log("unread_output_notification", unread_output_notification,
                    unread_output_notification["check_dict"])

        console.log("unread_test_request_notification", unread_test_request_notification,
                    unread_test_request_notification["check_dict"])
        console.log("unread_test_match_id_notification", unread_test_match_id_notification,
                    unread_test_match_id_notification["check_dict"])
        console.log("unread_test_output_notification", unread_test_output_notification,
                    unread_test_output_notification["check_dict"])

        if unread_request_notification["check_dict"]:
            unread_request(unread_request_notification)

        if unread_match_id_notification["check_dict"]:
            unread_match_id(unread_match_id_notification)

        if unread_situation_notification["check_dict"]:
            unread_situation(unread_situation_notification)

        if unread_output_notification["rounds_dict"]:
            unread_output(unread_output_notification)

        if unread_test_request_notification["check_dict"]:
            unread_test_request(unread_test_request_notification)

        if unread_test_match_id_notification["check_dict"]:
            unread_test_match_id(unread_test_match_id_notification)

        if unread_test_output_notification["check_dict"]
            unread_test_output(unread_test_output_notification)

        return


    def getNotification(self):

        """
        Short Polling for new Notifications

        Parameters:
         None

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """

        user_id = self.PersonalInformation_instance.get_user_id()
        url = self.base_url + "/users/" + user_id + "/notifications/"
        token = self.Network_instance.get_token()

        short_polling_res = requests.get(url, headers={'Authorization': 'Bearer ' + token})
        print("short_polling_res", short_polling_res)

        response_data = json.loads(short_polling_res.text)
        if len(response_data) >= 1:
            url = self.base_url + "update_all_notifications"
            data = {
                "response_data": response_data
            }
            update_all_notifications_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
            print("update_all_notifications", update_all_notifications)
            update_all_notifications_data = json.loads(update_all_notifications.text)
            self.__update_notification(update_all_notifications_data)


        return