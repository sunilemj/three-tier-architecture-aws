# Three-Tier Architecture on AWS

## Overview
This repository demonstrates a standard three-tier architecture consisting of a presentation layer, application layer, and database layer. The project is designed to showcase cloud architecture understanding and infrastructure separation following best practices.

## Architecture Layers
- Web Tier: Handles client requests and serves frontend content
- Application Tier: Processes business logic
- Database Tier: Stores and manages application data

## AWS Services (Conceptual)
- Web Tier: EC2 / Load Balancer
- App Tier: EC2 / Auto Scaling
- DB Tier: RDS

## Repository Structure
web/        # Presentation layer (frontend)
app/        # Application layer (backend)
db/         # Database layer (schema / config)
diagrams/   # Architecture diagrams

## Notes
This project is intended for learning and demonstration of three-tier architecture concepts.
