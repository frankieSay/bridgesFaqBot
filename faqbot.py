#!/usr/bin/env python3
#FAQ Bot
#Made with love in Sunnyvale Trailer Park
#bubbz

import requests
import json
import time

#discord webhook url
webhookUrl = 'https://discord.com/api/webhooks/#/#'


#post an embed to discord
def posttodiscord(_name, _value):
    data = {
        "username" : "FAQ"
        }

    data["embeds"] = [
        {
            #this color is bridges orange
            "color": 15105570,
            "fields": [
                {
                    "name": _name,
                    "value": _value
                }
            ]
        }
    ]

    result = requests.post(webhookUrl, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Embed sent successfully, code {}.".format(result.status_code))
    
    #give the api a 1 second breather between posts
    time.sleep(1)
		
#send a new embed, with the name of the embed and the content
posttodiscord("==TOKENOMICS==", "\n**What is the fee protocol?** \n \n The standard rate is 5% for every buy, sell, or transfer transaction. Broken down into the following portions: \n1% marketing fee.\n 1% liquidity pool feeding \n 3% BUSD dividends paid back to investors \n \n**Are you planning to change the fee protocol?** \n  \n After the exchange goes live the marketing fees will be set to 0%.  \n  \n Liquidity pool feeding will be dynamically managed. Being activated and deactivated according to the price volatility. \n   \n These 2 measures together will bring the tax protocol to between 3% and 4%.")

posttodiscord("==DIVIDENDS==", "\n**Why haven’t I received dividends? ** \n \nYou must have at least 100 tokens to receive dividends. In periods of low volume there could be some delays as each transaction must exceed the gas price on the Binance Smart Chain. Also, make sure you have Binance-pegged BUSD (BEP20) enabled in your wallet to have it appear in your balances – it’s not enabled by default.\n \n **Will the dividends need to be claimed? ** \n \n No. They will be delivered automatically every 6 hours. \n \n **How many dividends will an investor receive? ** \n \n To compute your daily dividends:\n (Daily Volume)(Wallet Balance/100M)(0.03) \n \n **Can the dividends be triggered at any given time; for example, when purchasing BRG or sending BRG to ones wallet? ** \n \n Yes, but to distribute dividend the amount must be higher than the BSC gas fee. Until then you’re owed balance will accrue.")

posttodiscord("==EXCHANGE==", "\n**Will our decentralized exchange (DEX) be comparable to Pancakceswap or Uniswap?**\n\nOur DEX will be similar to Pancakeswap in that it will be an Automated Market Maker decentralized exchange on the Binance Smart Chain, but we won’t list as many tokens. Our goal is quality over quantity. It’s better to have one reputable token project with $1M in 24hr volume than one hundred tokens with $10k in 24hr volume.\n\n **Which token will be used for liquidity pools?**\n\n All the tokens will be paired with Bridge$ thus bringing volume to our token.\n\n**Will there be additional features in the exchange?**\n\nYes. We will have other features that we will announce as we get closer to launching our exchange.\n\n**Will Bridges team screen the projects that apply to be listed?**\n\nYes, every project will be audited and will have to through our selection procedure. If it makes it through the process, it will be listed. This is to ensure that each project on our platform is safe.")

posttodiscord("==LISTINGS==", "\n**What are our guidelines for listing on our exchange? ** \n\n 1. Teams will not be forced to doxx publicly, but we will require meetings to vet the team privately or through a trusted third party KYC provider. \n2. We will facilitate audits with third parties\n3. Locked liquidity with multi-sig wallets\n4. Innovative projects and not clones of current projects\n5. Anti-whale practices\n6. Reasonable tokenomics fees\n *These requirements are subject to change and may be adjusted when necessary.* \n \n**How many projects are we inviting to be listed on the DEX?**\n\nInitially 10-15 projects covering a wide range of crypto fields, expanding form there. We’ll also include listings for major currencies like BTC, ETH, ADA, etc. to facilitate trading.\n\n**Can you name some of those projects?**\n\nNot yet! Let’s wait and see!")

posttodiscord("==TOKEN==", "\n**Where is the token listed?**\n\nBridge$ is a BEP20 token deployed on the Binance smart chain and is listed on Pancakeswap. \n\n**Is Bridge$ deflationary?** \n\n No. Bridge$ has a stable supply.\n\n**What are the total and circulating supplies? ** \n\nTotal supply of 100M with 70M in circulation.\n\n**What slippage is recommended?**\n\nStart at 5%.  If the transaction does not go through, increase by 1% and try again.\n\n**Will we list on other exchanges?**\n\nOur focus is on our own exchange for now but we will approach listings on centralized exchanges in the future.\n\n**Will we be able to buy Bridge$ with Fiat directly on exchange?** \n\nThis would require a centralized exchange partner. Our focus is on our own exchange for now but we will approach listings on centralized exchanges in the future.")

posttodiscord("==GENERAL==", "\n**Was there a presale? ** \n \nNo! The Fair Launch was on November 13th. Everyone had an equal chance to buy right at listing!\n\n**Is the team doxxed? ** \n\nNot yet! The CEO and COO will doxx at a $50M market cap.\n\n **Is the liquidity locked? ** \n\n70% of the liquidity is locked for 1 year. 30% is unlocked and will be withdrawn and used to create the new liquidity pool when our exchange is live. \n\n**What happens when liquidity isn’t locked anymore? ** \n\nWe will move all those funds to the exchange liquidity.")
