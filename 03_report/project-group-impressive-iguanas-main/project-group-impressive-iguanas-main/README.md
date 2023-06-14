<p align="center">
    <img width="200" src="fe/src/assets/logo.png">
</p>

<h1 align="center">Feature Flag System (featuresfly)</h1>

<div align="center">

![featuresflayGAE][featuresflayGAE-image] ![NPM version][npm-image] 
![featuresflayGKE][Event-To-GKE]
![featuresflayGKE][featuresflayGKE] ![featuresflayGKE][Write-To-GKE] ![featuresflayGKE][Gateway-To-GKE] 
![featuresflayGKE][Users-To-GKE] 
    
[featuresflayGAE-image]:https://github.com/UOA-CS732-SE750-Students-2023/project-group-impressive-iguanas/actions/workflows/React-To-GAE.yml/badge.svg
[Event-To-GKE]:https://github.com/UOA-CS732-SE750-Students-2023/project-group-impressive-iguanas/actions/workflows/Event-To-GKE.yml/badge.svg?event=push
[featuresflayGKE]:https://github.com/UOA-CS732-SE750-Students-2023/project-group-impressive-iguanas/actions/workflows/Featureflag-To-GKE.yml/badge.svg
[Write-To-GKE]:https://github.com/UOA-CS732-SE750-Students-2023/project-group-impressive-iguanas/actions/workflows/FeatureflagWrite-To-GKE.yml/badge.svg
[Gateway-To-GKE]:https://github.com/UOA-CS732-SE750-Students-2023/project-group-impressive-iguanas/actions/workflows/Gateway-To-GKE.yml/badge.svg
[Users-To-GKE]:https://github.com/UOA-CS732-SE750-Students-2023/project-group-impressive-iguanas/actions/workflows/Users-To-GKE.yml/badge.svg
[github-action-image]: https://github.com/ant-design/ant-design/workflows/%E2%9C%85%20test/badge.svg
[npm-image]: http://img.shields.io/npm/v/antd.svg?style=flat-square

</div>

A feature flag system is a powerful tool for managing and deploying software features in a controlled and flexible manner. With feature flags, developers can toggle specific features or functionality on and off in an application or system, enabling or disabling them based on configurable parameters such as user roles, geographic locations, or other conditions.


## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Getting Started

### Online
The all projects have been deployed to a GKE cluster and a GAE service. 
You can visit https://www.featuresfly.com

### Local
#### Frontend

##### Prerequisites
You should install Node.js and NPM or Yarn.

##### Installing
* Clone the repository to your local machine.
* Open a terminal window and navigate to the project directory.
* Run `npm install` or yarn to install the project dependencies.


##### Running the Project
Open a terminal window and navigate to the project directory.
Run `npm start` or yarn start to start the development server.
Open a web browser and navigate to http://localhost:3000 to view the app.

#### Backend

##### Prerequisites
Golang

##### Installing
Clone the repository to your local machine.
Open a terminal window and navigate to the project directory.
Run `go build` to build the project (as we have 5 microservices, so you need to build 5 projects seperately).

##### Databases
This project uses mongodb, please run the command to get a temporary mongodb cluster

```sh
npx run-rs -v 4.0.0
```
##### Built With
Golang,
Pubsub

##### env setup
If it is running locally, you need to set an environment variable hostname, which must be the value of the local hostname (please note that the environment variable and the hostname command are different). The `hostname` value will be used when connecting to mongodb, if the value is not set, four of microservices would fail to perform actions

##### GCP permissions
Because the project is built on the basis of cloud-native applications, some cloud services need to be used when running locally. Please send a permission request email to this `cliu797@aucklanduni.ac.nz` (please attach the gmail account you want to use to test this project), and he will give the project the permission to use the gcp service after receiving the email.

The way how to install Gcloud is : https://cloud.google.com/sdk/docs/install#deb

## Contributing

If you would like to contribute to the Golang Calculator, please follow these steps:

Fork the repository.
Create a new branch for your changes.
Make your changes and commit them with a descriptive message.
Push your changes to your forked repository.
Submit a pull request to the original repository.

## License
This project is licensed under the MIT License.


## Contact

* `cliu797@aucklanduni.ac.nz`
* `liyinjia0452@gmail.com`
* `swan506@aucklanduni.ac.nz`
* `yyan998@aucklanduni.ac.nz`
* `zliu941@aucklanduni.ac.nz`
