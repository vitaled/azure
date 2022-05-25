# How to create a basic Custom Skill for Azure Cognitive Search

This is a basic example that explains how to create a very simple custom skill in Azure Cognitive Search
by using an Azure Function as a backend

# The goal

We are going to create a very simple (and mostly useless) custom skill extracting all the palindromic words from a text

## Prerequisites

1) [Azure Cloud Subscription](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/initial-subscriptions)
2) [Azure Cognitive Search service](https://docs.microsoft.com/en-us/azure/search/search-create-service-portal)
3) [Python](https://www.python.org/downloads/)
4) [Visual Studio Code](https://code.visualstudio.com/Download)
5) [Azure Tools Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack)

### Step 1 

## Step 1: Import the repo

The first step is to import this repository into your Azure Devops project. 
To do so you should go to the **Repos** section, clickon the repository list and then on **Import repository**

![Open Import Repository](./img/01_import_repo.png)

The you should insert in the *Clone url* the link to this repository `https://github.com/vitaled/azure.git`   

![Import Repository](./img/02_import_git_repo.png)

After the import you should clone this repo locally from your Azure devops account. The fastest way to do that is to click on  **Clone in VS code**

![Clone to vs code](./img/03_clone_vs_code.png)

```bash
git clone https://github.com/vitaled/azure.git
```

Then you can open this folder using Visual Studio Code

## Step 2: Deploy the Azure Function

In the next step, we are going to manually deploy the Azure Function in your Azure Subscription.

To do that you should right-click on the `CognitiveSearchNERCustomSkill` subfolder and then click on **Deploy to Function App...**

![Deploy to Functions](./img/04_deploy_function_app.png)

You will be asked to select a subscription: 

![Select subscription](./img/05_select_subscription.png)

Then click on **Create new Function App in Azure...**

![Create new function](./img/06_create_new_function.png)

You will be asked to provide a unique name for your function

![get unique name](./img/07_select_unique_name.png) 

Select **Python 3.9** as runtime stack

![Select runtime](./img/08_select_runtime.png) 





