
$global:searchServiceKey = "";
$storageAccountKey = "";
$storageConnectionString = "";
$cogServicesKey = "";

while (!($subscriptionId = Read-Host "subscriptionId")) { Write-Host "You must provide a subscriptionId."; }


function Signin {
    # Sign in
    Write-Host "Logging in for '$subscriptionId'";
    Connect-AzAccount;

    # Select subscription
    Write-Host "Selecting subscription '$subscriptionId'";
    Select-AzSubscription -SubscriptionID $subscriptionId;
}

Signin;

function CallSearchAPI {
    param (
        [string]$url,
        [string]$body
    )
    Write-Host "Calling api: '"$global:searchServiceKey"'";
    $headers = @{
        'api-key'      = $global:searchServiceKey
        'Content-Type' = 'application/json' 
        'Accept'       = 'application/json' 
    }
    $baseSearchUrl = "https://" + $searchServiceName + ".search.windows.net"
    $fullUrl = $baseSearchUrl + $url

    Write-Host "Calling api: '"$fullUrl"'";
    Invoke-RestMethod -Uri $fullUrl -Headers $headers -Method Put -Body $body | ConvertTo-Json
}; 

Write-Host "Ensuring Azure dependencies are installed."
if (!(Get-Module -Name Az)) {
    Write-Host "Installing Az PowerShell..."
    Install-Module -Name Az
    Import-Module -Name Az
}
if (!(Get-Module -Name Az.Search)) {
    Write-Host "Installing Az.Search PowerShell..."
    Install-Module -Name Az.Search
    Import-Module -Name Az.Search
}

$storageContainerName = Read-Host "Please enter your storage account name: "
$storageContainerKey = Read-Host "Please enter your storage account key: "
$searchServiceName = Read-Host "Please enter your search service name: "
$global:searchServiceKey = Read-Host "Please enter your search service key: "
$cogServicesKey = Read-Host "Please enter your Cognitive Service Key: "
$azureFunctionUri = Read-Host "Please enter your Function App URI: "

# Create the datasource
$dataSourceBody = Get-Content -Path .\templates\datasource.json  
$dataSourceBody = $dataSourceBody -replace "{{accountName}}", $storageContainerName      
$dataSourceBody = $dataSourceBody -replace "{{accountKey}}", $storageContainerKey        
CallSearchAPI -url ("/datasources/books?api-version=2021-04-30-Preview") -body $dataSourceBody

# Create the skillset
$skillBody = Get-Content -Path .\templates\skillset.json
$skillBody = $skillBody -replace "{{cogServicesKey}}", $cogServicesKey  
$skillBody = $skillBody -replace "{{azureFunctionUri}}", $azureFunctionUri
CallSearchAPI -url ("/skillsets/books-skillset?api-version=2021-04-30-Preview") -body $skillBody

# Create the index
$indexBody = Get-Content -Path .\templates\index.json 
CallSearchAPI -url ("/indexes/books-index?api-version=2021-04-30-Preview") -body $indexBody
        
# Create the indexer
$indexerBody = Get-Content -Path .\templates\indexer.json
CallSearchAPI -url ("/indexers/books-indexer?api-version=2021-04-30-Preview") -body $indexerBody
