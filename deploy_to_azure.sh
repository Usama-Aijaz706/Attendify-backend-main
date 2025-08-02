#!/bin/bash

# Azure App Service Deployment Script
# This script deploys the Attendify application to Azure App Service using Docker

echo "🚀 Starting Azure App Service Deployment..."

# Configuration
RESOURCE_GROUP="attendify-rg"
APP_NAME="attendify-app"
LOCATION="eastus"
SKU="B1"  # Basic tier - can be upgraded to S1 or P1V3 for better performance

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}📋 Configuration:${NC}"
echo "Resource Group: $RESOURCE_GROUP"
echo "App Name: $APP_NAME"
echo "Location: $LOCATION"
echo "SKU: $SKU"
echo ""

# Check if Azure CLI is installed
if ! command -v az &> /dev/null; then
    echo -e "${RED}❌ Azure CLI is not installed. Please install it first.${NC}"
    echo "Visit: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli"
    exit 1
fi

# Check if logged in to Azure
if ! az account show &> /dev/null; then
    echo -e "${YELLOW}🔐 Please log in to Azure...${NC}"
    az login
fi

# Create resource group if it doesn't exist
echo -e "${YELLOW}📦 Creating resource group...${NC}"
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create App Service plan
echo -e "${YELLOW}📋 Creating App Service plan...${NC}"
az appservice plan create \
    --name "${APP_NAME}-plan" \
    --resource-group $RESOURCE_GROUP \
    --sku $SKU \
    --is-linux

# Create web app with Docker
echo -e "${YELLOW}🌐 Creating web app...${NC}"
az webapp create \
    --resource-group $RESOURCE_GROUP \
    --plan "${APP_NAME}-plan" \
    --name $APP_NAME \
    --deployment-local-git

# Configure the web app to use Docker
echo -e "${YELLOW}🐳 Configuring Docker deployment...${NC}"
az webapp config container set \
    --resource-group $RESOURCE_GROUP \
    --name $APP_NAME \
    --docker-custom-image-name attendify-backend:latest

# Set environment variables
echo -e "${YELLOW}🔧 Setting environment variables...${NC}"
az webapp config appsettings set \
    --resource-group $RESOURCE_GROUP \
    --name $APP_NAME \
    --settings \
    MONGO_URI="mongodb+srv://usamaaijaz707:Uk123uk321@attendify.tima9f4.mongodb.net/?retryWrites=true&w=majority&appName=Attendify" \
    DATABASE_NAME="Attendify"

# Enable continuous deployment from GitHub
echo -e "${YELLOW}🔗 Setting up GitHub deployment...${NC}"
az webapp deployment source config \
    --resource-group $RESOURCE_GROUP \
    --name $APP_NAME \
    --repo-url "https://github.com/Usama-Aijaz706/Attendify-backend-main.git" \
    --branch main \
    --manual-integration

# Get the web app URL
WEBAPP_URL=$(az webapp show --resource-group $RESOURCE_GROUP --name $APP_NAME --query defaultHostName --output tsv)

echo -e "${GREEN}✅ Deployment completed successfully!${NC}"
echo ""
echo -e "${GREEN}🌐 Your application is available at:${NC}"
echo -e "${GREEN}   https://$WEBAPP_URL${NC}"
echo ""
echo -e "${GREEN}📚 API Documentation:${NC}"
echo -e "${GREEN}   https://$WEBAPP_URL/docs${NC}"
echo ""
echo -e "${GREEN}🎓 Web Interface:${NC}"
echo -e "${GREEN}   https://$WEBAPP_URL:8501${NC}"
echo ""
echo -e "${YELLOW}📋 Next Steps:${NC}"
echo "1. Wait 5-10 minutes for the deployment to complete"
echo "2. Test your API endpoints"
echo "3. Access the web interface"
echo "4. Monitor the application in Azure Portal"
echo ""
echo -e "${YELLOW}🔍 To monitor your app:${NC}"
echo "Visit: https://portal.azure.com"
echo "Search for: App Services"
echo "Find your app: $APP_NAME" 