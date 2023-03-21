function getBNBInfo(){
    axios.get(coinInfoUrl, {
    params: {
        fsym: 'BNB'
    }
    })
    .then(response => {
        var accessData = response.data.Data['BNB']
        var name = accessData.Name
        var imageurl = accessData.ImageUrl
        var assetWebsite = accessData.AssetWebsiteUrl
        var whitepaper = accessData.AssetWhitepaperUrl
        var coinName = accessData.CoinName
        var proofType = accessData.ProofType
        var symbol = accessData.Symbol
        generateRow(name, assetWebsite, whitepaper, coinName, proofType, symbol)
    })
    .catch(error => {
        console.log(error.message);
    });
}
function getBTCInfo() {
    axios.get(coinInfoUrl, {
    params: {
        fsym: 'BTC'
    }
    })
    .then(response => {
        var accessData = response.data.Data['BTC']
        var name = accessData.Name
        var imageurl = accessData.ImageUrl
        var assetWebsite = accessData.AssetWebsiteUrl
        var whitepaper = accessData.AssetWhitepaperUrl
        var coinName = accessData.CoinName
        var proofType = accessData.ProofType
        var symbol = accessData.Symbol
        generateRow(name, assetWebsite, whitepaper, coinName, proofType, symbol)
    })
    .catch(error => {
        console.log(error.message);
    });
}

function getADAInfo(){
    axios.get(coinInfoUrl, {
    params: {
        fsym: 'ADA'
    }
    })
    .then(response => {
        var accessData = response.data.Data['ADA']
        var name = accessData.Name
        var imageurl = accessData.ImageUrl
        var assetWebsite = accessData.AssetWebsiteUrl
        var whitepaper = accessData.AssetWhitepaperUrl
        var coinName = accessData.CoinName
        var proofType = accessData.ProofType
        var symbol = accessData.Symbol
        generateRow(name, assetWebsite, whitepaper, coinName, proofType, symbol)
    })
    .catch(error => {
        console.log(error.message);
    });
}
function getDOGEInfo() {
    axios.get(coinInfoUrl, {
    params: {
        fsym: 'DOGE'
    }
    })
    .then(response => {
        var accessData = response.data.Data['DOGE']
        var name = accessData.Name
        var imageurl = accessData.ImageUrl
        var assetWebsite = accessData.AssetWebsiteUrl
        var whitepaper = accessData.AssetWhitepaperUrl
        var coinName = accessData.CoinName
        var proofType = accessData.ProofType
        var symbol = accessData.Symbol
        generateRow(name, assetWebsite, whitepaper, coinName, proofType, symbol)
    })
    .catch(error => {
        console.log(error.message);
    });
}

function getETHInfo() {
    axios.get(coinInfoUrl, {
    params: {
        fsym: 'ETH'
    }
    })
    .then(response => {
        var accessData = response.data.Data['ETH']
        var name = accessData.Name
        var imageurl = accessData.ImageUrl
        var assetWebsite = accessData.AssetWebsiteUrl
        var whitepaper = accessData.AssetWhitepaperUrl
        var coinName = accessData.CoinName
        var proofType = accessData.ProofType
        var symbol = accessData.Symbol
        generateRow(name, assetWebsite, whitepaper, coinName, proofType, symbol)
    })
    .catch(error => {
        console.log(error.message);
    });
}
function getSOLInfo(){
    axios.get(coinInfoUrl, {
    params: {
        fsym: 'SOL'
    }
    })
    .then(response => {
        var accessData = response.data.Data['SOL']
        var name = accessData.Name
        var imageurl = accessData.ImageUrl
        var assetWebsite = accessData.AssetWebsiteUrl
        var whitepaper = accessData.AssetWhitepaperUrl
        var coinName = accessData.CoinName
        var proofType = accessData.ProofType
        var symbol = accessData.Symbol
        generateRow(name, assetWebsite, whitepaper, coinName, proofType, symbol)
    })
    .catch(error => {
        console.log(error.message);
    });
}
