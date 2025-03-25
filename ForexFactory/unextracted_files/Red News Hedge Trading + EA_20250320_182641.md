

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#1](/thread/565676-red-news-hedge-trading-ea "Post Permalink")

  * First Post: Edited Sep 14, 2019 9:48pm  Nov 12, 2015 5:44am | Edited Sep 14, 2019 9:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

This trading strategy is based on taking advantage of high volatility in the market due to high impact red news. In this strategy, we open two trades on two different currency pairs which are known to be correlated (positively or negatively). For example, we open Long positions on both EURUSD and USDJPY a few seconds before a high impact red news in the hope of earning some pips from any imbalance in the basket. I have written an EA that makes it easier to trade this strategy. Attach the EA to one of currency pairs' chart (for example, EURUSD), and enter the hedge currency pair symbol (for example, USDJPY) in the input settings of the EA. There are four buttons to open positions,  
  
**1\. Buy/Sell:** the EA opens a Buy position on the attached chart, and a Sell position on the hedge currency pair.  
**2\. Sell/Buy:** the EA opens a Sell position on the attached chart, and a Buy position on the hedge currency pair.  
**3\. Buy/Buy:** the EA opens Buy positions on both currency pairs.  
**4\. Sell/Sell:** the EA opens Sell positions on both currency pairs.  
  
and there are three buttons to close the basket manually. You can specify the net take profit (in money, not pips!) in the input settings of the EA.  
  
**Positively Correlated Symbols**  
For a pair of symbols that are positively correlated (such as AUDUSD and AUDCAD), use either **Buy/Sell or Sell/Buy** button.  
  
**Negatively Correlated Symbols**  
For a pair of symbols that are negatively correlated (such as EURUSD and USDJPY), use either **Buy/Buy or Sell/Sell** button.  
  
**Forex Correlation Table**  
Here is a website where you can find a Forex correlation table,  

<https://www.mataf.net/en/forex/tools/correlation>

for example,  
AUDCAD ~ EURAUD  
AUDJPY ~ AUDNZD  
CADJPY ~ AUDJPY  
...  
  
**How I trade with this strategy:**  
1\. Choose a high impact red news of a major currency, for example AUD.  
2\. Choose two other major currencies to pair with AUD such that the absolute correlation of two pairs is greater than 0.5, for example AUDUSD and AUDCAD.  
3\. A few minutes before the news release time, look at a currency strength meter to observe which of above two currencies (USD or CAD) is more powerful.  
4\. Select a trade button according to both the sign of correlation (this can be automatically done by the EA for you), and the strongest currency you identified in the previous step.  
See an example here:  
[https://www.forexfactory.com/showthr...4#post10532124](https://www.forexfactory.com/showthread.php?p=10532124#post10532124)  
  
**How to load history data for hedge symbols?**  
In order to load history data of hedge symbols, you can follow the steps below:  
1\. Hit <F2> key to bring up History Center window.  
2\. Select the symbol (for example, EURUSD).  
3\. Click on <Download> button.  
4\. Repeat 1 to 3 for all symbols you want to load history data.  
  
**Thread Rules:**  
**1\. In this thread we discuss only the strategy and the EA presented here. I will IGNORE anyone who writes any irrelevant post in this thread.**  
**2\. TBD.**  
  
== **Update 2019-09-14** ======================  
**Ver. 1.84: An Experimental Currency Strength Meter (CSM) is added to the EA. Recompiled with MT4 build 1220.**  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURCADM1.png
Size: 40 KB](/attachment/image/3371700/thumbnail?d=1561563186)](/attachment/image/3371700?d=1561563186)   

  

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [MathTrader7_NewsHedgeEA.ex4](/attachment/file/3439689?d=1568465232) 148 KB | 1,647 downloads | Uploaded Sep 14, 2019 9:47pm 

  
  
**Note: The CSM needs your broker to provide all major currency pairs to work.**  
  
**Input settings description:**  

1\. Select Auto Time Based Action:

\- **Auto Trade Disabled** (default), This option disables auto time based trading.

\- **Buy/Buy** : This option makes the EA to open BUY/BUY positions at Auto Action Time.

\- **Sell/Sell** : This option makes the EA to open SELL/SELL positions at Auto Action Time.

\- **Buy/Sell** : This option makes the EA to open BUY/SELL positions at Auto Action Time.

\- **Sell/Buy:** This option makes the EA to open SELL/BUY positions at Auto Action Time.

2\. Enter Auto Action Time (broker time):

\- yyyy.mm.dd hh:mm:ss, for example 2015.11.19 14:29:30

\- The EA opens two positions at this time according to Select Auto Time Based Action setting.

3\. Auto Button Selection?

\- If enabled, the EA hides irrelevant trade buttons according to the correlation value between two symbols.

4\. Hedge Symbol:

\- Enter hedge symbol as exactly as it appears on the market watch of your MT4 platform.

5\. Net Take Profit (money):

\- When net profit becomes greater than this value, the EA automatically closes both positions.

6\. Net Stop Loss (money):

\- When net profit becomes less than negative of this value, the EA automatically closes both positions.

~~7\. Equalize Pips?~~

~~\- If enabled, the lot size of trading two positions will be recalculated such that one pip of both symbols will be (approximately) worth equal (see[Post 104](http://www.forexfactory.com/showthread.php?p=8599108#post8599108)).~~

~~\- If disabled, the EA opens two positions with the user specified lot size.~~

8.1 Lot Size: 0.1 (default)

8.2 Hedge Lot Size: 0.1 (default)

9\. Slippage (points): 30 (default)

10\. Magic Number: 1122 (default)

\- If you want to use the EA on the same symbol twice or more, you have to assign different magic numbers. Otherwise, leave it default.

  
====================================  
**How to install this EA on your MetaTrader4 Platform**  
For newbies, here is a **[video on youtube](https://goo.gl/rqSeGD)** that shows how to install any EA on MetaTrader 4 platform in 5 easy steps 

Trading is the hardest way to make easy money...

  * [#2](/thread/post/8587369#post8587369 "Post Permalink")

  * Nov 12, 2015 1:50pm  Nov 12, 2015 1:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar392927_1.gif) techlover](techlover)

  * | Joined Dec 2014  | Status: Trader | [117 Posts](/search?do=process&provider=Member&searchuser=392927)

Thank you for your Ea Math  
  
have placed it on Usdjpy chart with EURUSD to hedge and clicked Buy/sell button , it opened 0.1 Usdjpy and 0.08 Eurusd  
  
may i know why it opened 0.08 in EURUSD ? , will it calculate the perfect hedging lot size ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#3](/thread/post/8587934#post8587934 "Post Permalink")

  * Nov 12, 2015 6:55pm  Nov 12, 2015 6:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting techlover](/thread/post/8587369#post8587369 "View Quoted Post")
> 
> Disliked
> 
> Thank you for your Ea Math have placed it on Usdjpy chart with EURUSD to hedge and clicked Buy/sell button , it opened 0.1 Usdjpy and 0.08 Eurusd may i know why it opened 0.08 in EURUSD ? , will it calculate the perfect hedging lot size ?
> 
> Ignored

You're welcome! :-)  
  
And you're right! The EA calculates lots to equalize the worth of one point of both currency pairs. I uploaded a new version (v1.10) with an input to let the user enable/disable this function. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#4](/thread/post/8587960#post8587960 "Post Permalink")

  * Nov 12, 2015 7:04pm  Nov 12, 2015 7:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar392927_1.gif) techlover](techlover)

  * | Joined Dec 2014  | Status: Trader | [117 Posts](/search?do=process&provider=Member&searchuser=392927)

> [Quoting MathTrader7](/thread/post/8587934#post8587934 "View Quoted Post")
> 
> Disliked
> 
> {quote} You're welcome! :-) And you're right! The EA calculates lots to equalize the worth of one point of both currency pairs. I uploaded a new version (v1.10) with an input to let the user enable/disable this function.
> 
> Ignored

there is a Bug in Ea, its not closing at desired Profit 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#5](/thread/post/8587979#post8587979 "Post Permalink")

  * Nov 12, 2015 7:10pm  Nov 12, 2015 7:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting techlover](/thread/post/8587960#post8587960 "View Quoted Post")
> 
> Disliked
> 
> {quote} there is a Bug in Ea, its not closing at desired Profit
> 
> Ignored

Please test v1.10, I optimized the close basket functionality to send order close command to the broker server as fast as possible. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#6](/thread/post/8588069#post8588069 "Post Permalink")

  * Nov 12, 2015 7:56pm  Nov 12, 2015 7:56pm 

  * [ mpradeep](mpradeep)

  * | Joined Apr 2012  | Status: Trader | [168 Posts](/search?do=process&provider=Member&searchuser=246669)

Other than EU with UJ which will be the best pair? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#7](/thread/post/8588145#post8588145 "Post Permalink")

  * Nov 12, 2015 8:42pm  Nov 12, 2015 8:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting mpradeep](/thread/post/8588069#post8588069 "View Quoted Post")
> 
> Disliked
> 
> Other than EU with UJ which will be the best pair?
> 
> Ignored

For AUD red news, I trade AUDUSD and AUDCAD. Go for either BUY/SELL or SELL/BUY for this pair of symbols.  
For today's USD red news, I may go SELL/SELL for both symbols EURUSD and USDJPY. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#8](/thread/post/8589683#post8589683 "Post Permalink")

  * Nov 13, 2015 2:03pm  Nov 13, 2015 2:03pm 

  * [ mpradeep](mpradeep)

  * | Joined Apr 2012  | Status: Trader | [168 Posts](/search?do=process&provider=Member&searchuser=246669)

Any more progress? anyone trading with this ea? i got profit buy buy EU and UJ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#9](/thread/post/8589831#post8589831 "Post Permalink")

  * Nov 13, 2015 4:41pm  Nov 13, 2015 4:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.15** of the EA released. In this version a bug in auto closing the hedge basket is fixed. I updated Post 1. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#10](/thread/post/8589855#post8589855 "Post Permalink")

  * Nov 13, 2015 4:55pm  Nov 13, 2015 4:55pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Dear MathTrader,  
  
Thanks for the EA,... truly I need the clear tutorial when to apply BUY/SELL , SELL/BUY, SELL/SELL or BUY/BUY,....  
  
May be you have better clear hints how to determine that operation.  
  
Looking forward to have answer from you,...  
  
Thanks,  
  
Budi 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#11](/thread/post/8589974#post8589974 "Post Permalink")

  * Nov 13, 2015 5:56pm  Nov 13, 2015 5:56pm 

  * [ mpradeep](mpradeep)

  * | Joined Apr 2012  | Status: Trader | [168 Posts](/search?do=process&provider=Member&searchuser=246669)

Dear Mathtrader  
  
Where is is version 1.15. need to download. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#12](/thread/post/8590029#post8590029 "Post Permalink")

  * Nov 13, 2015 6:20pm  Nov 13, 2015 6:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar428395_2.gif) jagzuk](jagzuk)

  * Joined Sep 2015 | Status: Trader | [494 Posts](/search?do=process&provider=Member&searchuser=428395)

> [Quoting mpradeep](/thread/post/8589974#post8589974 "View Quoted Post")
> 
> Disliked
> 
> Dear Mathtrader Where is is version 1.15. need to download.
> 
> Ignored

Download from post 1. MathTrader updated the file (see the section at the end of post1 that says Update, and date after the download link?). Best Regards. 

Always read Post #1

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#13](/thread/post/8590626#post8590626 "Post Permalink")

  * Nov 13, 2015 10:42pm  Nov 13, 2015 10:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3151_5.gif) BLACKFEET](blackfeet)

  * | Joined Aug 2005  | Status: Trader | [327 Posts](/search?do=process&provider=Member&searchuser=3151)

Hi, Mathtrader  
  
I used your EA with the last NEW : Core Retail Sales.  
  
Everything worked perfect...but I asked for 30 bucks and it gave me only $10.91 (LOL)  
  
Thanks  
  
Best regards  
  
BBF 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 20151113_EURUSD.png
Size: 8 KB](/attachment/image/1792654/thumbnail?d=1447422097)](/attachment/image/1792654?d=1447422097)   

BigBlackfeet Always on the(forex) war path !

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#14](/thread/post/8590681#post8590681 "Post Permalink")

  * Nov 13, 2015 10:53pm  Nov 13, 2015 10:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar392927_1.gif) techlover](techlover)

  * | Joined Dec 2014  | Status: Trader | [117 Posts](/search?do=process&provider=Member&searchuser=392927)

Still Ea not closing trades at desired profit , kindly have a look Math Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#15](/thread/post/8590799#post8590799 "Post Permalink")

  * Nov 13, 2015 11:33pm  Nov 13, 2015 11:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting techlover](/thread/post/8590681#post8590681 "View Quoted Post")
> 
> Disliked
> 
> Still Ea not closing trades at desired profit , kindly have a look Math Thank you
> 
> Ignored

Are you using the last version (v1.15)? 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#16](/thread/post/8590802#post8590802 "Post Permalink")

  * Nov 13, 2015 11:33pm  Nov 13, 2015 11:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting BLACKFEET](/thread/post/8590626#post8590626 "View Quoted Post")
> 
> Disliked
> 
> Hi, Mathtrader I used your EA with the last NEW : Core Retail Sales. Everything worked perfect...but I asked for 30 bucks and it gave me only $10.91 (LOL) Thanks Best regards BBF {image}
> 
> Ignored

Good results! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
We have to accept what market gives us ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#17](/thread/post/8590805#post8590805 "Post Permalink")

  * Nov 13, 2015 11:36pm  Nov 13, 2015 11:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar392927_1.gif) techlover](techlover)

  * | Joined Dec 2014  | Status: Trader | [117 Posts](/search?do=process&provider=Member&searchuser=392927)

> [Quoting MathTrader7](/thread/post/8590799#post8590799 "View Quoted Post")
> 
> Disliked
> 
> {quote} Are you using the last version (v1.15)?
> 
> Ignored

I am Using v1.10 , sorry i will test latest version  
  
As of now the results with this Ea are very good , even we can use it for Scalping  
have to test it few more days 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#18](/thread/post/8590828#post8590828 "Post Permalink")

  * Nov 13, 2015 11:43pm  Nov 13, 2015 11:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar392927_1.gif) techlover](techlover)

  * | Joined Dec 2014  | Status: Trader | [117 Posts](/search?do=process&provider=Member&searchuser=392927)

New Version is Perfect ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: jpy.png
Size: 7 KB](/attachment/image/1792712/thumbnail?d=1447425806)](/attachment/image/1792712?d=1447425806)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#19](/thread/post/8590872#post8590872 "Post Permalink")

  * Nov 13, 2015 11:59pm  Nov 13, 2015 11:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting techlover](/thread/post/8590805#post8590805 "View Quoted Post")
> 
> Disliked
> 
> {quote} I am Using v1.10 , sorry i will test latest version As of now the results with this Ea are very good , even we can use it for Scalping have to test it few more days
> 
> Ignored

Trading hedge is one of my favorite strategies. As you mentioned, we can use it for scalping here and there. Please post your results which may help other traders to learn this style of trading. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#20](/thread/post/8590897#post8590897 "Post Permalink")

  * Nov 14, 2015 12:06am  Nov 14, 2015 12:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar392927_1.gif) techlover](techlover)

  * | Joined Dec 2014  | Status: Trader | [117 Posts](/search?do=process&provider=Member&searchuser=392927)

> [Quoting MathTrader7](/thread/post/8590872#post8590872 "View Quoted Post")
> 
> Disliked
> 
> {quote} Trading hedge is one of my favorite strategies. As you mentioned, we can use it for scalping here and there. Please post your results which may help other traders to learn this style of trading.
> 
> Ignored

Why cant it be Auto trading , we can set small profit and use for scalping  
  
leave the trader to chose the option of Buy/sell or Sell /Sell 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#21](/thread/post/8590923#post8590923 "Post Permalink")

  * Nov 14, 2015 12:13am  Nov 14, 2015 12:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting techlover](/thread/post/8590897#post8590897 "View Quoted Post")
> 
> Disliked
> 
> {quote} Why cant it be Auto trading , we can set small profit and use for scalping leave the trader to chose the option of Buy/sell or Sell /Sell
> 
> Ignored

To automate it, the question is what would be the entry logic? When to enter? There must be a logic behind it. I don't think randomly opening hedge positions would be profitable in long run....![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#22](/thread/post/8590971#post8590971 "Post Permalink")

  * Edited 2:48am  Nov 14, 2015 12:30am | Edited 2:48am 

  * [ akira00](akira00)

  * | Joined Nov 2012  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=310623)

Interesting strategy,mt7.  
Although my broker is not allowed EA.But I tested manually this strategy.I used it with the last NEWS：Prelim UoM Consumer Sentiment.Good results.  
But I still have a doubt.I think the two symbols the fluctuation is not the same.We can win may also lose.This depends on whether we choose to buy or sell.And we need to stoploss?How to takeprofit? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 8 KB](/attachment/image/1792761/thumbnail?d=1447428619)](/attachment/image/1792761?d=1447428619)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#23](/thread/post/8591177#post8591177 "Post Permalink")

  * Nov 14, 2015 2:25am  Nov 14, 2015 2:25am 

  * [ Stevefluff](stevefluff)

  * | Joined Nov 2015  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=432466)

Im unable to open the file, i copy and paste across to MQL4 from my download folder but nothing adding to the chart ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#24](/thread/post/8591229#post8591229 "Post Permalink")

  * Nov 14, 2015 2:55am  Nov 14, 2015 2:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Stevefluff](/thread/post/8591177#post8591177 "View Quoted Post")
> 
> Disliked
> 
> Im unable to open the file, i copy and paste across to MQL4 from my download folder but nothing adding to the chart ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)
> 
> Ignored

In Post 1, I added a link to a youtube video that shows how to install any EA on MetaTrader 4 platform. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#25](/thread/post/8591231#post8591231 "Post Permalink")

  * Nov 14, 2015 2:56am  Nov 14, 2015 2:56am 

  * [ Stevefluff](stevefluff)

  * | Joined Nov 2015  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=432466)

Thanks MathTrader 7 you`re a star ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#26](/thread/post/8591332#post8591332 "Post Permalink")

  * Nov 14, 2015 4:22am  Nov 14, 2015 4:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar357421_1.gif) bazze](bazze)

  * | Joined Dec 2013  | Status: Trader | [1,135 Posts](/search?do=process&provider=Member&searchuser=357421)

> [Quoting budidharma19](/thread/post/8589855#post8589855 "View Quoted Post")
> 
> Disliked
> 
> Dear MathTrader, Thanks for the EA,... truly I need the clear tutorial when to apply BUY/SELL , SELL/BUY, SELL/SELL or BUY/BUY,.... May be you have better clear hints how to determine that operation. Looking forward to have answer from you,... Thanks, Budi
> 
> Ignored

I wonder about the same criterias? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#27](/thread/post/8592439#post8592439 "Post Permalink")

  * Nov 15, 2015 11:37am  Nov 15, 2015 11:37am 

  * [ karamaramun](karamaramun)

  * | Joined Dec 2014  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=393975)

I'd like to add a URL which may help this strategy:  
  
<http://fxtrade.oanda.com/analysis/currency-correlation>  
  
It's [OANDA](/brokers/oanda "View OANDA Broker Profile") free currency correlation tables.  
  
=========================================  
  
MathTrader7,  
  
Thank you for the EA. Very interesting. I'll try it when the market resumes.  
  
I have one quick question.  
  
In your post, you mentioned that opening the positions before the new just a couple of seconds. Generally, I think opening positions during the time will lead us to face the widen [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") which may (?) affect the spreads.  
  
1.) Have you ever experienced a case when widen spreads ruined the setup?  
2.) Have you tried opening the positions like 5 minutes before the news? If yes, did the position work as well as the one that opened just a few seconds before the news announcement?  
  
K-Mun 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#28](/thread/post/8592541#post8592541 "Post Permalink")

  * Nov 15, 2015 5:48pm  Nov 15, 2015 5:48pm 

  * [ Surgefx](surgefx)

  * | Joined Apr 2015  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=406756)

Fantastistic EA. Can you make it have lines for SL and TP and lots auto calculated by risk settings. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#29](/thread/post/8592563#post8592563 "Post Permalink")

  * Edited 7:09pm  Nov 15, 2015 6:59pm | Edited 7:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting karamaramun](/thread/post/8592439#post8592439 "View Quoted Post")
> 
> Disliked
> 
> 1.) Have you ever experienced a case when widen spreads ruined the setup?  
>  2.) Have you tried opening the positions like 5 minutes before the news? If yes, did the position work as well as the one that opened just a few seconds before the news announcement?
> 
> Ignored

Hi K-Mun,  
  
First, thanks for the correlation table. I will put a link to a website for Forex pairs correlation in Post 1.  
  
1) I have a true ECN account with [IC Markets](/brokers/ic-markets "View IC Markets Broker Profile") broker, where up to 30 seconds before a high impact red news they keep the spread in a normal range (for example, 0.5 pips for EURUSD). I actually open two positions about 30 seconds before the news release time.  
  
2) No, I never open positions 5 minutes before a high impact red news.  
  
Best,  
Math 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#30](/thread/post/8592566#post8592566 "Post Permalink")

  * Edited 9:08pm  Nov 15, 2015 7:07pm | Edited 9:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Surgefx](/thread/post/8592541#post8592541 "View Quoted Post")
> 
> Disliked
> 
> Fantastistic EA. Can you make it have lines for SL and TP and lots auto calculated by risk settings.
> 
> Ignored

I think you want to trade straddle strategy where asking for SL and TP. Please note that true ECN brokers won't respect to your SL levels; they close your position at the first available quote (price) which could be hundred pips far from where you have set your SL level. This is also the case for pending orders, they will execute your pending order at the first available quote (price). According to my experience, if you are working with true ECN brokers straddle strategy won't work. But it may work with market makers brokers (but there are other problems with such brokers). The philosophy of this thread's strategy is to hedge one position with another, and without using broker side stop loss / take profit levels. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#31](/thread/post/8592577#post8592577 "Post Permalink")

  * Nov 15, 2015 7:40pm  Nov 15, 2015 7:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3151_5.gif) BLACKFEET](blackfeet)

  * | Joined Aug 2005  | Status: Trader | [327 Posts](/search?do=process&provider=Member&searchuser=3151)

> [Quoting MathTrader7](/thread/post/8592566#post8592566 "View Quoted Post")
> 
> Disliked
> 
> {quote} I think you want to trade straddle strategy where asking for SL and TP. Please note that true ECN brokers won't respect to your SL levels; they close your position at the first available quote (price) which could be hundred pips far from where you have set your SL level. This is the case for pending orders, they will execute your pending order at the first available quote (price). According to my experience, if you are working with true ECN brokers straddle strategy won't work. But it may work with market makers brokers (but there are other...
> 
> Ignored

Hi Mathtrader  
  
Quickly, about correlation, may I suggest :  
  
<https://www.mataf.net/fr/tools/01-01-correlation>  
  
Best regards  
  
BBF 

BigBlackfeet Always on the(forex) war path !

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#32](/thread/post/8592637#post8592637 "Post Permalink")

  * Edited 9:30pm  Nov 15, 2015 9:12pm | Edited 9:30pm 

  * [ Surgefx](surgefx)

  * | Joined Apr 2015  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=406756)

> [Quoting MathTrader7](/thread/post/8592566#post8592566 "View Quoted Post")
> 
> Disliked
> 
> {quote} I think you want to trade straddle strategy where asking for SL and TP. Please note that true ECN brokers won't respect to your SL levels; they close your position at the first available quote (price) which could be hundred pips far from where you have set your SL level. This is the case for pending orders, they will execute your pending order at the first available quote (price). According to my experience, if you are working with true ECN brokers straddle strategy won't work. But it may work with market makers brokers (but there are other...
> 
> Ignored

Actually am working on hegding trades on a pair by opening trades seconds before news(not with pending orders like you assume), closing one at a SL below fib lines (hence the need for lines for positioning the SL. Then lots proportional to the SL position and risk ) allowing the other to run to TP. If it takes.   
having market maker to carry out the strategy fine 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#33](/thread/post/8592791#post8592791 "Post Permalink")

  * Nov 16, 2015 1:13am  Nov 16, 2015 1:13am 

  * [ akira00](akira00)

  * | Joined Nov 2012  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=310623)

Choose two similar ADR currency pairs, will be more safe? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#34](/thread/post/8593271#post8593271 "Post Permalink")

  * Nov 16, 2015 12:56pm  Nov 16, 2015 12:56pm 

  * [ karamaramun](karamaramun)

  * | Joined Dec 2014  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=393975)

> [Quoting MathTrader7](/thread/post/8590923#post8590923 "View Quoted Post")
> 
> Disliked
> 
> {quote} To automate it, the question is what would be the entry logic? When to enter? There must be a logic behind it. I don't think randomly opening hedge positions would be profitable in long run....![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)
> 
> Ignored

Hi MathTrader7,  
  
Hm, I have some idea. What about...

  1. Calculating historical average correlation in a given timeframe... say EURUSD and USDJPY... we find that they have -0.9
  2. At the beginning of a new time, we calculate again and if the correlation deviates from the average, we will open a position.
  3. Essentially, we are assuming that the deviation is temporary and the pair will resume their correlation... For example, at the beginning of the trading day

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 33 KB](/attachment/image/1793525/thumbnail?d=1447646072)](/attachment/image/1793525?d=1447646072)   

  
  
These two deviate at the beginning of trading day (US EST)  
  
So we initiate the positions. We will close when

  1. Profit target is reached
  2. Correlation back to normal
  3. SL is hit

K-Mun 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#35](/thread/post/8594287#post8594287 "Post Permalink")

  * Edited 1:30am  Nov 17, 2015 1:09am | Edited 1:30am 

  * [ Surgefx](surgefx)

  * | Joined Apr 2015  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=406756)

Placed my first trade with the EA today ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) very please especially as the button goes blank after click thereb preventing multiple compulsive entry. Can we have a way to hide some of the buy/sell buttons that are not to be used. Also line controlled SL , lots proportional to risk and SL settings . The Close button to close all trades( currently it closes only trades opened by the EA) in a pair will be great.![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Thanks man 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#36](/thread/post/8594305#post8594305 "Post Permalink")

  * Nov 17, 2015 1:20am  Nov 17, 2015 1:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Surgefx](/thread/post/8594287#post8594287 "View Quoted Post")
> 
> Disliked
> 
> Placed my first trade with the EA today ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) very please especially as the button goes blank after click hereb prevent multiple compulsive entry. Can we have a way to hide some of the buy/sell buttons that are not to be used. Also line controlled SL , lots proportional to risk and SL settings . the Close button to close all trades in a pair will be great.![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Thanks man
> 
> Ignored

I can implement a correlation computation between the symbol of the chart that the EA attached to and the symbol that the user sets in the input settings of the EA, and accordingly I can make the EA to hide the buttons that are not to be used. ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) wait for the next versions.... 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#37](/thread/post/8594330#post8594330 "Post Permalink")

  * Nov 17, 2015 1:33am  Nov 17, 2015 1:33am 

  * [ Surgefx](surgefx)

  * | Joined Apr 2015  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=406756)

> [Quoting MathTrader7](/thread/post/8594305#post8594305 "View Quoted Post")
> 
> Disliked
> 
> {quote} I can implement a correlation computation between the symbol of the chart that the EA attached to and the symbol that the user sets in the input settings of the EA, and accordingly I can make the EA to hide the buttons that are not to be used. ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) wait for the next versions....
> 
> Ignored

Thanks man for the positive consideration. Also I know SL and Tp on each individual trade in pips and/or percentage of account can be great too if am not suggesting too much. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#38](/thread/post/8594803#post8594803 "Post Permalink")

  * Edited 8:45am  Nov 17, 2015 6:21am | Edited 8:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.20** of the EA released. In this version the EA calculates the correlation between two symbols based on which the EA automatically shows the relevant set of buttons for true hedge trading. The user can disable this auto button selection. I updated Post 1. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#39](/thread/post/8594906#post8594906 "Post Permalink")

  * Nov 17, 2015 7:19am  Nov 17, 2015 7:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting karamaramun](/thread/post/8593271#post8593271 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi MathTrader7, Hm, I have some idea. What about... Calculating historical average correlation in a given timeframe... say EURUSD and USDJPY... we find that they have -0.9 At the beginning of a new time, we calculate again and if the correlation deviates from the average, we will open a position. Essentially, we are assuming that the deviation is temporary and the pair will resume their correlation... For example, at the beginning of the trading day {image} These two deviate at the beginning of trading day (US EST) So we initiate the positions....
> 
> Ignored

Thanks for sharing your idea. I will think about that... 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#40](/thread/post/8594954#post8594954 "Post Permalink")

  * Nov 17, 2015 8:18am  Nov 17, 2015 8:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar398921_25.gif) BillYon](billyon)

  * Joined Feb 2015 | Status: Trader | [924 Posts](/search?do=process&provider=Member&searchuser=398921)

A THING OF BEAUTY MATH  
  
THANK YOU!!!  
  
  
  
What do you think of a money flow cross trigger for auto trigger?  
  
Crude but may be effective... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: USDCADH1.png
Size: 36 KB](/attachment/image/1794161/thumbnail?d=1447715871)](/attachment/image/1794161?d=1447715871)   

Solutions ONLY!!!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#41](/thread/post/8594977#post8594977 "Post Permalink")

  * Nov 17, 2015 8:48am  Nov 17, 2015 8:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting BillYon](/thread/post/8594954#post8594954 "View Quoted Post")
> 
> Disliked
> 
> A THING OF BEAUTY MATH THANK YOU!!! What do you think of a money flow cross trigger for auto trigger? Crude but may be effective... {image}
> 
> Ignored

You're welcome! :-)  
  
Thanks for sharing your idea! I'll study the performance of MFI indicator... 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#42](/thread/post/8595469#post8595469 "Post Permalink")

  * Nov 17, 2015 5:00pm  Nov 17, 2015 5:00pm 

  * [ Kandi Trader](kandi*trader)

  * | Joined Jan 2012  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=221540)

This is a great Idea - really would like to test drive it.   
I have installed the EA but it only shows the 'Close All' Button - Can you please advise?  
  
Thanks a mill. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#43](/thread/post/8595582#post8595582 "Post Permalink")

  * Nov 17, 2015 6:02pm  Nov 17, 2015 6:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Kandi Trader](/thread/post/8595469#post8595469 "View Quoted Post")
> 
> Disliked
> 
> This is a great Idea - really would like to test drive it. I have installed the EA but it only shows the 'Close All' Button - Can you please advise? Thanks a mill.
> 
> Ignored

Set the first input sttings to false 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#44](/thread/post/8595651#post8595651 "Post Permalink")

  * Nov 17, 2015 6:34pm  Nov 17, 2015 6:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar357421_1.gif) bazze](bazze)

  * | Joined Dec 2013  | Status: Trader | [1,135 Posts](/search?do=process&provider=Member&searchuser=357421)

Tried to open trades during the GBP news, at 10.30 (GMT+1) but none of the buttons worked???? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#45](/thread/post/8595674#post8595674 "Post Permalink")

  * Edited 7:20pm  Nov 17, 2015 6:43pm | Edited 7:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting bazze](/thread/post/8595651#post8595651 "View Quoted Post")
> 
> Disliked
> 
> Tried to open trades during the GBP news, at 10.30 (GMT+1) but none of the buttons worked????
> 
> Ignored

Probably it was a problem from your broker. I traded it with GBPUSD and EURUSD 30 seconds before news release successfully. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: GBPUSDM1.png
Size: 29 KB](/attachment/image/1794477/thumbnail?d=1447755651)](/attachment/image/1794477?d=1447755651)   

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#46](/thread/post/8595699#post8595699 "Post Permalink")

  * Nov 17, 2015 6:51pm  Nov 17, 2015 6:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar357421_1.gif) bazze](bazze)

  * | Joined Dec 2013  | Status: Trader | [1,135 Posts](/search?do=process&provider=Member&searchuser=357421)

Yes, I think so too![](https://resources.faireconomy.media/images/emojis/64/1f621.png?v=15.1)....(I used the same pairs like you did...) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#47](/thread/post/8595741#post8595741 "Post Permalink")

  * Nov 17, 2015 7:04pm  Nov 17, 2015 7:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8595674#post8595674 "View Quoted Post")
> 
> Disliked
> 
> {quote} Probably it was a problem from your broker. I traded it with GBPUSD and EURUSD 30 seconds before news release successfully.
> 
> Ignored

Hello , me too in GU/EU .   
% correlation TF H1 = +75%  
My entry was when GU stochastic was highter but no in area OB (maybe i wrong) ... i will test ![](https://resources.faireconomy.media/images/emojis/64/1f937-200d-2642-fe0f.png?v=15.1)  
At the start the trade was fast in profit of 5€ ( 0.5%) but i didn't close it and the trade finished in loss of 10€ (1%)   
  
Start :  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: INIZIO.png
Size: 130 KB](/attachment/image/1794456/thumbnail?d=1447754469)](/attachment/image/1794456?d=1447754469)   

  
  
Close SL (maybe here i could retry with buy/sell the correlation ( Stocastics in OS/OB)  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: fine.jpg
Size: 403 KB](/attachment/image/1794459/thumbnail?d=1447754640)](/attachment/image/1794459?d=1447754640)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#48](/thread/post/8595780#post8595780 "Post Permalink")

  * Edited 7:57pm  Nov 17, 2015 7:19pm | Edited 7:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8595741#post8595741 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello , me too in GU/EU . % correlation TF H1 = +75% My entry was when GU stochastic was highter but no in area OB (maybe i wrong) ... i will test ![](https://resources.faireconomy.media/images/emojis/64/1f937-200d-2642-fe0f.png?v=15.1) At the start the trade was fast in profit of 5 ( 0.5%) but i didn't close it and the trade finished in loss of 10 (1%) Start : {image} Close SL (maybe here i could retry with buy/sell the correlation ( Stocastics in OS/OB) {image}
> 
> Ignored

I usually set the lot size to 0.1, with perfect hedge calculation enabled and a target profit of 5 USD. Because EA checks if the net profit is greater than the target profit to close the basket, when price jumps there is a high probability that profit exceeds 5 USD. In my recent trade of GBP red news, it gave me a profit of about 20 USD :-)  
So, my advice is to set the target profit to a small amount. If the market is generous, it gives us more, if not, there is still higher probability to reach a small amount of profit to close the basket before it goes to loss zone.... 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#49](/thread/post/8595788#post8595788 "Post Permalink")

  * Nov 17, 2015 7:23pm  Nov 17, 2015 7:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8595780#post8595780 "View Quoted Post")
> 
> Disliked
> 
> {quote} I usually set the lot size to 0.1, with perfect hedge calculation enabled and a target profit of 5 USD. Because EA checks if profit is greater than the target profit to close the basket, when price jumps there is a high probability that profit exceeds 5 USD. In my recent trade of GBP red news, it gave me a profit of about 20 USD :-) So, my advice is to set the target profit to a small amount. If the market is generous, it gives you more, if not, there is still higher probability to reach a small amount of profit to close the basket before...
> 
> Ignored

Oh perfect ( i changed it to 10€ but now i took it in 5E) .. thank you very very mutch 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#50](/thread/post/8595795#post8595795 "Post Permalink")

  * Nov 17, 2015 7:28pm  Nov 17, 2015 7:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8595788#post8595788 "View Quoted Post")
> 
> Disliked
> 
> {quote} Oh perfect ( i changed it to 10 but now i took it in 5E) .. thank you very very mutch
> 
> Ignored

You're welcome! :-)  
And no doubt that one can trade higher lot size and accordingly increase the target profit... 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#51](/thread/post/8595818#post8595818 "Post Permalink")

  * Nov 17, 2015 7:38pm  Nov 17, 2015 7:38pm 

  * [ Surgefx](surgefx)

  * | Joined Apr 2015  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=406756)

Please how is the closing option working can it be made to keep the winning trade open while closing the losing trade? cos currently it seems to close the winning trade if the losing hedge trade is closed. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#52](/thread/post/8595831#post8595831 "Post Permalink")

  * Nov 17, 2015 7:41pm  Nov 17, 2015 7:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Surgefx](/thread/post/8595818#post8595818 "View Quoted Post")
> 
> Disliked
> 
> Please how is the closing option working can it be made to keep the winning trade open while closing the losing trade? cos currently it seems to close the winning trade if the losing hedge trade is closed.
> 
> Ignored

If the basket profit exceeds the Take Profit (money) value, the EA closes both positions.  
If the user clicks on Close All button, the EA closes both positions regardless of the profit/loss. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#53](/thread/post/8595858#post8595858 "Post Permalink")

  * Nov 17, 2015 7:50pm  Nov 17, 2015 7:50pm 

  * [ Surgefx](surgefx)

  * | Joined Apr 2015  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=406756)

> [Quoting MathTrader7](/thread/post/8595831#post8595831 "View Quoted Post")
> 
> Disliked
> 
> {quote} If the basket profit exceeds the Take Profit (money) value, the EA closes both positions. If the user clicks on Close All button, the EA closes both positions regardless of the profit/loss.
> 
> Ignored

Fine. But when the user manually closes the losing trade (maybe by setting a SL on it which gets hit like I did) can the winning one be allowed to keep running?. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#54](/thread/post/8595867#post8595867 "Post Permalink")

  * Nov 17, 2015 7:55pm  Nov 17, 2015 7:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Surgefx](/thread/post/8595858#post8595858 "View Quoted Post")
> 
> Disliked
> 
> {quote} Fine. But when the user manually closes the losing trade (maybe by setting a SL on it which gets hit like I did) can the winning one be allowed to keep running?.
> 
> Ignored

The EA won't work correctly if the user manipulates the open positions... 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#55](/thread/post/8595920#post8595920 "Post Permalink")

  * Nov 17, 2015 8:11pm  Nov 17, 2015 8:11pm 

  * [ Surgefx](surgefx)

  * | Joined Apr 2015  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=406756)

> [Quoting MathTrader7](/thread/post/8595867#post8595867 "View Quoted Post")
> 
> Disliked
> 
> {quote} The EA won't work correctly if the user manipulates the open positions...
> 
> Ignored

Please make this EA capable of executing "Let your winners run and cut your losers short! "![](https://resources.faireconomy.media/images/emojis/64/1f624.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#56](/thread/post/8595925#post8595925 "Post Permalink")

  * Nov 17, 2015 8:12pm  Nov 17, 2015 8:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Surgefx](/thread/post/8595920#post8595920 "View Quoted Post")
> 
> Disliked
> 
> {quote} Please make this EA "Let your winners run and cut your losers short! "![](https://resources.faireconomy.media/images/emojis/64/1f624.png?v=15.1)
> 
> Ignored

I'm working on a new version (v1.30, as you can see it on the screenshot I attached above) which adds positions in the direction of the winner instead of closing the loser. More about this when my test is done.... 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#57](/thread/post/8596072#post8596072 "Post Permalink")

  * Edited Nov 18, 2015 12:02pm  Nov 17, 2015 9:22pm | Edited Nov 18, 2015 12:02pm 

  * [ kevinmaroons](kevinmaroons)

  * | Joined Nov 2015  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=434931)

Hi,  
  
Im trading at [PFD-NZ](http://www.pfd-nz.com/vn) and used your EA to my live account for test with 250$ balance and 1:300 of leverage for 100% stop out.  
i have tested on demo and all working great until i traded on live acc. When i pressed Buy/sell then it opened on a buy position at 0.01 volume.  
Pls help me !  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#58](/thread/post/8596113#post8596113 "Post Permalink")

  * Edited 10:04pm  Nov 17, 2015 9:53pm | Edited 10:04pm 

  * [ Surgefx](surgefx)

  * | Joined Apr 2015  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=406756)

> [Quoting kevinmaroons](/thread/post/8596072#post8596072 "View Quoted Post")
> 
> Disliked
> 
> ...... 100% stop out....!
> 
> Ignored

What do you mean? the $250 gone?. Your leverage is too much BTW. A need for stoploss in the EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#59](/thread/post/8596127#post8596127 "Post Permalink")

  * Nov 17, 2015 10:00pm  Nov 17, 2015 10:00pm 

  * [ kevinmaroons](kevinmaroons)

  * | Joined Nov 2015  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=434931)

I mean that when i pressed buy/sell on my live account. The ea opened only buy 0.01 posion instead of 1 buy and 1 sell for 0.1 lot of settings 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#60](/thread/post/8596136#post8596136 "Post Permalink")

  * Nov 17, 2015 10:07pm  Nov 17, 2015 10:07pm 

  * [ yurez83](yurez83)

  * | Joined Nov 2015  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=434939)

> [Quoting MathTrader7](/thread/post/8595925#post8595925 "View Quoted Post")
> 
> Disliked
> 
> {quote} I'm working on a new version (v1.30, as you can see it on the screenshot I attached above) which adds positions in the direction of the winner instead of closing the loser. More about this when my test is done....
> 
> Ignored

Hello dear, MathTrader7. Thank you for the adviser.   
I have a question about his work. When we open the deal before the news and hedzhiruem another couple we did not know what the news will be released - positive or negative for the pair. If we assume we have sold GBP / DRC B and bought the EUR / DRC and the news came out negative for the pound and it because it is very volatile and can move 100 points in the opposite direction. The question then becomes what is the meaning of this short-term hedge? If I know that there are strategies work on the correlation of currencies, but then open the transaction only on the basis of large deviations and correlation of currencies 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#61](/thread/post/8596172#post8596172 "Post Permalink")

  * Nov 17, 2015 10:25pm  Nov 17, 2015 10:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting kevinmaroons](/thread/post/8596072#post8596072 "View Quoted Post")
> 
> Disliked
> 
> Hi, Im trading at PFD-NZ and used your EA to my live account for test with 250$ balance and 1:300 of leverage for 100% stop out. i have tested on demo and all working great until i traded on live acc. When i pressed Buy/sell then it opened on a buy position at 0.01 volume. Pls help me ! Thanks
> 
> Ignored

Check your MT4 Journal tab for any re-quote error. If that is the case, then it means that your broker had rejected to open a Sell position for the hedge symbol. Increase slippage and trade 30 seconds (not 2-3 seconds) before a red news release time. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#62](/thread/post/8596180#post8596180 "Post Permalink")

  * Nov 17, 2015 10:27pm  Nov 17, 2015 10:27pm 

  * [ Traffex](traffex)

  * | Joined Nov 2013  | Status: Trader | [366 Posts](/search?do=process&provider=Member&searchuser=356934)

> [Quoting MathTrader7](/thread/post/8595780#post8595780 "View Quoted Post")
> 
> Disliked
> 
> {quote} I usually set the lot size to 0.1, with perfect hedge calculation enabled and a target profit of 5 USD. Because EA checks if the net profit is greater than the target profit to close the basket, when price jumps there is a high probability that profit exceeds 5 USD. In my recent trade of GBP red news, it gave me a profit of about 20 USD :-) So, my advice is to set the target profit to a small amount. If the market is generous, it gives us more, if not, there is still higher probability to reach a small amount of profit to close the basket...
> 
> Ignored

When you trade a pair with positive correlation, when do you take the Buy/Sell and when the Sell/Buy Button? When do you close manually, before TP or SL is reached ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#63](/thread/post/8596196#post8596196 "Post Permalink")

  * Nov 17, 2015 10:35pm  Nov 17, 2015 10:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Traffex](/thread/post/8596180#post8596180 "View Quoted Post")
> 
> Disliked
> 
> {quote} When you trade a pair with positive correlation, when do you take the Buy/Sell and when the Sell/Buy Button? When do you close manually, before TP or SL is reached ?
> 
> Ignored

No one (except for a few people who are releasing a high impact news data) knows about the outcome of high impact red news. So, what I do is to analyze the recent data of that particular news and guess what would be most likely the outcome. Since I may be wrong, I go for hedging to reduce the possible loss of trading red news. For my take profit rule, see [Post 48](http://www.forexfactory.com/showthread.php?p=8595780#post8595780). For SL, I manually click on Close All button when I feel that it is not promising anymore to keep the positions running. Regarding when to enter, as I mentioned before, I open two positions 30 seconds before a high impact news release time. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#64](/thread/post/8596219#post8596219 "Post Permalink")

  * Nov 17, 2015 10:44pm  Nov 17, 2015 10:44pm 

  * [ Traffex](traffex)

  * | Joined Nov 2013  | Status: Trader | [366 Posts](/search?do=process&provider=Member&searchuser=356934)

> [Quoting MathTrader7](/thread/post/8596196#post8596196 "View Quoted Post")
> 
> Disliked
> 
> {quote} No one (except for a few people who are releasing a high impact news data) knows about the outcome of high impact red news. So, what I do is to analyze the recent data of that particular news and guess what would be most likely the outcome. Since I may be wrong, I go for hedging to reduce the possible loss of trading red news. For my take profit rule, see [Post 48](http://www.forexfactory.com/showthread.php?p=8595780#post8595780). For SL, I manually click on Close All button when I feel that it is not promising anymore to keep...
> 
> Ignored

Thank you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#65](/thread/post/8596231#post8596231 "Post Permalink")

  * Nov 17, 2015 10:48pm  Nov 17, 2015 10:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377125_1.gif) yorkshirelad](yorkshirelad)

  * | Joined Jul 2014  | Status: Trader | [250 Posts](/search?do=process&provider=Member&searchuser=377125)

worked perfectly on IC cheers MT 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#66](/thread/post/8596234#post8596234 "Post Permalink")

  * Nov 17, 2015 10:49pm  Nov 17, 2015 10:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting yorkshirelad](/thread/post/8596231#post8596231 "View Quoted Post")
> 
> Disliked
> 
> worked perfectly on IC cheers MT
> 
> Ignored

You're welcome! :-) 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#67](/thread/post/8596265#post8596265 "Post Permalink")

  * Nov 17, 2015 10:56pm  Nov 17, 2015 10:56pm 

  * [ Traffex](traffex)

  * | Joined Nov 2013  | Status: Trader | [366 Posts](/search?do=process&provider=Member&searchuser=356934)

> [Quoting MathTrader7](/thread/post/8596196#post8596196 "View Quoted Post")
> 
> Disliked
> 
> {quote} No one (except for a few people who are releasing a high impact news data) knows about the outcome of high impact red news. So, what I do is to analyze the recent data of that particular news and guess what would be most likely the outcome. Since I may be wrong, I go for hedging to reduce the possible loss of trading red news. For my take profit rule, see [Post 48](http://www.forexfactory.com/showthread.php?p=8595780#post8595780). For SL, I manually click on Close All button when I feel that it is not promising anymore to keep...
> 
> Ignored

  
I think, mostly the direction of the news-trade is equal to the direction of the last about 5 minutes of the watched pair. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#68](/thread/post/8596272#post8596272 "Post Permalink")

  * Nov 17, 2015 10:58pm  Nov 17, 2015 10:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Traffex](/thread/post/8596265#post8596265 "View Quoted Post")
> 
> Disliked
> 
> {quote} I think, mostly the direction of the news-trade is equal to the direction of the last about 5 minutes of the watched pair.
> 
> Ignored

This needs a study over past bars... 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#69](/thread/post/8596303#post8596303 "Post Permalink")

  * Edited 11:50pm  Nov 17, 2015 11:11pm | Edited 11:50pm 

  * [ kevinmaroons](kevinmaroons)

  * | Joined Nov 2015  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=434931)

> [Quoting MathTrader7](/thread/post/8596172#post8596172 "View Quoted Post")
> 
> Disliked
> 
> {quote} Check your MT4 Journal tab for any re-quote error. If that is the case, then it means that your broker had rejected to open a Sell position for the hedge symbol. Increase slippage and trade 30 seconds (not 2-3 seconds) before a red news release time.
> 
> Ignored

hi MT,  
  
Can you please check the files at the attachment. it showed error but i could not know what is it.  
i can see that in the DEMO account the symbosl go without DOT as normal. ex : **EURUSD USDJPY** and on the Real Account the symbols go with dots. ex: **EURUSD. USDJPY.**  
  
Please help me with this symbols 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: w.jpg
Size: 27 KB](/attachment/image/1794660/thumbnail?d=1447769444)](/attachment/image/1794660?d=1447769444)   
[![Click to Enlarge

Name: Untitled.jpg
Size: 32 KB](/attachment/image/1794661/thumbnail?d=1447769450)](/attachment/image/1794661?d=1447769450)   

Attached Image

![](/attachment/image/1794686?d=1447771730)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#70](/thread/post/8596315#post8596315 "Post Permalink")

  * Nov 17, 2015 11:17pm  Nov 17, 2015 11:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting yurez83](/thread/post/8596136#post8596136 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello dear, MathTrader7. Thank you for the adviser. I have a question about his work. When we open the deal before the news and hedzhiruem another couple we did not know what the news will be released - positive or negative for the pair. If we assume we have sold GBP / DRC B and bought the EUR / DRC and the news came out negative for the pound and it because it is very volatile and can move 100 points in the opposite direction. The question then becomes what is the meaning of this short-term hedge? If I know that there are strategies work...
> 
> Ignored

Sorry I couldn't understand your text because of machine translation (google?) but I think I can refer you to my answer in [Post 63](http://www.forexfactory.com/showthread.php?p=8596196#post8596196). 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#71](/thread/post/8596415#post8596415 "Post Permalink")

  * Edited 4:02am  Nov 18, 2015 12:06am | Edited 4:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting kevinmaroons](/thread/post/8596303#post8596303 "View Quoted Post")
> 
> Disliked
> 
> {quote} hi MT, Can you please check the files at the attachment. it showed error but i could not know what is it. i can see that in the DEMO account the symbosl go without DOT as normal. ex : EURUSD USDJPY and on the Real Account the symbols go with dots. ex: EURUSD. USDJPY. Please help me with this symbols {image} {image} {image}
> 
> Ignored

In real/demo accounts you have to enter the complete name of a symbol. In your example, enter **USDJPY.** (with a dot at the end of the symbol) as hedge symbol in the input settings of the EA (not **USDJPY**) 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#72](/thread/post/8596431#post8596431 "Post Permalink")

  * Nov 18, 2015 12:12am  Nov 18, 2015 12:12am 

  * [ kevinmaroons](kevinmaroons)

  * | Joined Nov 2015  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=434931)

> [Quoting MathTrader7](/thread/post/8596415#post8596415 "View Quoted Post")
> 
> Disliked
> 
> {quote} In real/demo account you have to enter the complete name of a symbol. In your example, enter USDJPY. (with dot at the end of the symbol) as hedge symbol in the input settings of the EA not USDJPY
> 
> Ignored

thanks so much for your help. it working now. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#73](/thread/post/8597177#post8597177 "Post Permalink")

  * Nov 18, 2015 8:33am  Nov 18, 2015 8:33am 

  * [ uzair18](uzair18)

  * | Joined May 2015  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=414029)

> [Quoting MathTrader7](/thread/post/8596415#post8596415 "View Quoted Post")
> 
> Disliked
> 
> {quote} In real/demo accounts you have to enter the complete name of a symbol. In your example, enter USDJPY. (with a dot at the end of the symbol) as hedge symbol in the input settings of the EA (not USDJPY)
> 
> Ignored

What you think the risk reward ratio should be? means if i start the EA and opened up trades then how i will cum to know that will the overall scenerio become positive or not? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#74](/thread/post/8597623#post8597623 "Post Permalink")

  * Nov 18, 2015 5:46pm  Nov 18, 2015 5:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

Good morning MathTrader7 , wich TF do you looking for watching the correlation ? Becouse in different TF there are different % of correlation , yesterday i tried h1 correlation but maybe is less stable than D1 TF ... what do you think ? Thank you in advance ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#75](/thread/post/8597638#post8597638 "Post Permalink")

  * Nov 18, 2015 5:54pm  Nov 18, 2015 5:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8597623#post8597623 "View Quoted Post")
> 
> Disliked
> 
> Good morning MathTrader7 , wich TF do you looking for watching the correlation ? Becouse in different TF there are different % of correlation , yesterday i tried h1 correlation but maybe is less stable than D1 TF ... what do you think ? Thank you in advance ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

Hello LvCa, and good morning to you from Sweden ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
This is a good question! I use H1 open prices of 200 past bars. This is just to identify if the correlation is positive or negative for two symbols so that the EA hides irrelevant buttons.  
  
Best,  
Math 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#76](/thread/post/8597709#post8597709 "Post Permalink")

  * Nov 18, 2015 6:19pm  Nov 18, 2015 6:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8597638#post8597638 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello LvCa, and good morning to you from Sweden ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) This is a good question! I use H1 open prices of 200 past bars. This is just to identify if the correlation is positive or negative for two symbols so that the EA hides irrelevant buttons. Best, Math
> 
> Ignored

oh , so today i will try the h1 200 periods becouse yesterday i whatched 50period ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
Great regards , from Italy 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#77](/thread/post/8597807#post8597807 "Post Permalink")

  * Nov 18, 2015 6:59pm  Nov 18, 2015 6:59pm 

  * [ Surgefx](surgefx)

  * | Joined Apr 2015  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=406756)

I got the EA to buy and sell the same pair by setting the hedge pair to be same with the hedge pair but now the SL of trade in one pair is an issue. Adding additional trades on winning side also means increasing risk which may not be palatable. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#78](/thread/post/8598007#post8598007 "Post Permalink")

  * Nov 18, 2015 8:34pm  Nov 18, 2015 8:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Building Permits** news is scheduled to release in 2 hours. Let's trade it!![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
I go for BUY/BUY on EURUSD hedged with USDJPY.

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#79](/thread/post/8598223#post8598223 "Post Permalink")

  * Nov 18, 2015 10:42pm  Nov 18, 2015 10:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8598007#post8598007 "View Quoted Post")
> 
> Disliked
> 
> Building Permits news is scheduled to release in 2 hours. Let's trade it!![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) I go for BUY/BUY on EURUSD hedged with USDJPY.
> 
> Ignored

Thanks , i dont look mutch movment .. maybe they attend the news '' USD FOMC meeting minuts'' release in 5.20 hours ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) and we' ll can see (maybe) a good movment 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#80](/thread/post/8598240#post8598240 "Post Permalink")

  * Nov 18, 2015 10:52pm  Nov 18, 2015 10:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8598223#post8598223 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks , i dont look mutch movment .. maybe they attend the news '' USD FOMC meeting minuts'' release in 5.20 hours ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) and we' ll can see (maybe) a good movment
> 
> Ignored

The news result was equal to the forecast, so no big jump in the price. I closed the basket at breakeven. Let's wait for another opportunity.![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#81](/thread/post/8598253#post8598253 "Post Permalink")

  * Nov 18, 2015 10:58pm  Nov 18, 2015 10:58pm 

  * [ skoda2008](skoda2008)

  * | Joined Mar 2010  | Status: Trader | [224 Posts](/search?do=process&provider=Member&searchuser=137969)

> [Quoting MathTrader7](/thread/post/8598007#post8598007 "View Quoted Post")
> 
> Disliked
> 
> Building Permits news is scheduled to release in 2 hours. Let's trade it!![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) I go for BUY/BUY on EURUSD hedged with USDJPY.
> 
> Ignored

  
I just tried your EA for the first time on this news release. It all worked okay, except both orders were opened with 0.01 lots, when I set the lot size in the EA to 1.0 lots. Any idea why? This was on [IC Markets](/brokers/ic-markets "View IC Markets Broker Profile"). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#82](/thread/post/8598294#post8598294 "Post Permalink")

  * Nov 18, 2015 11:17pm  Nov 18, 2015 11:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting skoda2008](/thread/post/8598253#post8598253 "View Quoted Post")
> 
> Disliked
> 
> {quote} I just tried your EA for the first time on this news release. It all worked okay, except both orders were opened with 0.01 lots, when I set the lot size in the EA to 1.0 lots. Any idea why? This was on IC Markets.
> 
> Ignored

Mmmm... it shouldn't! But I'll check this issue...  
Thanks for reporting!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#83](/thread/post/8598668#post8598668 "Post Permalink")

  * Nov 19, 2015 2:25am  Nov 19, 2015 2:25am 

  * [ Surgefx](surgefx)

  * | Joined Apr 2015  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=406756)

Since its going to be buy/sell anyway a time settings for the news time will be appropriate in case one will not be available to click during the news time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#84](/thread/post/8598677#post8598677 "Post Permalink")

  * Nov 19, 2015 2:31am  Nov 19, 2015 2:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8598007#post8598007 "View Quoted Post")
> 
> Disliked
> 
> Building Permits news is scheduled to release in 2 hours. Let's trade it!![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) I go for BUY/BUY on EURUSD hedged with USDJPY.
> 
> Ignored

This time i'll try with sell/sell ![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1) ( 1h and 30 min left) , obvius 30 sec before the news ![](https://resources.faireconomy.media/images/emojis/64/1f647-200d-2642-fe0f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#85](/thread/post/8598760#post8598760 "Post Permalink")

  * Nov 19, 2015 3:21am  Nov 19, 2015 3:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8598677#post8598677 "View Quoted Post")
> 
> Disliked
> 
> {quote} This time i'll try with sell/sell ![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1) ( 1h and 30 min left) , obvius 30 sec before the news ![](https://resources.faireconomy.media/images/emojis/64/1f647-200d-2642-fe0f.png?v=15.1)
> 
> Ignored

I have the same plan ;-) 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#86](/thread/post/8598764#post8598764 "Post Permalink")

  * Nov 19, 2015 3:22am  Nov 19, 2015 3:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Surgefx](/thread/post/8598668#post8598668 "View Quoted Post")
> 
> Disliked
> 
> Since its going to be buy/sell anyway a time settings for the news time will be appropriate in case one will not be available to click during the news time.
> 
> Ignored

This is a good idea! But I have to implement net stop loss in money as well. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#87](/thread/post/8598770#post8598770 "Post Permalink")

  * Nov 19, 2015 3:25am  Nov 19, 2015 3:25am 

  * [ Eng.JMD](eng.jmd)

  * | Joined Nov 2015  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=434536)

Good evening,   
This my first post here ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
Just would like to share:  
I opened Hedge Positions with NZDUSD and GBPNZD   
  
since correlation is 90% in 5min and H1   
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 11.png
Size: 8 KB](/attachment/image/1795499/thumbnail?d=1447871120)](/attachment/image/1795499?d=1447871120)   

Every day there is chances

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#88](/thread/post/8598797#post8598797 "Post Permalink")

  * Edited 3:52am  Nov 19, 2015 3:40am | Edited 3:52am 

  * [ Surgefx](surgefx)

  * | Joined Apr 2015  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=406756)

Yes I noticed how important the net SL is today I had gbpusd and usdjpy open for the building permit and both went into loss at some stage and I wondered what will happen if the scenerio continued. Please do me a favor do the SL for individual trade in pips 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#89](/thread/post/8598800#post8598800 "Post Permalink")

  * Nov 19, 2015 3:43am  Nov 19, 2015 3:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Eng.JMD](/thread/post/8598770#post8598770 "View Quoted Post")
> 
> Disliked
> 
> Good evening, This my first post here ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) Just would like to share: I opened Hedge Positions with NZDUSD and GBPNZD since correlation is 90% in 5min and H1 {image}
> 
> Ignored

For which news did you open that basket? 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#90](/thread/post/8598801#post8598801 "Post Permalink")

  * Nov 19, 2015 3:43am  Nov 19, 2015 3:43am 

  * [ Eng.JMD](eng.jmd)

  * | Joined Nov 2015  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=434536)

i have put target to 1000 or close manually 

Every day there is chances

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#91](/thread/post/8598865#post8598865 "Post Permalink")

  * Nov 19, 2015 4:10am  Nov 19, 2015 4:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8598677#post8598677 "View Quoted Post")
> 
> Disliked
> 
> {quote} This time i'll try with sell/sell ![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1) ( 1h and 30 min left) , obvius 30 sec before the news ![](https://resources.faireconomy.media/images/emojis/64/1f647-200d-2642-fe0f.png?v=15.1)
> 
> Ignored

I cashed in about 10 USD for this basket/news.  
Tomorrow, I am going to trade Retail Sales m/m**GBPUSD** and **EURUSD**

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#92](/thread/post/8598910#post8598910 "Post Permalink")

  * Nov 19, 2015 4:19am  Nov 19, 2015 4:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8598865#post8598865 "View Quoted Post")
> 
> Disliked
> 
> {quote} I cashed in about 10 USD for this basket/news. Tomorrow, I am going to trade Retail Sales m/m GBPUSD and EURUSD
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) but i don't understand .. i am in and now in loss of 11 usd ( i dont close it becouse i have 20$ SL ) and i think that EU can go down .  
TP in EA is 5$ (perfect hedge) ![](https://resources.faireconomy.media/images/emojis/64/1f937-200d-2642-fe0f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#93](/thread/post/8598918#post8598918 "Post Permalink")

  * Nov 19, 2015 4:21am  Nov 19, 2015 4:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8598910#post8598910 "View Quoted Post")
> 
> Disliked
> 
> {quote} ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) but i don't understand .. i am in and now in loss of 11 usd ( i dont close it becouse i have 20$ SL ) and i think that EU can go down . TP in EA is 5$ (perfect hedge) ![](https://resources.faireconomy.media/images/emojis/64/1f937-200d-2642-fe0f.png?v=15.1)
> 
> Ignored

What are your lot sizes?  
Did you do Sell/Sell or Buy/Buy? 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#94](/thread/post/8598928#post8598928 "Post Permalink")

  * Nov 19, 2015 4:25am  Nov 19, 2015 4:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8598918#post8598918 "View Quoted Post")
> 
> Disliked
> 
> {quote} What are your lot sizes? Did you do Sell/Sell or Buy/Buy?
> 
> Ignored

sell/sell , lot size 0.1 ( EU/UJ)  
PS : probably it dipend to broker 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#95](/thread/post/8598947#post8598947 "Post Permalink")

  * Nov 19, 2015 4:31am  Nov 19, 2015 4:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8598928#post8598928 "View Quoted Post")
> 
> Disliked
> 
> {quote} sell/sell , lot size 0.1 ( EU/UJ) PS : probably it dipend to broker
> 
> Ignored

The same settings here. However, I disabled perfect hedge lot calculation for this trade. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#96](/thread/post/8599006#post8599006 "Post Permalink")

  * Nov 19, 2015 4:54am  Nov 19, 2015 4:54am 

  * [ johnmack](johnmack)

  * | Joined Nov 2015  | Status: Trader | [15 Posts](/search?do=process&provider=Member&searchuser=435139)

Thanks for this great EA Math!  
  
I tried with the FOMC news today, with original settings (perfect hedge enabled and TP at 5$), EU/UJ, but instead of sell/sell, I went to buy/buy, and got almost 10$ profit on [TickMill](/brokers/tickmill "View Tickmill Broker Profile") ECN. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#97](/thread/post/8599039#post8599039 "Post Permalink")

  * Nov 19, 2015 5:05am  Nov 19, 2015 5:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting johnmack](/thread/post/8599006#post8599006 "View Quoted Post")
> 
> Disliked
> 
> Thanks for this great EA Math! I tried with the FOMC news today, with original settings (perfect hedge enabled and TP at 5$), EU/UJ, but instead of sell/sell, I went to buy/buy, and got almost 10$ profit on TickMill ECN.
> 
> Ignored

You're welcome! :-)  
And good results! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
The beauty of this strategy is that, if we target for a small profit, there will be a high probability to exit with some profit regardless of which button we select to trade. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#98](/thread/post/8599055#post8599055 "Post Permalink")

  * Nov 19, 2015 5:10am  Nov 19, 2015 5:10am 

  * [ Eng.JMD](eng.jmd)

  * | Joined Nov 2015  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=434536)

> [Quoting MathTrader7](/thread/post/8598800#post8598800 "View Quoted Post")
> 
> Disliked
> 
> {quote} For which news did you open that basket?
> 
> Ignored

USD news  
  
during uploading this pic i reached to 220 $  
  
i closed with net profit 166$ 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 11.png
Size: 8 KB](/attachment/image/1795541/thumbnail?d=1447877400)](/attachment/image/1795541?d=1447877400)   

Every day there is chances

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#99](/thread/post/8599056#post8599056 "Post Permalink")

  * Nov 19, 2015 5:11am  Nov 19, 2015 5:11am 

  * [ johnmack](johnmack)

  * | Joined Nov 2015  | Status: Trader | [15 Posts](/search?do=process&provider=Member&searchuser=435139)

If you don't mind, I have some suggestions about it:  
1 - Insert option to automatically open the orders 30 seconds before the hour and minute the user sets. For example. I can check the news for today, go to EA, insert the trading time of the news I want, and then the EA will open the trades for me 30 seconds before that time and day. The EA could also obtain the high impact news automatically, but that takes a lot more time to do I believe.  
2 - Insert option to set a maximum time to wait for the target profit to be reach. If after that time the target has not been reach yet, the EA will set a stop loss or breakeven level and close the order if one of both are hit. I know it will make it more automated and perhaps this is not your intention, but this helps a lot people that may not be available to follow the news 100% of time.  
  
Well, these are my thoughts for now. Thanks a lot! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#100](/thread/post/8599065#post8599065 "Post Permalink")

  * Nov 19, 2015 5:19am  Nov 19, 2015 5:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Eng.JMD](/thread/post/8599055#post8599055 "View Quoted Post")
> 
> Disliked
> 
> {quote} USD news during uploading this pic i reached to 220 $ i closed with net profit 166$ {image}
> 
> Ignored

You opened the basket half an hour before FOMC news release??? 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#101](/thread/post/8599066#post8599066 "Post Permalink")

  * Nov 19, 2015 5:20am  Nov 19, 2015 5:20am 

  * [ johnmack](johnmack)

  * | Joined Nov 2015  | Status: Trader | [15 Posts](/search?do=process&provider=Member&searchuser=435139)

Thanks Math!  
  
I have a doubt regarding the perfect hedge function. Instead of opening 0.08 EU and 0.1 UJ, the most approximated condition woudn't be 0.09 EU and 0.1 UJ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#102](/thread/post/8599078#post8599078 "Post Permalink")

  * Nov 19, 2015 5:25am  Nov 19, 2015 5:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting johnmack](/thread/post/8599056#post8599056 "View Quoted Post")
> 
> Disliked
> 
> 1 -**Insert option to automatically open the orders 30 seconds before the hour and minute the user sets. For example. I can check the news for today, go to EA, insert the trading time of the news I want, and then the EA will open the trades for me 30 seconds before that time and day.** The EA could also obtain the high impact news automatically, but that takes a lot more time to do I believe.  
>  2 - **Insert option to set a maximum time to wait for the target profit to be reach.** If after that time the target has not been reach yet, the EA...
> 
> Ignored

I'll implement the bold suggestions in the next versions. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
I didn't get the stop loss policy from your text. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#103](/thread/post/8599086#post8599086 "Post Permalink")

  * Nov 19, 2015 5:28am  Nov 19, 2015 5:28am 

  * [ Eng.JMD](eng.jmd)

  * | Joined Nov 2015  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=434536)

> [Quoting MathTrader7](/thread/post/8599065#post8599065 "View Quoted Post")
> 
> Disliked
> 
> {quote} You opened the basket half of hour before FOMC news release???
> 
> Ignored

actually i opened it before one hour before the news.  
  
i saw there is a strong correlation from this site on 5 min, hour, daily, weekly all of them above 90% moreover GBPNZD is high voiltry currency. when i opened the EA i saw Buy/Buy or Sell/Sell i press Sell/Sell  
  
<https://www.mataf.net/fr/tools/01-01-correlation>

Every day there is chances

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#104](/thread/post/8599108#post8599108 "Post Permalink")

  * Edited 6:03am  Nov 19, 2015 5:47am | Edited 6:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting johnmack](/thread/post/8599066#post8599066 "View Quoted Post")
> 
> Disliked
> 
> Thanks Math! I have a doubt regarding the perfect hedge function. Instead of opening 0.08 EU and 0.1 UJ, the most approximated condition woudn't be 0.09 EU and 0.1 UJ?
> 
> Ignored

Good question! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
Let me explain it. One pip of one lot USDJPY is worth about 8.1 USD (at the moment of writing this post), while one pip of one lot EURUSD is worth 10.0 USD. In order to equalize the worth of pips, we have to open, for example, 1.00 lot USDJPY and 0.81 lot EURUSD. Now, if both symbols move 10 pips in same direction, EURUSD symbol results in  
  
+10.0 pip x 0.81 lot x 10.0 USD/pip lot = +81 USD  
  
and USDJPY results in  
  
-10.0 pip x 1.00 lot x 8.1 USD/pip lot = -81 USD  
  
if we assume that EURUSD position would be in profit (and consequently USDJPY position would be in loss).  
  
We neglect the small change in one pip worth of USDJPY during the market move, as well as other trade costs such as commision, swap, etc. in this example.  
  
**Note:** It may be better not to call this function as perfect hedge lot size calculation, it's better to be called pip worth equalization. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#105](/thread/post/8599123#post8599123 "Post Permalink")

  * Nov 19, 2015 6:00am  Nov 19, 2015 6:00am 

  * [ Eng.JMD](eng.jmd)

  * | Joined Nov 2015  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=434536)

Mr. MathTrader,  
Check the correlation for EUR/USD and EUR/GBP  
in onada and the other site. it is a very good correlation.   
  
i just jump on them 

Every day there is chances

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#106](/thread/post/8599134#post8599134 "Post Permalink")

  * Nov 19, 2015 6:07am  Nov 19, 2015 6:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8598947#post8598947 "View Quoted Post")
> 
> Disliked
> 
> {quote} The same settings here. However, I disabled perfect hedge lot calculation for this trade.
> 
> Ignored

A ok , finally i close the trade in loss (-11€) becouse i go to sleep and i think that i was unlucky becouse it start in fast profit to 4/4,5 € and after it changed direction .  
Good night all guys ![](https://resources.faireconomy.media/images/emojis/64/1f634.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#107](/thread/post/8599269#post8599269 "Post Permalink")

  * Nov 19, 2015 8:09am  Nov 19, 2015 8:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.40** of the EA released. In this version two additional buttons let the user close main and/or hedge position individually. I updated Post 1. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURUSDH1.png
Size: 48 KB](/attachment/image/1795625/thumbnail?d=1447888155)](/attachment/image/1795625?d=1447888155)   

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#108](/thread/post/8599348#post8599348 "Post Permalink")

  * Nov 19, 2015 9:43am  Nov 19, 2015 9:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25514_6.gif) goldcourse](goldcourse)

  * | Joined Nov 2006  | Status: Go With The Randomness Of Price | [320 Posts](/search?do=process&provider=Member&searchuser=25514)

MathTrader7,  
  
I can't open version 1.4 . Is it due to my platform still on Build 902?  
  
All earlier versions I had no problem.  
  
I'm thanking you in advance for any assistance towards this issue. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#109](/thread/post/8599354#post8599354 "Post Permalink")

  * Nov 19, 2015 9:46am  Nov 19, 2015 9:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting goldcourse](/thread/post/8599348#post8599348 "View Quoted Post")
> 
> Disliked
> 
> MathTrader7, I can't open version 1.4 . Is it due to my platform still on Build 902? All earlier versions I had no problem. I'm thanking you in advance for any assistance towards this issue.
> 
> Ignored

Yes, that's because of your MT4 build 902. You can upgrade by adding MetaQuote-Demo account to your MT4 platform. Then restart it. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#110](/thread/post/8599357#post8599357 "Post Permalink")

  * Nov 19, 2015 9:49am  Nov 19, 2015 9:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25514_6.gif) goldcourse](goldcourse)

  * | Joined Nov 2006  | Status: Go With The Randomness Of Price | [320 Posts](/search?do=process&provider=Member&searchuser=25514)

> [Quoting MathTrader7](/thread/post/8599354#post8599354 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes, that's because of your MT4 build 902. You can upgrade by adding MetaQuote-Demo account to your MT4 platform. Then restart it.
> 
> Ignored

Ok,  
  
Will try that. Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#111](/thread/post/8599891#post8599891 "Post Permalink")

  * Nov 19, 2015 5:36pm  Nov 19, 2015 5:36pm 

  * [ Surgefx](surgefx)

  * | Joined Apr 2015  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=406756)

> [Quoting MathTrader7](/thread/post/8599269#post8599269 "View Quoted Post")
> 
> Disliked
> 
> Version 1.40 of the EA released. In this version two additional buttons let the user close main and/or hedge position individually. I updated Post 1. {image}
> 
> Ignored

During news, the price in most cases moves so fast that clicking either close buttons might not be the most effective thing to do instead a preset stoploss on each trade can be a better option. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#112](/thread/post/8599934#post8599934 "Post Permalink")

  * Nov 19, 2015 5:58pm  Nov 19, 2015 5:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

Good moorning ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
GBP news ''Retail Sales'' probably i will take CHF/JPY -GBP/JPY ; corr. -78% (BUY-BUY)  
I have an hard question that i muast resolve ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) , but is better write it after the news 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#113](/thread/post/8600043#post8600043 "Post Permalink")

  * Nov 19, 2015 6:54pm  Nov 19, 2015 6:54pm 

  * [ Eng.JMD](eng.jmd)

  * | Joined Nov 2015  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=434536)

> [Quoting Eng.JMD](/thread/post/8599123#post8599123 "View Quoted Post")
> 
> Disliked
> 
> Mr. MathTrader, Check the correlation for EUR/USD and EUR/GBP in onada and the other site. it is a very good correlation. i just jump on them
> 
> Ignored

Got 200$ 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: image.jpeg
Size: 50 KB](/attachment/image/1795957/thumbnail?d=1447926853)](/attachment/image/1795957?d=1447926853)   

Every day there is chances

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#114](/thread/post/8600286#post8600286 "Post Permalink")

  * Nov 19, 2015 9:00pm  Nov 19, 2015 9:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

One of the most interesting threads I've found in this year! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
Thank you for sharing. 

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#115](/thread/post/8600289#post8600289 "Post Permalink")

  * Nov 19, 2015 9:02pm  Nov 19, 2015 9:02pm 

  * [ johnmack](johnmack)

  * | Joined Nov 2015  | Status: Trader | [15 Posts](/search?do=process&provider=Member&searchuser=435139)

> [Quoting MathTrader7](/thread/post/8599108#post8599108 "View Quoted Post")
> 
> Disliked
> 
> {quote} Good question! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) Let me explain it. One pip of one lot USDJPY is worth about 8.1 USD (at the moment of writing this post), while one pip of one lot EURUSD is worth 10.0 USD. In order to equalize the worth of pips, we have to open, for example, 1.00 lot USDJPY and 0.81 lot EURUSD. Now, if both symbols move 10 pips in same direction, EURUSD symbol results in +10.0 pip x 0.81 lot x 10.0 USD/pip lot = +81 USD and USDJPY results in -10.0 pip x 1.00 lot x 8.1 USD/pip lot = -81 USD if we assume that EURUSD position would be in profit (and...
> 
> Ignored

Thanks a lot for the answer Math! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#116](/thread/post/8600320#post8600320 "Post Permalink")

  * Nov 19, 2015 9:15pm  Nov 19, 2015 9:15pm 

  * [ johnmack](johnmack)

  * | Joined Nov 2015  | Status: Trader | [15 Posts](/search?do=process&provider=Member&searchuser=435139)

> [Quoting MathTrader7](/thread/post/8599078#post8599078 "View Quoted Post")
> 
> Disliked
> 
> {quote} I'll implement the bold suggestions in the next versions. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) I didn't get the stop loss policy from your text.
> 
> Ignored

Cool thanks again!  
  
Regarding the stop loss suggestion, I mean that after some time set by the user after the news, if the positions aren't in profit, the EA could:  
1 - Set a Stop Loss of $$, which in case is reach it will close both orders, and  
2 - Set a "Negative" Take Profit. For Example: If both orders are showing a loss of -10$, the EA would place a negative Take Profit at -5$. So in case the order's losses reduces from -10$ to -5$, it will close the orders. This is a idea to catch the lowest loss possible. I see some EAs that uses this, and works most of the time, because before going into deeper losses, the market cycles and reduce the losses, before going deep again.  
  
Just some suggestions! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#117](/thread/post/8601236#post8601236 "Post Permalink")

  * Nov 20, 2015 4:00am  Nov 20, 2015 4:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting LvCa](/thread/post/8599934#post8599934 "View Quoted Post")
> 
> Disliked
> 
> Good moorning ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) GBP news ''Retail Sales'' probably i will take CHF/JPY -GBP/JPY ; corr. -78% (BUY-BUY) I have an hard question that i muast resolve ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) , but is better write it after the news
> 
> Ignored

I have a question 'cause I can not understand one thing: if there is' a news should always cover themselves with a couple who are interested in the news, or simply the correlation ??  
(sorry for my English, I make an example) ...  
If the news on the USD will then:  
1- work only on EUR / USD (example) against USD / xxx (only cross with the dollar) ??  
2-Work on EUR / USD vs any cross correlated ??  
  
![](https://resources.faireconomy.media/images/emojis/64/1f615.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/2753.png?v=15.1) , good night all 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#118](/thread/post/8601379#post8601379 "Post Permalink")

  * Edited 6:02am  Nov 20, 2015 5:46am | Edited 6:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.50** of the EA released. In this version the user can enter time of trade to let the EA automatically open two positions. I updated **Post 1**. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURUSDH1.png
Size: 50 KB](/attachment/image/1796409/thumbnail?d=1447965968)](/attachment/image/1796409?d=1447965968)   

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#119](/thread/post/8601406#post8601406 "Post Permalink")

  * Nov 20, 2015 6:17am  Nov 20, 2015 6:17am 

  * [ Eng.JMD](eng.jmd)

  * | Joined Nov 2015  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=434536)

> [Quoting MathTrader7](/thread/post/8601379#post8601379 "View Quoted Post")
> 
> Disliked
> 
> Version 1.50 of the EA released. In this version the user can enter time of trade to let the EA automatically open two positions. I updated Post 1. {image}
> 
> Ignored

Thanks very much. 

Every day there is chances

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#120](/thread/post/8601408#post8601408 "Post Permalink")

  * Nov 20, 2015 6:20am  Nov 20, 2015 6:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar357421_1.gif) bazze](bazze)

  * | Joined Dec 2013  | Status: Trader | [1,135 Posts](/search?do=process&provider=Member&searchuser=357421)

> [Quoting MathTrader7](/thread/post/8601379#post8601379 "View Quoted Post")
> 
> Disliked
> 
> Version 1.50 of the EA released. In this version the user can enter time of trade to let the EA automatically open two positions. I updated Post 1. {image}
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)...Broker, or pc time? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#121](/thread/post/8601421#post8601421 "Post Permalink")

  * Nov 20, 2015 6:34am  Nov 20, 2015 6:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting bazze](/thread/post/8601408#post8601408 "View Quoted Post")
> 
> Disliked
> 
> {quote} ![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)...Broker, or pc time?
> 
> Ignored

This version is in broker time, but I may change it to local PC time in the next version. Let's see how this version works. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#122](/thread/post/8601432#post8601432 "Post Permalink")

  * Nov 20, 2015 6:46am  Nov 20, 2015 6:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar352224_1.gif) dafa](dafa)

  * | Joined Oct 2013  | Status: Trader | [320 Posts](/search?do=process&provider=Member&searchuser=352224)

> [Quoting Eng.JMD](/thread/post/8600043#post8600043 "View Quoted Post")
> 
> Disliked
> 
> {quote} Got 200$ {image}
> 
> Ignored

It's great but what if it goes in opposite direction? You will loss $200? During news nobody knows where the price will go.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#123](/thread/post/8601440#post8601440 "Post Permalink")

  * Nov 20, 2015 6:51am  Nov 20, 2015 6:51am 

  * [ Eng.JMD](eng.jmd)

  * | Joined Nov 2015  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=434536)

> [Quoting dafa](/thread/post/8601432#post8601432 "View Quoted Post")
> 
> Disliked
> 
> {quote} It's great but what if it goes in opposite direction? You will loss $200? During news nobody knows where the price will go..
> 
> Ignored

You are totally right. But I am testing until I understand this EA correctly. 

Every day there is chances

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#124](/thread/post/8601461#post8601461 "Post Permalink")

  * Nov 20, 2015 7:12am  Nov 20, 2015 7:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar352224_1.gif) dafa](dafa)

  * | Joined Oct 2013  | Status: Trader | [320 Posts](/search?do=process&provider=Member&searchuser=352224)

> [Quoting Eng.JMD](/thread/post/8601440#post8601440 "View Quoted Post")
> 
> Disliked
> 
> {quote} You are totally right. But I am testing until I understand this EA correctly.
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) I will test it tomorow 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#125](/thread/post/8601513#post8601513 "Post Permalink")

  * Nov 20, 2015 8:15am  Nov 20, 2015 8:15am 

  * [ Iceberg001](iceberg001)

  * | Joined Oct 2015  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=431667)

Hello [_MathTrader7_ ](http://www.forexfactory.com/mathtrader7)!  
  
I'm basically new in the hedge trading.  
  
The first idea comes to my mind: is it proper to use ADR indicator as an additional correlation factor for calculating the lot sizes?   
  
For example: I want to trade EUR/USD vs NZDUSD. NZDUSD has lower ADR, so it needs extra multiplier (ADR EUR/USD : ADR NZDUSD). Maybe it's not very useful for a news trading, but for basical it should.  
  
The second idea : stop loss for overall loss. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#126](/thread/post/8601768#post8601768 "Post Permalink")

  * Nov 20, 2015 2:14pm  Nov 20, 2015 2:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar357421_1.gif) bazze](bazze)

  * | Joined Dec 2013  | Status: Trader | [1,135 Posts](/search?do=process&provider=Member&searchuser=357421)

> [Quoting MathTrader7](/thread/post/8601421#post8601421 "View Quoted Post")
> 
> Disliked
> 
> {quote} This version is in broker time, but I may change it to local PC time in the next version. Let's see how this version works. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)
> 
> Ignored

Thanks![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#127](/thread/post/8601822#post8601822 "Post Permalink")

  * Nov 20, 2015 3:20pm  Nov 20, 2015 3:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar410964_1.gif) samz321](samz321)

  * | Joined May 2015  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=410964)

> [Quoting MathTrader7](/thread/post/8599354#post8599354 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes, that's because of your MT4 build 902. You can upgrade by adding MetaQuote-Demo account to your MT4 platform. Then restart it.
> 
> Ignored

can you please post the link where can I create demo account for upgrading the MT4 build 902 to 904 ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#128](/thread/post/8602258#post8602258 "Post Permalink")

  * Nov 20, 2015 7:01pm  Nov 20, 2015 7:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.55** of the EA released. In this version the user can specify a net stop loss in money. The EA closes the basket if either SL or TP reaches regardless of being in Manual or Time Based Auto mode. I updated Post 1. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURUSDH1.png
Size: 52 KB](/attachment/image/1796763/thumbnail?d=1448013655)](/attachment/image/1796763?d=1448013655)   

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#129](/thread/post/8602286#post8602286 "Post Permalink")

  * Nov 20, 2015 7:12pm  Nov 20, 2015 7:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar410964_1.gif) samz321](samz321)

  * | Joined May 2015  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=410964)

> [Quoting MathTrader7](/thread/post/8602258#post8602258 "View Quoted Post")
> 
> Disliked
> 
> Version 1.55 of the EA released. In this version the user can specify a net stop loss in money. The EA closes the basket if either SL or TP reaches regardless of being in Manual or Time Based Auto mode. I updated Post 1. {image}
> 
> Ignored

Q:  
1\. How does it calculate the SL ?  
2\. correlation calculation for which timeframe is shown on the chart? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#130](/thread/post/8602354#post8602354 "Post Permalink")

  * Nov 20, 2015 7:51pm  Nov 20, 2015 7:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting samz321](/thread/post/8602286#post8602286 "View Quoted Post")
> 
> Disliked
> 
> {quote} Q: 1. How does it calculate the SL ? 2. correlation calculation for which timeframe is shown on the chart?
> 
> Ignored

A: 1. Let me explain it with an example. You set the SL input to **10.0 USD** , if the sum of profits of positions becomes equal to or less than **-10.0 USD** , the EA closes both positions. I assume that your account balance is in USD in this example.  
  
A: 2. The correlation is 200 H1 Open prices of the symbols. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#131](/thread/post/8602377#post8602377 "Post Permalink")

  * Nov 20, 2015 8:00pm  Nov 20, 2015 8:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar410964_1.gif) samz321](samz321)

  * | Joined May 2015  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=410964)

> [Quoting MathTrader7](/thread/post/8602354#post8602354 "View Quoted Post")
> 
> Disliked
> 
> {quote} A: 1. Let me explain it with an example. You set the SL input to 10.0 USD, if the sum of profits of positions becomes equal to or less than -10.0 USD, the EA closes both positions. I assume that your account balance is in USD in this example. A: 2. The correlation is 200 H1 Open prices of the symbols.
> 
> Ignored

Thanks MathTrader7. Got it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#132](/thread/post/8602392#post8602392 "Post Permalink")

  * Nov 20, 2015 8:08pm  Nov 20, 2015 8:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar410964_1.gif) samz321](samz321)

  * | Joined May 2015  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=410964)

> [Quoting MathTrader7](/thread/post/8602354#post8602354 "View Quoted Post")
> 
> Disliked
> 
> {quote} A: 1. Let me explain it with an example. You set the SL input to 10.0 USD, if the sum of profits of positions becomes equal to or less than -10.0 USD, the EA closes both positions. I assume that your account balance is in USD in this example. A: 2. The correlation is 200 H1 Open prices of the symbols.
> 
> Ignored

Another 2 Q:  
  
1\. which pairs are the best for positive correlation and negative correlation for this EA?  
  
2\. How percentage we should consider for both positive and negative correlation pairs for red news hedging? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#133](/thread/post/8602412#post8602412 "Post Permalink")

  * Edited 8:30pm  Nov 20, 2015 8:14pm | Edited 8:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting samz321](/thread/post/8602392#post8602392 "View Quoted Post")
> 
> Disliked
> 
> {quote} Another 2 Q: 1. which pairs are the best for positive correlation and negative correlation for this EA? 2. How percentage we should consider for both positive and negative correlation pairs for red news hedging?
> 
> Ignored

I personally look at M1 bars of two positively or negatively correlated pairs only at red news time releases to study how they move together. I use H1 correlation with a threshold of 0.5 to quickly filter out non-promising pairs of symbols. For example, if the correlation between two symbols is -0.45, I'll skip to another pair of symbols.  
After finding a pair of symbols with an absolute correlation greater than 0.5, you need to do your homework by studying M1 bars correlation between them at red news time releases. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#134](/thread/post/8602445#post8602445 "Post Permalink")

  * Nov 20, 2015 8:30pm  Nov 20, 2015 8:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar410964_1.gif) samz321](samz321)

  * | Joined May 2015  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=410964)

> [Quoting MathTrader7](/thread/post/8602412#post8602412 "View Quoted Post")
> 
> Disliked
> 
> {quote} I personally look at M1 bars of two positively or negatively pairs only at red news time release to study how they move together. I use H1 correlation with a threshold of 0.5 to quickly filter out non-promising pair of symbols. For example, if the correlation between two symbols is -0.45, I'll skip to another pair of symbols. After finding a pair of symbols with an absolute correlation greater than 0.5, you need to do your homework by studying M1 bars correlation between them at red news time releases.
> 
> Ignored

Gr8 Advice! Many thanks. It will be very much useful for me as I am new in forex. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#135](/thread/post/8602456#post8602456 "Post Permalink")

  * Edited Nov 21, 2015 12:02am  Nov 20, 2015 8:41pm | Edited Nov 21, 2015 12:02am 

  * [ Surgefx](surgefx)

  * | Joined Apr 2015  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=406756)

Nice improvements. No individual SL yet and the additional lots? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#136](/thread/post/8602463#post8602463 "Post Permalink")

  * Nov 20, 2015 8:46pm  Nov 20, 2015 8:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Surgefx](/thread/post/8602456#post8602456 "View Quoted Post")
> 
> Disliked
> 
> Nice improvements. No individual SL yet and the additional of lots?
> 
> Ignored

Not yet! I'll implement them in the next versions. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#137](/thread/post/8602479#post8602479 "Post Permalink")

  * Nov 20, 2015 8:57pm  Nov 20, 2015 8:57pm 

  * [ johnmack](johnmack)

  * | Joined Nov 2015  | Status: Trader | [15 Posts](/search?do=process&provider=Member&searchuser=435139)

> [Quoting MathTrader7](/thread/post/8601379#post8601379 "View Quoted Post")
> 
> Disliked
> 
> Version 1.50 of the EA released. In this version the user can enter time of trade to let the EA automatically open two positions. I updated Post 1. {image}
> 
> Ignored

Awesome thanks for the update Math! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#138](/thread/post/8602626#post8602626 "Post Permalink")

  * Nov 20, 2015 10:20pm  Nov 20, 2015 10:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8602258#post8602258 "View Quoted Post")
> 
> Disliked
> 
> Version 1.55 of the EA released. In this version the user can specify a net stop loss in money. The EA closes the basket if either SL or TP reaches regardless of being in Manual or Time Based Auto mode. I updated Post 1. {image}
> 
> Ignored

Wow , thank you , i will try it now on CAD news.  
I will try USDCAD/GBPCAD sell/buy 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#139](/thread/post/8602950#post8602950 "Post Permalink")

  * Nov 21, 2015 12:51am  Nov 21, 2015 12:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting johnmack](/thread/post/8602479#post8602479 "View Quoted Post")
> 
> Disliked
> 
> {quote} Awesome thanks for the update Math!
> 
> Ignored

You're welcome! :-) 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#140](/thread/post/8602952#post8602952 "Post Permalink")

  * Nov 21, 2015 12:52am  Nov 21, 2015 12:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8602626#post8602626 "View Quoted Post")
> 
> Disliked
> 
> {quote} Wow , thank you , i will try it now on CAD news. I will try USDCAD/GBPCAD sell/buy
> 
> Ignored

How did it work for you? 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#141](/thread/post/8603014#post8603014 "Post Permalink")

  * Nov 21, 2015 1:33am  Nov 21, 2015 1:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar287185_9.gif) jen101](jen101)

  * | Membership Revoked  | Joined Aug 2012 | [5,371 Posts](/search?do=process&provider=Member&searchuser=287185)

Hi MathTrader, I was drawn to this as I was looking for something to compliment my normal swing trading. Well, I downloaded your EA and played around with it for a bit. I tried various things: instead of correlated pair, I used a fast moving pair that had good momentum and a free run, or a pair that was about to hit a major s/r level to split for the hedge and I also tried correlated pairs.  
  
Anyway, here are the results for a few days testing on demo. Obviously it needs some refining on my part ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1), but I think I can get something out of this. Thanks ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)   
  
By the way, today I used GBPCAD and AUDCAD for the CAD news. Got the result ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: account.JPG
Size: 172 KB](/attachment/image/1797051/thumbnail?d=1448037048)](/attachment/image/1797051?d=1448037048)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#142](/thread/post/8603020#post8603020 "Post Permalink")

  * Nov 21, 2015 1:40am  Nov 21, 2015 1:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting jen101](/thread/post/8603014#post8603014 "View Quoted Post")
> 
> Disliked
> 
> Hi MathTrader, I was drawn to this as I was looking for something to compliment my normal swing trading. Well, I downloaded your EA and played around with it for a bit. I tried various things: instead of correlated pair, I used a fast moving pair that had good momentum and a free run, or a pair that was about to hit a major s/r level to split for the hedge and I also tried correlated pairs. Anyway, here are the results for a few days testing on demo. Obviously it needs some refining on my part ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1), but I think I can get something out of this. Thanks...
> 
> Ignored

Good results! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
Hedge trading is not limited to high impact red news, neither to highly correlated pairs of symbols. As you use the EA for various trading styles. Please keep posting your findings if you will ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#143](/thread/post/8603036#post8603036 "Post Permalink")

  * Nov 21, 2015 1:53am  Nov 21, 2015 1:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar287185_9.gif) jen101](jen101)

  * | Membership Revoked  | Joined Aug 2012 | [5,371 Posts](/search?do=process&provider=Member&searchuser=287185)

> [Quoting MathTrader7](/thread/post/8603020#post8603020 "View Quoted Post")
> 
> Disliked
> 
> {quote} Good results! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) Hedge trading is not limited to high impact red news, neither to highly correlated pairs of symbols. As you use the EA for various trading styles. Please keep posting your findings if you will ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

Hedge trading is completely new to me. I am trying to combine it with what I know best. I'll test it for a bit and hopefully I can find something that will consistently work well ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1). Good job on the EA, thanks again, that works perfectly. The timer addition is godsend as I am not often at my desk for long! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#144](/thread/post/8603081#post8603081 "Post Permalink")

  * Nov 21, 2015 2:17am  Nov 21, 2015 2:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8602952#post8602952 "View Quoted Post")
> 
> Disliked
> 
> {quote} How did it work for you?
> 
> Ignored

Hello, i must try again next week , becouse this trade was fast stopped out (loss -5 , 0.1lot , demo ;-) ) for large spread of my broker .  
I must filter the avarage spread (broker) , probably max avarage spread that i want (for me) is 3pips (3€) with SL of 10 or 15  
  
PS : Math i have some idea to test next week , i hope that it will be good ;-) but it isn't just news but also outside those zones ![](https://resources.faireconomy.media/images/emojis/64/1f918.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) . obviously if I will like it I will write my idea 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#145](/thread/post/8603096#post8603096 "Post Permalink")

  * Nov 21, 2015 2:29am  Nov 21, 2015 2:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar287185_9.gif) jen101](jen101)

  * | Membership Revoked  | Joined Aug 2012 | [5,371 Posts](/search?do=process&provider=Member&searchuser=287185)

> [Quoting LvCa](/thread/post/8603081#post8603081 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello, i must try again next week , becouse this trade was fast stopped out (loss -5 , 0.1lot , demo ;-) ) for large spread of my broker . I must filter the avarage spread (broker) , probably max avarage spread that i want (for me) is 3pips (3€) with SL of 10 or 15
> 
> Ignored

Yes, you need a good ecn broker. I am testing on FXOpen, seems fine. I am not currently using the SL feature because I want to try the right level. After I have enough appropriate results I will look at the max drawdown and decide from that. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#146](/thread/post/8603103#post8603103 "Post Permalink")

  * Nov 21, 2015 2:35am  Nov 21, 2015 2:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting jen101](/thread/post/8603096#post8603096 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes, you need a good ecn broker. I am testing on FXOpen, seems fine. I am not currently using the SL feature because I want to try the right level. After I have enough appropriate results I will look at the max drawdown and decide from that.
> 
> Ignored

Thank you for your suggestion ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#147](/thread/post/8603105#post8603105 "Post Permalink")

  * Nov 21, 2015 2:37am  Nov 21, 2015 2:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8603081#post8603081 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello, i must try again next week , becouse this trade was fast stopped out (loss -5 , 0.1lot , demo ;-) ) for large spread of my broker . I must filter the avarage spread (broker) , probably max avarage spread that i want (for me) is 3pips (3) with SL of 10 or 15 PS : Math i have some idea to test next week , i hope that it will be good ;-) but it isn't just news but also outside those zones ![](https://resources.faireconomy.media/images/emojis/64/1f918.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) . obviously if I will like it I will write my idea
> 
> Ignored

Hope it works for you the next time.  
Please feel free to write me your idea. I'm also thinking about a separate EA development based on hedge and correlation to scalp the market here and there. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#148](/thread/post/8603883#post8603883 "Post Permalink")

  * Nov 21, 2015 11:53pm  Nov 21, 2015 11:53pm 

  * [ sebast62](sebast62)

  * | Joined Feb 2015  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=399933)

Hello, excuse my English, @Mathtrader7 : You can add 2 buttons for taking such position; buy / buy and sell / sell, when a high correlation more pips in less time! Thank you in advance! Excellent working !!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#149](/thread/post/8604812#post8604812 "Post Permalink")

  * Nov 23, 2015 10:22am  Nov 23, 2015 10:22am 

  * [ sebast62](sebast62)

  * | Joined Feb 2015  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=399933)

Ok I found !!!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#150](/thread/post/8605075#post8605075 "Post Permalink")

  * Nov 23, 2015 3:10pm  Nov 23, 2015 3:10pm 

  * [ Antony_sg](antony_sg)

  * | Joined Oct 2013  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=352939)

Hello Mathtrader7  
I tried this EA for a few days last week and saw it can do during red news with good results, but now I can't try with your latest vision , bcoz my broker still use MT4 build 902. Can you establish it for all MT4 vision?  
I always try with micro lot size, not demo 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#151](/thread/post/8605699#post8605699 "Post Permalink")

  * Nov 23, 2015 9:24pm  Nov 23, 2015 9:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8603105#post8603105 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hope it works for you the next time. Please feel free to write me your idea. I'm also thinking about a separate EA development based on hedge and correlation to scalp the market here and there.
> 
> Ignored

Good morning , tell my 2cent idea is the minumum that i can do ...  
This is an axample of trading (no news) what i do today :  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: esempio.png
Size: 274 KB](/attachment/image/1798235/thumbnail?d=1448281351)](/attachment/image/1798235?d=1448281351)   

  
It was lucky becouse both went into profit.  
PS : I am a farmer, take my ideas as such ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#152](/thread/post/8605781#post8605781 "Post Permalink")

  * Nov 23, 2015 10:07pm  Nov 23, 2015 10:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar287185_9.gif) jen101](jen101)

  * | Membership Revoked  | Joined Aug 2012 | [5,371 Posts](/search?do=process&provider=Member&searchuser=287185)

> [Quoting LvCa](/thread/post/8605699#post8605699 "View Quoted Post")
> 
> Disliked
> 
> {quote} Good morning , tell my 2cent idea is the minumum that i can do ... This is an axample of trading (no news) what i do today : {image} It was lucky becouse both went into profit. PS : I am a farmer, take my ideas as such ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)
> 
> Ignored

I traded Euro this morning too on the German PMI. News was weak, but USDCAD was looking good for a buy, with a little space left before the reversal zone. So, got a result ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) I think I'm going to have to start looking at this seriously now... ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Great tool, Mathtrader! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: account.JPG
Size: 33 KB](/attachment/image/1798255/thumbnail?d=1448284002)](/attachment/image/1798255?d=1448284002)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#153](/thread/post/8605806#post8605806 "Post Permalink")

  * Nov 23, 2015 10:25pm  Nov 23, 2015 10:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting jen101](/thread/post/8605781#post8605781 "View Quoted Post")
> 
> Disliked
> 
> {quote} I traded Euro this morning too on the German PMI. News was weak, but USDCAD was looking good for a buy, with a little space left before the reversal zone. So, got a result ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) I think I'm going to have to start looking at this seriously now... ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Great tool, Mathtrader! {image}
> 
> Ignored

Wow , good result ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) . You use a very big lot size , not is it too mutch for 1500 account ? ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)  
Ps , now i am looking for EUR/GBP vs EUR/USD (sell/buy but is maybe earlier to take this , if i will have a good signal of short EUR/GBP i will enter ) ![](https://resources.faireconomy.media/images/emojis/64/1f918.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#154](/thread/post/8605828#post8605828 "Post Permalink")

  * Nov 23, 2015 10:37pm  Nov 23, 2015 10:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar287185_9.gif) jen101](jen101)

  * | Membership Revoked  | Joined Aug 2012 | [5,371 Posts](/search?do=process&provider=Member&searchuser=287185)

> [Quoting LvCa](/thread/post/8605806#post8605806 "View Quoted Post")
> 
> Disliked
> 
> {quote} Wow , good result ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) . You use a very big lot size , not is it too mutch for 1500 account ? ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) Ps , now i am looking for EUR/GBP vs EUR/USD (sell/buy but is maybe earlier to take this , if i will have a good signal of short EUR/GBP i will enter ) ![](https://resources.faireconomy.media/images/emojis/64/1f918.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

Well, I'm just playing around... I'm not after many pips. That last trade was 9.6 and 3.7 respectively. See how it goes. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#155](/thread/post/8605912#post8605912 "Post Permalink")

  * Nov 23, 2015 11:18pm  Nov 23, 2015 11:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar410964_1.gif) samz321](samz321)

  * | Joined May 2015  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=410964)

> [Quoting MathTrader7](/thread/post/8603105#post8603105 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hope it works for you the next time. Please feel free to write me your idea. I'm also thinking about a separate EA development based on hedge and correlation to scalp the market here and there.
> 
> Ignored

Issue: If I go for editing the attached EA parameters and then ok for exit the properties, it becomes vanish sometimes not always. It needs to be attached again. My MT4 build is 910. I always change the magic no. for every attached EA on the chart. Can you pls have a look on the issue? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#156](/thread/post/8605967#post8605967 "Post Permalink")

  * Nov 23, 2015 11:43pm  Nov 23, 2015 11:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting jen101](/thread/post/8605781#post8605781 "View Quoted Post")
> 
> Disliked
> 
> {quote} I traded Euro this morning too on the German PMI. News was weak, but USDCAD was looking good for a buy, with a little space left before the reversal zone. So, got a result ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) I think I'm going to have to start looking at this seriously now... ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Great tool, Mathtrader! {image}
> 
> Ignored

Good results!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#157](/thread/post/8605975#post8605975 "Post Permalink")

  * Edited 11:59pm  Nov 23, 2015 11:45pm | Edited 11:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting samz321](/thread/post/8605912#post8605912 "View Quoted Post")
> 
> Disliked
> 
> {quote} Issue: If I go for editing the attached EA parameters and then ok for exit the properties, it becomes vanish sometimes not always. It needs to be attached again. My MT4 build is 910. I always change the magic no. for every attached EA on the chart. Can you pls have a look on the issue?
> 
> Ignored

When it disappears after you edit some of the input settings, do you see a message such as "Auto Trade Time is passed!" on the top-left of the chart? 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#158](/thread/post/8605979#post8605979 "Post Permalink")

  * Nov 23, 2015 11:45pm  Nov 23, 2015 11:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8605699#post8605699 "View Quoted Post")
> 
> Disliked
> 
> {quote} Good morning , tell my 2cent idea is the minumum that i can do ... This is an axample of trading (no news) what i do today : {image} It was lucky becouse both went into profit. PS : I am a farmer, take my ideas as such ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)
> 
> Ignored

Keep posting your findings! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#159](/thread/post/8605996#post8605996 "Post Permalink")

  * Nov 23, 2015 11:53pm  Nov 23, 2015 11:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting LvCa](/thread/post/8605806#post8605806 "View Quoted Post")
> 
> Disliked
> 
> {quote} Wow , good result ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) . You use a very big lot size , not is it too mutch for 1500 account ? ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) Ps , now i am looking for EUR/GBP vs EUR/USD (sell/buy but is maybe earlier to take this , if i will have a good signal of short EUR/GBP i will enter ) ![](https://resources.faireconomy.media/images/emojis/64/1f918.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

It started , i try the perfect hadge (size) of Math7 ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I will stop when 2 stoch (or the two currencies ) are touching each other (or max SL of -5% )   

Attached Image (click to enlarge)

[![Click to Enlarge

Name: esempio.png
Size: 226 KB](/attachment/image/1798340/thumbnail?d=1448290252)](/attachment/image/1798340?d=1448290252)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#160](/thread/post/8606017#post8606017 "Post Permalink")

  * Nov 24, 2015 12:03am  Nov 24, 2015 12:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8605996#post8605996 "View Quoted Post")
> 
> Disliked
> 
> {quote} It started , i try the perfect hadge (size) of Math7 ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) I will stop when 2 stoch (or the two currencies ) are touching each other (or max SL of -5% ) {image}
> 
> Ignored

I think we can make it automate for easier forward testing...![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)  
But first let's see how it works with your test. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#161](/thread/post/8606153#post8606153 "Post Permalink")

  * Edited 1:40am  Nov 24, 2015 1:05am | Edited 1:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8606017#post8606017 "View Quoted Post")
> 
> Disliked
> 
> {quote} I think we can make it automate for easier forward testing...![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) But first let's see how it works with your test.
> 
> Ignored

Yes i must test it atleast for 1 week or more .  
I start this week a test with ONLY hedging sistem and this is the Myfxbook for this test ![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1) : [https://www.myfxbook.com/members/luc...ertura/1432697](https://www.myfxbook.com/members/luca_gr/test-copertura/1432697)  
For today i finish my entries and what i like is that today the DD was very little ( 0.5%) with a good profit of 6% .  
At the end of the week i can do an idea ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#162](/thread/post/8606871#post8606871 "Post Permalink")

  * Nov 24, 2015 11:50am  Nov 24, 2015 11:50am 

  * [ skoda2008](skoda2008)

  * | Joined Mar 2010  | Status: Trader | [224 Posts](/search?do=process&provider=Member&searchuser=137969)

> [Quoting LvCa](/thread/post/8605996#post8605996 "View Quoted Post")
> 
> Disliked
> 
> {quote} It started , i try the perfect hadge (size) of Math7 ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) I will stop when 2 stoch (or the two currencies ) are touching each other (or max SL of -5% )
> 
> Ignored

  
I used to trade in a similar way. It works until (for example) EUR and GBP break their correlation and head off in different directions - which will happen sooner or later. For this reason I like Mathtrader's idea of getting in and out of the market as quickly as possible and relying on the news for volatility, rather than taking longer term trades. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#163](/thread/post/8607004#post8607004 "Post Permalink")

  * Nov 24, 2015 3:22pm  Nov 24, 2015 3:22pm 

  * [ radadiya](radadiya)

  * | Joined Sep 2013  | Status: Trader | [305 Posts](/search?do=process&provider=Member&searchuser=350466)

> [Quoting skoda2008](/thread/post/8606871#post8606871 "View Quoted Post")
> 
> Disliked
> 
> {quote} I used to trade in a similar way. It works until (for example) EUR and GBP break their correlation and head off in different directions - which will happen sooner or later. For this reason I like Mathtrader's idea of getting in and out of the market as quickly as possible and relying on the news for volatility, rather than taking longer term trades.
> 
> Ignored

Hi skoda2008,  
Can you explain me how do you select pair for buy and sell based or correlation. For example from the attached table of correlation of major pair can you identify which pairs should be selected for Buy and which pair for Sell. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: MajorsCorelation.png
Size: 31 KB](/attachment/image/1798683/thumbnail?d=1448346111)](/attachment/image/1798683?d=1448346111)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#164](/thread/post/8607020#post8607020 "Post Permalink")

  * Nov 24, 2015 3:41pm  Nov 24, 2015 3:41pm 

  * [ naveel](naveel)

  * | Joined Oct 2011  | Status: Trader | [66 Posts](/search?do=process&provider=Member&searchuser=198934)

> [Quoting LvCa](/thread/post/8605996#post8605996 "View Quoted Post")
> 
> Disliked
> 
> {quote} It started , i try the perfect hadge (size) of Math7 ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) I will stop when 2 stoch (or the two currencies ) are touching each other (or max SL of -5% ) {image}
> 
> Ignored

Hi!  
  
Can you please share your indicator and template?  
  
Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#165](/thread/post/8607031#post8607031 "Post Permalink")

  * Nov 24, 2015 3:53pm  Nov 24, 2015 3:53pm 

  * [ skoda2008](skoda2008)

  * | Joined Mar 2010  | Status: Trader | [224 Posts](/search?do=process&provider=Member&searchuser=137969)

> [Quoting radadiya](/thread/post/8607004#post8607004 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi skoda2008, Can you explain me how do you select pair for buy and sell based or correlation. For example from the attached table of correlation of major pair can you identify which pairs should be selected for Buy and which pair for Sell.
> 
> Ignored

I didn't use a table or calculations to know which pairs were correlated. Just what I guess you could call fundamentals. For example, AUD and NZD tend to follow each other due to close geographical proximity, very similar political/social climate etc. AUD and CAD being resource based currencies and both stable political environments, etc...  
  
I then used percentage change from yesterday's close (NY Close) as the "difference factor". Buy the one that was underperforming, sell the one that was overperforming. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#166](/thread/post/8607553#post8607553 "Post Permalink")

  * Edited 8:25pm  Nov 24, 2015 7:51pm | Edited 8:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

The first version of the indicator which shows the relative price move between two symbols released. I updated Post 1.  
I think we can use this indicator to trade two correlated symbols ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURUSDH1.png
Size: 54 KB](/attachment/image/1798904/thumbnail?d=1448362231)](/attachment/image/1798904?d=1448362231)   

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#167](/thread/post/8607629#post8607629 "Post Permalink")

  * Nov 24, 2015 8:28pm  Nov 24, 2015 8:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar398921_25.gif) BillYon](billyon)

  * Joined Feb 2015 | Status: Trader | [924 Posts](/search?do=process&provider=Member&searchuser=398921)

> [Quoting MathTrader7](/thread/post/8607553#post8607553 "View Quoted Post")
> 
> Disliked
> 
> The first version of an indicator which shows the relative price move between two symbols released. I updated Post 1. I think we can use this indicator to trade two correlated symbols ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) {image}
> 
> Ignored

  
I would think the momentum indy that you created would be a good addition. Was it called need for speed or something like?  
  
You are looking to benefit from a quick imbalance in the correlation right? 

Solutions ONLY!!!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#168](/thread/post/8607639#post8607639 "Post Permalink")

  * Nov 24, 2015 8:31pm  Nov 24, 2015 8:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting BillYon](/thread/post/8607629#post8607629 "View Quoted Post")
> 
> Disliked
> 
> I would think the momentum indy that you created would be a good addition. Was it called need for speed or something like?
> 
> Ignored

Need for speed? Mmmm.... I remember a good work by [Abokwaik](http://www.forexfactory.com/abokwaik) named Need4Speed Scalping, but it has nothing to do with the strategy we trade in this thread ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  

> [Quoting BillYon](/thread/post/8607629#post8607629 "View Quoted Post")
> 
> Disliked
> 
> You are looking to benefit from a quick imbalance in the correlation right?
> 
> Ignored

Yes, the original idea is to benefit from a quick imbalance in the correlation. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#169](/thread/post/8607650#post8607650 "Post Permalink")

  * Nov 24, 2015 8:39pm  Nov 24, 2015 8:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar398921_25.gif) BillYon](billyon)

  * Joined Feb 2015 | Status: Trader | [924 Posts](/search?do=process&provider=Member&searchuser=398921)

[Abokwaik](http://www.forexfactory.com/abokwaik) Need4Speed Scalping  
  
that's it. Sorry for the mixup.  
  
If that idea could see the imbalance by a momentum burst on one vs the other and trigger the hedge... 

Solutions ONLY!!!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#170](/thread/post/8607655#post8607655 "Post Permalink")

  * Nov 24, 2015 8:42pm  Nov 24, 2015 8:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting naveel](/thread/post/8607020#post8607020 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi! Can you please share your indicator and template? Thanks!
> 
> Ignored

Sure  

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [OverLayChartLINE.mq4](/attachment/file/1798938?d=1448365289) 12 KB | 511 downloads 

  

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Stochastic different pairs 1.7_4.mq4](/attachment/file/1798939?d=1448365323) 19 KB | 537 downloads 

  
  
For the tpl is simply White chart with these 2 indicators 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#171](/thread/post/8607660#post8607660 "Post Permalink")

  * Nov 24, 2015 8:44pm  Nov 24, 2015 8:44pm 

  * [ naveel](naveel)

  * | Joined Oct 2011  | Status: Trader | [66 Posts](/search?do=process&provider=Member&searchuser=198934)

> [Quoting LvCa](/thread/post/8607655#post8607655 "View Quoted Post")
> 
> Disliked
> 
> {quote} Sure {file} {file} For the tpl is simply White chart with these 2 indicators
> 
> Ignored

Many Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#172](/thread/post/8608804#post8608804 "Post Permalink")

  * Nov 25, 2015 7:11am  Nov 25, 2015 7:11am 

  * [ armyda](armyda)

  * | Commercial User  | Joined Apr 2013 | [1,600 Posts](/search?do=process&provider=Member&searchuser=333058)

> [Quoting lvca](/thread/post/8605699#post8605699 "View Quoted Post")
> 
> Disliked
> 
> {quote} good morning , tell my 2cent idea is the minumum that i can do ... This is an axample of trading (no news) what i do today : {image} it was lucky becouse both went into profit. Ps : I am a farmer, take my ideas as such ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)
> 
> Ignored

can you better explaine your strategy ?  
You sell when ?  
You buy when? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#173](/thread/post/8609690#post8609690 "Post Permalink")

  * Nov 25, 2015 7:02pm  Nov 25, 2015 7:02pm 

  * [ pedrosimao](pedrosimao)

  * | Joined Feb 2015  | Status: Trader | [72 Posts](/search?do=process&provider=Member&searchuser=401912)

I am using the latest version and it doesnt open any trades.  
Actually it doesn't update the server time.  
So I think there is a bug with it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#174](/thread/post/8610469#post8610469 "Post Permalink")

  * Nov 26, 2015 12:38am  Nov 26, 2015 12:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting pedrosimao](/thread/post/8609690#post8609690 "View Quoted Post")
> 
> Disliked
> 
> I am using the latest version and it doesnt open any trades. Actually it doesn't update the server time. So I think there is a bug with it.
> 
> Ignored

Do you see any error in the Experts tab of the terminal? 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#175](/thread/post/8610563#post8610563 "Post Permalink")

  * Nov 26, 2015 1:05am  Nov 26, 2015 1:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting armyda](/thread/post/8608804#post8608804 "View Quoted Post")
> 
> Disliked
> 
> {quote} can you better explaine your strategy ? You sell when ? You buy when?
> 
> Ignored

Hello , i need more time for a good test strategy ...for now i have big problems with the negative correlation and repairing some things of positive correlation : i will have an hard job ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#176](/thread/post/8611146#post8611146 "Post Permalink")

  * Nov 26, 2015 8:11am  Nov 26, 2015 8:11am 

  * [ pedrosimao](pedrosimao)

  * | Joined Feb 2015  | Status: Trader | [72 Posts](/search?do=process&provider=Member&searchuser=401912)

> [Quoting MathTrader7](/thread/post/8610469#post8610469 "View Quoted Post")
> 
> Disliked
> 
> {quote} Do you see any error in the Experts tab of the terminal?
> 
> Ignored

It says it doesn't have enough money. But its not true. My account is 5k... and the order should be sized at 0.5 lot...  
I can pretty much open it manually.  
When clicking on the EA buttons. it opens and closes the positions in terms of seconds. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#177](/thread/post/8612447#post8612447 "Post Permalink")

  * Nov 27, 2015 2:55am  Nov 27, 2015 2:55am 

  * [ pedrosimao](pedrosimao)

  * | Joined Feb 2015  | Status: Trader | [72 Posts](/search?do=process&provider=Member&searchuser=401912)

I just found out what the problem was.  
I needed to let charts of all hedge pairs opened. No matter if they were enabled in the market watch window already...  
I have done some three losses today during news. But it is working. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#178](/thread/post/8612451#post8612451 "Post Permalink")

  * Nov 27, 2015 2:57am  Nov 27, 2015 2:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting pedrosimao](/thread/post/8612447#post8612447 "View Quoted Post")
> 
> Disliked
> 
> I just found out what the problem was. I needed to let charts of all hedge pairs opened. No matter if they were enabled in the market watch window already... I have done some three losses today during news. But it is working.
> 
> Ignored

Glad to hear that you managed to find and solve the problem. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#179](/thread/post/8612524#post8612524 "Post Permalink")

  * Nov 27, 2015 4:12am  Nov 27, 2015 4:12am 

  * [ karamaramun](karamaramun)

  * | Joined Dec 2014  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=393975)

> [Quoting radadiya](/thread/post/8607004#post8607004 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi skoda2008, Can you explain me how do you select pair for buy and sell based or correlation. For example from the attached table of correlation of major pair can you identify which pairs should be selected for Buy and which pair for Sell. {image}
> 
> Ignored

I wasn't asked but would like 2 shares my 2 cents. Let's start with the meaning of correlation  
  
1.) 1 = positive correlation; EURUSD GO UP / XXX GO UP ; EURUSD GO DOWN / XXX GO DOWN  
2.) -1 = negative correlation; EURUSD GO UP / XXX GO DOWN; EURUSD GO DOWN / XXX GO UP  
  
The closer to 1 or -1, the higher the chance of 1.) and 2.)  
  
You would want to look for some pair with correlation either close to 1 or -1.  
  
EURUSD/EURGBP = 0.98 (positive)  
  
It means when EU goes up, the chance is EG will go down and vice versa.  
  
So, the hedge then will be "BUY and SELL" or "SELL and BUY"  
  
  
  
But if the correlation is negative then it will be  
  
"BUY and BUY" or "SELL and SELL" 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#180](/thread/post/8612746#post8612746 "Post Permalink")

  * Nov 27, 2015 9:27am  Nov 27, 2015 9:27am 

  * [ radadiya](radadiya)

  * | Joined Sep 2013  | Status: Trader | [305 Posts](/search?do=process&provider=Member&searchuser=350466)

> [Quoting karamaramun](/thread/post/8612524#post8612524 "View Quoted Post")
> 
> Disliked
> 
> {quote} I wasn't asked but would like 2 shares my 2 cents. Let's start with the meaning of correlation 1.) 1 = positive correlation; EURUSD GO UP / XXX GO UP ; EURUSD GO DOWN / XXX GO DOWN 2.) -1 = negative correlation; EURUSD GO UP / XXX GO DOWN; EURUSD GO DOWN / XXX GO UP The closer to 1 or -1, the higher the chance of 1.) and 2.) You would want to look for some pair with correlation either close to 1 or -1. EURUSD/EURGBP = 0.98 (positive) It means when EU goes up, the chance is EG will go down and vice versa. So, the hedge then will be "BUY and...
> 
> Ignored

Thank you! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#181](/thread/post/8613737#post8613737 "Post Permalink")

  * Nov 27, 2015 10:40pm  Nov 27, 2015 10:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

Good morning ,  
If i have different ADR between 2 pairs , is it better to increase the size of the pair with lower adr?  
Example (it is only an example) GBPNZD vs EURJPY :  
GBPNZD : adr 300 , value pips o.7$ (equal to EJ)  
EURJPY : adr 150 , value pips 0.7$ (equal to GN)  
Correlated +80%  
If i buy GBPNZD i must sell the doble size (0.20) of EJ or the size must stay equal (0.10 ) for both pairs ? ![](https://resources.faireconomy.media/images/emojis/64/1f615.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/2753.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#182](/thread/post/8613744#post8613744 "Post Permalink")

  * Nov 27, 2015 10:46pm  Nov 27, 2015 10:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8613737#post8613737 "View Quoted Post")
> 
> Disliked
> 
> Good morning , If i have different ADR between 2 pairs , is it better to increase the size of the pair with lower adr? Example (it is only an example) GBPNZD vs EURJPY : GBPNZD : adr 300 , value pips o.7$ (equal to EJ) EURJPY : adr 150 , value pips 0.7$ (equal to GN) Correlated +80% If i buy GBPNZD i must sell the doble size (0.20) of EJ or the size must stay equal (0.10 ) for both pairs ? ![](https://resources.faireconomy.media/images/emojis/64/1f615.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/2753.png?v=15.1)
> 
> Ignored

Hi LvCa,  
  
I assume that ADR value is statistically valid (averaged over a long period, 200 days or more for example). Then, if you are going to trade for a long term, I would personally go for selling 0.20 EJ. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#183](/thread/post/8613787#post8613787 "Post Permalink")

  * Nov 27, 2015 11:09pm  Nov 27, 2015 11:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8613744#post8613744 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi LvCa, I assume that ADR value is statistically valid (averaged over a long period, 200 days or more for example). Then, if you are going to trade for a long term, I would personally go for selling 0.20 EJ.
> 
> Ignored

ok, thanks I appreciate your suggestion ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#184](/thread/post/8613981#post8613981 "Post Permalink")

  * Nov 28, 2015 12:50am  Nov 28, 2015 12:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar398473_1.gif) eghbaleh](eghbaleh)

  * | Joined Jan 2015  | Status: Trader | [88 Posts](/search?do=process&provider=Member&searchuser=398473)

Hi Math Trader 7  
I have a question!!!  
I am newest in this thread .  
Today release red news of GBP . I selected eur/gbp and gbp/chf for trade with -80 correlation in h1 time frame.  
I selected SELL/SELL in ea settings and after 30-40 min hit to stop loss .  
If i selected BUY/BUY instead of SELL/SELL , my trades result was profit .  
Is it true ???  
My question is how can i understand BUY/BUY is true or SELL/SELL , for same as these pairs ?  
Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#185](/thread/post/8614005#post8614005 "Post Permalink")

  * Nov 28, 2015 1:06am  Nov 28, 2015 1:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting eghbaleh](/thread/post/8613981#post8613981 "View Quoted Post")
> 
> Disliked
> 
> Hi Math Trader 7 I have a question!!! I am newest in this thread . Today release red news of GBP . I selected eur/gbp and gbp/chf for trade with -80 correlation in h1 time frame. I selected SELL/SELL in ea settings and after 30-40 min hit to stop loss . If i selected BUY/BUY instead of SELL/SELL , my trades result was profit . Is it true ??? My question is how can i understand BUY/BUY is true or SELL/SELL , for same as these pairs ? Thank you
> 
> Ignored

Hi eghbaleh,  
  
I traded this red news with GBPUSD and EURGBP, going for SELL/SELL with 0.2 lot size, 10 USD take profit and 30 USD stop loss.  
The reason I chose SELL/SELL is that I observed that GBPUSD is in down trend, so even if the red news would be good for GBP, it could temprary pull up the price (and it turn out to be good for GBP, and GBPUSD went up for one minute or so, but then it returned back to its main down trend). The EA closed both positions in a total profit of about 10 USD. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: GBPUSDM1.png
Size: 29 KB](/attachment/image/1801341/thumbnail?d=1448640404)](/attachment/image/1801341?d=1448640404)   
[![Click to Enlarge

Name: EURGBPM1.png
Size: 30 KB](/attachment/image/1801342/thumbnail?d=1448640410)](/attachment/image/1801342?d=1448640410)   

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#186](/thread/post/8614014#post8614014 "Post Permalink")

  * Edited 1:27am  Nov 28, 2015 1:11am | Edited 1:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar287185_9.gif) jen101](jen101)

  * | Membership Revoked  | Joined Aug 2012 | [5,371 Posts](/search?do=process&provider=Member&searchuser=287185)

> [Quoting eghbaleh](/thread/post/8613981#post8613981 "View Quoted Post")
> 
> Disliked
> 
> Hi Math Trader 7 I have a question!!! I am newest in this thread . Today release red news of GBP . I selected eur/gbp and gbp/chf for trade with -80 correlation in h1 time frame. I selected SELL/SELL in ea settings and after 30-40 min hit to stop loss . If i selected BUY/BUY instead of SELL/SELL , my trades result was profit . Is it true ??? My question is how can i understand BUY/BUY is true or SELL/SELL , for same as these pairs ? Thank you
> 
> Ignored

I traded the same pairs for the GBP release today and chose buy/buy. My reasoning? Look at EurChf. Which is stronger Euro or Swiss Franc? Is it about to hit a S/R level and reverse imminently? It is crucial you use your trading knowledge to decide where EurChf is going. Well, I thought the Euro was stronger so i would want to buy that. The loss on EURGBP was limited due to the strength of the Euro, whereas GBPCHF had a bigger gain due to the weakness of the Swiss Franc. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#187](/thread/post/8614116#post8614116 "Post Permalink")

  * Nov 28, 2015 2:39am  Nov 28, 2015 2:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

> [Quoting Traffex](/thread/post/8596265#post8596265 "View Quoted Post")
> 
> Disliked
> 
> {quote} I think, mostly the direction of the news-trade is equal to the direction of the last about 5 minutes of the watched pair.
> 
> Ignored

Jarratt Davis also told this but personally i doubt it...... 

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#188](/thread/post/8614142#post8614142 "Post Permalink")

  * Nov 28, 2015 3:05am  Nov 28, 2015 3:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

This strategy requires double the trading cost.... Will this affect trading performance in the long run? 

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#189](/thread/post/8614173#post8614173 "Post Permalink")

  * Nov 28, 2015 3:36am  Nov 28, 2015 3:36am 

  * [ dimitri](dimitri)

  * | Joined Oct 2006  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=21677)

Am I missing something? This strategy can be done by taking just one position... You pick the stronger currency and no need to hedge it... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#190](/thread/post/8614640#post8614640 "Post Permalink")

  * Nov 28, 2015 11:56pm  Nov 28, 2015 11:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

Good morning everyone, I have finished the test for the first week of so much chaos in my trade.  
Next week I have to improve absolutely becouse in the forex there is no room for sentiment and I, for now, I have too many of these: I always want two pairs are as close up to give a kiss (if then they make love , It would be even better) as in the old days , or... a clear divorce between them if they are correalte negatively and therefore incompatible.  
Good weekend to everyone. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#191](/thread/post/8614794#post8614794 "Post Permalink")

  * Nov 29, 2015 6:13am  Nov 29, 2015 6:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar398473_1.gif) eghbaleh](eghbaleh)

  * | Joined Jan 2015  | Status: Trader | [88 Posts](/search?do=process&provider=Member&searchuser=398473)

> [Quoting MathTrader7](/thread/post/8614005#post8614005 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi eghbaleh, I traded this red news with GBPUSD and EURGBP, going for SELL/SELL with 0.2 lot size, 10 USD take profit and 30 USD stop loss. The reason I chose SELL/SELL is that I observed that GBPUSD is in down trend, so even if the red news would be good for GBP, it could temprary pull up the price (and it turn out to be good for GBP, and GBPUSD went up for one minute or so, but then it returned back to its main down trend). The EA closed both positions in a total profit of about 10 USD. {image} {image}
> 
> Ignored

Hi Math Trader 7  
I will test it next week and hope to get profit .  
Thank you so much 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#192](/thread/post/8614796#post8614796 "Post Permalink")

  * Nov 29, 2015 6:15am  Nov 29, 2015 6:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar398473_1.gif) eghbaleh](eghbaleh)

  * | Joined Jan 2015  | Status: Trader | [88 Posts](/search?do=process&provider=Member&searchuser=398473)

> [Quoting jen101](/thread/post/8614014#post8614014 "View Quoted Post")
> 
> Disliked
> 
> {quote} I traded the same pairs for the GBP release today and chose buy/buy. My reasoning? Look at EurChf. Which is stronger Euro or Swiss Franc? Is it about to hit a S/R level and reverse imminently? It is crucial you use your trading knowledge to decide where EurChf is going. Well, I thought the Euro was stronger so i would want to buy that. The loss on EURGBP was limited due to the strength of the Euro, whereas GBPCHF had a bigger gain due to the weakness of the Swiss Franc.
> 
> Ignored

Hi Jen101  
Thanks for your good advise . 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#193](/thread/post/8614871#post8614871 "Post Permalink")

  * Nov 29, 2015 10:43am  Nov 29, 2015 10:43am 

  * [ menpowerup](menpowerup)

  * | Joined Jun 2014  | Status: Trader | [49 Posts](/search?do=process&provider=Member&searchuser=375068)

> [Quoting techlover](/thread/post/8590828#post8590828 "View Quoted Post")
> 
> Disliked
> 
> New Version is Perfect ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) {image}
> 
> Ignored

pardon me, for post no. 18 by techlover, why do we open up one buy and the other sell when they are negatively correlated? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#194](/thread/post/8615088#post8615088 "Post Permalink")

  * Nov 29, 2015 9:48pm  Nov 29, 2015 9:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar287185_9.gif) jen101](jen101)

  * | Membership Revoked  | Joined Aug 2012 | [5,371 Posts](/search?do=process&provider=Member&searchuser=287185)

> [Quoting dimitri](/thread/post/8614173#post8614173 "View Quoted Post")
> 
> Disliked
> 
> Am I missing something? This strategy can be done by taking just one position... You pick the stronger currency and no need to hedge it...
> 
> Ignored

If you know which way the news will go.......... Well, I don't ![](https://resources.faireconomy.media/images/emojis/64/1f973.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#195](/thread/post/8615517#post8615517 "Post Permalink")

  * Nov 30, 2015 9:43am  Nov 30, 2015 9:43am 

  * [ dimitri](dimitri)

  * | Joined Oct 2006  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=21677)

> [Quoting jen101](/thread/post/8615088#post8615088 "View Quoted Post")
> 
> Disliked
> 
> {quote} If you know which way the news will go.......... Well, I don't ![](https://resources.faireconomy.media/images/emojis/64/1f973.png?v=15.1)
> 
> Ignored

The thing is... if you want the long term profitability with this system, you need to be on the right side of stronger pair(currency) most of the time. So it means to have more than 50% success rate - you need predict the outcome of news and be on right side, otherwise you will not make profit in the long run. Basically if you find the stronger currency then the outcome of the news is not so important but problem is finding currently strong currency. I did some backtesting with this system for USD/CAD and EUR/CAD from begining of the 2015. The main rule was enter trade couple of seconds before news. I chose only time when US and CAD news were announced togeher(for example, only US and CAD NFP together, US and CAD trade balance together etc). The results were great, around 500 pips. The positions were always long USD/CAD and short EUR/CAD. But similar results, minus trading cost, were if I enter only long USD/CAD. TP for this test was strictly on close of 3 minutes candle. These results are only possible because us dollar has been objectively stronger than cad for last months. I tried test this on 2013 and 2014, but results were break even(because usd not so strong at these times). My conclusion from this is to find stronger currency and enter only one, possibly two positions with hedge. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#196](/thread/post/8615540#post8615540 "Post Permalink")

  * Nov 30, 2015 10:11am  Nov 30, 2015 10:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar167532_2.gif) Kilian19](kilian19)

  * Joined Jan 2011 | Status: Currently in Asia | [839 Posts](/search?do=process&provider=Member&searchuser=167532)

> [Quoting jen101](/thread/post/8615088#post8615088 "View Quoted Post")
> 
> Disliked
> 
> {quote} If you know which way the news will go.......... Well, I don't ![](https://resources.faireconomy.media/images/emojis/64/1f973.png?v=15.1)
> 
> Ignored

But you still need to know it to get an edge.  
  
The problem with this type of trading is that you are still entering a directional bet! This can be best compared with pairs trading in which you usually bet on the mean return of 2 financial instruments. You basically trade how 2 symbols behave relatively to each other, by hedging you still take a bet on which pair will move stronger than the other based on the outcome of the news.  
  
What you are doing is hedge maybe 80% of the movement of the news but your 50% chance of success of being on the correct side of the news does not change. If you are correct the pair will move the same distance apart or together as they will in the opposite case giving you no edge at all.  
  
Example: Pair 1 and Pair 2 are positively correlated and Pair1's value will increase if the news are good.  
  
Positive News:  
  
Long/Short +10  
Short/Long -10  
  
Negative News:  
  
Long/Short -10  
Short/Long +10  
  
The problem is expectations of the news are priced in before the numbers are released meaning that is is only important if the number are better or worse than expected. Those expectations can be found in any news calendar and they come from some of the most reputable bankers (are we going to be more accurate than they are? probably not that's why they are professionals after all).  
  
The exact same result can be achieved by trading a single pair with a smaller lot size. You might get some good results now because you tp is fixed and your sl is unlimited and you let it run until your basket is in profit but that will not yield long term profits.  
  
This type of trading might be useful trading stocks as good news tend to affect the price more heavily than bad news decrease the value of a stock (at least that is what I have heard but I would need to do some number crunching on that one). I doubt that this philosophy can be applied to forex as you are trading pairs instead of a single underlying.  
  
If I am somehow incorrect I am looking forward to someone pointing me out my mistake. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#197](/thread/post/8616204#post8616204 "Post Permalink")

  * Nov 30, 2015 7:15pm  Nov 30, 2015 7:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar287185_9.gif) jen101](jen101)

  * | Membership Revoked  | Joined Aug 2012 | [5,371 Posts](/search?do=process&provider=Member&searchuser=287185)

Looking at the ForexLive calendar at 3pm GMT we have Pending Home Sales as high impact, but not on FF calendar. I might give it a shot. EU and USDCHF are well negatively correlated, so I am trying to work out where EURCHF is going. I don't normally trade that pair and looking at that chart, I would really steer clear, but as I have to make a decision.... currently I would say Euro has the edge, so I would want to buy that. Of course, things can change in a few hours.  
  
If Euro is strong, Swiss Franc weak, and we see USD go up, then the loss on EU would be limited. The gain on CHF would be much bigger relatively, so profit. If USD goes down, then we would see a bigger gain on EU and relatively smaller loss on Chf, so profit. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EurChf.JPG
Size: 456 KB](/attachment/image/1802128/thumbnail?d=1448878448)](/attachment/image/1802128?d=1448878448)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#198](/thread/post/8616796#post8616796 "Post Permalink")

  * Dec 1, 2015 12:50am  Dec 1, 2015 12:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar287185_9.gif) jen101](jen101)

  * | Membership Revoked  | Joined Aug 2012 | [5,371 Posts](/search?do=process&provider=Member&searchuser=287185)

> [Quoting jen101](/thread/post/8616204#post8616204 "View Quoted Post")
> 
> Disliked
> 
> Looking at the ForexLive calendar at 3pm GMT we have Pending Home Sales as high impact, but not on FF calendar. I might give it a shot. EU and USDCHF are well negatively correlated, so I am trying to work out where EURCHF is going. I don't normally trade that pair and looking at that chart, I would really steer clear, but as I have to make a decision.... currently I would say Euro has the edge, so I would want to buy that. Of course, things can change in a few hours. If Euro is strong, Swiss Franc weak, and we see USD go up, then the loss on EU...
> 
> Ignored

EURCHF fell through support, so I sold instead. I have now SL at 2R, because of volatility and extra spread around news time. It doesn't affect my previous trades. With SL at 2R I need to get the buy or sell right much more than half the time! ![](https://resources.faireconomy.media/images/emojis/64/1f61f.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: usd news.JPG
Size: 25 KB](/attachment/image/1802382/thumbnail?d=1448898624)](/attachment/image/1802382?d=1448898624)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#199](/thread/post/8617084#post8617084 "Post Permalink")

  * Dec 1, 2015 3:29am  Dec 1, 2015 3:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar287185_9.gif) jen101](jen101)

  * | Membership Revoked  | Joined Aug 2012 | [5,371 Posts](/search?do=process&provider=Member&searchuser=287185)

Big news day tomorrow. I would like to trade the RBA rate as that is always a good mover, but that's 3:30am for me and I'm not prepared to lose my sleep to be sure which way things are going. Though I think AUDUSD and AUDJPY as a sell/buy. UJ is moving well upwards, currently in a bit of a pullback, but it should bounce up again soon. Anyhow, there's plenty more tomorrow.   
  
If I'm right about this and time will tell, it could be worth a live account soon. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) My normal stuff is soooo slow! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#200](/thread/post/8617111#post8617111 "Post Permalink")

  * Dec 1, 2015 3:56am  Dec 1, 2015 3:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting jen101](/thread/post/8617084#post8617084 "View Quoted Post")
> 
> Disliked
> 
> Big news day tomorrow. I would like to trade the RBA rate as that is always a good mover, but that's 3:30am for me and I'm not prepared to lose my sleep to be sure which way things are going. Though I think AUDUSD and AUDJPY as a sell/buy. UJ is moving well upwards, currently in a bit of a pullback, but it should bounce up again soon. Anyhow, there's plenty more tomorrow. If I'm right about this and time will tell, it could be worth a live account soon. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) My normal stuff is soooo slow!
> 
> Ignored

You are doing your homework very well! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
P.S. You can set the EA to automatically open positions at the time you are asleep. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#201](/thread/post/8617117#post8617117 "Post Permalink")

  * Dec 1, 2015 3:59am  Dec 1, 2015 3:59am 

  * [ Garbucci](garbucci)

  * | Joined Dec 2015  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=436664)

great idea this one, i was actually about to get started. On something similar. Some of my thoughts to help or add , as have spent a fair bit of time analysing this as a system. To fully automate would be an idea. Ie the start of he week, you review the major releases , only preset the entries for the big releases. , smaller news is pointless in the long run.   
  
  
Im not sure if anyone has discovered good raw data on historical and average pip move and time for each release. I found a programme called news trader pro but they are dodgy. Never sent me a license so don't subscribe. But if anyone knows of a source of solid historic data , would be very grateful . As I think this is key.   
  
Eg this would allow you to get more accurate with stop losses and targets.   
I also think that you should have three potential entry types:   
1\. One directional trade , entered one minute before news release, with target and stop , and trailing ? This is for when it is quite obvious which way the release is going to go.   
  
2\. Hedge , same as above opened just before , release. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#202](/thread/post/8617125#post8617125 "Post Permalink")

  * Dec 1, 2015 4:04am  Dec 1, 2015 4:04am 

  * [ Garbucci](garbucci)

  * | Joined Dec 2015  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=436664)

sorry my iPhone is hard work , contd......  
3\. Is a straddle this is riskier as its when slippage can be bad but still a good position in that your orders are preset , and not always both positions will be opened, a safer hedge so to speak .  
  
Some other things: by finding a source of good historic news data , you can actually find the optimum pairs to trade for release , and the optimum targets and safest stop losses.   
And has anyone's tried using fixed spread accounts that stay unchanged for news this maybe a way to avoid slippage etc ?   
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#203](/thread/post/8617407#post8617407 "Post Permalink")

  * Dec 1, 2015 7:27am  Dec 1, 2015 7:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar287185_9.gif) jen101](jen101)

  * | Membership Revoked  | Joined Aug 2012 | [5,371 Posts](/search?do=process&provider=Member&searchuser=287185)

> [Quoting MathTrader7](/thread/post/8617111#post8617111 "View Quoted Post")
> 
> Disliked
> 
> {quote} You are doing your homework very well! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) P.S. You can set the EA to automatically open positions at the time you are asleep.
> 
> Ignored

Thanks. Yes I do use the timer, but I need to see which way things are going, say within half an hour prior. These judgment calls aren't easy, they aren't setups that jump out and hit you in the face! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#204](/thread/post/8619059#post8619059 "Post Permalink")

  * Dec 2, 2015 1:12am  Dec 2, 2015 1:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

UAH! Good start of the week ![](https://resources.faireconomy.media/images/emojis/64/1f917.png?v=15.1) without negative correlation that i lose them.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: TEST.png
Size: 219 KB](/attachment/image/1803312/thumbnail?d=1448986417)](/attachment/image/1803312?d=1448986417)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#205](/thread/post/8621428#post8621428 "Post Permalink")

  * Dec 3, 2015 2:16am  Dec 3, 2015 2:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

oh, have a bad day. I see now that my trades are under a lot of pips but I do not understand: in theory, 80% were positive correlated, now they are at 73%. Probably if I will have to go below the 70% 'close everything in loss ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
EDIT : the cross are CHFJPY vs GBPUSD ( i entered in sell/buy) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#206](/thread/post/8621442#post8621442 "Post Permalink")

  * Dec 3, 2015 2:24am  Dec 3, 2015 2:24am 

  * [ Lorran](lorran)

  * | Joined Dec 2015  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=436930)

The EA doenst work on my Broker(ActivTrade).  
  
Someone knows what? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#207](/thread/post/8621844#post8621844 "Post Permalink")

  * Dec 3, 2015 4:41am  Dec 3, 2015 4:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8621428#post8621428 "View Quoted Post")
> 
> Disliked
> 
> oh, have a bad day. I see now that my trades are under a lot of pips but I do not understand: in theory, 80% were positive correlated, now they are at 73%. Probably if I will have to go below the 70% 'close everything in loss ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) EDIT : the cross are CHFJPY vs GBPUSD ( i entered in sell/buy)
> 
> Ignored

Hi LvCa,  
  
I just wanted to mentioned that I personally never trade two currency pairs with no common currency between them. If I were to trade CHFJPY with another pair, it would be AUDCHF (CHF is the common currency here). 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#208](/thread/post/8622860#post8622860 "Post Permalink")

  * Dec 3, 2015 7:01pm  Dec 3, 2015 7:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8621844#post8621844 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi LvCa, I just wanted to mentioned that I personally never trade two currency pairs with no common currency between them. If I were to trade CHFJPY with another pair, it would be AUDCHF (CHF is the common currency here).
> 
> Ignored

Hello MathTrader7 , it is very intresting ... what do you mentioned i used for the news time but now i will try to trade only piar with common currency .  
Thanks ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
PS : my last test is stopped by a big DD (too mutch risk for me with out filter :-( ) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#209](/thread/post/8623878#post8623878 "Post Permalink")

  * Dec 4, 2015 12:03am  Dec 4, 2015 12:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8622860#post8622860 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello MathTrader7 , it is very intresting ... what do you mentioned i used for the news time but now i will try to trade only piar with common currency . Thanks ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) PS : my last test is stopped by a big DD (too mutch risk for me with out filter :-( )
> 
> Ignored

You're welcome! :-)  
Just another tip: Try to compare the strength of non-common currencies (AUD with respect to JPY, in our example, CHFJPY, AUDCHF) to decide going Long/Short.  
  
Good luck! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
Math 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#210](/thread/post/8624237#post8624237 "Post Permalink")

  * Dec 4, 2015 1:39am  Dec 4, 2015 1:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8623878#post8623878 "View Quoted Post")
> 
> Disliked
> 
> {quote} You're welcome! :-) Just another tip: Try to compare the strength of non-common currencies (AUD with respect to JPY, in our example, CHFJPY, AUDCHF) to decide going Long/Short. Good luck! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) Math
> 
> Ignored

So i' am no sure to have understood well so i do an example becouse this tip could change my system (absolutly )  
Before i traded AUDCHF vs AUDUSD (buy/sell ) with ''common pairs filter'' but without the power filter ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) .. so i could add this power filter :  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: TEST.png
Size: 183 KB](/attachment/image/1805151/thumbnail?d=1449159935)](/attachment/image/1805151?d=1449159935)   

  
  
In the Graph 1 i see that AUDUSD has temporarily follen out with AUDCHF so i will enter only in long AUDCHF and sell AUDUSD : this could be my frist filter BUT.......  
in the graph 2 i see that CHF have more power than USD so this is not the best time to trade them : probably the two couples could go back to kissing when CHF have LESS power than USD (no now)  
  
![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) massimum regard 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#211](/thread/post/8624994#post8624994 "Post Permalink")

  * Edited 8:35am  Dec 4, 2015 7:13am | Edited 8:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8624237#post8624237 "View Quoted Post")
> 
> Disliked
> 
> {quote} So i' am no sure to have understood well so i do an example becouse this tip could change my system (absolutly ) Before i traded AUDCHF vs AUDUSD (buy/sell ) with ''common pairs filter'' but without the power filter ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) .. so i could add this power filter : {image} In the Graph 1 i see that AUDUSD has temporarily follen out with AUDCHF so i will enter only in long AUDCHF and sell AUDUSD : this could be my frist filter BUT....... in the graph 2 i see that CHF have more power than USD so this is not the best time to trade them : probably...
> 
> Ignored

The chart you have attached is a very good example for the explanation. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
**My personal strategy:** Wait for the currency strength meter indicator to show a cross, then there would be a high probability [1] that at least one of the currencies (USD or CHF, in this example) to continue in the direction of the cross. In the cross you highlighted in blue, I would go for selling AUDCHF and buying AUDUSD.  
**Note:** Always check the correlation between two pairs on H1 (base time frame) and make sure that their**absolute correlation** over 200 last bars is more than 0.5 (50%).  
  
[1] keep in mind that no prediction can be made for sure in Forex market!  
  
P.S. Could you please share the currency strength meter indicator? 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#212](/thread/post/8625071#post8625071 "Post Permalink")

  * Dec 4, 2015 8:16am  Dec 4, 2015 8:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8624994#post8624994 "View Quoted Post")
> 
> Disliked
> 
> {quote} The chart you have attached is a very good example for the explanation. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) My personal strategy: Wait for the currency strength meter indicator to show a cross, then there would be a high probability [1] that at least one of the currencies (USD or CHF, in this example) continue in the direction of the cross. In the cross you highlighted in blue, I would go for selling AUDCHF and buying AUDUSD. Note: Always check the correlation between two pairs on H1 (base time frame) and make sure that their absolute correlation over 200 last bars...
> 
> Ignored

Sure , in the setting you can see only the pairs in the grapic or you can select the pair what you want to see .  
(i use ''showPairOnChartOnly'' = True ; tf = 0 so the tf is the tf of the chart)  
Thank you for you suggestion ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Nihilist_CSM_mtf_V2.ex4](/attachment/file/1805437?d=1449184621) 30 KB | 353 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#213](/thread/post/8625075#post8625075 "Post Permalink")

  * Dec 4, 2015 8:20am  Dec 4, 2015 8:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8625071#post8625071 "View Quoted Post")
> 
> Disliked
> 
> {quote} Sure , in the setting you can see only the pairs in the grapic or you can select the pair what you want to see . Thank you for you suggestion ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) {file}
> 
> Ignored

You're welcome! And thanks for the indicator :-)  
  
**P.S.** For those who are wondering why Nihilist_CSM_mtf_V2.ex4 doesn't work, it simply needs the attached indicator, myRSIOMA.ex4, to work properly. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [myRSIOMA.ex4](/attachment/file/1805441?d=1449185215) 4 KB | 408 downloads 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#214](/thread/post/8625085#post8625085 "Post Permalink")

  * Dec 4, 2015 8:32am  Dec 4, 2015 8:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8625071#post8625071 "View Quoted Post")
> 
> Disliked
> 
> {quote} Sure , in the setting you can see only the pairs in the grapic or you can select the pair what you want to see . (i use ''showPairOnChartOnly'' = True ; tf = 0 so the tf is the tf of the chart) Thank you for you suggestion ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) {file}
> 
> Ignored

I may start implementing an EA to automatically trade based on this currency strength meter indicator and [my strategy](http://www.forexfactory.com/showthread.php?p=8624994#post8624994).![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#215](/thread/post/8625111#post8625111 "Post Permalink")

  * Dec 4, 2015 9:04am  Dec 4, 2015 9:04am 

  * [ menpowerup](menpowerup)

  * | Joined Jun 2014  | Status: Trader | [49 Posts](/search?do=process&provider=Member&searchuser=375068)

Hi Mathtrader, ytd there were news for the FOMC member speech at 6:10PM. Expecting the USD to be hawkish than expected, I had alrdy set the EA according to my broker time to execute right on time at 6:10PM:  
  
1) BUY/BUY for USDCHF and EURJPY (both are negatively correlated)  
  
2) SELL/SELL for EURUSD and USDJPY (both negatively correlated)  
  
Am I doing right for the above? Also, the EA does not execute out the actions.. where have I done wrong? Pardon my ignorance.. thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#216](/thread/post/8625142#post8625142 "Post Permalink")

  * Dec 4, 2015 9:44am  Dec 4, 2015 9:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

> [Quoting LvCa](/thread/post/8625071#post8625071 "View Quoted Post")
> 
> Disliked
> 
> {quote} Sure , in the setting you can see only the pairs in the grapic or you can select the pair what you want to see . (i use ''showPairOnChartOnly'' = True ; tf = 0 so the tf is the tf of the chart) Thank you for you suggestion ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) {file}
> 
> Ignored

Hi, LvCa  
Just curious... There are so many CSMs available. Do you find any edge over others in Nihilist's CSM?  
See also: [http://www.forexfactory.com/showthre...87#post8599587](http://www.forexfactory.com/showthread.php?p=8599587#post8599587)  
  
Thanks, 

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#217](/thread/post/8625202#post8625202 "Post Permalink")

  * Dec 4, 2015 10:53am  Dec 4, 2015 10:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

Good source to find which news is worth trading:  
[http://www.forexpeacearmy.com/commun...ng-signals.19/](http://www.forexpeacearmy.com/community/forums/current-forex-trading-signals.19/)  
You can subscribe it to receive daily email notification. 

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#218](/thread/post/8625206#post8625206 "Post Permalink")

  * Dec 4, 2015 10:55am  Dec 4, 2015 10:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

CSM of my choice:  
<http://fxtrade.oanda.com/analysis/currency-heatmap>

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#219](/thread/post/8625678#post8625678 "Post Permalink")

  * Dec 4, 2015 5:33pm  Dec 4, 2015 5:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting heispark](/thread/post/8625142#post8625142 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, LvCa Just curious... There are so many CSMs available. Do you find any edge over others in Nihilist's CSM? See also: [http://www.forexfactory.com/showthre...87#post8599587](http://www.forexfactory.com/showthread.php?p=8599587#post8599587) Thanks,
> 
> Ignored

Hello Heispark ,  
Yesterday i attach the Nihilist'CSM in my chart becouse was the first csm that i found in my platform , and that is ''no digital''( have the line with his cross )... so i must try it to tell you if i will have any edge ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) .  
Thank you for the link ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#220](/thread/post/8625961#post8625961 "Post Permalink")

  * Dec 4, 2015 7:19pm  Dec 4, 2015 7:19pm 

  * [ moncsicsi78](moncsicsi78)

  * | Joined Sep 2011  | Status: Trader | [160 Posts](/search?do=process&provider=Member&searchuser=196773)

> [Quoting Kilian19](/thread/post/8615540#post8615540 "View Quoted Post")
> 
> Disliked
> 
> {quote} But you still need to know it to get an edge. The problem with this type of trading is that you are still entering a directional bet! This can be best compared with pairs trading in which you usually bet on the mean return of 2 financial instruments. You basically trade how 2 symbols behave relatively to each other, by hedging you still take a bet on which pair will move stronger than the other based on the outcome of the news. What you are doing is hedge maybe 80% of the movement of the news but your 50% chance of success of being on the...
> 
> Ignored

You are right.  
And it no needs to make difficult: hedging two currency pairs with a commun currency in them, is the same as to trade only one pair.  
For example: long EURUSD and short GBPUSD = long EURGBP.  
But this doesn't mean that correlation hedge can't work.  
Just no need to make it complicated.  
I use this strategy not just before news, but always, independently from every news or not news, just using simply the OverLayChart indicator, and apply grid if it is necessary (most of the time is necessary.)  
If somebody become ill from using grid, DON'T USE IT! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#221](/thread/post/8626430#post8626430 "Post Permalink")

  * Dec 4, 2015 10:39pm  Dec 4, 2015 10:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

My first live test using NFP. 0.01 lot used and it's closed in profit even before the release...  

Attached Image

![](/attachment/image/1805943?d=1449236231)

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2015-12-04_18-39-46.png
Size: 17 KB](/attachment/image/1805944/thumbnail?d=1449236249)](/attachment/image/1805944?d=1449236249)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2015-12-04_18-50-16.png
Size: 62 KB](/attachment/image/1805945/thumbnail?d=1449236265)](/attachment/image/1805945?d=1449236265)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2015-12-04_22-31-53.png
Size: 6 KB](/attachment/image/1805947/thumbnail?d=1449236280)](/attachment/image/1805947?d=1449236280)   

  
  
More live test will be continued.... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#222](/thread/post/8626782#post8626782 "Post Permalink")

  * Dec 5, 2015 12:06am  Dec 5, 2015 12:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

Another winner. CAD Ivey PMI:  

Attached Image

![](/attachment/image/1806033?d=1449241457)

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2015-12-04_23-11-43.png
Size: 18 KB](/attachment/image/1806034/thumbnail?d=1449241474)](/attachment/image/1806034?d=1449241474)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2015-12-04_23-10-56.png
Size: 63 KB](/attachment/image/1806035/thumbnail?d=1449241490)](/attachment/image/1806035?d=1449241490)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2015-12-05_0-02-08.png
Size: 6 KB](/attachment/image/1806036/thumbnail?d=1449241504)](/attachment/image/1806036?d=1449241504)   

  
  
Getting more interesting.... ![](https://resources.faireconomy.media/images/emojis/64/1f911.png?v=15.1)  
  
Daily News Information: [http://www.forexpeacearmy.com/commun...ng-signals.19/](http://www.forexpeacearmy.com/community/forums/current-forex-trading-signals.19/)  
Currency Correlation: <http://www.myfxbook.com/forex-market/correlation>  
Currency Hit Map: <http://fxtrade.oanda.com/analysis/currency-heatmap>

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#223](/thread/post/8628768#post8628768 "Post Permalink")

  * Dec 7, 2015 1:27am  Dec 7, 2015 1:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar410964_1.gif) samz321](samz321)

  * | Joined May 2015  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=410964)

Hello MathTrader7/anyone,  
  
can you/anyone pls write a simple EA which will open trade according to the following rules for any time frame. Would appreciate very much if you/anyone advise on this to make it perfect.  
  
Entry rules:  
Buy:  
if the bullish candle has long body with no lower wicks (belt hold bullish candle) in down trend market  
  
Sell:  
if the bearish candle has long body and no uppers wicks (belt hold bearish candle) in uptrend market  
  
Exit rules:  
TP: manually assign based on time frame  
SL: manually assign based on time frame  
  
Thanks & Best regards  
SAM 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#224](/thread/post/8628978#post8628978 "Post Permalink")

  * Dec 7, 2015 7:08am  Dec 7, 2015 7:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting heispark](/thread/post/8626782#post8626782 "View Quoted Post")
> 
> Disliked
> 
> Another winner. CAD Ivey PMI: {image} {image} {image} {image} Getting more interesting.... ![](https://resources.faireconomy.media/images/emojis/64/1f911.png?v=15.1)
> 
> Ignored

Good results! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
Please keep posting your findings here. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#225](/thread/post/8629106#post8629106 "Post Permalink")

  * Dec 7, 2015 9:29am  Dec 7, 2015 9:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

> [Quoting MathTrader7](/thread/post/8628978#post8628978 "View Quoted Post")
> 
> Disliked
> 
> {quote} Good results! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) Please keep posting your findings here.
> 
> Ignored

Thank you MT7! I will.  
The news I am interested in this week: [http://www.forexpeacearmy.com/commun...-2015_43243_2F](http://www.forexpeacearmy.com/community/threads/forex-news-trading-plans-for-week-50-dec-6-dec-12-2015.43243/?utm_source=MadMimi&utm_medium=email&utm_content=FNG+and+DTS+Trade+Plans+for+Week+50+2015&utm_campaign=20151207_m128736576_Custom+NEW+HTML+Mailer+Template+-+DO+NOT+DELETE&utm_term=http_3A_2F_2Fwww_forexpeacearmy_com_2Fcommunity_2Fthreads_2Fforex-news-trading-plans-for-week-50-dec-6-dec-12-2015_43243_2F)

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#226](/thread/post/8629108#post8629108 "Post Permalink")

  * Dec 7, 2015 9:31am  Dec 7, 2015 9:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

> [Quoting samz321](/thread/post/8628768#post8628768 "View Quoted Post")
> 
> Disliked
> 
> Hello MathTrader7/anyone, can you/anyone pls write a simple EA which will open trade according to the following rules for any time frame. Would appreciate very much if you/anyone advise on this to make it perfect. Entry rules: Buy: if the bullish candle has long body with no lower wicks (belt hold bullish candle) in down trend market Sell: if the bearish candle has long body and no uppers wicks (belt hold bearish candle) in uptrend market Exit rules: TP: manually assign based on time frame SL: manually assign based on time frame Thanks & Best regards...
> 
> Ignored

You may want to post your request to [http://www.forexfactory.com/showthre...05#post8629105](http://www.forexfactory.com/showthread.php?p=8629105#post8629105) or [https://www.forex-tsd.com/forum/deba...60-coding-help](https://www.forex-tsd.com/forum/debates-discussions/indicators-expert-systems-and-tools/metatrader-4/2360-coding-help), instead of this thread.... ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#227](/thread/post/8631151#post8631151 "Post Permalink")

  * Dec 8, 2015 9:15am  Dec 8, 2015 9:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

Another good source to identify high impact news:  

Inserted Video

  
This weekly video is released every Tuesday either from [https://www.youtube.com/channel/UCcn...xoVdbasgeQc_6w](https://www.youtube.com/channel/UCcnrfjcqqxoVdbasgeQc_6w) or from <http://www.jarrattdavis.com/blog/>. 

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#228](/thread/post/8633462#post8633462 "Post Permalink")

  * Edited 8:48am  Dec 9, 2015 8:36am | Edited 8:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

Here is **the first version** of an EA that trades based on Nihilist Currency Strength Meter indicator. When **1st Currency** and **2nd Currency** power lines cross, the EA opens two hedge positions based on **Common Currency**.  
  
**Note 1:** This EA needs the attached indicators to be copied in <MQL4\Indicators>.  
**Note 2:** This EA is experimental, and is served "as is".  
**Note 3:** The EA automatically detects the correct currency pairs made of the input currencies.  
**Note 4:** The EA works on any time frame (I am testing it on H1 time frame).  
**Note 5:** Attach the EA to one of the pairs you set the EA to trade (for example, the default settings are for AUDUSD and AUDJPY). 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: AUDUSDH1.png
Size: 41 KB](/attachment/image/1808443/thumbnail?d=1449617440)](/attachment/image/1808443?d=1449617440)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [MathTrader7_CSHedgeEA.ex4](/attachment/file/1808447?d=1449617770) 131 KB | 690 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Nihilist_CSM_mtf_V2.ex4](/attachment/file/1808448?d=1449617779) 30 KB | 597 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [myRSIOMA.ex4](/attachment/file/1808449?d=1449617785) 4 KB | 562 downloads 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [View Post](/thread/post/8633466#post8633466)
  * Hidden for breach of [Trader Code of Conduct](/userguide#membership-trader_coc)

  * [topemi](topemi)

  * [#230](/thread/post/8633507#post8633507 "Post Permalink")

  * Dec 9, 2015 9:17am  Dec 9, 2015 9:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

> [Quoting MathTrader7](/thread/post/8633462#post8633462 "View Quoted Post")
> 
> Disliked
> 
> Here is the first version of an EA that trades based on Nihilist Currency Strength Meter indicator. When 1st Currency and 2nd Currency power lines cross, the EA opens two hedge positions based on Common Currency. Note 1: This EA needs the attached indicators to be copied in <MQL4\Indicators>. Note 2: This EA is experimental, and is served "as is". Note 3: The EA automatically detects the correct currency pairs made of the input currencies. Note 4: The EA works on any time frame (I am testing it on H1 time frame). Note 5: Attach the EA to one of...
> 
> Ignored

Thank you for the new tool! Sounds interesting although I don't trust lines crossing stuff any longer.... ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#231](/thread/post/8633644#post8633644 "Post Permalink")

  * Dec 9, 2015 11:10am  Dec 9, 2015 11:10am 

  * [ radadiya](radadiya)

  * | Joined Sep 2013  | Status: Trader | [305 Posts](/search?do=process&provider=Member&searchuser=350466)

> [Quoting MathTrader7](/thread/post/8633462#post8633462 "View Quoted Post")
> 
> Disliked
> 
> Here is the first version of an EA that trades based on Nihilist Currency Strength Meter indicator. When 1st Currency and 2nd Currency power lines cross, the EA opens two hedge positions based on Common Currency. Note 1: This EA needs the attached indicators to be copied in <MQL4\Indicators>. Note 2: This EA is experimental, and is served "as is". Note 3: The EA automatically detects the correct currency pairs made of the input currencies. Note 4: The EA works on any time frame (I am testing it on H1 time frame). Note 5: Attach the EA to one of...
> 
> Ignored

Hi,  
Thank you for all work and providing EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#232](/thread/post/8633812#post8633812 "Post Permalink")

  * Dec 9, 2015 2:40pm  Dec 9, 2015 2:40pm 

  * [ mpradeep](mpradeep)

  * | Joined Apr 2012  | Status: Trader | [168 Posts](/search?do=process&provider=Member&searchuser=246669)

Dear Mathtrader  
  
I tried to put your new CSHedgeEA in EU H1 chart but immidiate it is removing from the chart. Is there any problem?I copied indicator and put in indicator folder also. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#233](/thread/post/8633977#post8633977 "Post Permalink")

  * Dec 9, 2015 4:49pm  Dec 9, 2015 4:49pm 

  * [ Traffex](traffex)

  * | Joined Nov 2013  | Status: Trader | [366 Posts](/search?do=process&provider=Member&searchuser=356934)

> [Quoting mpradeep](/thread/post/8633812#post8633812 "View Quoted Post")
> 
> Disliked
> 
> Dear Mathtrader I tried to put your new CSHedgeEA in EU H1 chart but immidiate it is removing from the chart. Is there any problem?I copied indicator and put in indicator folder also.
> 
> Ignored

**Note 5:** Attach the EA to one of the pairs you set the EA to trade (for example, the default settings are for AUDUSD and AUDJPY).  
Attached Image (click to enlarge) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#234](/thread/post/8634374#post8634374 "Post Permalink")

  * Dec 9, 2015 7:52pm  Dec 9, 2015 7:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting heispark](/thread/post/8633507#post8633507 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thank you for the new tool! Sounds interesting although I don't trust lines crossing stuff any longer.... ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)
> 
> Ignored

You're welcome! :-)  
  
Unfortunately the Nihilist CSM indicator is very slow. I am getting the following messages:

Attached Image (click to enlarge)

[![Click to Enlarge

Name: csm_error.png
Size: 13 KB](/attachment/image/1808791/thumbnail?d=1449658293)](/attachment/image/1808791?d=1449658293)   

  
  
I have to develop a CSM indicator/formula to use in my EA which would be much faster ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#235](/thread/post/8634526#post8634526 "Post Permalink")

  * Dec 9, 2015 9:00pm  Dec 9, 2015 9:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

> [Quoting MathTrader7](/thread/post/8634374#post8634374 "View Quoted Post")
> 
> Disliked
> 
> {quote} You're welcome! :-) Unfortunately the Nihilist CSM indicator is very slow. I am getting the following messages:{image} I have to develop a CSM indicator/formula to use in my EA which would be much faster ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)
> 
> Ignored

Perhaps [Hanover](http://www.forexfactory.com/hanover) can give you some advice or help when you make it....... He's a super expert. 

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#236](/thread/post/8635617#post8635617 "Post Permalink")

  * Dec 10, 2015 3:41am  Dec 10, 2015 3:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting MathTrader7](/thread/post/8634374#post8634374 "View Quoted Post")
> 
> Disliked
> 
> {quote} You're welcome! :-) Unfortunately the Nihilist CSM indicator is very slow. I am getting the following messages:{image} I have to develop a CSM indicator/formula to use in my EA which would be much faster ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)
> 
> Ignored

Hello , becouse this work (trader) is very very hard , it's no easy (abosute no easy!)  
This week i try the csm in digital , becouse the nihilist csm is too big for my little pc so... for now i have success (only 3 days) but i want see in bad days before tell anymore.  
Very good luck at all , i hope to tell good news next week 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#237](/thread/post/8636113#post8636113 "Post Permalink")

  * Dec 10, 2015 7:44am  Dec 10, 2015 7:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8635617#post8635617 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello , becouse this work (trader) is very very hard , it's no easy (abosute no easy!) This week i try the csm in digital , becouse the nihilist csm is too big for my little pc so... for now i have success (only 3 days) but i want see in bad days before tell anymore. Very good luck at all , i hope to tell good news next week
> 
> Ignored

Hi LvCa!  
  
I'm so eager to see your results and know about the strategy.  
  
Please keep updating us with your progress!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
Best,  
Math 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#238](/thread/post/8636114#post8636114 "Post Permalink")

  * Dec 10, 2015 7:45am  Dec 10, 2015 7:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting heispark](/thread/post/8634526#post8634526 "View Quoted Post")
> 
> Disliked
> 
> {quote} Perhaps [Hanover](http://www.forexfactory.com/hanover) can give you some advice or help when you make it....... He's a super expert.
> 
> Ignored

Honover created a [great currency strength indicator](http://www.forexfactory.com/showthread.php?t=163158), however, unfortunately it is very slow (slower than Nihilist's indicator). 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#239](/thread/post/8636117#post8636117 "Post Permalink")

  * Dec 10, 2015 7:47am  Dec 10, 2015 7:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

Anyone got NZD rate decision trade? I set NU/NJ B/S trade and went to bed but f***ing Windows 10 rebooted my PC without notice before the new... ![](https://resources.faireconomy.media/images/emojis/64/1f624.png?v=15.1) By default, Windows 10 regularly reboot without notice after update, even if I have open apps or documents on it! Now I turned on reboot notification. People in M$ are all nuts. I really hate M$ products.... I will run it on my Macbook from next time...  
Guys, when you use Windows 10, be careful!  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2015-12-10_7-45-21.png
Size: 31 KB](/attachment/image/1809394/thumbnail?d=1449701147)](/attachment/image/1809394?d=1449701147)   

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#240](/thread/post/8636119#post8636119 "Post Permalink")

  * Dec 10, 2015 7:49am  Dec 10, 2015 7:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

Here is a screenshot of the beta version of my own currency strength indicator (it is still under development).

Attached Image (click to enlarge)

[![Click to Enlarge

Name: NZDUSDH1.png
Size: 57 KB](/attachment/image/1809395/thumbnail?d=1449701157)](/attachment/image/1809395?d=1449701157)   

  
  
The **blue line** shows the strength of **NZD** while the white line shows the strength of USD. The indicator's base point (reset point in time) is the beginning of the day. What do you think to trade the cross between two currencies strength lines? Did anybody try to trade with such crosses? If so, how profitable is this strategy?![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#241](/thread/post/8636124#post8636124 "Post Permalink")

  * Dec 10, 2015 7:56am  Dec 10, 2015 7:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

> [Quoting MathTrader7](/thread/post/8636119#post8636119 "View Quoted Post")
> 
> Disliked
> 
> Here is a screenshot of the beta version of my own currency strength indicator (it is still under development).{image} The blue line shows the strength of NZD while the white line shows the strength of USD. The indicator's base point (reset point in time) is the beginning of the day. What do you think to trade the cross between two currencies strength lines? Did anybody try to trade with such crosses? If so, how profitable is this strategy?![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)
> 
> Ignored

Just like any other line-crossing strategies (such as MA), it's prone to whipsaw.... 

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#242](/thread/post/8636141#post8636141 "Post Permalink")

  * Dec 10, 2015 8:13am  Dec 10, 2015 8:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting heispark](/thread/post/8636124#post8636124 "View Quoted Post")
> 
> Disliked
> 
> {quote} Just like any other line-crossing strategies (such as MA), it's prone to whipsaw....
> 
> Ignored

So, have you tried a similar strategy based on a cross between two currencies' strength lines? If so, would you please tell me which indicator did you use? 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#243](/thread/post/8636216#post8636216 "Post Permalink")

  * Dec 10, 2015 9:19am  Dec 10, 2015 9:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

> [Quoting MathTrader7](/thread/post/8636141#post8636141 "View Quoted Post")
> 
> Disliked
> 
> {quote} So, have you tried a similar strategy based on a cross between two currencies' strength lines? If so, would you please tell me which indicator did you use?
> 
> Ignored

I tried Nihilist's CSM as well without much success. May others have different experience though... 

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#244](/thread/post/8636238#post8636238 "Post Permalink")

  * Dec 10, 2015 9:34am  Dec 10, 2015 9:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting heispark](/thread/post/8636216#post8636216 "View Quoted Post")
> 
> Disliked
> 
> {quote} I tried Nihilist's CSM as well without much success. May others have different experience though...
> 
> Ignored

Thanks! Let's see how trading based on my CSM would work... I am developing an EA for the cross strategy to do forward test. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#245](/thread/post/8636257#post8636257 "Post Permalink")

  * Dec 10, 2015 9:42am  Dec 10, 2015 9:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

AUD Employment change. One loser... ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2015-12-10_9-41-05.png
Size: 6 KB](/attachment/image/1809479/thumbnail?d=1449708166)](/attachment/image/1809479?d=1449708166)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2015-12-10_9-47-49.png
Size: 37 KB](/attachment/image/1809488/thumbnail?d=1449708501)](/attachment/image/1809488?d=1449708501)   

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#246](/thread/post/8637289#post8637289 "Post Permalink")

  * Dec 10, 2015 9:05pm  Dec 10, 2015 9:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

GBP Rate decision. Market wasn't much impressed by the news and I manually closed the trading with small profit.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2015-12-10_21-03-48.png
Size: 6 KB](/attachment/image/1809904/thumbnail?d=1449749112)](/attachment/image/1809904?d=1449749112)   

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#247](/thread/post/8637528#post8637528 "Post Permalink")

  * Dec 10, 2015 10:33pm  Dec 10, 2015 10:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting heispark](/thread/post/8637251#post8637251 "View Quoted Post")
> 
> Disliked
> 
> I have an idea. What if I hedge using EURUSD and USDCHF? They are almost opposite like a mirror. My broker's swap rate is listed below: EURUSD Long: -2.38 Short: 0.96 USDCHF Long: 1.56 Short: -4.06 So, what if I sell EURUSD and buy USDCHF and keep them open (without stop loss, but only with profit target) till the EA closes the trade when profit taget hits (ex. 20 or 30 pips). Even if the profit target doesn't hit for a long period of time, I will still be collecting small money from swap. Once, PT hits, I open another hedge position. What do you...
> 
> Ignored

I think this strategy is called Carry Trade. And it works if the correlation between two currency pairs holds for a long time and that the broker do not change the swap rates regularly. What is your broker by the way? 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#248](/thread/post/8637567#post8637567 "Post Permalink")

  * Dec 10, 2015 10:44pm  Dec 10, 2015 10:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

> [Quoting MathTrader7](/thread/post/8637528#post8637528 "View Quoted Post")
> 
> Disliked
> 
> {quote} I think this strategy is called Carry Trade. And it works if the correlation between two currency pairs holds for a long time and that the broker do not change the swap rates regularly. What is your broker by the way?
> 
> Ignored

[Pepperstone](/brokers/pepperstone "View Pepperstone Broker Profile"). 

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#249](/thread/post/8637681#post8637681 "Post Permalink")

  * Dec 10, 2015 11:29pm  Dec 10, 2015 11:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

Hello guys itry to tell an idea that i hope it could be good , i dont' know .  
in the graph there are 1EA that i use only as an indicator ( no ea) and an indicator of power ( there are many power indicator and this is the ''cash spitting sensor'') .  
In the ''ea'' are sign in yellow the possible trade with good %correlation , the total spread , etc.. but if we can use the power i think that we can cancel the 3 column with zs indicator and put in only one column with the difference of power.  
In this example :  
AUDJPY/CADJPY ( i filetred the pairs with more than +70%correlation and 4pips max spread )  
% corr = +81%  
diff power is -37.3 = AUDJPY have more power tha CADJPY so...  
...so i could trade long AUDJPY and short CADJPY (obvius AUD have more power than CAD) ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: IDEA.png
Size: 275 KB](/attachment/image/1810042/thumbnail?d=1449757640)](/attachment/image/1810042?d=1449757640)   

  
  
IF it is no an stupid idea and it could be easy to do , i will share the indicators (obvious) if someone want it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#250](/thread/post/8638047#post8638047 "Post Permalink")

  * Dec 11, 2015 1:59am  Dec 11, 2015 1:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388536_1.gif) darpa](darpa)

  * | Joined Nov 2014  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=388536)

> [Quoting LvCa](/thread/post/8637681#post8637681 "View Quoted Post")
> 
> Disliked
> 
> Hello guys itry to tell an idea that i hope it could be good , i dont' know . in the graph there are 1EA that i use only as an indicator ( no ea)......
> 
> Ignored

Have you been profitable or at least tested and got good performance in demo, mixing these indicators and @MathTrader7 EA?  
If so please share them ![](https://resources.faireconomy.media/images/emojis/64/270c-fe0f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#251](/thread/post/8639946#post8639946 "Post Permalink")

  * Dec 11, 2015 10:32pm  Dec 11, 2015 10:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

USD Core Retail Sales. Another small winner...  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2015-12-11_22-31-01.png
Size: 6 KB](/attachment/image/1810801/thumbnail?d=1449840731)](/attachment/image/1810801?d=1449840731)   

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#252](/thread/post/8641792#post8641792 "Post Permalink")

  * Dec 13, 2015 10:54am  Dec 13, 2015 10:54am 

  * [ ArrietaTech](arrietatech)

  * | Joined Oct 2010  | Status: Douche | [268 Posts](/search?do=process&provider=Member&searchuser=158359)

Once I've identified pairs with good correlation, and am close to high impact news:   
  
Which button to press? (Which direction to enter?)  
  
or is this supposed to be indifferent as the hedging takes care of it?  
  
I'm trying to understand how this strategy makes money if we're taking (in theory) perfectly hedged positions.  
  
If someone could post a complete example of a winning trade (in the scenario that everything goes as planned)! it'd be much appreciated by traders like me who are 100% new to this type of strategy.  
  
I've already read the whole thread by the way. Still feel compelled to ask!  
Thx!  
DIego 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#253](/thread/post/8641879#post8641879 "Post Permalink")

  * Dec 13, 2015 2:11pm  Dec 13, 2015 2:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

> [Quoting acostafulano](/thread/post/8641792#post8641792 "View Quoted Post")
> 
> Disliked
> 
> Once I've identified pairs with good correlation, and am close to high impact news: **Which button to press? (Which direction to enter?)** or is this supposed to be indifferent as the hedging takes care of it? I'm trying to understand how this strategy makes money if we're taking (in theory) perfectly hedged positions. If someone could post a complete example of a winning trade (in the scenario that everything goes as planned)! it'd be much appreciated by traders like me who are 100% new to this type of strategy. I've already read the whole thread...
> 
> Ignored

I'd bet for stronger currency against weaker one... Either see currency strength meter or analysis report, or just watch the charts... Of course, none of them can guarantee wining trade you know... And this is imperfect hedge...if it's perfect hedge, you don't make/lose any money. 

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#254](/thread/post/8642011#post8642011 "Post Permalink")

  * Dec 13, 2015 7:41pm  Dec 13, 2015 7:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar340717_1.gif) PBPTaker](pbptaker)

  * | Joined Jun 2013  | Status: Trader | [63 Posts](/search?do=process&provider=Member&searchuser=340717)

> [Quoting MathTrader7](/thread/post/8636238#post8636238 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks! Let's see how trading based on my CSM would work... I am developing an EA for the cross strategy to do forward test.
> 
> Ignored

I also have had bad results with the nihilists CSM. It was simply to CPU intensive especially using many charts . For CSM I'm using the currency strenght meter and (more important) the rsioma v4. This is the best indi I know. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [currency-strength-meter.ex4](/attachment/file/1811510?d=1450003099) 25 KB | 585 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [RSIOMA_v4.ex4](/attachment/file/1811511?d=1450003134) 27 KB | 492 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [RSIOMA_v4.mq4](/attachment/file/1811512?d=1450003140) 11 KB | 644 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#255](/thread/post/8642013#post8642013 "Post Permalink")

  * Dec 13, 2015 7:46pm  Dec 13, 2015 7:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting PBPTaker](/thread/post/8642011#post8642011 "View Quoted Post")
> 
> Disliked
> 
> {quote} I also have had bad results with the nihilists CSM. It was simply to CPU intensive especially using many charts . For CSM I'm using the currency strenght meter and (more important) the rsioma v4. This is the best indi I know. {file} {file} {file}
> 
> Ignored

Hi PBPTaker,  
  
Thanks for the indicators! :-)  
  
Since my CSM indicator is still under development, I'll make an EA using your attached indicators. Let's see how it would work.  
  
Best,  
Math 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#256](/thread/post/8642035#post8642035 "Post Permalink")

  * Dec 13, 2015 8:38pm  Dec 13, 2015 8:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar340717_1.gif) PBPTaker](pbptaker)

  * | Joined Jun 2013  | Status: Trader | [63 Posts](/search?do=process&provider=Member&searchuser=340717)

> [Quoting MathTrader7](/thread/post/8642013#post8642013 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi PBPTaker, Thanks for the indicators! :-) Since my CSM indicator is still under development, I'll make an EA using your attached indicators. Let's see how it would work. Best, Math
> 
> Ignored

Hi MathTrader7. You can't rely on my (it is not my Indi, I've found it somewhere on FF) CSM because it gives you only the current market view (in opposite to the nihilist csm). I've created a powershellscript which agregates the values from the past and two indicators which are getting the values into a file and the second puts the aggregated values back back to the MT4 into global variables. But this is far too complicated (this is because I do not share my powershell script). Perhaps you knwo how to do this using mql.  
  
But using the rsioma it is simply not neccessary to use it. I've modified the TCO-trader to use the rsioma. It works, but it has still to much unnedet code and input parameters in it.  
If you can help to clean my Tco-Trader ... otherwhise you can have it as an idea. I share my things because I also have found those things free available ... 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [TCO_Trader_RSIOMA.ex4](/attachment/file/1811514?d=1450006624) 133 KB | 375 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [TCO_Trader_RSIOMA.mq4](/attachment/file/1811515?d=1450006632) 91 KB | 478 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#257](/thread/post/8642061#post8642061 "Post Permalink")

  * Dec 13, 2015 9:40pm  Dec 13, 2015 9:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

> [Quoting damodaranuda](/thread/post/8638047#post8638047 "View Quoted Post")
> 
> Disliked
> 
> {quote} Have you been profitable or at least tested and got good performance in demo, mixing these indicators and @MathTrader7 EA? If so please share them ![](https://resources.faireconomy.media/images/emojis/64/270c-fe0f.png?v=15.1)
> 
> Ignored

Hello i read your post only now , sorry .  
The last week was good before the big DD of last day that dragged my account in Break even (near break even with 0.6% of profit ) so i think that the problem (for me ) is the bigger size (0.10 on 1000$ demo account) , probably i must test it with half size.  
I upload the cash spitting sensor and the csm that i see now called CC (probably is more light than Nihlist's indicator)  
The EA was only for looking the correaltion , I USE IT ONLY AS AN INDICATOR ( but everyone does as he wishes) .  
  

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Cash Spitting Sensor (e).ex4](/attachment/file/1811521?d=1450010405) 98 KB | 404 downloads 

  

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Cash Spitting Sensor (e).mq4](/attachment/file/1811522?d=1450010414) 40 KB | 507 downloads 

  

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [CC mtf & alerts 2.03 nmc.ex4](/attachment/file/1811523?d=1450010451) 121 KB | 402 downloads 

  

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [CC mtf & alerts 2.03 nmc.mq4](/attachment/file/1811524?d=1450010461) 30 KB | 440 downloads 

  

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [japi-EA-CORR (1).ex4](/attachment/file/1811525?d=1450010474) 144 KB | 487 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [View Post](/thread/post/8642084#post8642084)
  * Hidden for breach of [Trader Code of Conduct](/userguide#membership-trader_coc)

  * [Mnlop500](mnlop500)

  * [#259](/thread/post/8642518#post8642518 "Post Permalink")

  * Dec 14, 2015 8:53am  Dec 14, 2015 8:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

Tradable red news in this week: [http://www.forexpeacearmy.com/commun...19-2015.43319/](http://www.forexpeacearmy.com/community/threads/forex-news-trading-plans-for-week-51-dec-13-dec-19-2015.43319/)

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#260](/thread/post/8644877#post8644877 "Post Permalink")

  * Dec 15, 2015 3:14pm  Dec 15, 2015 3:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar337765_5.gif) dokopy](dokopy)

  * Joined May 2013 | Status: Trader | [894 Posts](/search?do=process&provider=Member&searchuser=337765)

> [Quoting MathTrader7](/thread/post/8624994#post8624994 "View Quoted Post")
> 
> Disliked
> 
> {quote} The chart you have attached is a very good example for the explanation. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) My personal strategy: Wait for the currency strength meter indicator to show a cross, then there would be a high probability [1] that at least one of the currencies (USD or CHF, in this example) to continue in the direction of the cross. In the cross you highlighted in blue, I would go for selling AUDCHF and buying AUDUSD. Note: Always check the correlation between two pairs on H1 (base time frame) and make sure that their absolute correlation over 200 last...
> 
> Ignored

About what currency strength meter indicator write? And what TF is placed? I attach to assess different currency strength meter indicator. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [10.5 CSS 4H 1.0.8_6xxA.ex4](/attachment/file/1812632?d=1450160025) 52 KB | 429 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [10.5 CSS 4H 1.0.8_6xxA.mq4](/attachment/file/1812633?d=1450160038) 32 KB | 526 downloads 

Please excuse the bad English via Google Translate.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#261](/thread/post/8645752#post8645752 "Post Permalink")

  * Dec 15, 2015 10:48pm  Dec 15, 2015 10:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar337765_5.gif) dokopy](dokopy)

  * Joined May 2013 | Status: Trader | [894 Posts](/search?do=process&provider=Member&searchuser=337765)

If you change the variable "Auto Trade Disabled" to "Sell / Sell" (for example).  
Expert Advisor will disappear from the chart. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Axiory MetaTrader 4.jpg
Size: 108 KB](/attachment/image/1812991/thumbnail?d=1450187270)](/attachment/image/1812991?d=1450187270)   

Please excuse the bad English via Google Translate.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#262](/thread/post/8645771#post8645771 "Post Permalink")

  * Edited 11:07pm  Dec 15, 2015 10:55pm | Edited 11:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting dokopy](/thread/post/8645752#post8645752 "View Quoted Post")
> 
> Disliked
> 
> If you change the variable "Auto Trade Disabled" to "Sell / Sell" (for example). Expert Advisor will disappear from the chart. {image}
> 
> Ignored

That's because you haven't set the time at which the EA must execute Sell/Sell. You need to set a time in the future when you are willing the EA execute an action (for example, Sell/Sell) and then changing the input variable "Auto Trade Disabled". 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#263](/thread/post/8646198#post8646198 "Post Permalink")

  * Dec 16, 2015 2:02am  Dec 16, 2015 2:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar337765_5.gif) dokopy](dokopy)

  * Joined May 2013 | Status: Trader | [894 Posts](/search?do=process&provider=Member&searchuser=337765)

> [Quoting MathTrader7](/thread/post/8645771#post8645771 "View Quoted Post")
> 
> Disliked
> 
> {quote} That's because you haven't set the time at which the EA must execute Sell/Sell. You need to set a time in the future when you are willing the EA execute an action (for example, Sell/Sell) and then changing the input variable "Auto Trade Disabled".
> 
> Ignored

It does not help:  
2015.12.19 21:57:00  
2016.11.19 21:57:00 

Please excuse the bad English via Google Translate.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#264](/thread/post/8646709#post8646709 "Post Permalink")

  * Dec 16, 2015 6:25am  Dec 16, 2015 6:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting dokopy](/thread/post/8646198#post8646198 "View Quoted Post")
> 
> Disliked
> 
> {quote} It does not help: 2015.12.19 21:57:00 2016.11.19 21:57:00
> 
> Ignored

I tested it again, and it just works fine! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: USDJPYH1.png
Size: 57 KB](/attachment/image/1813298/thumbnail?d=1450214708)](/attachment/image/1813298?d=1450214708)   

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#265](/thread/post/8646728#post8646728 "Post Permalink")

  * Dec 16, 2015 6:41am  Dec 16, 2015 6:41am 

  * [ ArrietaTech](arrietatech)

  * | Joined Oct 2010  | Status: Douche | [268 Posts](/search?do=process&provider=Member&searchuser=158359)

MathTrader,  
  
I've been playing with the method, just to get the grip of it.  
  
Ok, I have not been particularly entering trades precisely at times right before the news, but I did enter when there was some volatility as to have some movement and test the method.  
  
I've had 5 winning / 3 losing combinations, for a combined Loss of Around US$10, considering spread and commissions  
  
I don't understand how this is supposed to make money, if this is always depending if you enter the "good" or the "bad" side of a symbols movement.  
  
How is having two trades supposed to cover the higher trading costs in the long run?  
Someone please explain the underlying concept of the method.  
  
Thanks! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Captura.PNG
Size: 102 KB](/attachment/image/1813307/thumbnail?d=1450215649)](/attachment/image/1813307?d=1450215649)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#266](/thread/post/8646743#post8646743 "Post Permalink")

  * Dec 16, 2015 6:53am  Dec 16, 2015 6:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting acostafulano](/thread/post/8646728#post8646728 "View Quoted Post")
> 
> Disliked
> 
> MathTrader, I've been playing with the method, just to get the grip of it. Ok, I have not been particularly entering trades precisely at times right before the news, but I did enter when there was some volatility as to have some movement and test the method. I've had 5 winning / 3 losing combinations, for a combined Loss of Around US$10, considering spread and commissions I don't understand how this is supposed to make money, if this is always depending if you enter the "good" or the "bad" side of a symbols movement. How is having two trades supposed...
> 
> Ignored

Hi acostafulano,  
  
I have already mentioned my strategy in previous posts, but I collect them here and later put them in Post 1.  
  
**How do I trade with this strategy:**  
1\. Choose a high impact red news of a major currency, for example AUD.  
2\. Choose two other major currencies to pair with AUD such that the absolute correlation of two pairs is greater than 0.5, for example AUDUSD and AUDCAD.  
3\. A few minutes before the news release time, look at a currency strength meter to observe which of above two currencies (USD or CAD) is more powerful.  
4\. Select a trade button according to both the sign of correlation (this can be automatically done by the EA for you), and the strongest currency you identified in the previous step.  
  
**Note:** There is no holy grail strategy that makes green pips all the time. Above steps are my own strategy to trade with this EA.  
  
Best,  
Math 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#267](/thread/post/8650530#post8650530 "Post Permalink")

  * Dec 17, 2015 9:58pm  Dec 17, 2015 9:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

Is there any body who is testing **MathTrader7_CSHedgeEA.ex4** EA? 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#268](/thread/post/8654009#post8654009 "Post Permalink")

  * Dec 19, 2015 4:45pm  Dec 19, 2015 4:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar337765_5.gif) dokopy](dokopy)

  * Joined May 2013 | Status: Trader | [894 Posts](/search?do=process&provider=Member&searchuser=337765)

CADCHF buy + EURCAD buy = PT, CADCHF sell + EURCAD sell = SL 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: H1.jpg
Size: 78 KB](/attachment/image/1815957/thumbnail?d=1450511017)](/attachment/image/1815957?d=1450511017)   
[![Click to Enlarge

Name: M30.jpg
Size: 77 KB](/attachment/image/1815959/thumbnail?d=1450511039)](/attachment/image/1815959?d=1450511039)   
[![Click to Enlarge

Name: M15.jpg
Size: 82 KB](/attachment/image/1815960/thumbnail?d=1450511060)](/attachment/image/1815960?d=1450511060)   
[![Click to Enlarge

Name: M5.jpg
Size: 90 KB](/attachment/image/1815961/thumbnail?d=1450511082)](/attachment/image/1815961?d=1450511082)   
[![Click to Enlarge

Name: M1.jpg
Size: 78 KB](/attachment/image/1815962/thumbnail?d=1450511099)](/attachment/image/1815962?d=1450511099)   
[![Click to Enlarge

Name: M1 after.jpg
Size: 84 KB](/attachment/image/1815963/thumbnail?d=1450511118)](/attachment/image/1815963?d=1450511118)   

Please excuse the bad English via Google Translate.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#269](/thread/post/8654497#post8654497 "Post Permalink")

  * Dec 20, 2015 6:48am  Dec 20, 2015 6:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

***** Hedge Move Indicator *****

  
**Version 1.10** of the indicator released. The indicator shows the relative price move between two symbols. I updated Post 1.

Attached Image (click to enlarge)

[![Click to Enlarge

Name: HedgeMove.png
Size: 60 KB](/attachment/image/1816144/thumbnail?d=1450561723)](/attachment/image/1816144?d=1450561723)   

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#270](/thread/post/8654504#post8654504 "Post Permalink")

  * Dec 20, 2015 6:57am  Dec 20, 2015 6:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.60** of the EA released. In this version a few bugs fixed. I updated Post 1. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#271](/thread/post/8657132#post8657132 "Post Permalink")

  * Dec 22, 2015 2:26pm  Dec 22, 2015 2:26pm 

  * [ karamaramun](karamaramun)

  * | Joined Dec 2014  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=393975)

> [Quoting MathTrader7](/thread/post/8654497#post8654497 "View Quoted Post")
> 
> Disliked
> 
> *** Hedge Move Indicator *** Version 1.10 of the indicator released. The indicator shows the relative price move between two symbols. I updated Post 1.{image}
> 
> Ignored

Hi MathTrader7,  
  
Can you please explain on how to interpret the Hedge Move Indicator?  
  
Thanks 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Image 1.jpg
Size: 118 KB](/attachment/image/1817250/thumbnail?d=1450761941)](/attachment/image/1817250?d=1450761941)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#272](/thread/post/8657918#post8657918 "Post Permalink")

  * Dec 22, 2015 10:58pm  Dec 22, 2015 10:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar337765_5.gif) dokopy](dokopy)

  * Joined May 2013 | Status: Trader | [894 Posts](/search?do=process&provider=Member&searchuser=337765)

> [Quoting MathTrader7](/thread/post/8654504#post8654504 "View Quoted Post")
> 
> Disliked
> 
> Version 1.60 of the EA released. In this version a few bugs fixed. I updated Post 1.
> 
> Ignored

The new version has opened only one pair. 

Please excuse the bad English via Google Translate.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#273](/thread/post/8657943#post8657943 "Post Permalink")

  * Dec 22, 2015 11:09pm  Dec 22, 2015 11:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting dokopy](/thread/post/8657918#post8657918 "View Quoted Post")
> 
> Disliked
> 
> {quote} The new version has opened only one pair.
> 
> Ignored

Mmmm...![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)  
Could you check your MT4 terminal log to see if there is any error there? I guess your broker (for some reason) rejected to open the second position. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#274](/thread/post/8657950#post8657950 "Post Permalink")

  * Edited 11:28pm  Dec 22, 2015 11:12pm | Edited 11:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting karamaramun](/thread/post/8657132#post8657132 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi MathTrader7, Can you please explain on how to interpret the Hedge Move Indicator? Thanks {image}
> 
> Ignored

Hi karamaramun,  
  
Hedge move indicator shows the relative moves (in points) of two pairs starting from the open price of the day. If two pairs are, for example, highly and positively correlated, then a trade signal could be when they start diverging from each other for more than some amount of points.  
  
Best,  
Math 

Trading is the hardest way to make easy money...

[1 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#275](/thread/post/8660886#post8660886 "Post Permalink")

  * Dec 25, 2015 12:09am  Dec 25, 2015 12:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar337765_5.gif) dokopy](dokopy)

  * Joined May 2013 | Status: Trader | [894 Posts](/search?do=process&provider=Member&searchuser=337765)

> [Quoting MathTrader7](/thread/post/8657943#post8657943 "View Quoted Post")
> 
> Disliked
> 
> {quote} Mmmm...![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) Could you check your MT4 terminal log to see if there is any error there? I guess your broker (for some reason) rejected to open the second position.
> 
> Ignored

Thanks, I forgot to write in the name suffix pair. 

Please excuse the bad English via Google Translate.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#276](/thread/post/8661239#post8661239 "Post Permalink")

  * Dec 25, 2015 10:58am  Dec 25, 2015 10:58am 

  * [ karamaramun](karamaramun)

  * | Joined Dec 2014  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=393975)

> [Quoting MathTrader7](/thread/post/8657950#post8657950 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi karamaramun, Hedge move indicator shows the relative moves (in points) of two pairs starting from the open price of the day. If two pairs are, for example, highly and positively correlated, then a trade signal could be when they start diverging from each other for more than some amount of points. Best, Math
> 
> Ignored

Thank you for the explanation.  
  
If the indicator shows the number of movement points of a pair, if we are directional bias... say news is expected to positively affect a pair. So doesn't it imply that we should buy the pair that moves with more points and sell the pair with less point as a hedge?  
  
K.Mun 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#277](/thread/post/8661610#post8661610 "Post Permalink")

  * Dec 26, 2015 9:48am  Dec 26, 2015 9:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388198_7.gif) LvCa](lvca)

  * | Joined Oct 2014  | Status: Trader | [174 Posts](/search?do=process&provider=Member&searchuser=388198)

Happy Cristmas Math7 and happy Critmas at all people ![](https://resources.faireconomy.media/images/emojis/64/1f973.png?v=15.1). Luca 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#278](/thread/post/8661804#post8661804 "Post Permalink")

  * Dec 27, 2015 12:03am  Dec 27, 2015 12:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting LvCa](/thread/post/8661610#post8661610 "View Quoted Post")
> 
> Disliked
> 
> Happy Cristmas Math7 and happy Critmas at all people ![](https://resources.faireconomy.media/images/emojis/64/1f973.png?v=15.1). Luca
> 
> Ignored

Merry Christmas! :-) 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#279](/thread/post/8784917#post8784917 "Post Permalink")

  * Mar 1, 2016 1:33pm  Mar 1, 2016 1:33pm 

  * [ mpradeep](mpradeep)

  * | Joined Apr 2012  | Status: Trader | [168 Posts](/search?do=process&provider=Member&searchuser=246669)

Dear Mathtrader  
  
Can you make an EA based on this strategy. It should work both in Renko and non Renko chart.  
  
[https://forexfriends.wordpress.com/2...ading-hedging/](https://forexfriends.wordpress.com/2013/05/30/three-pairs-hedging-forex-trading-hedging/)  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#280](/thread/post/9016393#post9016393 "Post Permalink")

  * Edited 9:00pm  Jul 6, 2016 6:43pm | Edited 9:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.63** of the EA released. In this version a few bugs fixed. I updated Post 1. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: NZDJPYH1.png
Size: 33 KB](/attachment/image/1965788/thumbnail?d=1467798281)](/attachment/image/1965788?d=1467798281)   

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#281](/thread/post/9017436#post9017436 "Post Permalink")

  * Jul 7, 2016 5:57am  Jul 7, 2016 5:57am 

  * [ surfeur](surfeur)

  * | Joined Jan 2008  | Status: Trader | [195 Posts](/search?do=process&provider=Member&searchuser=59404)

> [Quoting MathTrader7](/thread/post/8654497#post8654497 "View Quoted Post")
> 
> Disliked
> 
> *** Hedge Move Indicator *** Version 1.10 of the indicator released. The indicator shows the relative price move between two symbols. I updated Post 1.{image}
> 
> Ignored

MathTrader7, i don't see this indicator in the post #1? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#282](/thread/post/9017914#post9017914 "Post Permalink")

  * Jul 7, 2016 3:45pm  Jul 7, 2016 3:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting surfeur](/thread/post/9017436#post9017436 "View Quoted Post")
> 
> Disliked
> 
> {quote} MathTrader7, i don't see this indicator in the post #1?
> 
> Ignored

I will release a new version of the indicator soon. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#283](/thread/post/9130902#post9130902 "Post Permalink")

  * Edited 2:41pm  Sep 10, 2016 1:03pm | Edited 2:41pm 

  * [ ronald_fsm](ronald_fsm)

  * | Joined Jun 2009  | Status: Trader | [366 Posts](/search?do=process&provider=Member&searchuser=107376)

> [Quoting MathTrader7](/thread/post/9017914#post9017914 "View Quoted Post")
> 
> Disliked
> 
> {quote} I will release a new version of the indicator soon.
> 
> Ignored

I try this ea but it's not working . it's**"there is not enough history data"** ,why this happen? Waiting for new version . anyway is there any suggestion which broker suit for this EA ? thanks for sharing 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#284](/thread/post/9229219#post9229219 "Post Permalink")

  * Nov 1, 2016 8:36pm  Nov 1, 2016 8:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar352744_1.gif) aComaS](acomas)

  * | Joined Oct 2013  | Status: Trader | [53 Posts](/search?do=process&provider=Member&searchuser=352744)

I try to attach to chart but it disappear .Can you update it pls Mathtrader7. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#285](/thread/post/9254964#post9254964 "Post Permalink")

  * Nov 16, 2016 4:13am  Nov 16, 2016 4:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.64** of the EA released (I updated Post 1). In this version a few bugs fixed. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#286](/thread/post/9255088#post9255088 "Post Permalink")

  * Nov 16, 2016 4:43am  Nov 16, 2016 4:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar349391_1.gif) Piphoarder](piphoarder)

  * | Joined Sep 2013  | Status: Trader | [24 Posts](/search?do=process&provider=Member&searchuser=349391)

> [Quoting MathTrader7](/thread/post/9254964#post9254964 "View Quoted Post")
> 
> Disliked
> 
> Version 1.64 of the EA released (I updated Post 1). In this version a few bugs fixed.
> 
> Ignored

Thanks MT7, 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#287](/thread/post/9257610#post9257610 "Post Permalink")

  * Nov 16, 2016 9:23pm  Nov 16, 2016 9:23pm 

  * [ Pelepae](pelepae)

  * | Joined Feb 2016  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=450719)

Hi,  
I just try ver 1.64 , don't know why open order was closed after open 2-3sec  
please advise  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EA.jpg
Size: 757 KB](/attachment/image/2065980/thumbnail?d=1479298952)](/attachment/image/2065980?d=1479298952)   

  
  
Thanks you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#288](/thread/post/9258858#post9258858 "Post Permalink")

  * Edited 2:45am  Nov 17, 2016 1:48am | Edited 2:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Pelepae](/thread/post/9257610#post9257610 "View Quoted Post")
> 
> Disliked
> 
> Hi, I just try ver 1.64 , don't know why open order was closed after open 2-3sec please advise {image} Thanks you
> 
> Ignored

Hi, if the net profit reaches either TP or SL, the EA will close both positions regardless of how long it would take. Check your SL setting. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#289](/thread/post/9260050#post9260050 "Post Permalink")

  * Nov 17, 2016 8:56am  Nov 17, 2016 8:56am 

  * [ Pelepae](pelepae)

  * | Joined Feb 2016  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=450719)

> [Quoting MathTrader7](/thread/post/9258858#post9258858 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, if the net profit reaches either TP or SL, the EA will close both positions regardless of how long it would take. Check your SL setting.
> 
> Ignored

Thanks you very much it works now after I input SL for some number, it because I changed SL to "0" because I don't want SL  
  
  
Thanks you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#290](/thread/post/9265956#post9265956 "Post Permalink")

  * Nov 18, 2016 8:59pm  Nov 18, 2016 8:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar352744_1.gif) aComaS](acomas)

  * | Joined Oct 2013  | Status: Trader | [53 Posts](/search?do=process&provider=Member&searchuser=352744)

it load succesfully now but dont open any order with click button why .? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#291](/thread/post/9269627#post9269627 "Post Permalink")

  * Nov 20, 2016 8:49pm  Nov 20, 2016 8:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar480988_3.gif) Ipodbob](ipodbob)

  * | Joined Aug 2016  | Status: Trader | [179 Posts](/search?do=process&provider=Member&searchuser=480988)

This is a great thread thank you for sharing this hopefully I can test it this week on demo ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#292](/thread/post/9270374#post9270374 "Post Permalink")

  * Nov 21, 2016 5:58am  Nov 21, 2016 5:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting aComaS](/thread/post/9265956#post9265956 "View Quoted Post")
> 
> Disliked
> 
> it load succesfully now but dont open any order with click button why .?
> 
> Ignored

It doesn't work in the strategy tester. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#293](/thread/post/9270377#post9270377 "Post Permalink")

  * Nov 21, 2016 5:59am  Nov 21, 2016 5:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Ipodbob](/thread/post/9269627#post9269627 "View Quoted Post")
> 
> Disliked
> 
> This is a great thread thank you for sharing this hopefully I can test it this week on demo ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

You're welcome! :-) 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#294](/thread/post/9270693#post9270693 "Post Permalink")

  * Nov 21, 2016 9:19am  Nov 21, 2016 9:19am 

  * [ jilpangs](jilpangs)

  * | Commercial User  | Joined Nov 2016 | [37 Posts](/search?do=process&provider=Member&searchuser=526663)

Hi MT7,  
  
Quote: Choose two other major currencies to pair with AUD such that the absolute correlation of two pairs is greater than 0.5, for example AUDUSD and AUDCAD.  
  
Where can i get complete list of Pairs with "absolute correlation of two pairs is greater than 0.5"?  
  
~Jil

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#295](/thread/post/9273308#post9273308 "Post Permalink")

  * Nov 22, 2016 3:15am  Nov 22, 2016 3:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting jilpangs](/thread/post/9270693#post9270693 "View Quoted Post")
> 
> Disliked
> 
> Hi MT7, Quote: Choose two other major currencies to pair with AUD such that the absolute correlation of two pairs is greater than 0.5, for example AUDUSD and AUDCAD. Where can i get complete list of Pairs with "absolute correlation of two pairs is greater than 0.5"? ~Jil
> 
> Ignored

Here is one such indicator: 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: multi_pairs_correlation.jpg
Size: 560 KB](/attachment/image/2072508/thumbnail?d=1479752147)](/attachment/image/2072508?d=1479752147)   

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [multi_pairs_correlation.mq4](/attachment/file/2072510?d=1479752151) 15 KB | 945 downloads 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#296](/thread/post/9273845#post9273845 "Post Permalink")

  * Nov 22, 2016 6:35am  Nov 22, 2016 6:35am 

  * [ jilpangs](jilpangs)

  * | Commercial User  | Joined Nov 2016 | [37 Posts](/search?do=process&provider=Member&searchuser=526663)

Thanks MT7. Can you let me know which pair your normally trade? Does the correlation change? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#297](/thread/post/9273888#post9273888 "Post Permalink")

  * Nov 22, 2016 6:59am  Nov 22, 2016 6:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting jilpangs](/thread/post/9273845#post9273845 "View Quoted Post")
> 
> Disliked
> 
> Thanks MT7. Can you let me know which pair your normally trade? Does the correlation change?
> 
> Ignored

You're welcome!  
I choose two pairs with the most positive (or negative) correlation where their average spread on my broker is minimum. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#298](/thread/post/9273907#post9273907 "Post Permalink")

  * Nov 22, 2016 7:09am  Nov 22, 2016 7:09am 

  * [ jilpangs](jilpangs)

  * | Commercial User  | Joined Nov 2016 | [37 Posts](/search?do=process&provider=Member&searchuser=526663)

Once you select on pair, how do you decide whether it is BUY/BUY, SELL/SELL etc ?  
  
does correlation number changes as market moves? Is that mean we should always choose most positive/negative CR? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#299](/thread/post/9276708#post9276708 "Post Permalink")

  * Edited 6:49pm  Nov 23, 2016 12:38am | Edited 6:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting jilpangs](/thread/post/9273907#post9273907 "View Quoted Post")
> 
> Disliked
> 
> Once you select on pair, how do you decide whether it is BUY/BUY, SELL/SELL etc ? does correlation number changes as market moves? Is that mean we should always choose most positive/negative CR?
> 
> Ignored

1\. If the correlation is positive, we only use either BUY/SELL or SELL/BUY  
2\. If the correlation is negative, we only use either BUY/BUY or SELL/SELL  
  
\- Let's assume that we have selected **EURUSD** and **USDJPY** with a negative correlation of **-0.85** , and we want to trade a high impact **red news of USD**.  
  
**How do I make a decision to trade the news?**  
\- I look at a few currency strength indices (including fundamentals) to predict which currency, **EUR** or **JPY** is more powerful at the time of trading.  
\- Let's say that it is **JPY**. In this case I will use **SELL/SELL** button to open a sell position for **EURUSD** and a sell position for **USDJPY**.  
\- If the result of news is very good for **USD** , **EURUSD** will go down to my favor while the other pair, **USDJPY** would go up, however, the strength of **JPY** would resist more than the weakness of **EUR**.  
\- If the result of the news is very bad for **USD** , **USDJPY** will go down sharply due to strength of **JPY** , while **EURUSD** won't go up too sharply due to weakness of **EUR**.  
\- This is the basis of my reasoning for hitting **SELL/SELL** , **BUY/BUY** buttons or just **stay away** from trading that red news!  
  
Best,  
Math 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#300](/thread/post/9277665#post9277665 "Post Permalink")

  * Nov 23, 2016 6:51am  Nov 23, 2016 6:51am 

  * [ jilpangs](jilpangs)

  * | Commercial User  | Joined Nov 2016 | [37 Posts](/search?do=process&provider=Member&searchuser=526663)

Excellent. Thanks MT7. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#301](/thread/post/9429330#post9429330 "Post Permalink")

  * Edited 1:30pm  Jan 12, 2017 9:40am | Edited 1:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546759_1.gif) parashara](parashara)

  * | Joined Jan 2017  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=546759)

Hello Math,  
  
I'm receiving this error. "there is not enough history data". Nor I was able to execute this EA.  
  
I tried the EA from the first post.  
  
Please advise  
  
Thanks 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: image.png
Size: 141 KB](/attachment/image/2136488/thumbnail?d=1484191230)](/attachment/image/2136488?d=1484191230)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#302](/thread/post/9431082#post9431082 "Post Permalink")

  * Jan 12, 2017 8:40pm  Jan 12, 2017 8:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting parashara](/thread/post/9429330#post9429330 "View Quoted Post")
> 
> Disliked
> 
> Hello Math, I'm receiving this error. "there is not enough history data". Nor I was able to execute this EA. I tried the EA from the first post. Please advise Thanks {image}
> 
> Ignored

You need to download history data of the symbols you want to trade with this EA. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#303](/thread/post/9433382#post9433382 "Post Permalink")

  * Jan 13, 2017 5:54am  Jan 13, 2017 5:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546759_1.gif) parashara](parashara)

  * | Joined Jan 2017  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=546759)

> [Quoting MathTrader7](/thread/post/9431082#post9431082 "View Quoted Post")
> 
> Disliked
> 
> {quote} You need to download history data of the symbols you want to trade with this EA.
> 
> Ignored

Hello Math.  
  
I have downloaded the historical data,  
  
I'm reveiving the below error saying that Autotrade time has passed  
  
Can you please advise? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 160 KB](/attachment/image/2138137/thumbnail?d=1484254414)](/attachment/image/2138137?d=1484254414)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#304](/thread/post/9433578#post9433578 "Post Permalink")

  * Jan 13, 2017 7:25am  Jan 13, 2017 7:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting parashara](/thread/post/9433382#post9433382 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello Math. I have downloaded the historical data, I'm reveiving the below error saying that Autotrade time has passed Can you please advise? {image}
> 
> Ignored

I uploaded a new version (v1.65), please use this new version. If there is any bug, please let me know. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#305](/thread/post/9433631#post9433631 "Post Permalink")

  * Jan 13, 2017 7:48am  Jan 13, 2017 7:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546759_1.gif) parashara](parashara)

  * | Joined Jan 2017  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=546759)

> [Quoting MathTrader7](/thread/post/9433578#post9433578 "View Quoted Post")
> 
> Disliked
> 
> {quote} I uploaded a new version (v1.65), please use this new version. If there is any bug, please let me know.
> 
> Ignored

The error still persists. I'm not sure what went wrong. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 159 KB](/attachment/image/2138254/thumbnail?d=1484261270)](/attachment/image/2138254?d=1484261270)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#306](/thread/post/9433753#post9433753 "Post Permalink")

  * Jan 13, 2017 8:30am  Jan 13, 2017 8:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting parashara](/thread/post/9433631#post9433631 "View Quoted Post")
> 
> Disliked
> 
> {quote} The error still persists. I'm not sure what went wrong. {image}
> 
> Ignored

Make sure that you use the last version. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#307](/thread/post/9449130#post9449130 "Post Permalink")

  * Edited 2:11am  Jan 18, 2017 1:00am | Edited 2:11am 

  * [ jaayazan](jaayazan)

  * | Joined Mar 2009  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=96606)

Sorry MT7, cant PM you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#308](/thread/post/9684705#post9684705 "Post Permalink")

  * Mar 20, 2017 4:55pm  Mar 20, 2017 4:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar167511_1.gif) achab](achab)

  * | Joined Jan 2011  | Status: Trader | [154 Posts](/search?do=process&provider=Member&searchuser=167511)

> [Quoting MathTrader7](/thread/post/9433753#post9433753 "View Quoted Post")
> 
> Disliked
> 
> {quote} Make sure that you use the last version.
> 
> Ignored

I am experiencing the same error said above here: "Auto Trade Time is passed". Please, note I redownloaded the version at post number one: there is another version somewhere else?  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: MetaTrader 4 - 01.png
Size: 56 KB](/attachment/image/2236696/thumbnail?d=1489996511)](/attachment/image/2236696?d=1489996511)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#309](/thread/post/9729924#post9729924 "Post Permalink")

  * Apr 3, 2017 4:55am  Apr 3, 2017 4:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar527728_6.gif) sinusgamma](sinusgamma)

  * | Joined Nov 2016  | Status: Trader | [46 Posts](/search?do=process&provider=Member&searchuser=527728)

Ok, so we hedge EURUSD with USDJPY, and try to exploit the imbalance. Why not to buy or sell EURJPY before usd news towards the strongest currency? 

Only my scepticism keep me from being an atheist. Be sceptic ever.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#310](/thread/post/9730719#post9730719 "Post Permalink")

  * Apr 3, 2017 3:47pm  Apr 3, 2017 3:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar167511_1.gif) achab](achab)

  * | Joined Jan 2011  | Status: Trader | [154 Posts](/search?do=process&provider=Member&searchuser=167511)

As already said a couple of weeks ago, I am not able to use this last version of EA, here it is the log (initialization failed, code 32767):  

Inserted Code
    
    
    0 08:41:32.968 MathTrader7_NewsHedgeEA EURUSD,H1 inputs: InpAction=0; InpTime=2018.12.12 23:30:00; InpRelevantButtonsOnly=true; InpHedgeSymbol=USDCHF; InpTPmoney=75.0; InpSLmoney=5000.0; InpEqualizePips=true; InpLotSize=1.0; InpSlippage=30; InpMagicNumber=1122;
    3 08:41:33.015 MathTrader7_NewsHedgeEA EURUSD,H1: initialization failed (32767)
    0 08:41:33.015 MathTrader7_NewsHedgeEA EURUSD,H1: uninit reason 8
    0 08:41:33.015 Expert MathTrader7_NewsHedgeEA EURUSD,H1: removed

A help will be appreciated.  
  
Best regards.  
/achab 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#311](/thread/post/9731280#post9731280 "Post Permalink")

  * Apr 3, 2017 7:47pm  Apr 3, 2017 7:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting sinusgamma](/thread/post/9729924#post9729924 "View Quoted Post")
> 
> Disliked
> 
> Ok, so we hedge EURUSD with USDJPY, and try to exploit the imbalance. **Why not to buy or sell EURJPY before usd news towards the strongest currency?**
> 
> Ignored

It is possible! 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#312](/thread/post/9733711#post9733711 "Post Permalink")

  * Apr 4, 2017 2:21pm  Apr 4, 2017 2:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar392927_1.gif) techlover](techlover)

  * | Joined Dec 2014  | Status: Trader | [117 Posts](/search?do=process&provider=Member&searchuser=392927)

iam also facing same issue with the latest version  
  
2017.04.04 10:43:39.518 MathTrader7_NewsHedgeEA EURUSD,H1: initialization failed (32767) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#313](/thread/post/9817428#post9817428 "Post Permalink")

  * May 2, 2017 10:03am  May 2, 2017 10:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar576292_1.gif) Anyname](anyname)

  * | Joined May 2017  | Status: Global Citizen | [47 Posts](/search?do=process&provider=Member&searchuser=576292)

> [Quoting MathTrader7](/thread/post/9731280#post9731280 "View Quoted Post")
> 
> Disliked
> 
> {quote} It is possible!
> 
> Ignored

I'm new to Forex. FF has is an awesome resource. Having stated that I think it's pretty amazing to see your contributions here. I salute you MathTrader7! 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#314](/thread/post/9821490#post9821490 "Post Permalink")

  * May 3, 2017 5:39am  May 3, 2017 5:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

Version **1.66** of the EA released. I updated Post 1. This version has been compiled with MT4 build 1069. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#315](/thread/post/9902934#post9902934 "Post Permalink")

  * May 24, 2017 10:29am  May 24, 2017 10:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar145433_1.gif) princefred](princefred)

  * Joined Jun 2010 | Status: Trader | [449 Posts](/search?do=process&provider=Member&searchuser=145433)

It will be good if one can select the lots for the hedge trade sepratly. Also a option to open a pending order x pips away after initial entry will be great . 

Know News/time; WAIT for Edge Entries, MPLC Normalization, Exits & TP's..

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#316](/thread/post/9904519#post9904519 "Post Permalink")

  * Edited 9:29pm  May 24, 2017 8:43pm | Edited 9:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.67** of the EA released (I updated Post 1). In this version users can specify the lot size of the hedge symbol separately. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#317](/thread/post/9943355#post9943355 "Post Permalink")

  * Jun 5, 2017 7:37pm  Jun 5, 2017 7:37pm 

  * [ halunek](halunek)

  * | Joined May 2017  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=581569)

Hey MathTrader, do you have version which i can make 2 hedge positions on 1 pair? for example SELL and BUY on EU at the same time 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#318](/thread/post/9943440#post9943440 "Post Permalink")

  * Jun 5, 2017 7:53pm  Jun 5, 2017 7:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting halunek](/thread/post/9943355#post9943355 "View Quoted Post")
> 
> Disliked
> 
> Hey MathTrader, do you have version which i can make 2 hedge positions on 1 pair? for example SELL and BUY on EU at the same time
> 
> Ignored

Hej! I don't have such version of the EA. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#319](/thread/post/10171722#post10171722 "Post Permalink")

  * Aug 9, 2017 10:32pm  Aug 9, 2017 10:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar487939_1.gif) CreativeT](creativet)

  * | Joined Sep 2016  | Status: Trader | [56 Posts](/search?do=process&provider=Member&searchuser=487939)

Can you please explain or resolve the problem in your EA, I set up $3 as TP and $10 as SL but after experiencing on many pairs trades were closed above $3 please take a look at the screenshot. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Math Trader EA.jpg
Size: 547 KB](/attachment/image/2432548/thumbnail?d=1502285148)](/attachment/image/2432548?d=1502285148)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#320](/thread/post/10429954#post10429954 "Post Permalink")

  * Oct 26, 2017 9:46pm  Oct 26, 2017 9:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar404578_1.gif) Ferro](ferro)

  * | Joined Mar 2015  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=404578)

Hi Math, This EA sounds interesting as I am also an active news trader. I have download your EA and installed it to my MT4. Unfortunately after being successfully installed, it has being automatically removed. Did I do something wrong?   
  
Thanks heaps 

Attached Image

![](/attachment/image/2534674?d=1509021969)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#321](/thread/post/10431673#post10431673 "Post Permalink")

  * Oct 27, 2017 2:06am  Oct 27, 2017 2:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Ferro](/thread/post/10429954#post10429954 "View Quoted Post")
> 
> Disliked
> 
> Hi Math, This EA sounds interesting as I am also an active news trader. I have download your EA and installed it to my MT4. Unfortunately after being successfully installed, it has being automatically removed. Did I do something wrong? Thanks heaps {image}
> 
> Ignored

Hi Ferro,  
  
The EA must be updated to work with the latest version of MT4. I may release a new version of this EA.  
  
Best,  
Math 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#322](/thread/post/10436018#post10436018 "Post Permalink")

  * Oct 28, 2017 1:08am  Oct 28, 2017 1:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.70** of the EA released (I updated Post 1). 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#323](/thread/post/10436868#post10436868 "Post Permalink")

  * Oct 28, 2017 9:02am  Oct 28, 2017 9:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar404578_1.gif) Ferro](ferro)

  * | Joined Mar 2015  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=404578)

Thanks Math. You are superb! Will test this ASAP. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#324](/thread/post/10483386#post10483386 "Post Permalink")

  * Nov 11, 2017 2:27pm  Nov 11, 2017 2:27pm 

  * [ prodos](prodos)

  * | Joined May 2014  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=372742)

How to trade on real account??? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#325](/thread/post/10484837#post10484837 "Post Permalink")

  * Nov 12, 2017 7:33pm  Nov 12, 2017 7:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting prodos](/thread/post/10483386#post10483386 "View Quoted Post")
> 
> Disliked
> 
> How to trade on real account???
> 
> Ignored

I release a stable version of the EA soon. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#326](/thread/post/10484863#post10484863 "Post Permalink")

  * Nov 12, 2017 7:53pm  Nov 12, 2017 7:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar618921_1.gif) senna](senna)

  * | Additional Username  | Joined Oct 2017 | [67 Posts](/search?do=process&provider=Member&searchuser=618921)

nice EA mate 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#327](/thread/post/10485504#post10485504 "Post Permalink")

  * Edited 3:57am  Nov 13, 2017 3:43am | Edited 3:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

Version 1.71 of the EA released (I updated Post 1). This version works with the latest version of the MT4 platform and live accounts. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#328](/thread/post/10485631#post10485631 "Post Permalink")

  * Nov 13, 2017 5:13am  Nov 13, 2017 5:13am 

  * [ prodos](prodos)

  * | Joined May 2014  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=372742)

it's real good!  
i must open two chart or one chart？ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#329](/thread/post/10485634#post10485634 "Post Permalink")

  * Nov 13, 2017 5:17am  Nov 13, 2017 5:17am 

  * [ prodos](prodos)

  * | Joined May 2014  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=372742)

sorry，i know！ haha~，thanks！！！ 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#330](/thread/post/10485648#post10485648 "Post Permalink")

  * Nov 13, 2017 5:21am  Nov 13, 2017 5:21am 

  * [ prodos](prodos)

  * | Joined May 2014  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=372742)

How to set？can't set for hedge！！！  
  
  

Attached Image

![](/attachment/image/2557913?d=1510518083)

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: HOW TO SET 01.png
Size: 3 KB](/attachment/image/2557908/thumbnail?d=1510518065)](/attachment/image/2557908?d=1510518065)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: HOW TO SET 04.png
Size: 3 KB](/attachment/image/2557921/thumbnail?d=1510518233)](/attachment/image/2557921?d=1510518233)   

  

Attached Image

![](/attachment/image/2557924?d=1510518236)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#331](/thread/post/10485663#post10485663 "Post Permalink")

  * Nov 13, 2017 5:33am  Nov 13, 2017 5:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting prodos](/thread/post/10485648#post10485648 "View Quoted Post")
> 
> Disliked
> 
> How to set？can't set for hedge！！！ {image} {image} {image} {image}
> 
> Ignored

Please read the first post, it explains the input settings. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#332](/thread/post/10485667#post10485667 "Post Permalink")

  * Nov 13, 2017 5:39am  Nov 13, 2017 5:39am 

  * [ prodos](prodos)

  * | Joined May 2014  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=372742)

**Positively Correlated Symbols**  
For a pair of symbols that are positively correlated (such as AUDUSD and AUDCAD), use either **Buy/Sell or Sell/Buy** button.  
  
very soory!!! i don't see it !!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#333](/thread/post/10485847#post10485847 "Post Permalink")

  * Nov 13, 2017 8:11am  Nov 13, 2017 8:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar608462_3.gif) T4Trade](t4trade)

  * Joined Sep 2017 | Status: Trend Following,Price Action,Grid | [2,484 Posts](/search?do=process&provider=Member&searchuser=608462)

> [Quoting MathTrader7](/thread/post/10485663#post10485663 "View Quoted Post")
> 
> Disliked
> 
> {quote} Please read the first post, it explains the input settings.
> 
> Ignored

Best EA,well done and thanks for sharing! 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#334](/thread/post/10486364#post10486364 "Post Permalink")

  * Nov 13, 2017 2:33pm  Nov 13, 2017 2:33pm 

  * [ qq963110866](qq963110866)

  * | Joined Sep 2017  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=611061)

> [Quoting MathTrader7](/thread/post/10485504#post10485504 "View Quoted Post")
> 
> Disliked
> 
> Version 1.71 of the EA released (I updated Post 1). This version works with the latest version of the MT4 platform and live accounts.
> 
> Ignored

Manual order? Semi automatic EA????????? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#335](/thread/post/10486947#post10486947 "Post Permalink")

  * Nov 13, 2017 6:28pm  Nov 13, 2017 6:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting qq963110866](/thread/post/10486364#post10486364 "View Quoted Post")
> 
> Disliked
> 
> {quote} Manual order? Semi automatic EA?????????
> 
> Ignored

You can trade manually or semi-automatic with this EA. Please read the description of the EA in the first post. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#336](/thread/post/10510225#post10510225 "Post Permalink")

  * Nov 20, 2017 10:19am  Nov 20, 2017 10:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar618921_1.gif) senna](senna)

  * | Additional Username  | Joined Oct 2017 | [67 Posts](/search?do=process&provider=Member&searchuser=618921)

> [Quoting MathTrader7](/thread/post/10486947#post10486947 "View Quoted Post")
> 
> Disliked
> 
> {quote} You can trade manually or semi-automatic with this EA. Please read the description of the EA in the first post.
> 
> Ignored

it say there is not enought history dana (as least 201) for usdjpy, what is that mean..? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#337](/thread/post/10531370#post10531370 "Post Permalink")

  * Nov 27, 2017 9:14am  Nov 27, 2017 9:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar115498_1.gif) freedom48](freedom48)

  * | Joined Sep 2009  | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=115498)

My had was fulfilled of strategies and I found myself in this thread...It is very interesting because on previous trading years of mine, I did try some similar like this manually, but after few days of success it always failed. I have some simple questions, while I went almost troughout all pages I could not understand very clear the trade enter correctly, some few things.  
Now lets say, are we trading only on the specific red news of a currecny ?..Because I read somewhere here that it is not neccesery to trade on red news..So, it is to be on red news or on any other criteria ?  
What I want actually to understand is, lets again saying example, we do have a red news upcoming for AUD after 5 minutes.. Next step we check for pairs. So lets do with AUD/USD and AUD/CAD ... The USD is stronger on daily currency strengh against CAD. USD is 7.0 and CAD is 3.7 (example) Now do we have to decide to going long for AUD/USD and going short for AUD/CAD..or what is the reason to not do the opposite.  
"3. A few minutes before the news release time, look at a currency strength meter to observe which of above two currencies (USD or CAD) is more powerful.  
4\. Select a trade button according to both the sign of correlation (this can be automatically done by the EA for you), and the strongest currency you identified in the previous step." Not so clear with this.  
I can not get the enrtry philosophy with this paragraph, sorry for the silly question. But I believe as this thread is alive and updated it is worth to understand what it is all about.  
Thanks for enlighten me in advance.  
Good week to all.

" Accepting losses is the most important single investment devise "

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#338](/thread/post/10532124#post10532124 "Post Permalink")

  * Nov 27, 2017 5:38pm  Nov 27, 2017 5:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting freedom48](/thread/post/10531370#post10531370 "View Quoted Post")
> 
> Disliked
> 
> My had was fulfilled of strategies and I found myself in this thread...It is very interesting because on previous trading years of mine, I did try some similar like this manually, but after few days of success it always failed. I have some simple questions, while I went almost troughout all pages I could not understand very clear the trade enter correctly, some few things. Now lets say, are we trading only on the specific red news of a currecny ?..Because I read somewhere here that it is not neccesery to trade on red news..So, it is to be on red...
> 
> Ignored

Hi freedom48,  
  
I personally trade with this EA for red news only. But there are people who use this EA to enter the market with their own entry logic.  
For your example of AUD**USD** and AUD**CAD,** we need to check the currency strength of **USD** and **CAD**. Let's say that USD is 7.0 and CAD is 3.6.  
\- If the red news of AUD is good for this currency, then the prediction is that AUDUSD would probably goes up less than AUDCAD because USD is stronger (about twice in our example) than CAD.  
\- If the red news of AUD is bad for this currency, then the prediction is that AUDUSD would probably goes down more than AUDCAD because USD is stronger (about twice in our example) than CAD.  
Hence, I will **SELL AUDUSD** and **BUY AUDCAD**.  
  
Best,  
Math 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#339](/thread/post/10533092#post10533092 "Post Permalink")

  * Nov 27, 2017 10:46pm  Nov 27, 2017 10:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar115498_1.gif) freedom48](freedom48)

  * | Joined Sep 2009  | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=115498)

> [Quoting MathTrader7](/thread/post/10532124#post10532124 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi freedom48, I personally trade with this EA for red news only. But there are people who use this EA to enter the market with their own entry logic. For your example of AUDUSD and AUDCAD, we need to check the currency strength of USD and CAD. Let's say that USD is 7.0 and CAD is 3.6. - If the red news of AUD is good for this currency, then the prediction is that AUDUSD would probably goes up less than AUDCAD because USD is stronger (about twice in our example) than CAD. - If the red news of AUD is bad for this currency, then the prediction...
> 
> Ignored

Thank you. Now very clear about without doing any test for the moment. Fundamentals playing important role for the specific pair, in the example here the AUD....Otherwise I wouldn't say and guess it could be important without the red news as others are doing. Without the AUD red news, trade directly USD/CAD. Why others trying it without the role player. So better I will take this on my chart and be able to better analyze. I think somehow behind the 2 years of this EA experience , things were going good. I missed the thread so I can start soon to see forward. 

" Accepting losses is the most important single investment devise "

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#340](/thread/post/10533289#post10533289 "Post Permalink")

  * Nov 27, 2017 11:31pm  Nov 27, 2017 11:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar115498_1.gif) freedom48](freedom48)

  * | Joined Sep 2009  | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=115498)

> [Quoting MathTrader7](/thread/post/10532124#post10532124 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi freedom48, I personally trade with this EA for red news only. But there are people who use this EA to enter the market with their own entry logic. For your example of AUDUSD and AUDCAD, we need to check the currency strength of USD and CAD. Let's say that USD is 7.0 and CAD is 3.6. - If the red news of AUD is good for this currency, then the prediction is that AUDUSD would probably goes up less than AUDCAD because USD is stronger (about twice in our example) than CAD. - If the red news of AUD is bad for this currency, then the prediction...
> 
> Ignored

Sorry I had to quote again. From your description of the both options , seems like from your sentence that for both options you have to " Hence, I will **SELL AUDUSD** and **BUY AUDCAD**. " 

" Accepting losses is the most important single investment devise "

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#341](/thread/post/10533702#post10533702 "Post Permalink")

  * Nov 28, 2017 12:43am  Nov 28, 2017 12:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting freedom48](/thread/post/10533289#post10533289 "View Quoted Post")
> 
> Disliked
> 
> {quote} Sorry I had to quote again. From your description of the both options , seems like from your sentence that for both options you have to " Hence, I will SELL AUDUSD and BUY AUDCAD. "
> 
> Ignored

I didn't understand your message/question here... 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#342](/thread/post/10534331#post10534331 "Post Permalink")

  * Nov 28, 2017 3:50am  Nov 28, 2017 3:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting freedom48](/thread/post/10533092#post10533092 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thank you. Now very clear about without doing any test for the moment. Fundamentals playing important role for the specific pair, in the example here the AUD....Otherwise I wouldn't say and guess it could be important without the red news as others are doing. Without the AUD red news, trade directly USD/CAD. Why others trying it without the role player. So better I will take this on my chart and be able to better analyze. I think somehow behind the 2 years of this EA experience , things were going good. I missed the thread so I can start...
> 
> Ignored

You're welcome!  
Sure you can trade USDCAD without looking at any news! :-) 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#343](/thread/post/10535694#post10535694 "Post Permalink")

  * Nov 28, 2017 3:13pm  Nov 28, 2017 3:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar115498_1.gif) freedom48](freedom48)

  * | Joined Sep 2009  | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=115498)

> [Quoting MathTrader7](/thread/post/10533702#post10533702 "View Quoted Post")
> 
> Disliked
> 
> {quote} I didn't understand your message/question here...
> 
> Ignored

Hi back, sorry I was not so clear about my question, I mean:   
  
\- If the red news of **AUD is good** for this currency, then the prediction is that **AUDUSD would probably goes up less than AUDCAD** because USD is stronger (about twice in our example) than CAD.  
  
\- If the red news of **AUD is bad** for this currency, then the prediction is that **AUDUSD would probably goes down more than AUDCAD** because USD is stronger (about twice in our example) than CAD.  
Hence, I will **SELL AUDUSD** and **BUY AUDCAD**.  
  
So you mean that in both option of red news ( good or bad) you will make the same action **SELL AUDUSD** and **BUY AUDCAD**. ?  
Or did you mean if the red news for **AUD is good** we do not trade?  
When we will do **BUY AUDUSD** and **SELL AUDCAD** if USD is 7.0 and CAD is 3.6 in currency strengh meter is remain as my question.  
  
I hope now I was more clear. Thank you Math 

" Accepting losses is the most important single investment devise "

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#344](/thread/post/10536121#post10536121 "Post Permalink")

  * Nov 28, 2017 5:51pm  Nov 28, 2017 5:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting freedom48](/thread/post/10535694#post10535694 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi back, sorry I was not so clear about my question, I mean: - If the red news of AUD is good for this currency, then the prediction is that AUDUSD would probably goes up less than AUDCAD because USD is stronger (about twice in our example) than CAD. - If the red news of AUD is bad for this currency, then the prediction is that AUDUSD would probably goes down more than AUDCAD because USD is stronger (about twice in our example) than CAD. Hence, I will SELL AUDUSD and BUY AUDCAD. So you mean that in both option of red news ( good or bad)...
> 
> Ignored

Hi freedom48,  
  
Please note that we do an analysis before the red news release time. Let's say that half an hour before a red news for AUD, we analyze the possible outcomes given currency strength values of USD (7.0) and CAD (3.6). So, I will SELL AUDUSD and BUY AUDCAD one minute before the red news release. If the red news outcome is good for AUD, I expect to see more bullish movement in AUDCAD which would cover my loss on selling AUDUSD (and possibly makes a profit in total). And if the red news outcome is bad for AUD, I expect to see a more bearish movement in AUDUSD which would cover my loss on buying AUDCAD (and possibly makes a profit in total).  
  
Hope this explanation helps you to get the whole idea :-)  
  
P.S. Our analysis is valid as long as the currency strength values are (at least to some degree) correct.  
  
Best,  
Math 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#345](/thread/post/10539895#post10539895 "Post Permalink")

  * Nov 29, 2017 8:23am  Nov 29, 2017 8:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar115498_1.gif) freedom48](freedom48)

  * | Joined Sep 2009  | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=115498)

> [Quoting MathTrader7](/thread/post/10536121#post10536121 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi freedom48, Please note that we do an analysis before the red news release time. Let's say that half an hour before a red news for AUD, we analyze the possible outcomes given currency strength values of USD (7.0) and CAD (3.6). So, I will SELL AUDUSD and BUY AUDCAD one minute before the red news release. If the red news outcome is good for AUD, I expect to see more bullish movement in AUDCAD which would cover my loss on selling AUDUSD (and possibly makes a profit in total). And if the red news outcome is bad for AUD, I expect to see a...
> 
> Ignored

Thank you much. Now I get it totally clear. In overall from above example it is also very important to seek a pair combination with AUD before the news outcome. A 7.0 can lead to 8 and a 3.6 can wipe out totally till 0.5 or the opposite can happen. So I probably will need to test very often many options .  
Again thanks for clear my mind.  
Wish best trades. 

" Accepting losses is the most important single investment devise "

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#346](/thread/post/10546136#post10546136 "Post Permalink")

  * Nov 30, 2017 9:45pm  Nov 30, 2017 9:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar608462_3.gif) T4Trade](t4trade)

  * Joined Sep 2017 | Status: Trend Following,Price Action,Grid | [2,484 Posts](/search?do=process&provider=Member&searchuser=608462)

I downloaded this EA,but it doesn't give correct corealtion pairing,for example when USDJPY is low,GU is high but the options are only both sell or both buy.it should be one buy and one sell option.Pleae fix this,i like this EA very much otherwise.  
  
please guide me to latest version.i have the first one only. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#347](/thread/post/10546480#post10546480 "Post Permalink")

  * Nov 30, 2017 11:22pm  Nov 30, 2017 11:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting T4Trade](/thread/post/10546136#post10546136 "View Quoted Post")
> 
> Disliked
> 
> I downloaded this EA,but it doesn't give correct corealtion pairing,for example when USDJPY is low,GU is high but the options are only both sell or both buy.it should be one buy and one sell option.Pleae fix this,i like this EA very much otherwise. please guide me to latest version.i have the first one only.
> 
> Ignored

I always put the latest version of the EA in Post 1.  
This EA uses D1 candles of two pairs to calculate the correlation over last 200 candles. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#348](/thread/post/10546619#post10546619 "Post Permalink")

  * Nov 30, 2017 11:50pm  Nov 30, 2017 11:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar608462_3.gif) T4Trade](t4trade)

  * Joined Sep 2017 | Status: Trend Following,Price Action,Grid | [2,484 Posts](/search?do=process&provider=Member&searchuser=608462)

> [Quoting MathTrader7](/thread/post/10546480#post10546480 "View Quoted Post")
> 
> Disliked
> 
> {quote} I always put the latest version of the EA in Post 1. This EA uses D1 candles of two pairs to calculate the correlation over last 200 candles.
> 
> Ignored

I am using that EA what is there in post 1 and by the way there is only one version there right? I have seen other traders also having the same problem that this EA is not showing correct correlation.plese refer to this screen shot. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 54 KB](/attachment/image/2582881/thumbnail?d=1512053374)](/attachment/image/2582881?d=1512053374)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#349](/thread/post/10547764#post10547764 "Post Permalink")

  * Dec 1, 2017 4:03am  Dec 1, 2017 4:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting T4Trade](/thread/post/10546619#post10546619 "View Quoted Post")
> 
> Disliked
> 
> {quote} I am using that EA what is there in post 1 and by the way there is only one version there right? I have seen other traders also having the same problem that this EA is not showing correct correlation.plese refer to this screen shot. {image}
> 
> Ignored

A correlation of **-0.78** between EURUSD and USDJPY is correct. And for a negative correlation higher than 0.5 we either use the button BUY/BUY or SELL/SELL. Please read Post 1. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#350](/thread/post/10548044#post10548044 "Post Permalink")

  * Dec 1, 2017 5:22am  Dec 1, 2017 5:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar608462_3.gif) T4Trade](t4trade)

  * Joined Sep 2017 | Status: Trend Following,Price Action,Grid | [2,484 Posts](/search?do=process&provider=Member&searchuser=608462)

> [Quoting MathTrader7](/thread/post/10547764#post10547764 "View Quoted Post")
> 
> Disliked
> 
> {quote} A correlation of -0.78 between EURUSD and USDJPY is correct. And for a negative correlation higher than 0.5 we either use the button BUY/BUY or SELL/SELL. Please read Post 1.
> 
> Ignored

Thankyou for assisting,but still I don't understand the logic to enter,should we be trading on D1 time frame? red news I trade on 15 min chart normally.  
  
please guide me to the psot where I can read more about sound entry other times than news events. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#351](/thread/post/10588939#post10588939 "Post Permalink")

  * Dec 14, 2017 7:23am  Dec 14, 2017 7:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar608462_3.gif) T4Trade](t4trade)

  * Joined Sep 2017 | Status: Trend Following,Price Action,Grid | [2,484 Posts](/search?do=process&provider=Member&searchuser=608462)

does this EA still gives good correlation results? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#352](/thread/post/10980523#post10980523 "Post Permalink")

  * Edited Apr 20, 2018 5:04pm  Apr 19, 2018 10:49pm | Edited Apr 20, 2018 5:04pm 

  * [ El1000](el1000)

  * | Joined Jun 2016  | Status: Trader | [202 Posts](/search?do=process&provider=Member&searchuser=470939)

Hi MathTrader7,  
Does this EA work today? I got a Message up in the left corner "auto trade time has passed!" and it's not working? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#353](/thread/post/11007500#post11007500 "Post Permalink")

  * Apr 28, 2018 5:03am  Apr 28, 2018 5:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

Version **1.72** of the EA released (I updated Post 1). 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#354](/thread/post/11007539#post11007539 "Post Permalink")

  * Apr 28, 2018 5:29am  Apr 28, 2018 5:29am 

  * [ El1000](el1000)

  * | Joined Jun 2016  | Status: Trader | [202 Posts](/search?do=process&provider=Member&searchuser=470939)

> [Quoting MathTrader7](/thread/post/11007500#post11007500 "View Quoted Post")
> 
> Disliked
> 
> Version 1.72 of the EA released (I updated Post 1).
> 
> Ignored

Tusen takk ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#355](/thread/post/11007657#post11007657 "Post Permalink")

  * Apr 28, 2018 6:16am  Apr 28, 2018 6:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting El1000](/thread/post/11007539#post11007539 "View Quoted Post")
> 
> Disliked
> 
> {quote} Tusen takk ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)
> 
> Ignored

Varsågod!![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#356](/thread/post/11011440#post11011440 "Post Permalink")

  * Apr 30, 2018 8:42pm  Apr 30, 2018 8:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar670501_2.gif) ekoveadvisor](ekoveadvisor)

  * | Additional Username  | Joined Apr 2018 | [71 Posts](/search?do=process&provider=Member&searchuser=670501)

> [Quoting T4Trade](/thread/post/10546619#post10546619 "View Quoted Post")
> 
> Disliked
> 
> {quote} I am using that EA what is there in post 1 and by the way there is only one version there right? I have seen other traders also having the same problem that this EA is not showing correct correlation.plese refer to this screen shot. {image}
> 
> Ignored

HI T4Trade. Would you mind to share your template? because my MathTrader7_NewsHedgeEA.ex4 doesnt look like this. And im pretty sure there is some special set up you have there. Thank you. 

forex is better than cryptocurrency, trust me.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#357](/thread/post/11014636#post11014636 "Post Permalink")

  * May 1, 2018 6:46pm  May 1, 2018 6:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar608462_3.gif) T4Trade](t4trade)

  * Joined Sep 2017 | Status: Trend Following,Price Action,Grid | [2,484 Posts](/search?do=process&provider=Member&searchuser=608462)

sorry I don't have it,im no more using this EA,but I would like to practice hedging,good luck! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [View Post](/thread/post/11037512#post11037512)
  * Disliked by [Thread Starter](mathtrader7)

  * [ktooph](ktooph)

  * [#359](/thread/post/11311104#post11311104 "Post Permalink")

  * Jul 30, 2018 7:43am  Jul 30, 2018 7:43am 

  * [ fairtraderuk](fairtraderuk)

  * | Joined Jul 2018  | Status: Trader | [574 Posts](/search?do=process&provider=Member&searchuser=701559)

Hi MathTrader thank you also from a relative newbie. I have been researching fundamentals for a few months and testing out few strategies including news straddling on demo and live accounts using a custom EA with mixed results. Just came across your EA MathTrader7_NewsHedgeEA.ex4 Uploaded Apr 27, 2018 3:01pm and tried to add this to a Demo account following what I thought were the right steps. Unfortunately I cannot seem to attach the EA to any chart as it drops out following settings update. I am also assuming if the step was successful I would see the EA name on top right hand side of the chart? Is there something I'm missing? I really appreciate your help. Best regards Ben 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#360](/thread/post/11312785#post11312785 "Post Permalink")

  * Jul 30, 2018 10:05pm  Jul 30, 2018 10:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.73** of the EA released (I updated Post 1). This version is compiled with MT4 build **1126**. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#361](/thread/post/11312956#post11312956 "Post Permalink")

  * Jul 30, 2018 10:47pm  Jul 30, 2018 10:47pm 

  * [ fairtraderuk](fairtraderuk)

  * | Joined Jul 2018  | Status: Trader | [574 Posts](/search?do=process&provider=Member&searchuser=701559)

Much appreciated MathTrader! I shall get to work ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#362](/thread/post/11313867#post11313867 "Post Permalink")

  * Jul 31, 2018 1:51am  Jul 31, 2018 1:51am 

  * [ fairtraderuk](fairtraderuk)

  * | Joined Jul 2018  | Status: Trader | [574 Posts](/search?do=process&provider=Member&searchuser=701559)

> [Quoting MathTrader7](/thread/post/11312785#post11312785 "View Quoted Post")
> 
> Disliked
> 
> Version 1.73 of the EA released (I updated Post 1). This version is compiled with MT4 build 1126.
> 
> Ignored

Hi MathTrader could you possibly elaborate on how slippage default value of 30 lower or higher impacts potential outcome from the EA? Am I correct in thinking lower slippage value will limit risk but at the expense of hitting stop loss particularly around news release? Just experienced 50 pips slippage on certain Australian news at least according to brokers; in such extreme cases what should the value be around? I'm analysing news impact across multiple pairs and brokers and welcome anything that would assist an analytical approach. Will be more than happy to share results once I get the hang of the tricks of trading around news. Thanks again 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#363](/thread/post/11313895#post11313895 "Post Permalink")

  * Jul 31, 2018 2:01am  Jul 31, 2018 2:01am 

  * [ fairtraderuk](fairtraderuk)

  * | Joined Jul 2018  | Status: Trader | [574 Posts](/search?do=process&provider=Member&searchuser=701559)

> [Quoting MathTrader7](/thread/post/11312785#post11312785 "View Quoted Post")
> 
> Disliked
> 
> Version 1.73 of the EA released (I updated Post 1). This version is compiled with MT4 build 1126.
> 
> Ignored

By the way MT I seem to have a little trouble removing the EA from a chart by Expert Advisors -> Remove - leads to MT session hanging for 10 seconds or more with the buttons remaining on chart. Cheers 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#364](/thread/post/11315740#post11315740 "Post Permalink")

  * Jul 31, 2018 4:36pm  Jul 31, 2018 4:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting fairtraderuk](/thread/post/11313867#post11313867 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi MathTrader could you possibly elaborate on how slippage default value of 30 lower or higher impacts potential outcome from the EA? Am I correct in thinking lower slippage value will limit risk but at the expense of hitting stop loss particularly around news release? Just experienced 50 pips slippage on certain Australian news at least according to brokers; in such extreme cases what should the value be around? I'm analysing news impact across multiple pairs and brokers and welcome anything that would assist an analytical approach. Will...
> 
> Ignored

Hi fairtraderuk,  
  
The Slippage in the input settings has a different meaning. When an EA sends an order to the broker's server, it has to mention the price at which the EA wants the broker to open a BUY or SELL position. However, since it takes some time (for example, 200 miliseconds) for the order to be processed by the broker's server, the actual price in the market may have been changed a few points. Slippage tells the broker how much change in the market price is acceptable for the order to be executed.  
  
Best,  
Matt 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#365](/thread/post/11316028#post11316028 "Post Permalink")

  * Jul 31, 2018 5:51pm  Jul 31, 2018 5:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting fairtraderuk](/thread/post/11313895#post11313895 "View Quoted Post")
> 
> Disliked
> 
> {quote} By the way MT I seem to have a little trouble removing the EA from a chart by Expert Advisors -> Remove - leads to MT session hanging for 10 seconds or more with the buttons remaining on chart. Cheers
> 
> Ignored

What is your MT4 build version? 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#366](/thread/post/11332621#post11332621 "Post Permalink")

  * Aug 4, 2018 6:53am  Aug 4, 2018 6:53am 

  * [ icey4826](icey4826)

  * | Joined Aug 2014  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=379948)

Mathtrader would it possible for you to perhaps create MT4 Expert Advisor that will monitor the price action of two different currency pairs, e.g. EUR/USD and GBP/USD and calculate the correlation gap between them.  
  
The EA should place a trade when the gap reaches a certain level and close the trade in profit when the gap has closed to a preset lower level. I have been testing this strategy and its amazing. I basically have EA's that take care of the trade after I already opened the trade, but I need something that will trigger the trade in the first place. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#367](/thread/post/11335027#post11335027 "Post Permalink")

  * Aug 6, 2018 2:59am  Aug 6, 2018 2:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting icey4826](/thread/post/11332621#post11332621 "View Quoted Post")
> 
> Disliked
> 
> Mathtrader would it possible for you to perhaps create MT4 Expert Advisor that will monitor the price action of two different currency pairs, e.g. EUR/USD and GBP/USD and calculate the correlation gap between them. The EA should place a trade when the gap reaches a certain level and close the trade in profit when the gap has closed to a preset lower level. I have been testing this strategy and its amazing. I basically have EA's that take care of the trade after I already opened the trade, but I need something that will trigger the trade in the first...
> 
> Ignored

Hi, I sent you a PM in this regard. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#368](/thread/post/11335826#post11335826 "Post Permalink")

  * Aug 6, 2018 1:48pm  Aug 6, 2018 1:48pm 

  * [ Mianssg1](mianssg1)

  * | Joined Aug 2018  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=704156)

i have found one problem but i dont know how to slove? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Untitled.jpg
Size: 381 KB](/attachment/image/2929503/thumbnail?d=1533530883)](/attachment/image/2929503?d=1533530883)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#369](/thread/post/11336261#post11336261 "Post Permalink")

  * Edited 7:52pm  Aug 6, 2018 4:45pm | Edited 7:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Mianssg1](/thread/post/11335826#post11335826 "View Quoted Post")
> 
> Disliked
> 
> i have found one problem but i dont know how to slove? {image}
> 
> Ignored

In order to load history data of hedge symbols, you can follow the steps below:  
1\. Hit <F2> key to bring up History Center window.  
2\. Select the symbol (for example, AUDCAD).  
3\. Click on <Download> button.  
4\. Repeat steps 1 to 3 for all symbols you want to load history data. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#370](/thread/post/11350288#post11350288 "Post Permalink")

  * Aug 9, 2018 10:52pm  Aug 9, 2018 10:52pm 

  * [ fairtraderuk](fairtraderuk)

  * | Joined Jul 2018  | Status: Trader | [574 Posts](/search?do=process&provider=Member&searchuser=701559)

> [Quoting MathTrader7](/thread/post/11316028#post11316028 "View Quoted Post")
> 
> Disliked
> 
> {quote} What is your MT4 build version?
> 
> Ignored

Hi MathTrader apologies for the late response; the build seems to be 1090 May 2017 however the problem seems to have gone away - so thank you!  
  
On a separate note and hope this is not too much a rookie question - do you think it would be feasible for this EA or another adapted version to open both Buy & Sell positions at certain minutes/seconds before news and for the EA to close one of the positions once the specific trade has hit a certain money loss but allowing the reverse trade to continue?  
  
Having faced slippage, manipulation and market lockout both manually and through an existing EA I am coming to the conclusion that perhaps being in the trade and taking a limited loss could increase the probability of profits(?) Alternatively entering minutes after the news based on historical behaviours could at times be equally profitable.  
  
Thanks again for all your efforts and look forward to your comments.  
Ben 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#371](/thread/post/11350303#post11350303 "Post Permalink")

  * Aug 9, 2018 10:54pm  Aug 9, 2018 10:54pm 

  * [ fairtraderuk](fairtraderuk)

  * | Joined Jul 2018  | Status: Trader | [574 Posts](/search?do=process&provider=Member&searchuser=701559)

> [Quoting fairtraderuk](/thread/post/11350288#post11350288 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi MathTrader apologies for the late response; the build seems to be 1090 May 2017 however the problem seems to have gone away - so thank you! On a separate note and hope this is not too much a rookie question - do you think it would be feasible for this EA or another adapted version to open both Buy & Sell positions at certain minutes/seconds before news and for the EA to close one of the positions once the specific trade has hit a certain money loss but allowing the reverse trade to continue? Having faced slippage, manipulation and market...
> 
> Ignored

Thanks in advance Matt! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#372](/thread/post/11350532#post11350532 "Post Permalink")

  * Aug 9, 2018 11:37pm  Aug 9, 2018 11:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting fairtraderuk](/thread/post/11350288#post11350288 "View Quoted Post")
> 
> Disliked
> 
> do you think it would be feasible for this EA or another adapted version to open both Buy & Sell positions at certain minutes/seconds before news and for the EA to close one of the positions once the specific trade has hit a certain money loss but allowing the reverse trade to continue?
> 
> Ignored

Hi fairtraderuk!  
  
I believe that it is fairly easy to program such idea, but I don't have such EA.  
  
Best,  
Matt 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#373](/thread/post/11350751#post11350751 "Post Permalink")

  * Aug 10, 2018 12:07am  Aug 10, 2018 12:07am 

  * [ fairtraderuk](fairtraderuk)

  * | Joined Jul 2018  | Status: Trader | [574 Posts](/search?do=process&provider=Member&searchuser=701559)

> [Quoting MathTrader7](/thread/post/11350532#post11350532 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi fairtraderuk! I believe that it is fairly easy to program such idea, but I don't have such EA. Best, Matt
> 
> Ignored

Thanks Matt,  
  
Based on your expertise do you think the idea of opening synchronised Buy&Sell trades on the same or correlated pair before news release and relying on the EA to close the losing trade reasonably within target during volatile news is realistic or feasible? ie is it worth investing into the idea?  
  
Also aside from the great material you kindly share here, do you take on customised development work?  
  
Cheers  
Ben 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#374](/thread/post/11351118#post11351118 "Post Permalink")

  * Aug 10, 2018 1:19am  Aug 10, 2018 1:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting fairtraderuk](/thread/post/11350751#post11350751 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks Matt, Based on your expertise do you think the idea of opening synchronised Buy&Sell trades on the same or correlated pair before news release and relying on the EA to close the losing trade reasonably within target during volatile news is realistic or feasible? ie is it worth investing into the idea? Also aside from the great material you kindly share here, do you take on customised development work? Cheers Ben
> 
> Ignored

I think we need to backtest this idea to see the results. I haven't traded news like this.   
  
/Matt 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [View Post](/thread/post/11351292#post11351292)
  * Disliked by [Thread Starter](mathtrader7)

  * [rizkh](rizkh)

  * [#376](/thread/post/11515812#post11515812 "Post Permalink")

  * Sep 26, 2018 5:26am  Sep 26, 2018 5:26am 

  * [ doura](doura)

  * | Joined Oct 2005  | Status: Trader | [57 Posts](/search?do=process&provider=Member&searchuser=4006)

Mathtrader7,  
Please I need your help with the Mathtrader7_NewHedgeEA.  
Whenever, I turn off my mt4, the EA get disabled and could not get it on to monitor any pairs opened with it before. Therefore, the take profit will not be active to continue monitoring the trade--have to close it manually. Any help please. I also would appreciate if you add in the input the coordinates xy to help us position the EA in a different location than where it is opening right now such lower, upper, right or left corners.  
Thank you. 

[doura](doura#14 "View Trade Explorer") Return Today: 0.1%

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#377](/thread/post/11805170#post11805170 "Post Permalink")

  * Dec 18, 2018 12:26pm  Dec 18, 2018 12:26pm 

  * [ SkyD](skyd)

  * | Joined Oct 2016  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=523441)

Hi friends, can anyone help me please, I was using the Mathtrader7_NewHedgeEA and my MT4 updated to build 1160 and now it does not work anymore.  
  
Thank you! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#378](/thread/post/11904842#post11904842 "Post Permalink")

  * Jan 21, 2019 1:44am  Jan 21, 2019 1:44am 

  * [ El1000](el1000)

  * | Joined Jun 2016  | Status: Trader | [202 Posts](/search?do=process&provider=Member&searchuser=470939)

> [Quoting MathTrader7](/thread/post/11007657#post11007657 "View Quoted Post")
> 
> Disliked
> 
> {quote} Varsågod!![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)
> 
> Ignored

Hi MathTrader7 ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I was trying the NewsHedgeEA and i got a message on MT4 "Incompatible MT4 client build version"  
Can you please update your NewsHedgeEA for us? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#379](/thread/post/11907774#post11907774 "Post Permalink")

  * Jan 21, 2019 10:58pm  Jan 21, 2019 10:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting El1000](/thread/post/11904842#post11904842 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi MathTrader7 ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) I was trying the NewsHedgeEA and i got a message on MT4 "Incompatible MT4 client build version" Can you please update your NewsHedgeEA for us?
> 
> Ignored

Hi, I will take a look at the issue and come back to you. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#380](/thread/post/11945841#post11945841 "Post Permalink")

  * Jan 31, 2019 9:21am  Jan 31, 2019 9:21am 

  * [ zularizal](zularizal)

  * | Joined Jan 2019  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=762100)

> [Quoting MathTrader7](/thread/post/11907774#post11907774 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, I will take a look at the issue and come back to you.
> 
> Ignored

Hi Math, can I use this ea without news? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#381](/thread/post/11947367#post11947367 "Post Permalink")

  * Jan 31, 2019 6:15pm  Jan 31, 2019 6:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting zularizal](/thread/post/11945841#post11945841 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Math, can I use this ea without news?
> 
> Ignored

Yes, you can use it to open two positions without waiting for any news. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#382](/thread/post/11950558#post11950558 "Post Permalink")

  * Feb 1, 2019 5:55am  Feb 1, 2019 5:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.74** of the EA released (I updated Post 1). This version is compiled with MT4 build 1170. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#383](/thread/post/11951398#post11951398 "Post Permalink")

  * Feb 1, 2019 12:56pm  Feb 1, 2019 12:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar758367_3.gif) luogen](luogen)

  * | Joined Jan 2019  | Status: Trader | [106 Posts](/search?do=process&provider=Member&searchuser=758367)

> [Quoting MathTrader7](/thread/post/11950558#post11950558 "View Quoted Post")
> 
> Disliked
> 
> Version 1.74 of the EA released (I updated Post 1). This version is compiled with MT4 build 1170.
> 
> Ignored

My MT4 is also version 1170. Unfortunately, when loading your EA, I was prompted to upgrade it. Incompatible? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#384](/thread/post/11952127#post11952127 "Post Permalink")

  * Edited 11:22pm  Feb 1, 2019 6:03pm | Edited 11:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting luogen](/thread/post/11951398#post11951398 "View Quoted Post")
> 
> Disliked
> 
> {quote} My MT4 is also version 1170. Unfortunately, when loading your EA, I was prompted to upgrade it. Incompatible?
> 
> Ignored

I hope not! :-)  
Mine is build 1170, I will see what happens when my MT4 platform upgrades... 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#385](/thread/post/11953779#post11953779 "Post Permalink")

  * Feb 1, 2019 11:22pm  Feb 1, 2019 11:22pm 

  * [ El1000](el1000)

  * | Joined Jun 2016  | Status: Trader | [202 Posts](/search?do=process&provider=Member&searchuser=470939)

> [Quoting MathTrader7](/thread/post/11952127#post11952127 "View Quoted Post")
> 
> Disliked
> 
> {quote} I hope not! :-) Mine is build 1170, I will see what happens when the MT4 platform upgrades...
> 
> Ignored

Hi I will check this when i get home on Monday ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#386](/thread/post/11956211#post11956211 "Post Permalink")

  * Feb 2, 2019 6:45pm  Feb 2, 2019 6:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar758367_3.gif) luogen](luogen)

  * | Joined Jan 2019  | Status: Trader | [106 Posts](/search?do=process&provider=Member&searchuser=758367)

[quote = MathTrader7; 11952127] {quote}我希望不是！:-)我的构建是1170，我会看到当我的MT4平台升级时会发生什么... [/ quote]  
Emmm loading EA occurs this way 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: QQå›¾ç‰‡20190202174252.png
Size: 34 KB](/attachment/image/3196540/thumbnail?d=1549100649)](/attachment/image/3196540?d=1549100649)   

Attached Image

![](/attachment/image/3196541?d=1549100650)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#387](/thread/post/11959826#post11959826 "Post Permalink")

  * Feb 4, 2019 4:26pm  Feb 4, 2019 4:26pm 

  * [ El1000](el1000)

  * | Joined Jun 2016  | Status: Trader | [202 Posts](/search?do=process&provider=Member&searchuser=470939)

> [Quoting MathTrader7](/thread/post/11952127#post11952127 "View Quoted Post")
> 
> Disliked
> 
> {quote} I hope not! :-) Mine is build 1170, I will see what happens when my MT4 platform upgrades...
> 
> Ignored

I have also build 1170, and I got also a error : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2019-02-04_08-24-58.jpg
Size: 78 KB](/attachment/image/3198329/thumbnail?d=1549265190)](/attachment/image/3198329?d=1549265190)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#388](/thread/post/11960563#post11960563 "Post Permalink")

  * Feb 4, 2019 7:38pm  Feb 4, 2019 7:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting El1000](/thread/post/11959826#post11959826 "View Quoted Post")
> 
> Disliked
> 
> {quote} I have also build 1170, and I got also a error : {image}
> 
> Ignored

I am working on a new version with integrated currency strength meter into the EA. I will release a new version to fix this issue. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#389](/thread/post/11961225#post11961225 "Post Permalink")

  * Feb 4, 2019 11:00pm  Feb 4, 2019 11:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.75** of the EA released (I updated Post 1). This version is compiled with MT4 build 1170 (bug fixes). 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#390](/thread/post/11963853#post11963853 "Post Permalink")

  * Feb 5, 2019 4:00pm  Feb 5, 2019 4:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar694080_2.gif) MarkStep](markstep)

  * | Commercial User  | Joined Jul 2018 | [247 Posts](/search?do=process&provider=Member&searchuser=694080)

> [Quoting MathTrader7](/thread/post/11960563#post11960563 "View Quoted Post")
> 
> Disliked
> 
> {quote} I am working on a new version with integrated currency strength meter into the EA. I will release a new version to fix this issue.
> 
> Ignored

How does the integrated currency strength meter work? thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#391](/thread/post/11964908#post11964908 "Post Permalink")

  * Feb 5, 2019 8:43pm  Feb 5, 2019 8:43pm 

  * [ El1000](el1000)

  * | Joined Jun 2016  | Status: Trader | [202 Posts](/search?do=process&provider=Member&searchuser=470939)

> [Quoting MathTrader7](/thread/post/11961225#post11961225 "View Quoted Post")
> 
> Disliked
> 
> Version 1.75 of the EA released (I updated Post 1). This version is compiled with MT4 build 1170 (bug fixes).
> 
> Ignored

Thank you very much MathTrader7, now it's working fine ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#392](/thread/post/11966779#post11966779 "Post Permalink")

  * Feb 6, 2019 3:32am  Feb 6, 2019 3:32am 

  * [ Checkz](checkz)

  * | Joined Dec 2009  | Status: Trader | [1,152 Posts](/search?do=process&provider=Member&searchuser=126739)

> [Quoting MathTrader7](/thread/post/11961225#post11961225 "View Quoted Post")
> 
> Disliked
> 
> Version 1.75 of the EA released (I updated Post 1). This version is compiled with MT4 build 1170 (bug fixes).
> 
> Ignored

Hello MathTrader7 I am using this current version and I noticed that once I place a hedged trade and either change timeframes or log out and then log back into my mt4 account that the EA no longer seems to track the pips of the hedge trade I just placed. You cant even use the EA to close the trade with the __**close all button**__ any more. Is this suppose to happen? I kind of like how it was keeping track of the pips I was am winning and losing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#393](/thread/post/11967052#post11967052 "Post Permalink")

  * Feb 6, 2019 4:58am  Feb 6, 2019 4:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting Checkz](/thread/post/11966779#post11966779 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello MathTrader7 I am using this current version and I noticed that once I place a hedged trade and either change timeframes or log out and then log back into my mt4 account that the EA no longer seems to track the pips of the hedge trade I just placed. You cant even use the EA to close the trade with the close all button any more. Is this suppose to happen? I kind of like how it was keeping track of the pips I was am winning and losing.
> 
> Ignored

The EA is designed for being used for a short time during red news release which we usually do not restart the MT4 platform, or change the timeframe of the chart. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#394](/thread/post/11967364#post11967364 "Post Permalink")

  * Feb 6, 2019 6:32am  Feb 6, 2019 6:32am 

  * [ Checkz](checkz)

  * | Joined Dec 2009  | Status: Trader | [1,152 Posts](/search?do=process&provider=Member&searchuser=126739)

> [Quoting MathTrader7](/thread/post/11967052#post11967052 "View Quoted Post")
> 
> Disliked
> 
> {quote} The EA is designed for being used for a short time during red news release which we usually do not restart the MT4 platform, or change the timeframe of the chart.
> 
> Ignored

Okay thanks 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [View Post](/thread/post/11967620#post11967620)
  * Disliked by [Thread Starter](mathtrader7)

  * [T4Trade](t4trade)

  * [#396](/thread/post/11982456#post11982456 "Post Permalink")

  * Feb 9, 2019 4:29pm  Feb 9, 2019 4:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar678589_2.gif) kudafoolhu](kudafoolhu)

  * | Joined May 2018  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=678589)

> [Quoting MathTrader7](/thread/post/9276708#post9276708 "View Quoted Post")
> 
> Disliked
> 
> {quote} 1. If the correlation is positive, we only use either BUY/SELL or SELL/BUY 2. If the correlation is negative, we only use either BUY/BUY or SELL/SELL - Let's assume that we have selected EURUSD and USDJPY with a negative correlation of -0.85, and we want to trade a high impact red news of USD. How do I make a decision to trade the news? - I look at a few currency strength indices (including fundamentals) to predict which currency, EUR or JPY is more powerful at the time of trading. - Let's say that it is JPY. In this case I will use SELL/SELL...
> 
> Ignored

Can we go for buy/buy also? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#397](/thread/post/11986931#post11986931 "Post Permalink")

  * Feb 11, 2019 6:57pm  Feb 11, 2019 6:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar678589_2.gif) kudafoolhu](kudafoolhu)

  * | Joined May 2018  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=678589)

Does the EA calculate lot size automatically? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#398](/thread/post/11987504#post11987504 "Post Permalink")

  * Feb 11, 2019 8:53pm  Feb 11, 2019 8:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting kudafoolhu](/thread/post/11986931#post11986931 "View Quoted Post")
> 
> Disliked
> 
> Does the EA calculate lot size automatically?
> 
> Ignored

In the early versions it does but in the newer versions it is all up to the trader to enter the lot sizes for the main and the hedge symbols. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#399](/thread/post/11987609#post11987609 "Post Permalink")

  * Feb 11, 2019 9:12pm  Feb 11, 2019 9:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar678589_2.gif) kudafoolhu](kudafoolhu)

  * | Joined May 2018  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=678589)

> [Quoting MathTrader7](/thread/post/11987504#post11987504 "View Quoted Post")
> 
> Disliked
> 
> {quote} In the early versions it does but in the newer versions it is all up to the trader to enter the lot sizes for the main and the hedge symbols.
> 
> Ignored

How do we calculate the lot sizes? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#400](/thread/post/11988060#post11988060 "Post Permalink")

  * Feb 11, 2019 10:52pm  Feb 11, 2019 10:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting kudafoolhu](/thread/post/11987609#post11987609 "View Quoted Post")
> 
> Disliked
> 
> {quote} How do we calculate the lot sizes?
> 
> Ignored

Basically you need first to find out how much a point of the main and hedge symbols worth in your account currency. Then look at ADR (Average Daily Range) values for both symbols and calculate lot sizes based on these values. Note: do calculation based on the assumption that what would be the profit/loss if the price of the main and hedge symbols goes to X and Y values given Lm and Lh lot sizes for the main and hedge symbols. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#401](/thread/post/12056081#post12056081 "Post Permalink")

  * Feb 28, 2019 3:11am  Feb 28, 2019 3:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.80 released (I updated Post 1). In this version an Experimental Currency Strength Meter is added to the EA.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURUSDM1.png
Size: 39 KB](/attachment/image/3242087/thumbnail?d=1551291053)](/attachment/image/3242087?d=1551291053)   

**

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [View Post](/thread/post/12056252#post12056252)
  * Disliked by [Thread Starter](mathtrader7)

  * [T4Trade](t4trade)

  * [#403](/thread/post/12056292#post12056292 "Post Permalink")

  * Edited 10:15pm  Feb 28, 2019 4:46am | Edited 10:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting T4Trade](/thread/post/12056252#post12056252 "View Quoted Post")
> 
> Disliked
> 
> if you are a coder,please would you make me an inidcator? i have been asking for very long time with no success,i dont know if this is a dumb idea or is it too difficult to make? i want to see present pip count on top of anycandle indicator (MTF) and secondly the percentage line like 25%,50% or 100 % depending on ATR 20 days on side of it. Thanks {image}
> 
> Ignored

This thread is not about anything other than the subject of Post 1. You can open a new thread in the [Platform Tech Forum](https://www.forexfactory.com/forumdisplay.php?f=69) for your programming request, or send me a private message (PM). But you are not allowed to write your programming request here in this thread. This is my last warning for you. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#404](/thread/post/12061936#post12061936 "Post Permalink")

  * Mar 1, 2019 5:17am  Mar 1, 2019 5:17am 

  * [ El1000](el1000)

  * | Joined Jun 2016  | Status: Trader | [202 Posts](/search?do=process&provider=Member&searchuser=470939)

> [Quoting MathTrader7](/thread/post/12056081#post12056081 "View Quoted Post")
> 
> Disliked
> 
> Version 1.80 released (I updated Post 1). In this version an Experimental Currency Strength Meter is added to the EA. {image}
> 
> Ignored

Hi I will test this tomorrow ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#405](/thread/post/12068528#post12068528 "Post Permalink")

  * Mar 2, 2019 11:57pm  Mar 2, 2019 11:57pm 

  * [ f3n_dy](f3n_dy)

  * | Joined Jul 2006  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=13590)

what do you think about triangular hedge ..is it posibble because i saw consistency in Wuxiaoming System.  
here is the live account of him.  
Account login id 60304  
Password r6pimbd  
Server CsiGroupLtd-Live  
Login only at mobile 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#406](/thread/post/12068554#post12068554 "Post Permalink")

  * Mar 3, 2019 12:29am  Mar 3, 2019 12:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar757265_1.gif) tidal](tidal)

  * | Membership Revoked  | Joined Jan 2019 | [81 Posts](/search?do=process&provider=Member&searchuser=757265)

Man, this is what I’m looking for. Thank you for youur great share of news trigger EA 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#407](/thread/post/12077431#post12077431 "Post Permalink")

  * Mar 5, 2019 7:38pm  Mar 5, 2019 7:38pm 

  * [ billbss](billbss)

  * Joined Apr 2006 | Status: Trader | [4,301 Posts](/search?do=process&provider=Member&searchuser=9243)

Mathtrader,  
I'm late to the party with this thread.  
I'm just now trying to make the EA work.  
I'm enclosing a screen shot of my settings.  
I had the time set for 12:20 chart time. I had pressed the BUY/SELL button.  
12:20 came and went and nothing happened.  
The "last known broker time" never advanced from 12:09 which was the time I added the EA to the chart.  
What did I do wrong?  
I'm sure I made a stupid mistake.  
Thanks

Attached Image (click to enlarge)

[![Click to Enlarge

Name: RED EA.png
Size: 136 KB](/attachment/image/3251200/thumbnail?d=1551782311)](/attachment/image/3251200?d=1551782311)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#408](/thread/post/12077451#post12077451 "Post Permalink")

  * Mar 5, 2019 7:46pm  Mar 5, 2019 7:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting billbss](/thread/post/12077431#post12077431 "View Quoted Post")
> 
> Disliked
> 
> Mathtrader, I'm late to the party with this thread. I'm just now trying to make the EA work. I'm enclosing a screen shot of my settings. I had the time set for 12:20 chart time. I had pressed the BUY/SELL button. 12:20 came and went and nothing happened. The "last known broker time" never advanced from 12:09 which was the time I added the EA to the chart. What did I do wrong? I'm sure I made a stupid mistake. Thanks{image}
> 
> Ignored

Hi billbss,  
  
It seems that the EA didn't receive any ticks after you have changed the input settings. Please check your MT4's Expert tab to see if there is any error caused the EA to crash or something? I will try to reporduce this error on my MT4 and come back to you when I have more info about this problem.  
  
/Matt 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#409](/thread/post/12078442#post12078442 "Post Permalink")

  * Mar 5, 2019 11:41pm  Mar 5, 2019 11:41pm 

  * [ billbss](billbss)

  * Joined Apr 2006 | Status: Trader | [4,301 Posts](/search?do=process&provider=Member&searchuser=9243)

I got it working.  
1\. There was a divide by zero error in the CSM that seemed to mess it up.  
2\. I changed to the previous version (without the CSM)  
3\. I found I was using the wrong time. I had assumed the EA wanted chart time. In my case it wanted chart time - 2.  
The screenshot shows the only settings that let it work. I'm good with that. I can use it.  
Thank you!  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EA WORKED.png
Size: 28 KB](/attachment/image/3251612/thumbnail?d=1551796863)](/attachment/image/3251612?d=1551796863)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#410](/thread/post/12081562#post12081562 "Post Permalink")

  * Mar 6, 2019 5:18pm  Mar 6, 2019 5:18pm 

  * [ billbss](billbss)

  * Joined Apr 2006 | Status: Trader | [4,301 Posts](/search?do=process&provider=Member&searchuser=9243)

I made $150 on the AUD GDP. Thank you.  
Couple of questions.  
If both trades are active how do you ever get into profit or loss so the EA will close the trades? I let the EA initiate the trades and did the rest manually. Is there any other way?  
Which time frame do you check for correlation and currency strength?  
Thanks in advance. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#411](/thread/post/12082098#post12082098 "Post Permalink")

  * Mar 6, 2019 7:35pm  Mar 6, 2019 7:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting billbss](/thread/post/12081562#post12081562 "View Quoted Post")
> 
> Disliked
> 
> I made $150 on the AUD GDP. Thank you. Couple of questions. If both trades are active how do you ever get into profit or loss so the EA will close the trades? I let the EA initiate the trades and did the rest manually. Is there any other way? Which time frame do you check for correlation and currency strength? Thanks in advance.
> 
> Ignored

Great to hear that you made profits using this EA.  
  
As written in Post 1,  
  
5\. Net Take Profit (money):  
\- **When net profit becomes greater than this value, the EA automatically closes both positions.**  
6\. Net Stop Loss (money):  
\- **When net profit becomes less than negative of this value, the EA automatically closes both positions.**  
  
The other way it to close the basket manually using the buttons of the EA.  
  
The correlation is calculated based on D1 data. The currency strength calculations are complex, I use both price (M1~H1) and _tick volume_.  
  
/Matt 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#412](/thread/post/12082139#post12082139 "Post Permalink")

  * Mar 6, 2019 7:46pm  Mar 6, 2019 7:46pm 

  * [ billbss](billbss)

  * Joined Apr 2006 | Status: Trader | [4,301 Posts](/search?do=process&provider=Member&searchuser=9243)

5\. Net Take Profit (money):  
\- **When net profit becomes greater than this value, the EA automatically closes both positions.**  
6\. Net Stop Loss (money):  
\- **When net profit becomes less than negative of this value, the EA automatically closes both positions.**  
  
How can you have net profit or net loss with the hedge still in place? The net should be roughly zero - one pair in profit and the opposite pair in loss. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#413](/thread/post/12083556#post12083556 "Post Permalink")

  * Mar 7, 2019 12:36am  Mar 7, 2019 12:36am 

  * [ billbss](billbss)

  * Joined Apr 2006 | Status: Trader | [4,301 Posts](/search?do=process&provider=Member&searchuser=9243)

I'm beginning to see. Sometimes the pairs don't move in the opposite direction like they're supposed to and don't counter balance each other.  
It takes awhile to get used to this. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#414](/thread/post/12089625#post12089625 "Post Permalink")

  * Mar 8, 2019 4:44am  Mar 8, 2019 4:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting billbss](/thread/post/12082139#post12082139 "View Quoted Post")
> 
> Disliked
> 
> 5\. Net Take Profit (money): - When net profit becomes greater than this value, the EA automatically closes both positions. 6. Net Stop Loss (money): - When net profit becomes less than negative of this value, the EA automatically closes both positions. How can you have net profit or net loss with the hedge still in place? The net should be roughly zero - one pair in profit and the opposite pair in loss.
> 
> Ignored

Let's have an example. The main symbol is **EURUSD** and the hedge symbol is **USDCAD**. After opening two positions, if we call the profit on EURUSD, **Pm** and the profit on USDCAD, **Ph** , the net profit is just the sum of them,  
  
**Pnet = Pm + Ph.**  
  
For example, if **Pm** is equal to **+150** USD (in profit) and **Ph** is equal to **-90** USD (in loss), the net profit becomes +**60** USD (in profit),  
  
**Pnet = 150 - 90 = 60.**  
  
There is no guarantee that if one pair (EURUSD) is in profit, the other pair (USDCAD) be in the same amount of loss!  
  
Hope this answers your questions. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#415](/thread/post/12107184#post12107184 "Post Permalink")

  * Mar 13, 2019 5:25am  Mar 13, 2019 5:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar781348_2.gif) Dzlabre](dzlabre)

  * | Joined Mar 2019  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=781348)

Congratulations on the ea .. I have a question can I insert only the time instead of entering the year, day, month? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#416](/thread/post/12234561#post12234561 "Post Permalink")

  * Apr 23, 2019 1:14pm  Apr 23, 2019 1:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar566242_1.gif) andylaudj](andylaudj)

  * | Joined Mar 2017  | Status: Trader | [22 Posts](/search?do=process&provider=Member&searchuser=566242)

> [Quoting billbss](/thread/post/12077431#post12077431 "View Quoted Post")
> 
> Disliked
> 
> Mathtrader, I'm late to the party with this thread. I'm just now trying to make the EA work. I'm enclosing a screen shot of my settings. I had the time set for 12:20 chart time. I had pressed the BUY/SELL button. 12:20 came and went and nothing happened. The "last known broker time" never advanced from 12:09 which was the time I added the EA to the chart. What did I do wrong? I'm sure I made a stupid mistake. Thanks{image}
> 
> Ignored

I also have the same problem as you.help me,thank you 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: fac.png
Size: 100 KB](/attachment/image/3320068/thumbnail?d=1555992855)](/attachment/image/3320068?d=1555992855)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#417](/thread/post/12234779#post12234779 "Post Permalink")

  * Apr 23, 2019 5:10pm  Apr 23, 2019 5:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting andylaudj](/thread/post/12234561#post12234561 "View Quoted Post")
> 
> Disliked
> 
> {quote} I also have the same problem as you.help me,thank you {image}
> 
> Ignored

From the log data it looks there is a problem with reading GBPJPY values. Try to open a chart of GBPJPY (for example, M1). 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#418](/thread/post/12304590#post12304590 "Post Permalink")

  * Jun 1, 2019 5:48am  Jun 1, 2019 5:48am 

  * [ poliihor](poliihor)

  * | Joined May 2009  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=102258)

Hi Math,  
  
Just found this thread and your EA looks very promissing - thank you very much for sharing it  
  
I have one problem with running it on build 1170, ver 4  
  
When I add EA to chart with settings below it would give thew following error:  
  
I know it was previously discussed in hear, so I tried to input date and time 1 hour ahead of mt4 time even though Auto trade was disabled, but it still did not work. I tried next year the same problem  
  
  
  
Can you kindly help to solve it  
  
Thank you in advance !! 

Attached Images

![](/attachment/image/3350568?d=1559335563) ![](/attachment/image/3350570?d=1559335662) ![](/attachment/image/3350571?d=1559335698)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#419](/thread/post/12306213#post12306213 "Post Permalink")

  * Jun 3, 2019 1:22am  Jun 3, 2019 1:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting poliihor](/thread/post/12304590#post12304590 "View Quoted Post")
> 
> Disliked
> 
> Hi Math, Just found this thread and your EA looks very promissing - thank you very much for sharing it I have one problem with running it on build 1170, ver 4 When I add EA to chart with settings below it would give thew following error: I know it was previously discussed in hear, so I tried to input date and time 1 hour ahead of mt4 time even though Auto trade was disabled, but it still did not work. I tried next year the same problem Can you kindly help to solve it Thank you in advance !! {image} {image} {image}
> 
> Ignored

Hi, I will look at this problem and possibly recompile it with the latest build of MT4. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#420](/thread/post/12306279#post12306279 "Post Permalink")

  * Jun 3, 2019 2:53am  Jun 3, 2019 2:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.81 released** (I updated Post 1). This version is compiled with MT4 build 1170. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#421](/thread/post/12306549#post12306549 "Post Permalink")

  * Jun 3, 2019 9:14am  Jun 3, 2019 9:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar41845_13.gif) RisingSun](risingsun)

  * Joined Jun 2007 | Status: trader | [1,703 Posts](/search?do=process&provider=Member&searchuser=41845)

Thanks Math for sharing an interesting EA. Couple of points.  
1\. When I see the broker time reading is not up to date, I clicked on the EA to open the input window and closed, then the EA does not reflect/read/manage the on-going trades any more. Since it important that the broker time reading be correct in order that the EA opens trades at the input time, it there anyway you can have a button to click so the time reading can be re activated?  
2\. Re. the CSM how to read the strength, i.e., the upper or lower of the zero line, and/or the length of the bar?  
Thanks,  
RS 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#422](/thread/post/12307051#post12307051 "Post Permalink")

  * Edited 7:16pm  Jun 3, 2019 4:27pm | Edited 7:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting RisingSun](/thread/post/12306549#post12306549 "View Quoted Post")
> 
> Disliked
> 
> Thanks Math for sharing an interesting EA. Couple of points. 1. When I see the broker time reading is not up to date, I clicked on the EA to open the input window and closed, then the EA does not reflect/read/manage the on-going trades any more. Since it important that the broker time reading be correct in order that the EA opens trades at the input time, it there anyway you can have a button to click so the time reading can be re activated? 2. Re. the CSM how to read the strength, i.e., the upper or lower of the zero line, and/or the length of...
> 
> Ignored

Hi RisingSun!  
  
I will fix (1) in the next release.  
  
Regarding (2), a CSM bar above (below) zero line means an increase (decrease) to the power of the corresponding currency. The CSM bars are normalized to the maximum absolute power values. In the next versions I am going to remove normalization from EA code in order to show the absolute currency powers.  
  
Best,  
Matt 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#423](/thread/post/12310383#post12310383 "Post Permalink")

  * Jun 4, 2019 11:43pm  Jun 4, 2019 11:43pm 

  * [ poliihor](poliihor)

  * | Joined May 2009  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=102258)

> [Quoting MathTrader7](/thread/post/12306279#post12306279 "View Quoted Post")
> 
> Disliked
> 
> Version 1.81 released (I updated Post 1). This version is compiled with MT4 build 1170.
> 
> Ignored

Thank you very much for update Math !!  
  
Strange though, now i'm getting different error - buttons and strength meter won't work (I have tested on 2 different brokers MT4 to make sure it is not a problem of MT4)  
  
Can you please take a look what may be wrong ?  
  
Thanks in advance !  
  
2019.06.04 15:38:53.947 MathTrader7_NewsHedgeEA AUDUSD..,M15: zero divide in 'CForexStrengthMeter.mqh' (122,28)  
2019.06.04 15:38:51.322 MathTrader7_NewsHedgeEA AUDUSD..,M15: initialized  
2019.06.04 15:38:51.213 MathTrader7_NewsHedgeEA AUDUSD..,M15 inputs: InpAction=0; InpTime=2020.06.15 14:30:00; InpRelevantButtonsOnly=false; InpHedgeSymbol=EURUSD..; InpTPmoney=5.0; InpSLmoney=10.0; InpLotSize=0.01; InpHedgeLotSize=0.01; InpSlippage=30; InpMagicNumber=1122;  
2019.06.04 15:38:31.432 Expert MathTrader7_NewsHedgeEA AUDUSD..,M15: loaded successfully 

Attached Image

![](/attachment/image/3353213?d=1559659314)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#424](/thread/post/12310645#post12310645 "Post Permalink")

  * Jun 5, 2019 1:49am  Jun 5, 2019 1:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting poliihor](/thread/post/12310383#post12310383 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thank you very much for update Math !! Strange though, now i'm getting different error - buttons and strength meter won't work (I have tested on 2 different brokers MT4 to make sure it is not a problem of MT4) Can you please take a look what may be wrong ? Thanks in advance ! 2019.06.04 15:38:53.947 MathTrader7_NewsHedgeEA AUDUSD..,M15: zero divide in 'CForexStrengthMeter.mqh' (122,28) 2019.06.04 15:38:51.322 MathTrader7_NewsHedgeEA AUDUSD..,M15: initialized 2019.06.04 15:38:51.213 MathTrader7_NewsHedgeEA AUDUSD..,M15 inputs: InpAction=0;...
> 
> Ignored

I will look at the problem. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#425](/thread/post/12315454#post12315454 "Post Permalink")

  * Jun 7, 2019 2:58am  Jun 7, 2019 2:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.82** released (I updated Post 1).  
**Note: The CSM needs your broker to provide all major Forex currency pairs to work.**

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#426](/thread/post/12318578#post12318578 "Post Permalink")

  * Jun 9, 2019 1:21am  Jun 9, 2019 1:21am 

  * [ phuongtien](phuongtien)

  * | Joined Jun 2019  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=815609)

> [Quoting akira00](/thread/post/8590971#post8590971 "View Quoted Post")
> 
> Disliked
> 
> Interesting strategy,mt7. Although my broker is not allowed EA.But I tested manually this strategy.I used it with the last NEWS：Prelim UoM Consumer Sentiment.Good results. But I still have a doubt.I think the two symbols the fluctuation is not the same.We can win may also lose.This depends on whether we choose to buy or sell.And we need to stoploss?How to takeprofit? {image}
> 
> Ignored

How about this MT7 "We can win may also lose.This depends on whether we choose to buy or sell" -> we accept this right? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#427](/thread/post/12319950#post12319950 "Post Permalink")

  * Jun 10, 2019 4:37pm  Jun 10, 2019 4:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting phuongtien](/thread/post/12318578#post12318578 "View Quoted Post")
> 
> Disliked
> 
> {quote} How about this MT7 "We can win may also lose.This depends on whether we choose to buy or sell" -> we accept this right?
> 
> Ignored

There is no system of trading Forex that wins 100%! Keep this in mind! 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#428](/thread/post/12320009#post12320009 "Post Permalink")

  * Jun 10, 2019 5:20pm  Jun 10, 2019 5:20pm 

  * [ phuongtien](phuongtien)

  * | Joined Jun 2019  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=815609)

> [Quoting MathTrader7](/thread/post/12319950#post12319950 "View Quoted Post")
> 
> Disliked
> 
> {quote} There is no system of trading Forex that wins 100%! Keep this in mind!
> 
> Ignored

Yes i know, so i ask we will accept it?because we just predict what red new is good for this currency, what is not good right? or is there anyway to lower the risk?  
  
Thanks for your attention 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#429](/thread/post/12320325#post12320325 "Post Permalink")

  * Jun 10, 2019 8:31pm  Jun 10, 2019 8:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting phuongtien](/thread/post/12320009#post12320009 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes i know, so i ask we will accept it?because we just predict what red new is good for this currency, what is not good right? or is there anyway to lower the risk? Thanks for your attention
> 
> Ignored

If you know this fact, then you have already accepted it; there is no question.  
Regarding a way to reduce the risk, I would say to use only "**high impact red news** ". 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#430](/thread/post/12322156#post12322156 "Post Permalink")

  * Jun 11, 2019 7:15pm  Jun 11, 2019 7:15pm 

  * [ poliihor](poliihor)

  * | Joined May 2009  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=102258)

> [Quoting MathTrader7](/thread/post/12315454#post12315454 "View Quoted Post")
> 
> Disliked
> 
> Version 1.82 released (I updated Post 1). Note: The CSM needs your broker to provide all major Forex currency pairs to work.
> 
> Ignored

Hi Math,  
Do you think it would be possible to add in setting suffix/prefix field ?  
Fot example, I have just downloaded latest version and put it on Rakuten broker where all symbols have "austd" suffix. Now I'm getting error below as CMS wants to get history for all majors, EURNZD in this case while broker has data for EURNZDaustd  
  
2019.06.11 11:09:25.639 MathTrader7_NewsHedgeEA EURUSDaustd,M15: Error!: There is no history data for EURNZD in your broker's server!  
  
Many thanks in advance ! 

Attached Image

![](/attachment/image/3358227?d=1560248009)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#431](/thread/post/12322233#post12322233 "Post Permalink")

  * Edited Jun 12, 2019 2:56pm  Jun 11, 2019 7:56pm | Edited Jun 12, 2019 2:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting poliihor](/thread/post/12322156#post12322156 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Math, Do you think it would be possible to add in setting suffix/prefix field ? Fot example, I have just downloaded latest version and put it on Rakuten broker where all symbols have "austd" suffix. Now I'm getting error below as CMS wants to get history for all majors, EURNZD in this case while broker has data for EURNZDaustd 2019.06.11 11:09:25.639 MathTrader7_NewsHedgeEA EURUSDaustd,M15: Error!: There is no history data for EURNZD in your broker's server! Many thanks in advance ! {image}
> 
> Ignored

Hi!  
I will fix it in the next version. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#432](/thread/post/12352122#post12352122 "Post Permalink")

  * Jun 27, 2019 12:34am  Jun 27, 2019 12:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Version 1.83** released (I updated Post 1). **The CSM is now working on brokers with suffix symbols.**

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#433](/thread/post/12491112#post12491112 "Post Permalink")

  * Sep 9, 2019 7:58pm  Sep 9, 2019 7:58pm 

  * [ yoyo888](yoyo888)

  * | Joined Jun 2019  | Status: Trader | [18 Posts](/search?do=process&provider=Member&searchuser=823733)

> [Quoting MathTrader7](/thread/post/12352122#post12352122 "View Quoted Post")
> 
> Disliked
> 
> Version 1.83 released (I updated Post 1). The CSM is now working on brokers with suffix symbols.
> 
> Ignored

How can I not automate trading? I don't want to buy and sell every time. can you help me 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#434](/thread/post/12492370#post12492370 "Post Permalink")

  * Edited Sep 11, 2019 3:52am  Sep 10, 2019 6:21am | Edited Sep 11, 2019 3:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

I am attaching an experimental version of the EA to this post that reads calendar news of FF and automatically trades. This version is simplified, and its main purpose is **to test its functionality**. This version only trades "EURUSD" and "GBPUSD" based on **High Imapct Red news** of "USD" currency and the currency strength meter that I have developed. It works only on demo accounts (the EA is unstable and risky!) and expires at the end of this year. If everything goes well, I would release a full version. If you are using this EA, please share the results and report the bugs in this thread.  
  
Note: You need to add the following URL to your MT4 platform, **<https://cdn-nfs.faireconomy.media>**.  

Attached Image

![](/attachment/image/3435106?d=1568064248)

  
Edit: A minor bug fixed.  

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [MT7_NewsHedgeEA.ex4](/attachment/file/3435995?d=1568141498) 95 KB | 422 downloads 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#435](/thread/post/12500091#post12500091 "Post Permalink")

  * Sep 13, 2019 6:01am  Sep 13, 2019 6:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

I recompiled the EA with MT4 build 1212. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [MT7_NewsHedgeEA.ex4](/attachment/file/3438312?d=1568322063) 95 KB | 613 downloads 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#436](/thread/post/12500505#post12500505 "Post Permalink")

  * Sep 13, 2019 1:40pm  Sep 13, 2019 1:40pm 

  * [ yoyo888](yoyo888)

  * | Joined Jun 2019  | Status: Trader | [18 Posts](/search?do=process&provider=Member&searchuser=823733)

[quote = MathTrader7; 12500091]我用MT4 build 1212重新编译了EA。{file} [/ quote]  
  
Can I set up an automated trade? I don't want to buy and sell every time. can you help me 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#437](/thread/post/12500626#post12500626 "Post Permalink")

  * Sep 13, 2019 3:11pm  Sep 13, 2019 3:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting yoyo888](/thread/post/12500505#post12500505 "View Quoted Post")
> 
> Disliked
> 
> [quote = MathTrader7; 12500091]我用MT4 build 1212重新编译了EA。{file} [/ quote] Can I set up an automated trade? I don't want to buy and sell every time. can you help me
> 
> Ignored

Sorry! I can't help you. 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#438](/thread/post/12502949#post12502949 "Post Permalink")

  * Sep 14, 2019 9:49pm  Sep 14, 2019 9:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

**Ver. 1.84 released (I updated Post 1). Recompiled with MT4 build 1220.**

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#439](/thread/post/12509459#post12509459 "Post Permalink")

  * Sep 18, 2019 4:16pm  Sep 18, 2019 4:16pm 

  * [ morne72](morne72)

  * | Joined Dec 2014  | Status: Trader | [85 Posts](/search?do=process&provider=Member&searchuser=394797)

> [Quoting MathTrader7](/thread/post/12492370#post12492370 "View Quoted Post")
> 
> Disliked
> 
> I am attaching an experimental version of the EA to this post that reads calendar news of FF and automatically trades. This version is simplified, and its main purpose is to test its functionality. This version only trades "EURUSD" and "GBPUSD" based on High Imapct Red news of "USD" currency and the currency strength meter that I have developed. It works only on demo accounts (the EA is unstable and risky!) and expires at the end of this year. If everything goes well, I would release a full version. If you are using this EA, please share the results...
> 
> Ignored

  
@Mathtrader what is the default lot size ?I see the trail version doesn't have any input for a lot size ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#440](/thread/post/12509584#post12509584 "Post Permalink")

  * Sep 18, 2019 5:26pm  Sep 18, 2019 5:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar380581_2.gif) MathTrader7](mathtrader7)

  * Joined Aug 2014 | Status: Trading | [2,162 Posts](/search?do=process&provider=Member&searchuser=380581)

> [Quoting morne72](/thread/post/12509459#post12509459 "View Quoted Post")
> 
> Disliked
> 
> {quote} @Mathtrader what is the default lot size ?I see the trail version doesn't have any input for a lot size ?
> 
> Ignored

The lot size is fixed for now (0.1). The purpose of this version is to test the functionality of the EA (whether it reads the news from FF calendar correctly and executes the orders as planned). Please share your results in this thread if you are using this EA. I am going to further develop this EA (and I also have plans to develop other news based EAs). 

Trading is the hardest way to make easy money...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

  
Thanks!") 4 replies

[Best Broker for (High Impact) Red News](/thread/711133-best-broker-for-high-impact-red-news "Sorry if this is a repeat. Oanda? IB? 
Also anyone tried futures brokers for red news?") 6 replies

[Trading or Lack Thereof During Red/High Impact News](/thread/666395-trading-or-lack-thereof-during-redhigh-impact-news "Guys, 
If a High Impact News is scheduled, say 
  
CAD- CPI Numbers 
  
 
  
Keeping aside the Systems/approaches that trade news...") 5 replies

[Historical Data Mine - FF Red Folder News and Impact](/thread/461446-historical-data-mine-ff-red-folder-news "Hi, 
 

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)
  * Subscribe
  * [113](javascript:void\(0\);)

Attachments: Red News Hedge Trading + EA

Tags: Red News Hedge Trading + EA

#  [](/thread/565676-red-news-hedge-trading-ea)Red News Hedge Trading + EA 

  * 

  * [#441](/thread/post/12831515#post12831515 "Post Permalink")

  * Mar 24, 2020 1:13am  Mar 24, 2020 1:13am 

  * [ saman1](saman1)

  * | Joined Dec 2017  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=633195)

hello everyone... is there an EA according to below condition i mention..  
buy sell both trade should open at once... ( in 1 click i need to put Buy sell Both trades)  
want to use fixed SL and TP for both trades  
help me if you can...  
sorry for my bad english... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#442](/thread/post/12834873#post12834873 "Post Permalink")

  * Mar 25, 2020 6:54am  Mar 25, 2020 6:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar134243_3.gif) danjuma](danjuma)

  * | Joined Feb 2010  | Status: Trader | [585 Posts](/search?do=process&provider=Member&searchuser=134243)

The EA, as downloaded in post no.1 does not appear to be working. When I drag onto a chart and click okay, it comes up with the message: "Auto Trade Time is passed!" even when "Auto Trade Disabled" is selected in the inputs! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#443](/thread/post/12835238#post12835238 "Post Permalink")

  * Mar 25, 2020 1:10pm  Mar 25, 2020 1:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar561720_1.gif) bojack34](bojack34)

  * Joined Mar 2017 | Status: Trader | [2,042 Posts](/search?do=process&provider=Member&searchuser=561720)

> [Quoting saman1](/thread/post/12831515#post12831515 "View Quoted Post")
> 
> Disliked
> 
> hello everyone... is there an EA according to below condition i mention.. buy sell both trade should open at once... ( in 1 click i need to put Buy sell Both trades) want to use fixed SL and TP for both trades help me if you can... sorry for my bad english...
> 
> Ignored

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [script_cm_open_2_stoporders.mq4](/attachment/file/3587929?d=1585109387) 9 KB | 278 downloads 

  
  
Here is a Script that should do what your asking. Make sure you put it in your Script Folder and NOT your Experts Folder. This is a script and NOT an EA. I hope this helps. GL. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#444](/thread/post/12836760#post12836760 "Post Permalink")

  * Mar 26, 2020 12:23am  Mar 26, 2020 12:23am 

  * [ saman1](saman1)

  * | Joined Dec 2017  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=633195)

> [Quoting bojack34](/thread/post/12835238#post12835238 "View Quoted Post")
> 
> Disliked
> 
> {quote} {file} Here is a Script that should do what your asking. Make sure you put it in your Script Folder and NOT your Experts Folder. This is a script and NOT an EA. I hope this helps. GL.
> 
> Ignored

Thank You very much bojack34 ... I'ii try 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#445](/thread/post/12881671#post12881671 "Post Permalink")

  * Apr 17, 2020 4:42am  Apr 17, 2020 4:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar134243_3.gif) danjuma](danjuma)

  * | Joined Feb 2010  | Status: Trader | [585 Posts](/search?do=process&provider=Member&searchuser=134243)

> [Quoting danjuma](/thread/post/12834873#post12834873 "View Quoted Post")
> 
> Disliked
> 
> The EA, as downloaded in post no.1 does not appear to be working. When I drag onto a chart and click okay, it comes up with the message: "Auto Trade Time is passed!" even when "Auto Trade Disabled" is selected in the inputs!
> 
> Ignored

@[MathTrader7](https://www.forexfactory.com/mathtrader7), see my original post above. Any solution tot he problem I am experiencing with your EA, as I would like to demo the EA? Thanks

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#446](/thread/post/12886218#post12886218 "Post Permalink")

  * Apr 20, 2020 8:38am  Apr 20, 2020 8:38am 

  * [ 42967U](42967u)

  * | Joined Apr 2020  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=941731)

Tried to trade the NZD newsat 23:45 GMT but also had the same problem saying the auto trade time had passed despite auto trade being disabled.  
  
I'm using MT4 version 4.00 build 1260. Any help will be helpful 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#447](/thread/post/14037502#post14037502 "Post Permalink")

  * Jun 19, 2022 2:20am  Jun 19, 2022 2:20am 

  * [ leobrowtrade](leobrowtrade)

  * | Joined Jun 2022  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=1468958)

I'm trying to put it on the chart, but a message appears "auto trade time is passed", how can I solve this? Thanks in advance!  
  

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#448](/thread/post/14992719#post14992719 "Post Permalink")

  * Last Post: Sep 10, 2024 9:12pm  Sep 10, 2024 9:12pm 

  * [ idriss33999](idriss33999)

  * | Joined May 2019  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=810469)

the ea that is provided when i load it it says that it has been expired 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Red News Hedge Trading + EA
  *   * [ **Reply to Thread** ](/thread/565676-red-news-hedge-trading-ea/reply#reply)

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)
