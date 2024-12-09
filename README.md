# Deadlock Detection in Resource Allocation System

## Description

This project implements a deadlock detection mechanism for a system with multiple processes and resources, where each resource has multiple instances. It reads input from CSV files representing the current state of resource allocation, outstanding requests, and available resources. The project then verifies the consistency of the input dimensions, detects any deadlocks, and provides appropriate outputs based on the system's state.

## Overview

### Input Files

1. **Allocation.csv**: Represents the NxM allocation matrix, where N is the number of processes and M is the number of resource types.
2. **Request.csv**: Represents the NxM request matrix, indicating the current outstanding requests for resources by each process.
3. **Available.csv**: Represents the M vector of available resources, indicating the number of available instances for each resource type.

### Functionality

1. **Reading Input Files**: The system reads the allocation, request, and available matrices from the provided CSV files.
2. **Verifying Dimensions**: It ensures that the dimensions of the input matrices are consistent with the specified number of processes and resources.
3. **Deadlock Detection**: The project detects whether the system is in a deadlocked state by analyzing the resource allocation and requests.
4. **Output**:
   - If a deadlock is detected, the system lists the processes involved in the deadlock.
   - If no deadlock is detected, it provides a safe sequence of process executions that avoid deadlock.

### Usage

To use this project, ensure that the `Allocation.csv`, `Request.csv`, and `Available.csv` files are in the project directory. Run the provided script to check for deadlocks and obtain the corresponding output.
