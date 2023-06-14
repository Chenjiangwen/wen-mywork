provider "google" {
  credentials = file("/Users/chenghao/Downloads/cs732/wired-yeti-383208-60b0fe6029c0.json")
  project = "wired-yeti-383208"
  region = "us-central1"
}

data "google_client_config" "current" {}


# Reference the existing GKE cluster
data "google_container_cluster" "autopilot-cluster-1" {
  name     = "autopilot-cluster-1"
  location = "us-central1"
}

# Configure the Kubernetes provider
provider "kubernetes" {
  host                   =  "https://${data.google_container_cluster.autopilot-cluster-1.endpoint}"
  token                  = data.google_client_config.current.access_token
  cluster_ca_certificate = base64decode(data.google_container_cluster.autopilot-cluster-1.master_auth[0].cluster_ca_certificate)
}

# Create a Kubernetes Secret to store the username and password
variable "atlasUsername" {
  type      = string
  sensitive = true
}

variable "atlasPassword" {
  type      = string
  sensitive = true
}




resource "kubernetes_secret" "autopilot-cluster-1" {
  metadata {
    name = "autopilot-cluster-1-secret"
  }

  
data = {
    atlasUsername = var.atlasUsername
    atlasPassword = var.atlasPassword

  }
  

  type = "Opaque"
}

