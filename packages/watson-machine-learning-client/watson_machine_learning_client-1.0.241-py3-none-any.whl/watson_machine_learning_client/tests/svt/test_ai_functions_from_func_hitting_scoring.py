import unittest

from watson_machine_learning_client.log_util import get_logger
from preparation_and_cleaning import *
from models_preparation import *


class TestAIFunction(unittest.TestCase):
    runtime_uid = None
    deployment_uid = None
    function_uid = None
    scoring_url = None
    logger = get_logger(__name__)

    @classmethod
    def setUpClass(self):
        TestAIFunction.logger.info("Service Instance: setting up credentials")

        self.wml_credentials = get_wml_credentials()
        self.client = get_client()

        self.function_name = 'simplest AI function'
        self.deployment_name = "Test deployment"

    def test_01_service_instance_details(self):
        TestAIFunction.logger.info("Check client ...")
        self.assertTrue(self.client.__class__.__name__ == 'WatsonMachineLearningAPIClient')

        TestAIFunction.logger.info("Getting instance details ...")
        details = self.client.service_instance.get_details()
        TestAIFunction.logger.debug(details)

        self.assertTrue("published_models" in str(details))
        self.assertEqual(type(details), dict)

    def test_02_create_ai_function(self):

        self.client.repository.FunctionMetaNames.show()

        meta = {
            self.client._runtimes.ConfigurationMetaNames.NAME: "runtime_spec_python_3.5",
            self.client._runtimes.ConfigurationMetaNames.DESCRIPTION: "runtime spec created for custom libraries",
            self.client._runtimes.ConfigurationMetaNames.PLATFORM: {
                "name": "python",
                "version": "3.5"
            }
        }
        runtime_details = self.client._runtimes.create(meta)
        TestAIFunction.runtime_uid = self.client._runtimes.get_uid(runtime_details)
        runtime_url = self.client._runtimes.get_url(runtime_details)

        function_props = {
            self.client.repository.FunctionMetaNames.NAME: 'simplest AI function',
            self.client.repository.FunctionMetaNames.TYPE: 'python',
            self.client.repository.FunctionMetaNames.DESCRIPTION: 'desc',
            self.client.repository.FunctionMetaNames.RUNTIME_URL: runtime_url,
            self.client.repository.FunctionMetaNames.TAGS: [{"value": "ProjectA", "description": "Functions created for ProjectA"}],
            self.client.repository.FunctionMetaNames.INPUT_DATA_SCHEMA: {
              "type": "struct",
              "fields": [
                {
                  "name": "x",
                  "type": "double",
                  "nullable": False,
                  "metadata": {}
                },
                {
                  "name": "y",
                  "type": "double",
                  "nullable": False,
                  "metadata": {}
                }
              ]
            },
            self.client.repository.FunctionMetaNames.OUTPUT_DATA_SCHEMA: {
              "type": "struct",
              "fields": [
                {
                  "name": "multiplication",
                  "type": "double",
                  "nullable": False,
                  "metadata": {}
                }
              ]
            }
        }

        def score(payload):
            """AI function with model version.

            Example:
              {"fields": ["ID", "Gender", "Status", "Children", "Age", "Customer_Status", "Car_Owner", "Customer_Service"],
               "values": [[2624, 'Male', 'S', 0, 49.27, 'Active', 'No', "Good experience with all the rental co.'s I contacted. I Just called with rental dates and received pricing and selected rental co.", 1]]}
            """
            from watson_machine_learning_client import WatsonMachineLearningAPIClient

            wml_credentials = {
                "instance_id": "000263d8-04e0-4060-ad69-fcfe40069018",
                "password": "7419325b-3de4-476c-94cb-4b158fa335b0",
                "url": "https://us-south.ml.cloud.ibm.com",
                "username": "cdc4b5da-8380-42f1-bd82-da044b283959"}
            client = WatsonMachineLearningAPIClient(wml_credentials)

            modelver_area = '7f865b26-f55d-47af-9d11-7fd9692f76ac'
            scoring_url_area = 'https://us-south.ml.cloud.ibm.com/v3/wml_instances/000263d8-04e0-4060-ad69-fcfe40069018/published_models/0db673e9-1c62-4381-b7de-ef4de0d38b39/deployments/76886441-7656-424a-9060-a0ca770d5a08/online'

            modelver_action = 'a9816c12-7896-488e-9427-73926f6fa5fd'
            scoring_url_action = 'https://us-south.ml.cloud.ibm.com/v3/wml_instances/000263d8-04e0-4060-ad69-fcfe40069018/published_models/fef7671d-6877-46ae-a13b-617026e494ba/deployments/84872281-f46f-4fd1-afab-4dc6d44bd345/online'

            scores_area = client.deployments.score(scoring_url_area, payload)
            scores_action = client.deployments.score(scoring_url_action, payload)

            values = [rec + scores_area['values'][i][slice(15, 17)] + [modelver_area] + scores_action['values'][i][
                slice(20, 22)] + [modelver_action] for i, rec in enumerate(payload['values'])]

            fields = payload['fields'] + ['Probability_Area', 'Prediction_Area', 'Model_Version_Area'] + [
                'Probability_Action', 'Prediction_Action', 'Model_Version_Action']

            return {'fields': fields, 'values': values}

        ai_function_details = self.client.repository.store_function(function_props, score)

        TestAIFunction.function_uid = self.client.repository.get_function_uid(ai_function_details)
        function_url = self.client.repository.get_function_url(ai_function_details)
        TestAIFunction.logger.info("AI function ID:" + str(TestAIFunction.function_uid))
        TestAIFunction.logger.info("AI function URL:" + str(function_url))
        self.assertIsNotNone(TestAIFunction.function_uid)
        self.assertIsNotNone(function_url)

    def test_03_download_ai_function_content(self):
        try:
            os.remove('test_ai_function.tar.gz')
        except:
            pass

        self.client.repository.download(TestAIFunction.function_uid, filename='test_ai_function.tar.gz')

        try:
            os.remove('test_ai_function.tar.gz')
        except:
            pass

    def test_04_get_details(self):
        details = self.client.repository.get_function_details()
        self.assertTrue(self.function_name in str(details))

        details = self.client.repository.get_function_details(self.function_uid)
        self.assertTrue(self.function_name in str(details))

        details = self.client.repository.get_details()
        self.assertTrue("functions" in details)

        details = self.client.repository.get_details(self.function_uid)
        self.assertTrue(self.function_name in str(details))

    def test_05_list(self):
        self.client.repository.list()

        self.client.repository.list_functions()

    def test_06_create_deployment(self):
        TestAIFunction.logger.info("Create deployment")
        deployment = self.client.deployments.create(asset_uid=self.function_uid, name=self.deployment_name, asynchronous=False)
        TestAIFunction.logger.debug("Online deployment: " + str(deployment))
        TestAIFunction.scoring_url = self.client.deployments.get_scoring_url(deployment)
        TestAIFunction.logger.debug("Scoring url: {}".format(TestAIFunction.scoring_url))
        TestAIFunction.deployment_uid = self.client.deployments.get_uid(deployment)
        TestAIFunction.logger.debug("Deployment uid: {}".format(TestAIFunction.deployment_uid))
        self.assertTrue("online" in str(deployment))

    def test_07_get_deployment_details(self):
        TestAIFunction.logger.info("Get deployment details")
        deployment_details = self.client.deployments.get_details()
        TestAIFunction.logger.debug("Deployment details: {}".format(deployment_details))
        self.assertTrue(self.deployment_name in str(deployment_details))

    def test_08_score(self):
        sample_payload = {
            "fields": ["ID", "Gender", "Status", "Children", "Age", "Customer_Status", "Car_Owner", "Customer_Service",
                       "Satisfaction"],
            "values": [[2624, 'Male', 'S', 0, 49.27, 'Active', 'No',
                        "Good experience with all the rental co.'s I contacted. I Just called with rental dates and received pricing and selected rental co.",
                        1]]}
        predictions = self.client.deployments.score(TestAIFunction.scoring_url, sample_payload)
        print("Predictions: {}".format(predictions))
        self.assertTrue("values" in str(predictions))

    def test_09_delete_deployment(self):
        TestAIFunction.logger.info("Delete deployment")
        self.client.deployments.delete(TestAIFunction.deployment_uid)

    def test_10_delete_function(self):
        TestAIFunction.logger.info("Delete function")
        self.client.repository.delete(TestAIFunction.function_uid)

    def test_11_delete_runtime(self):
        self.client._runtimes.delete(TestAIFunction.runtime_uid)


if __name__ == '__main__':
    unittest.main()
