project_id       = ""
analytics_region = "us-central1"
runtime_type     = "HYBRID"
apigee_environments = [
  "test",
  "newtest"
]
apigee_envgroups = {
  evg1 = {
    environments = ["test", "newtest"]
    hostnames    = ["dev3-test.hybrid-apigee.net"]
  }
  gr2 = {
    environments = ["test"]
    hostnames    = ["dev1-test1.hybrid-apigee.net"]
  }
}

env="non-prod"
hybrid_home="/home/nmakhijani/apigeebase/hybrid-files/"
apigeectl_home="/home/nmakhijani/apigeebase/apigeectl/"