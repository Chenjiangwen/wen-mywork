resource "google_artifact_registry_repository" "microservices" {
  repository_id = var.repository_id
  description   = "service all microservices docker files"
  format        = var.format
  location      = var.region
  project       = var.project_id

  docker_config {
    immutable_tags = true
  }
}
