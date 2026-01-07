# Three-Tier Shopping Application Architecture on AWS

## Overview
This repository demonstrates a three-tier architecture using a simple shopping application. 
The focus is on architectural separation between the Web, Application, and Database layers.

## Architecture Layers
- Web Tier: HTML frontend
- Application Tier: Python backend handling business logic
- Database Tier: Python-based data layer

## Conceptual AWS Mapping
- Web Tier: EC2 / Load Balancer
- Application Tier: EC2 / Auto Scaling
- Database Tier: Amazon RDS

## Repository Structure
web/        # Presentation layer (frontend)
app/        # Application layer (Python backend)
db/         # Database layer (simulated)
diagrams/   # Architecture diagrams

## Notes
This project is intended for learning and demonstration of three-tier architecture concepts.
