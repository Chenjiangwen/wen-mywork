terraform {
  required_version = ">= 1.3"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.61.0"
    }
  }
  backend "gcs" {
    bucket = "986864338a3f10e9-bucket-tfstate"
    prefix = "terraform/artifactRegistry"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}
