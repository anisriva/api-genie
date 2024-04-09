# API-Genie: Dynamic Response Simulation
## Overview

API-Genie is an innovative FastAPI project designed to emulate and simulate the behavior of e-commerce websites and other applications in terms of response time and payload. It provides developers and testers with a powerful tool to mimic real-world web application behaviors, facilitating performance analysis, load testing, and the development of robust, responsive applications.

## Features
- Response Time Simulation: Mimic real-world response latencies with customizable delay mechanisms. Whether you need a fixed delay or randomized response times to simulate varying server loads, API-Genie has you covered.
- Dynamic Response Payloads: Generate response payloads that replicate the size and structure of real application responses. From small JSON objects to large binary files, API-Genie can dynamically adjust the payload size to meet your testing needs.

## Getting Started

### Prerequisites

- docker / podman

### Installation

Clone the repository:

```bash
git clone https://github.com/anisriva/api-genie.git
cd api-genie
```

### Build the Docker image
```bash
podman build -t api-genie:0.0.v1 .
```

### Run the container 
```bash
podman run -d -p 8000:8000 api-genie:0.0.v1
```

Visit http://localhost:8000 in your browser to access API-Genie.


## Usage
Describe how to use the application, including any available endpoints and how to simulate different scenarios.

## Deployment
Instructions on deploying the application with Docker and creating Kubernetes deployment files for scalability.

## Contributing
Contributions are welcome! Please feel free to submit a pull request.

## Contact
Animesh Srivastava - postanisrivastava@outlook.com
Project Link: https://github.com/anisriva/api-genie.git