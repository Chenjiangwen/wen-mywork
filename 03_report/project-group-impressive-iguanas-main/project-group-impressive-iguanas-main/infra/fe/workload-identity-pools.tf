resource "google_iam_workload_identity_pool" "workload_identity_pool" {
  workload_identity_pool_id = "github-action"
  display_name              = "github action"
  description               = "workload identity pool used for github action"
  disabled                  = false
}

resource "google_iam_workload_identity_pool_provider" "github_action_provider" {
  workload_identity_pool_id          = google_iam_workload_identity_pool.workload_identity_pool.workload_identity_pool_id
  workload_identity_pool_provider_id = "github-action-provider"
  attribute_mapping = {
    "google.subject"  = "assertion.sub",
    "attribute.actor" = "assertion.actor",
    "attribute.aud"   = "assertion.aud"
  }
  oidc {
    issuer_uri = "https://token.actions.githubusercontent.com"
  }
}
