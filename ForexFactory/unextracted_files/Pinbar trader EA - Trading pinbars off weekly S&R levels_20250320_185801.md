

  * 

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#1](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly "Post Permalink")

  * First Post: Edited Jan 29, 2018 1:39am  Jan 27, 2018 6:15pm | Edited Jan 29, 2018 1:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

**=== Pinbar Trader EA ===**

  
Hi everyone, welcome !  
I would like to present my latest EA.  
It implements a very basic, but very effective strategy. trading pinbars from weekly S&R levels  
  
**Strategy:**  
\- we wait for a pinbar to appear which rejects a weekly support & resistance level  
\- When the candle with the pinbar is closed we open a new buy/sell trade on the next candle  
  
**The Pinbar trader EA**  
The pinbar trader EA implements the strategy and has lots of extra features:

  1. it scans multiple currencies. So load the EA on 1 chart and it will scan all major currencies by default (you can change which ones in the settings)
  2. it can send you alerts when a pinbar is detected on a weekly S&R level
  3. it can do auto trading, although please run this on demo first before you decide to go live with this
  4. You can choose between a trailing stops or risk:reward exit strategy
  5. You can choose if it should use a fixed lot sizes, a fixed amount of $, or a risk % of your account balance
  6. It has a news filter implemented to skip trading during news events

**Installation:**  
Download the zip file and unzip it somewhere

  1. copy the pinbartrader.tpl to your MT4 templates folder
  2. copy the SupportResistance.ex4 to your MT4 indicators folder
  3. copy the PinbarTrader.ex4 to your MT4 experts folder
  4. Now start MT4, enable auto trading and DLL imports
  5. put the EA on any chart on the **Daily (D1) timeframe !**

and voila..  
By default auto-trading and alerts are turned off. So enable them if you want to use them  
  
**Source code:**  
Want to get involved ? you can find all source code for this (and my other ea's & indicators) on GitHub  
<https://github.com/erwin-beckers/SimpleTrendReversalEA>  
  
**Backtesting:**  
Attached the results of a 2-year backtest on EURUSD  
  
**Idea's for the next version/future:**  
\- add a distributed S&R filter. Instead of trying to calculate the correct S&R levels, simply download them from a central server.  
\- send alerts for mean reversal setups (and perhaps auto trade those)  
\- open with-the-trend trades on pinbars for pinbars on/to the mean  
  
  
  
**General usage:**  
The EA will show you a table with the pairs which have a pinbar or are at a weekly S&R resistance level.  
Pairs which don't have any pinbar and are not at a weekly S&R level are filtered out and are not shown.  
In short.. the EA will only show pairs which looks interesting  
Off course when time goes by new pairs will be shown or removed automatically.  
  
The color of a pair indicates if we are looking to buy (green) or sell (red)  
When all signals are valid the last column will contain the word buy or sell and when this happens the EA will send you an alert and/or open a trade.  
If you want to look at the chart , then simply click on the name of the currency pair in the 1st column (e.g. EURUSD in the screenshot)  
This will open a new chart with the S&R indicator attached so you can take a quick look  
  
When auto-trading is enabled the EA will also show you a list of all open trades and a trade statistics panel where you can keep track on its performance  
  
**Manual Trading**  
The EA can be used as an aid for manual trading or it can do automated trading.  
  
For manual trading just set _sendAlerts_ =true (and/or _sendEmails_ = true)  
The EA will then send an alert (or email) when it detects a valid buy/sell signal.  
Alerts can even be send to your phone!  
See here on how to set this up : [http://www.cmapllc.com/how-to-set-up...nd-iphone.html](http://www.cmapllc.com/how-to-set-up-push-notifications-in-mt4-mobile-android-and-iphone.html)  
When you receive an alert you can look at the chart and if you like the signal or not and perhaps open a trade manually  
  
**Automated Trading**  
For automated trading just set _allowTrading=true_ and choose your lotsize and exit strategy  
The EA will open trades automatically when it detects valid buy/sell signals and manage these trades for you.  
When auto trading you must tell the EA how much money it is allowed to use for each trade  
Here you have 3 options:  
  
**MoneyManagement _:_**  

_Fixed Lot Size / trade_

Set _MoneyManagent = UseFixedLotSize_ and fill in your lotsize under _FixedLotSize_

Each trade opened by the EA will use this fixed lot size

  

 _Fixed Amount of $ / trade_

Set _MoneyManagement = UseFixedAmount_ and fill in the amount of under _FixedAmount_.

Note that this is your account currency. So if your account is in EUR then FixedAmount is also in EUR

Each trade opened by the EA will use a fixed amount of money.

When the SL is bigger it must use a smaller lotsize and when the SL is smaller it can use a higher lotsize.

So it will always risk the same amount of money on each and every trade

  

 _Percentage of Account Balance / trade_

Set _MoneyManagement = UsePercentageOfAccountBalance_ and fill in the percentage (1-100) under _RiskPercentage_.

Each trade opened by the EA will risk a fixed % of your total balance

So if you have a $1000 account and Riskpercentage = 5 it will risk 5% of $1000 = $50,- / trade

  
**Exit Strategies**  
Here you can choose between a trailing stop or a fixed Risk/Reward ratio  

_Trailing stop:_

Set _trailingmethod=UseTrailingStops_ and fill in the _OrderHiddenSL, OrderTSx , OrderTSxTrigger_ levels

It uses a hidden / virtual stoploss.

This allows us to put the stop loss anywhere without the broker knowing and without any broker restrictions

So.. When the EA places a new order then the initial hidden/virtual stoploss is placed at the S&R level

then when trade gets into profit we trail the hidden / virtual stoploss like this:

when profit reaches Order TS1 Trigger pips, the virtual stoploss is moved to Order TS1 pips

when profit reaches Order TS2 Trigger pips, the virtual stoploss is moved to Order TS2 pips

when profit reaches Order TS3 Trigger pips, the virtual stoploss is moved to Order TS3 pips

when profit reaches Order TS4 Trigger pips, the virtual stoploss is moved to Order TS4 pips

when profit goes above Order TS4 Trigger pips then the rest gets trailed with a Trailing Step

  

 _Risk/Reward ratio_

Set _trailing method = UseRiskRewardRations_ and set _TakeProfit_ to your R:R

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screen Shot 2018-01-27 at 10.25.20.png
Size: 115 KB](/attachment/image/2650769/thumbnail?d=1517045300)](/attachment/image/2650769?d=1517045300)   
[![Click to Enlarge

Name: Screen Shot 2018-01-27 at 10.07.10.png
Size: 115 KB](/attachment/image/2650771/thumbnail?d=1517045307)](/attachment/image/2650771?d=1517045307)   
[![Click to Enlarge

Name: Screen Shot 2018-01-27 at 10.07.24.png
Size: 109 KB](/attachment/image/2650773/thumbnail?d=1517045312)](/attachment/image/2650773?d=1517045312)   
[![Click to Enlarge

Name: pinbar.jpg
Size: 189 KB](/attachment/image/2650776/thumbnail?d=1517045320)](/attachment/image/2650776?d=1517045320)   
[![Click to Enlarge

Name: backtest.jpg
Size: 265 KB](/attachment/image/2650939/thumbnail?d=1517057928)](/attachment/image/2650939?d=1517057928)   

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [pinbar trader ea v1.20.zip](/attachment/file/2651560?d=1517157585) 243 KB | 9,022 downloads | Uploaded Jan 29, 2018 1:39am 

  * [#2](/thread/post/10714459#post10714459 "Post Permalink")

  * Jan 27, 2018 9:25pm  Jan 27, 2018 9:25pm 

  * [ Sladen23](sladen23)

  * | Joined Nov 2014  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=390913)

ebeckers,  
thanks for sharing your idea as usual.Where do i find and 

  1. copy the SupportResistance.ex4 to your MT4 indicators folder
  2. copy the PinbarTrader.ex4 to your MT4 experts folder

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#3](/thread/post/10714493#post10714493 "Post Permalink")

  * Jan 27, 2018 9:52pm  Jan 27, 2018 9:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar526867_15.gif) AndrewBa-](andrewba-)

  * | Commercial User  | Joined Nov 2016 | [422 Posts](/search?do=process&provider=Member&searchuser=526867)

Seems very promising! Subscribed. 

Check page 1 for all infos...

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#4](/thread/post/10714499#post10714499 "Post Permalink")

  * Jan 27, 2018 9:55pm  Jan 27, 2018 9:55pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

subscribed. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#5](/thread/post/10714506#post10714506 "Post Permalink")

  * Jan 27, 2018 9:58pm  Jan 27, 2018 9:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting ebeckers](/thread/post/10714321#post10714321 "View Quoted Post")
> 
> Disliked
> 
> === Pinbar Trader EA === Hi everyone, welcome ! I would like to present my latest EA. It implements a very basic, but very effective strategy. trading pinbars from weekly S&R levels Strategy: - we wait for a pinbar to appear which rejects a weekly support & resistance level - When the candle with the pinbar is closed we open a new buy/sell trade on the next candle The Pinbar trader EA The pinbar trader EA implements the strategy and has lots of extra features: it scans multiple currencies. So load the EA on 1 chart and it will scan all major currencies...
> 
> Ignored

  
Hi, Thanks for sharing your work here, i have similar liking of this candle pattern based trading method. I have done a my share of research on it as well. Using the weekly support and resistance is a good way to filter these signals indeed. For others they also utilise Pivots, Some use Fibs and others use Value charts. Keeping it simple is great and i will surely be testing your hard work. I look forward to further development if it is required. I also look to assist where i can.   
  
I like your trade dashboard and trade info panel. I will also be looking for those two trades that the system has alerted and traded.   
My only question is the method of entry:

  1. Is it an aggressive entry, which means you enter as soon as the bar closes? **Market order.**
  2. Do you wait for retrace? **Limit order**
  3. Break of the nose of the pinbar? **Stop order**

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#6](/thread/post/10714509#post10714509 "Post Permalink")

  * Jan 27, 2018 9:59pm  Jan 27, 2018 9:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar527771_3.gif) jenbols](jenbols)

  * Joined Nov 2016 | Status: Getting there, but not just yet | [2,430 Posts](/search?do=process&provider=Member&searchuser=527771)

> [Quoting ebeckers](/thread/post/10714321#post10714321 "View Quoted Post")
> 
> Disliked
> 
> === Pinbar Trader EA === H _i everyone, welcome ! I would like to present my latest EA. It implements a very basic, but very effective strategy. trading pinbars from weekly S &R levels Strategy: - we wait for a pinb_ar {image} {image} {image} {image} {image} {file}
> 
> Ignored

Hi Ebeckers, many thanx to offer this for the FF community, looks like a simple system and effective for price action ,,  
Pls could you clarify some points ?  
-**I use normally 1000** bar history and default Ea is 3000 bars, is it okay to keep it still at 1000  
or it will make conflict somehow with the Ea ?  
-**Also some of the Pinbars** patterns might not display the same way , and i think it is best to use the New York close  
i find almost identical patterns with brokers using +2 gmt, is that what you have used too ?  
\- **For now this works on Daily chart** only and perhaps do you have any plan to make this work on **H4** too?  
There are quite a few reliable PinBars on that type of TF too  
-**Also is it possible temporarily hyde** the box showing data on the chart ?  
-**The Entry** is it straight away after PIn Bar forms or does the Ea looks at the next candle for reference ?  
I have switched to price action and normally i am entering long tailed pin bars or med sized ones from half 50% of it _  
If you could confirm ...  
Thank you and best of luck _ 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: pin bar .jpg
Size: 328 KB](/attachment/image/2650934/thumbnail?d=1517057797)](/attachment/image/2650934?d=1517057797)   

The arriving better than the arrival, the journey has just started

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#7](/thread/post/10714510#post10714510 "Post Permalink")

  * Jan 27, 2018 10:00pm  Jan 27, 2018 10:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting PrinceJ58](/thread/post/10714506#post10714506 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, Thanks for sharing your work here, i have similar liking of this candle pattern based trading method. I have done a my share of research on it as well. Using the weekly support and resistance is a good way to filter these signals indeed. For others they also utilise Pivots, Some use Fibs and others use Value charts. Keeping it simple is great and i will surely be testing your hard work. I look forward to further development if it is required. I also look to assist where i can. I like your trade dashboard and trade info panel. I will...
> 
> Ignored

Thx.. yeah at the moment the EA simply opens a trader right after the pinbar candle closes.  
I'll be playing with 50% retracements next week to see if this makes things even better ! 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#8](/thread/post/10714517#post10714517 "Post Permalink")

  * Jan 27, 2018 10:03pm  Jan 27, 2018 10:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting jenbols](/thread/post/10714509#post10714509 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ebeckers, many thanx to offer this for the FF community, looks like a simple system and effective for price action ,, Pls could you clarify some points ? -I use normally 1000 bar history and default Ea is 3000 bars, is it okay to keep it still at 1000 or it will make conflict somehow with the Ea ? -Also some of the Pinbars patterns might not display the same way , and i think it is best to use the New York close i find almost identical patterns with brokers using +2 gmt, is that what you have used too ? - For now this works on Daily chart...
> 
> Ignored

> I use normally **1000** bar history and default Ea is 3000 bars, is it okay to keep it still at 1000  
Fine with me ;-) When there is less then 3000 bars the EA will simply use less bars  
So 3000 is the max it will use, if there are only 1000. it will use 1000  
  
>Also some of the Pinbars patterns might not display the same way , and i think it is best to use the New York close  
I agree, NY close brokers are the best, but it depends on which broker you use  
  
> i find almost identical patterns with brokers using +2 gmt, is that what you have used too ?  
I do al my trading on a broker which has NY closing charts. Dunno about other brokers  
  
> For now this works on Daily chart only and perhaps do you have any plan to make this work on ha4 too?  
Yes  
  
> Also is it possible temporarily hide the box showing data on the chart ?  
No, it appears when you have auto trading enabled.  
But the source code is open to all, so you could change it ;-)  
  
Erwin 

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#9](/thread/post/10714530#post10714530 "Post Permalink")

  * Jan 27, 2018 10:10pm  Jan 27, 2018 10:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar527771_3.gif) jenbols](jenbols)

  * Joined Nov 2016 | Status: Getting there, but not just yet | [2,430 Posts](/search?do=process&provider=Member&searchuser=527771)

> [Quoting ebeckers](/thread/post/10714517#post10714517 "View Quoted Post")
> 
> Disliked
> 
> {quote} > I use normally 1000 bar history and default Ea is 3000 bars, is it okay to keep it still at 1000 Fine with me ;-) >Also some of the Pinbars patterns might not display the same way , and i think it is best to use the New York close I agree, NY close brokers are the best, but it depends on which broker you use > i find almost identical patterns with brokers using +2 gmt, is that what you have used too ? I do al my trading on a broker which has NY closing charts. Dunno about other brokers > For now this works on Daily chart only and perhaps...
> 
> Ignored

Aww, Lol you faster than me ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Okay thanx for the answers, not sure if i have seen this before  
but i like what i see now and it is promising_  
What i am careful of when playing Pin bars is to play them only of course when there is a clear trend  
visible on a Daily Chart to avoid some fake signal.  
The addition of the Risk Reward Ratio is a good feature Btw,,,  
So we wait for Monday then _ Nice work man ! 

The arriving better than the arrival, the journey has just started

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#10](/thread/post/10714533#post10714533 "Post Permalink")

  * Jan 27, 2018 10:14pm  Jan 27, 2018 10:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting ebeckers](/thread/post/10714517#post10714517 "View Quoted Post")
> 
> Disliked
> 
> {quote} > I use normally 1000 bar history and default Ea is 3000 bars, is it okay to keep it still at 1000 Fine with me ;-) When there is less then 3000 bars the EA will simply use less bars So 3000 is the max it will use, if there are only 1000. it will use 1000 >Also some of the Pinbars patterns might not display the same way , and i think it is best to use the New York close I agree, NY close brokers are the best, but it depends on which broker you use > i find almost identical patterns with brokers using +2 gmt, is that what you have used too...
> 
> Ignored

  
Yes i agree even the colours sometimes are opposite versus the direction the signals are indicating. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: pin-bars-in-trend.png
Size: 27 KB](/attachment/image/2650954/thumbnail?d=1517058852)](/attachment/image/2650954?d=1517058852)   

Attached Images

![](/attachment/image/2650947?d=1517058748) ![](/attachment/image/2650949?d=1517058757) ![](/attachment/image/2650952?d=1517058774)

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#11](/thread/post/10714538#post10714538 "Post Permalink")

  * Jan 27, 2018 10:19pm  Jan 27, 2018 10:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546078_1.gif) johnsmith2nd](johnsmith2nd)

  * Joined Jan 2017 | Status: Trader | [530 Posts](/search?do=process&provider=Member&searchuser=546078)

Looks interesting! Subbed and keen to follow! 

[1 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#12](/thread/post/10714581#post10714581 "Post Permalink")

  * Jan 27, 2018 10:59pm  Jan 27, 2018 10:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar545840_1.gif) Joseph95](joseph95)

  * | Joined Jan 2017  | Status: Trader | [379 Posts](/search?do=process&provider=Member&searchuser=545840)

This is the kind of stuff i was searching for a lot of time for improve my trading and making it stress-less. Thank you and subscribed :-) 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#13](/thread/post/10714617#post10714617 "Post Permalink")

  * Jan 27, 2018 11:26pm  Jan 27, 2018 11:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar447385_1.gif) HumbleLearne](humblelearne)

  * | Joined Feb 2016  | Status: Trader | [318 Posts](/search?do=process&provider=Member&searchuser=447385)

Amazing stuff guru ![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f60e.png?v=15.1) Subscribed ![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#14](/thread/post/10714619#post10714619 "Post Permalink")

  * Jan 27, 2018 11:28pm  Jan 27, 2018 11:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar581555_2.gif) mrdfx](mrdfx)

  * Joined May 2017 | Status: Trader | [3,804 Posts](/search?do=process&provider=Member&searchuser=581555)

Nice one ebeckers, this looks good! I'm in! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Truth is like poetry. And most people f*cking hate poetry.

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#15](/thread/post/10714696#post10714696 "Post Permalink")

  * Jan 28, 2018 12:06am  Jan 28, 2018 12:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar608462_3.gif) T4Trade](t4trade)

  * Joined Sep 2017 | Status: Trend Following,Price Action,Grid | [2,484 Posts](/search?do=process&provider=Member&searchuser=608462)

Thank you for creating this thread,Subscribed and All the best! 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#16](/thread/post/10714698#post10714698 "Post Permalink")

  * Jan 28, 2018 12:14am  Jan 28, 2018 12:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar435730_2.gif) renkotop](renkotop)

  * Joined Nov 2015 | Status: Trader | [923 Posts](/search?do=process&provider=Member&searchuser=435730)

@ebeckers:thank you for this ea, subscribed, renkotop 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#17](/thread/post/10714783#post10714783 "Post Permalink")

  * Jan 28, 2018 1:44am  Jan 28, 2018 1:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar239126_2.gif) dennisd](dennisd)

  * | Joined Mar 2012  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=239126)

Ebeckers I'm subscribed. Your coding skills and generosity is truely amazing!  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#18](/thread/post/10714814#post10714814 "Post Permalink")

  * Jan 28, 2018 2:33am  Jan 28, 2018 2:33am 

  * [ billbss](billbss)

  * Joined Apr 2006 | Status: Trader | [4,301 Posts](/search?do=process&provider=Member&searchuser=9243)

I didn't see the template in your zip file.  
Thanks 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#19](/thread/post/10714823#post10714823 "Post Permalink")

  * Jan 28, 2018 2:54am  Jan 28, 2018 2:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting ebeckers](/thread/post/10714321#post10714321 "View Quoted Post")
> 
> Disliked
> 
> === Pinbar Trader EA === Hi everyone, welcome ! I would like to present my latest EA. It implements a very basic, but very effective strategy. trading pinbars from weekly S&R levels Strategy: - we wait for a pinbar to appear which rejects a weekly support & resistance level - When the candle with the pinbar is closed we open a new buy/sell trade on the next candle The Pinbar trader EA The pinbar trader EA implements the strategy and has lots of extra features: it scans multiple currencies. So load the EA on 1 chart and it will scan all major currencies...
> 
> Ignored

Great thread. Pin Bar is such a great candlestick, especially when formed in ranging market. Almost similar to Hammer. They fly the pair to a great height. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#20](/thread/post/10714829#post10714829 "Post Permalink")

  * Jan 28, 2018 2:56am  Jan 28, 2018 2:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar357421_1.gif) bazze](bazze)

  * | Joined Dec 2013  | Status: Trader | [1,135 Posts](/search?do=process&provider=Member&searchuser=357421)

Thank you for sharing, ebeckers![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)...Up and ready for next week![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#21](/thread/post/10714838#post10714838 "Post Permalink")

  * Jan 28, 2018 3:01am  Jan 28, 2018 3:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting jenbols](/thread/post/10714509#post10714509 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ebeckers, many thanx to offer this for the FF community, looks like a simple system and effective for price action ,, Pls could you clarify some points ? -I use normally 1000 bar history and default Ea is 3000 bars, is it okay to keep it still at 1000 or it will make conflict somehow with the Ea ? -Also some of the Pinbars patterns might not display the same way , and i think it is best to use the New York close i find almost identical patterns with brokers using +2 gmt, is that what you have used too ? - For now this works on Daily chart...
> 
> Ignored

I believe this chart was __**USDJPY**__ Pin Bar formed recently, 25th January. __**Such Pin Bar or hammer**__ may be ignored because it formed right at the bottom of bearish market. It would not work. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#22](/thread/post/10714889#post10714889 "Post Permalink")

  * Jan 28, 2018 4:05am  Jan 28, 2018 4:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar446899_1.gif) TroyDiane](troydiane)

  * | Joined Feb 2016  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=446899)

Hi,  
Just passing through,   
I thought this would be of concern in the NU daily. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: NZDUSDDaily.png
Size: 55 KB](/attachment/image/2651074/thumbnail?d=1517079827)](/attachment/image/2651074?d=1517079827)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#23](/thread/post/10714891#post10714891 "Post Permalink")

  * Jan 28, 2018 4:06am  Jan 28, 2018 4:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar527771_3.gif) jenbols](jenbols)

  * Joined Nov 2016 | Status: Getting there, but not just yet | [2,430 Posts](/search?do=process&provider=Member&searchuser=527771)

> [Quoting 9jatrader](/thread/post/10714838#post10714838 "View Quoted Post")
> 
> Disliked
> 
> {quote} I believe this chart was USDJPY Pin Bar formed recently, 25th January. Such Pin Bar or hammer may be ignored because it formed right at the bottom of bearish market. It would not work.
> 
> Ignored

Smart eye, I see what you mean ,, but the photo was more for illustration purposes , wasn't UJ, i must have moved it to see things around_  
i had it on **NU and EU** as the Ea showed those two pairs on photo, so i thought i would see what type of pin bars they are  
,,,in other words if i had seen them on chart how would i trade them and what the Ea would do _  
And of course before considering it as a **potential reversal candlestick** i look at 4/5 things  
-The Trend  
-The **context** of where it forms on a price chart,  
-The **Intersecting** points etc ...  
-How many points of **Rejections**  
-Figuring out if the "**Smart Money** " is attempting fake break outs by taking out all the newbies stops and money  
  
Lol you made go back and open my mt4 to look at UJ ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: bars charts pin bars .jpg
Size: 275 KB](/attachment/image/2651085/thumbnail?d=1517079976)](/attachment/image/2651085?d=1517079976)   

The arriving better than the arrival, the journey has just started

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#24](/thread/post/10714928#post10714928 "Post Permalink")

  * Jan 28, 2018 4:50am  Jan 28, 2018 4:50am 

  * [ RoyPK](roypk)

  * | Joined Apr 2010  | Status: Trader | [176 Posts](/search?do=process&provider=Member&searchuser=140755)

Hi ebeckers,  
  
Thanks for starting this thread and sharing us the Price Action EA. I admire your crystal clear style of explanation, great.  
I am in.  
  
Have a nice weekend.  
  
Roy 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#25](/thread/post/10715041#post10715041 "Post Permalink")

  * Jan 28, 2018 6:26am  Jan 28, 2018 6:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting ebeckers](/thread/post/10714321#post10714321 "View Quoted Post")
> 
> Disliked
> 
> === Pinbar Trader EA === Hi everyone, welcome ! I would like to present my latest EA. It implements a very basic, but very effective strategy. trading pinbars from weekly S&R levels Strategy: - we wait for a pinbar to appear which rejects a weekly support & resistance level - When the candle with the pinbar is closed we open a new buy/sell trade on the next candle The Pinbar trader EA The pinbar trader EA implements the strategy and has lots of extra features: it scans multiple currencies. So load the EA on 1 chart and it will scan all major currencies...
> 
> Ignored

  
  
_**The aspect i want to talk about where pinbars are concerned is for further development as was mentioned above.** _  
If one understands this price action, it is one price action method that is really good once done correctly. This system allows any new trader and experienced trader to have a simple system that is very effective. The next thing is that the risk can always be at the same location, as-well as the targets (R/R ratio, pips, previous S/R areas etc) which makes it systematic. The simplicity makes it easy to learn, however it is the proper identification of the best points to enter that separates the type of traders.   
  
Good things about it, It does not come very often in the daily timeframe unless observing many types of markets not just FX, but Commodities as well and other tradable markets.   
_**Now for the entry versus stop-loss:**_  
The different entries have different Stop-loss ratios-  
  
**Stop order** entry and **market order** entry has a larger stop loss risk to that of the **limit order** entry- (50% retrace). These three entry types can be found sometimes on the same Signal but not always. It all depends on what the market is doing that determines the entries available:  
Sometimes the market does not retraces at all and only gives the opportunity for 2 types of entries and that's either the **market entry or stop order entry. Personally the best entry in my opinion is the limit order** whenever it is possible to take. The plus is that when you are right- the reward can be endless,  
for example of a signal and size of the signal bar in terms of pips. A long standing position. Eg. Gold/Xauusd on **december 12, 2017** _Bullish Signal_. Gold trade Still running up to now 1202 pips strong.  
  
**When i am trading pin bars (Trapped Traders) i look for 2 entries, i look for the stop-order and limit order entry. I will expound on the stop-loss differences that i like about the two order types:**  
Let's say the candle in golds case (**Bullish signal** 12/12/17) is **100 pips** from tail to nose tip:  
Buy **Stop order** entry would be at the break of the nose and **100** pips stop-loss at the tail  
Buy **Limit order** would be 50% of the candlestick and the stop-loss would be**50** pips for the same signal.   
  
I think in this case there was an entry for the Limit order entry, Should price continue to break below the signal bar one would be stopped out at 50 pips rather than 100 pips. _Otherwise one can employ a backup plan for trades that don't work out. Like an opposing pending order some pips away from the stop-loss area just in case.-Any thoughts?_

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: pinbar2.png
Size: 16 KB](/attachment/image/2651162/thumbnail?d=1517087496)](/attachment/image/2651162?d=1517087496)   
[![Click to Enlarge

Name: 30ndksp.png
Size: 9 KB](/attachment/image/2651164/thumbnail?d=1517087504)](/attachment/image/2651164?d=1517087504)   

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#26](/thread/post/10715046#post10715046 "Post Permalink")

  * Jan 28, 2018 6:33am  Jan 28, 2018 6:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting RoyPK](/thread/post/10714928#post10714928 "View Quoted Post")
> 
> Disliked
> 
> Hi ebeckers, Thanks for starting this thread and sharing us the Price Action EA. I admire your crystal clear style of explanation, great. I am in. Have a nice weekend. Roy
> 
> Ignored

Pls note we're looking at the weekly S&R levels and not the daily S&R levels  
Daily S&R levels are more pointing to recent swing hi/lo's and not points where the market reversed.  
If you for example look at the EURNZD on the W1 timeframe, you will see that market reversed couple of times in the past. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: sr.jpg
Size: 167 KB](/attachment/image/2651197/thumbnail?d=1517088719)](/attachment/image/2651197?d=1517088719)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#27](/thread/post/10715054#post10715054 "Post Permalink")

  * Edited 6:52am  Jan 28, 2018 6:41am | Edited 6:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting PrinceJ58](/thread/post/10715041#post10715041 "View Quoted Post")
> 
> Disliked
> 
> {quote} The aspect i want to talk about where pinbars are concerned ...
> 
> Ignored

Thx for your detailed explanation. It's a bit late now where i live, but i'll study it in more detail tomorrow!  
but know that 50% retracement entries is already on my todo list for the next version ;-) 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#28](/thread/post/10715065#post10715065 "Post Permalink")

  * Edited 7:22am  Jan 28, 2018 6:51am | Edited 7:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting ebeckers](/thread/post/10715054#post10715054 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thx for your detailed explanation. It's a bit late now where i live, but i'll study it in more detail tomorrow! but know that 50% retrachement entries is already on my todo list for the next version ;-)
> 
> Ignored

Yes no problem... Sleep well...There is a lot to discuss on this topic my friend...Later.  
  
For the Gold Example posted below. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Gold Example.png
Size: 83 KB](/attachment/image/2651223/thumbnail?d=1517091454)](/attachment/image/2651223?d=1517091454)   
[![Click to Enlarge

Name: Gold Results.png
Size: 66 KB](/attachment/image/2651225/thumbnail?d=1517091713)](/attachment/image/2651225?d=1517091713)   

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#29](/thread/post/10715381#post10715381 "Post Permalink")

  * Edited 6:54pm  Jan 28, 2018 6:15pm | Edited 6:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar477099_2.gif) knullasomfan](knullasomfan)

  * | Joined Jul 2016  | Status: Trader | [59 Posts](/search?do=process&provider=Member&searchuser=477099)

very well done, thanks for sharing. It is really worth to invest time on it. You can count on me for whatever test you need. Any chance to add a traditional TP and trailing without TS1 etc? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#30](/thread/post/10715385#post10715385 "Post Permalink")

  * Jan 28, 2018 6:21pm  Jan 28, 2018 6:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546078_1.gif) johnsmith2nd](johnsmith2nd)

  * Joined Jan 2017 | Status: Trader | [530 Posts](/search?do=process&provider=Member&searchuser=546078)

Question - How long is signal valid before it is null and void?  
  
I've got a sell signal for NZDUSD. the pinbar was generated on the 24th, there's been two days trading since, final day had a small retracement. looks like it's testing the weekly resistance level, question is, will market sentiment see the signal and trigger a downtrend or not.. That is the question.   
  
Does anyone have experience in how long a pin-bar is generally valid for? An option would be to enter a sell limit order.. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 6 KB](/attachment/image/2651345/thumbnail?d=1517131287)](/attachment/image/2651345?d=1517131287)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#31](/thread/post/10715534#post10715534 "Post Permalink")

  * Jan 28, 2018 8:36pm  Jan 28, 2018 8:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting johnsmith2nd](/thread/post/10715385#post10715385 "View Quoted Post")
> 
> Disliked
> 
> Question - How long is signal valid before it is null and void? I've got a sell signal for NZDUSD. the pinbar was generated on the 24th, there's been two days trading since, final day had a small retracement. looks like it's testing the weekly resistance level, question is, will market sentiment see the signal and trigger a downtrend or not.. That is the question. Does anyone have experience in how long a pin-bar is generally valid for? An option would be to enter a sell limit order.. {image}
> 
> Ignored

__**NZDUSD**__ Pin Bar formed right at the top of bulls. It may not work because the trend is too strong. Just my take. It works best when market ranges or after consolidation 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#32](/thread/post/10715574#post10715574 "Post Permalink")

  * Edited 9:15pm  Jan 28, 2018 9:04pm | Edited 9:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting 9jatrader](/thread/post/10715534#post10715534 "View Quoted Post")
> 
> Disliked
> 
> {quote} NZDUSD Pin Bar formed right at the top of bulls. It may not work because the trend is too strong. Just my take. It works best when market ranges or after consolidation
> 
> Ignored

Nothing is certain in forex, we can only judge setups by probability.  
That said... i think we have a situation here where changes are high that the bull trend might come to an end.  
  
1) We have a really strong weekly level here which goes back all the way to march 2004  
2) We have a big pinbar at the daily D1 timeframe  
3) We even see a (smaller) pinbar on the weekly W1 timeframe  
4) We can see that the uptrend has been slowing down the last week/days  
5) We can see that the market respected the resistance level on the 24th-26th jan  
6) We have a huge gap between price and the mean on the Weekly W1 timeframe, meaning pressure is building up higher and higher and the urge for a mean reversal is getting strong  
7) The risk/reward ratio is (potentially) really good and allows for an easy 3:1 and maybe 4:1  
  
All in all good enough for me to take this trade.  
Off course market can always go against us, so make sure to always use good money management and risk / reward ratios ! 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screen Shot 2018-01-28 at 13.09.56.png
Size: 149 KB](/attachment/image/2651430/thumbnail?d=1517141410)](/attachment/image/2651430?d=1517141410)   
[![Click to Enlarge

Name: Screen Shot 2018-01-28 at 13.11.54.png
Size: 55 KB](/attachment/image/2651433/thumbnail?d=1517141734)](/attachment/image/2651433?d=1517141734)   

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#33](/thread/post/10715584#post10715584 "Post Permalink")

  * Jan 28, 2018 9:09pm  Jan 28, 2018 9:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting johnsmith2nd](/thread/post/10715385#post10715385 "View Quoted Post")
> 
> Disliked
> 
> Question - How long is signal valid before it is null and void? I've got a sell signal for NZDUSD. the pinbar was generated on the 24th, there's been two days trading since, final day had a small retracement. looks like it's testing the weekly resistance level, question is, will market sentiment see the signal and trigger a downtrend or not.. That is the question. Does anyone have experience in how long a pin-bar is generally valid for? An option would be to enter a sell limit order.. {image}
> 
> Ignored

**Pin Bar, Hammer, Shooting Star, Gravestone Doji Bearish/Bullish Engulfing** have same validity period. Watch out for reversal especially around clear and visible S/R 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#34](/thread/post/10715594#post10715594 "Post Permalink")

  * Jan 28, 2018 9:15pm  Jan 28, 2018 9:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting ebeckers](/thread/post/10715574#post10715574 "View Quoted Post")
> 
> Disliked
> 
> {quote} Nothing is certain in forex, we can only judge setups by probability. That said... i think we have a situation here where changes are high that the bull trend might come to an end. 1) We have a really strong weekly level here which goes back all the way to march 2004 2) We have a big pinbar at the daily D1 timeframe 3) We even see a (smaller) pinbar on the weekly W1 timeframe 4) We can see that the uptrend has been slowing down the last week/days 5) We can see that the market respected the resistance level on the 24th-26th jan 6) We have...
> 
> Ignored

You're correct. It's a game of probability. That's the reason I used the word "__**may not**__ ". I did not say "__**it will not**__ " 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#35](/thread/post/10715603#post10715603 "Post Permalink")

  * Jan 28, 2018 9:26pm  Jan 28, 2018 9:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

Hi Ebeckers and everyone here,  
Whatever post I share am not contradicting your points. Just sharing my take.   
Ebeckers, as you rightly said, is close to resistance level. I believe you use MA. Bollinger bands is also a MA. I have the chart here which shows the strength of the bulls- the movement are strongly along the upper band. we have to allow to consolidate before joining at this time. Just my take. Pick no offence please 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: nzdusd.png
Size: 50 KB](/attachment/image/2651438/thumbnail?d=1517142243)](/attachment/image/2651438?d=1517142243)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#36](/thread/post/10715604#post10715604 "Post Permalink")

  * Jan 28, 2018 9:28pm  Jan 28, 2018 9:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar128477_10.gif) Patso](patso)

  * | Joined Dec 2009  | Status: Trader | [221 Posts](/search?do=process&provider=Member&searchuser=128477)

Thank you for sharing. Subscribed. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#37](/thread/post/10715608#post10715608 "Post Permalink")

  * Jan 28, 2018 9:34pm  Jan 28, 2018 9:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting 9jatrader](/thread/post/10715603#post10715603 "View Quoted Post")
> 
> Disliked
> 
> Hi Ebeckers and everyone here, Whatever post I share am not contradicting your points. Just sharing my take. Ebeckers, as you rightly said, is close to resistance level. I believe you use MA. Bollinger bands is also a MA. I have the chart here which shows the strength of the bulls- the movement are strongly along the upper band. we have to allow to consolidate before joining at this time. Just my take. Pick no offence please {image}
> 
> Ignored

No worries mate, I didn't feel offended, sorry if you thought that ;-)  
Actually I love to hear how you guys & girls are thinking about possible setups.  
Sadly I don't have any crystal ball, so i'm just sharing how i see the market.  
But i'm always interested in other opinions so pls keep on sharing your idea's and lets all be open and learn from each other ! 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#38](/thread/post/10715622#post10715622 "Post Permalink")

  * Jan 28, 2018 9:45pm  Jan 28, 2018 9:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting ebeckers](/thread/post/10715608#post10715608 "View Quoted Post")
> 
> Disliked
> 
> {quote} No worries mate, I didn't feel offended, sorry if you thought that ;-) Actually I love to hear how you guys & girls are thinking about possible setups. Sadly I don't have any crystal ball, so i'm just sharing how i see the market. But i'm always interested in other opinions so pls keep on sharing your idea's and lets all be open and learn from each other !
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#39](/thread/post/10715811#post10715811 "Post Permalink")

  * Jan 29, 2018 12:09am  Jan 29, 2018 12:09am 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 51 KB](/attachment/image/2651493/thumbnail?d=1517152181)](/attachment/image/2651493?d=1517152181)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#40](/thread/post/10715880#post10715880 "Post Permalink")

  * Jan 29, 2018 1:05am  Jan 29, 2018 1:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546131_3.gif) pamc](pamc)

  * Joined Jan 2017 | Status: Trader | [1,305 Posts](/search?do=process&provider=Member&searchuser=546131)

> [Quoting ebeckers](/thread/post/10715608#post10715608 "View Quoted Post")
> 
> Disliked
> 
> {quote} No worries mate, I didn't feel offended, sorry if you thought that ;-) Actually I love to hear how you guys & girls are thinking about possible setups. Sadly I don't have any crystal ball, so i'm just sharing how i see the market. But i'm always interested in other opinions so pls keep on sharing your idea's and lets all be open and learn from each other !
> 
> Ignored

Hi Ebeckers. Here is a very good PinBar strategy PDF by Justin Bennett which i use more or less alone. If you can go through it, I am sure you will be able to make your EA alot more accurate, safer and profitable with lower cost losers.   
[https://dailypriceaction.com/pin-bar...e893067a1a7480](https://dailypriceaction.com/pin-bar-trading-course?inf_contact_key=884ef42f23d7fe3bded958ec1249d3b1aa73b64a9a0c08aa76e893067a1a7480)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#41](/thread/post/10715903#post10715903 "Post Permalink")

  * Edited 5:24am  Jan 29, 2018 1:18am | Edited 5:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting pamc](/thread/post/10715880#post10715880 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ebeckers. Here is a very good PinBar strategy PDF by Justin Bennett which i use more or less alone. If you can go through it, I am sure you will be able to make your EA alot more accurate, safer and profitable with lower cost losers. [https://dailypriceaction.com/pin-bar...e893067a1a7480](https://dailypriceaction.com/pin-bar-trading-course?inf_contact_key=884ef42f23d7fe3bded958ec1249d3b1aa73b64a9a0c08aa76e893067a1a7480)
> 
> Ignored

Thx , but I'm already a lifetime member of DPA for some time there ;-) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#42](/thread/post/10715957#post10715957 "Post Permalink")

  * Edited 2:12am  Jan 29, 2018 1:47am | Edited 2:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

**=== Pinbar Trader EA v 1.20 available ===**

  
_**See the 1st post for a new version of the EA**_  
  
Whats new:  
\- 50% retracement entries  
  
The EA can now open trades on 50% retracements of the pinbar.  
When enabled this will give you a much better risk/reward ratio since the stoploss needed is much smaller.  
But there's also a downside. Not every pinbar will give you a 50% retracement, so you might miss some trades. Can't win them all ;-)  
  
You can enable this feature on by setting _Use50PercentRetracementEntry_ to true or false  
When enabled a new column will be shown called 50%rt as shown in this screenshot.. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screen Shot 2018-01-28 at 17.46.15.png
Size: 40 KB](/attachment/image/2651567/thumbnail?d=1517157991)](/attachment/image/2651567?d=1517157991)   

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [pinbar trader ea v1.20.zip](/attachment/file/2651569?d=1517158099) 243 KB | 1,859 downloads 

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#43](/thread/post/10716094#post10716094 "Post Permalink")

  * Edited 3:14am  Jan 29, 2018 2:56am | Edited 3:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting ebeckers](/thread/post/10715957#post10715957 "View Quoted Post")
> 
> Disliked
> 
> === Pinbar Trader EA v 1.20 available === See the 1st post for a new version of the EA Whats new: - 50% retracement entries The EA can now open trades on 50% retracements of the pinbar. When enabled this will give you a much better risk/reward ratio since the stoploss needed is much smaller. But there's also a downside. Not every pinbar will give you a 50% retracement, so you might miss some trades. Can't win them all ;-) You can enable this feature on by setting Use50PercentRetracementEntry to true or false When enabled a new column will be shown...
> 
> Ignored

Excellent,  
Even better if both the Stop order and the limit order can be activated at once on the close of the signal bar.  
  
The stop order would be first priority if one needs to close a trade or cut half of it, while the 50% entry could run as long as the pair is trending in that direction as a free trade at breakeven or above the nose of the signal bar. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#44](/thread/post/10716117#post10716117 "Post Permalink")

  * Jan 29, 2018 3:14am  Jan 29, 2018 3:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546078_1.gif) johnsmith2nd](johnsmith2nd)

  * Joined Jan 2017 | Status: Trader | [530 Posts](/search?do=process&provider=Member&searchuser=546078)

> [Quoting ebeckers](/thread/post/10715957#post10715957 "View Quoted Post")
> 
> Disliked
> 
> === Pinbar Trader EA v 1.20 available === See the 1st post for a new version of the EA Whats new: - 50% retracement entries The EA can now open trades on 50% retracements of the pinbar. When enabled this will give you a much better risk/reward ratio since the stoploss needed is much smaller. But there's also a downside. Not every pinbar will give you a 50% retracement, so you might miss some trades. Can't win them all ;-) You can enable this feature on by setting Use50PercentRetracementEntry to true or false When enabled a new column will be shown...
> 
> Ignored

Great!   
  
Q. If using R:R do we keep the 'stoplossatzigzag' arrow to true? Despite not having zigzag arrow installed? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#45](/thread/post/10716126#post10716126 "Post Permalink")

  * Jan 29, 2018 3:18am  Jan 29, 2018 3:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting johnsmith2nd](/thread/post/10716117#post10716117 "View Quoted Post")
> 
> Disliked
> 
> {quote} Great! Q. If using R:R do we keep the 'stoplossatzigzag' arrow to true? Despite not having zigzag arrow installed?
> 
> Ignored

stoplossatzigzag is not used in this EA. I'll remove the setting in the next version 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#46](/thread/post/10716173#post10716173 "Post Permalink")

  * Edited 6:18am  Jan 29, 2018 3:48am | Edited 6:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

Yes those are good courses and reads...No wonder your info is effortlessly high probability information. Use your cutting edge. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#47](/thread/post/10716217#post10716217 "Post Permalink")

  * Jan 29, 2018 4:37am  Jan 29, 2018 4:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar631867_1.gif) paolo7](paolo7)

  * | Joined Nov 2017  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=631867)

Thanks Ebeckers!  
  
Ready to follow your fantasy!  
  
Paolo 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#48](/thread/post/10716256#post10716256 "Post Permalink")

  * Jan 29, 2018 5:01am  Jan 29, 2018 5:01am 

  * [ Forexholy](forexholy)

  * Joined Jul 2017 | Status: Trader | [2,403 Posts](/search?do=process&provider=Member&searchuser=591923)

ebeckers  
  
This is a very nice work you got going here I really like it. I Had a question, would it be very hard for you to add a few more reversal candles to your system? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#49](/thread/post/10716277#post10716277 "Post Permalink")

  * Jan 29, 2018 5:16am  Jan 29, 2018 5:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,577 Posts](/search?do=process&provider=Member&searchuser=185229)

> [Quoting pamc](/thread/post/10715880#post10715880 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ebeckers. Here is a very good PinBar strategy PDF by Justin Bennett which i use more or less alone. If you can go through it, I am sure you will be able to make your EA alot more accurate, safer and profitable with lower cost losers. [https://dailypriceaction.com/pin-bar...e893067a1a7480](https://dailypriceaction.com/pin-bar-trading-course?inf_contact_key=884ef42f23d7fe3bded958ec1249d3b1aa73b64a9a0c08aa76e893067a1a7480)
> 
> Ignored

All newbies, please note the rules, I suggest that you read them:  
  
<https://www.forexfactory.com/userguide.php>  
  
**VIII. No commercial agendas**  
  

  
Members who are focused on a product or service, or new members who mention a little-know website, are generally suspected to be company shills. Action may be taken against suspected shills without conclusive evidence, as they compromise the integrity of discussions and can be difficult to prove conclusively.  
  
Members who wish to promote a commercial product or service must be designated a 'Commercial Member' and are expected to abide by the Commercial Code of Conduct. 

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.7%

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#50](/thread/post/10716279#post10716279 "Post Permalink")

  * Jan 29, 2018 5:18am  Jan 29, 2018 5:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,577 Posts](/search?do=process&provider=Member&searchuser=185229)

> [Quoting ebeckers](/thread/post/10715903#post10715903 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thx , but I'm already a lifetime member of DPA for some time there ;-) In fact.. i'm a lifetime member on all of the following websites. I can recommend all of them if you want to learn more about price action trading - <http://theforexguy.com> \- <http://2ndskiesforex.com> \- <http://dailypriceaction.com> \- <http://www.learntotradethemarket.com>
> 
> Ignored

Is ForexFactory now allowing link to 3rd party commercial websites?  
  
Really, if so, I'm totally confused on the policy enforced previously  
  
![](https://resources.faireconomy.media/images/emojis/64/1f635.png?v=15.1)

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.7%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#51](/thread/post/10716287#post10716287 "Post Permalink")

  * Jan 29, 2018 5:26am  Jan 29, 2018 5:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting Erebus](/thread/post/10716279#post10716279 "View Quoted Post")
> 
> Disliked
> 
> {quote} Is ForexFactory now allowing link to 3rd party commercial websites? Really, if so, I'm totally confused on the policy enforced previously ![](https://resources.faireconomy.media/images/emojis/64/1f635.png?v=15.1)
> 
> Ignored

It was not my intention to promote any product or service. I just mentioned the courses i'm a member of  
Anyway.. i removed the links to those course from the post now  
Sadly they can still be found since you quoted me :-) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#52](/thread/post/10716292#post10716292 "Post Permalink")

  * Jan 29, 2018 5:36am  Jan 29, 2018 5:36am 

  * [ mallee](mallee)

  * Joined Jun 2013 | Status: Trader | [1,526 Posts](/search?do=process&provider=Member&searchuser=339383)

> [Quoting 9jatrader](/thread/post/10715534#post10715534 "View Quoted Post")
> 
> Disliked
> 
> {quote} NZDUSD Pin Bar formed right at the top of bulls. It may not work because the trend is too strong. Just my take. It works best when market ranges or after consolidation
> 
> Ignored

Unless you've picked a change in the trend. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#53](/thread/post/10716459#post10716459 "Post Permalink")

  * Jan 29, 2018 7:32am  Jan 29, 2018 7:32am 

  * [ Shnopse](shnopse)

  * | Joined Jan 2018  | Status: Trader | [15 Posts](/search?do=process&provider=Member&searchuser=645709)

hey man...thx for the ea great job so far,am trying to run it in my rdp vps for 24hours and i tried many brokers but it doesn't seem to open trades am sure i applied the right setting...ea works fine in my computer but on my rdp server doesn't seems to work ? any advise would be much appreciated 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#54](/thread/post/10716684#post10716684 "Post Permalink")

  * Jan 29, 2018 10:24am  Jan 29, 2018 10:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar605942_2.gif) hzs10](hzs10)

  * Joined Aug 2017 | Status: Trader | [526 Posts](/search?do=process&provider=Member&searchuser=605942)

can the EA use on any time frame? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#55](/thread/post/10716767#post10716767 "Post Permalink")

  * Edited 11:12am  Jan 29, 2018 11:00am | Edited 11:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting hzs10](/thread/post/10716684#post10716684 "View Quoted Post")
> 
> Disliked
> 
> can the EA use on any time frame?
> 
> Ignored

  1. put the EA on any chart on the **Daily (D1) timeframe !**

It's on the first post under "installation", all I did was copy and paste exact same notation. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#56](/thread/post/10716989#post10716989 "Post Permalink")

  * Jan 29, 2018 1:55pm  Jan 29, 2018 1:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting Shnopse](/thread/post/10716459#post10716459 "View Quoted Post")
> 
> Disliked
> 
> hey man...thx for the ea great job so far,am trying to run it in my rdp vps for 24hours and i tried many brokers but it doesn't seem to open trades am sure i applied the right setting...ea works fine in my computer but on my rdp server doesn't seems to work ? any advise would be much appreciated
> 
> Ignored

Pls look in the experts log for any errors  
Perhaps you didn't enable auto trading in MT4 or you didn't enable DLL imports ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#57](/thread/post/10717013#post10717013 "Post Permalink")

  * Jan 29, 2018 2:37pm  Jan 29, 2018 2:37pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Dear EBECKERS,  
  
Any best setup ? I tried so many times,.. not so good result,...  
  
Hope you can guide us with the best setting ,..  
  
Thanks,  
  
Paolo 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#58](/thread/post/10717069#post10717069 "Post Permalink")

  * Jan 29, 2018 3:19pm  Jan 29, 2018 3:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546078_1.gif) johnsmith2nd](johnsmith2nd)

  * Joined Jan 2017 | Status: Trader | [530 Posts](/search?do=process&provider=Member&searchuser=546078)

> [Quoting budidharma19](/thread/post/10717013#post10717013 "View Quoted Post")
> 
> Disliked
> 
> Dear EBECKERS, Any best setup ? I tried so many times,.. not so good result,... Hope you can guide us with the best setting ,.. Thanks, Paolo
> 
> Ignored

I am assuming you trying to forward test this? If so, you are a bit early!  
There's plenty of good results on backtest. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#59](/thread/post/10717077#post10717077 "Post Permalink")

  * Jan 29, 2018 3:21pm  Jan 29, 2018 3:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting johnsmith2nd](/thread/post/10717069#post10717069 "View Quoted Post")
> 
> Disliked
> 
> {quote} I am assuming you trying to forward test this? If so, you are a bit early! There's plenty of good results on backtest.
> 
> Ignored

I'm still playing around finding the best settings my self by doing forward & backward tests on multiple currencies  
When i have more results i'll post them here. For now i suggest to use this EA as an aid for manual trading or use it on a demo for automated trading 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#60](/thread/post/10717086#post10717086 "Post Permalink")

  * Jan 29, 2018 3:24pm  Jan 29, 2018 3:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar550345_1.gif) aimsttrader](aimsttrader)

  * | Membership Revoked  | Joined Jan 2017 | [330 Posts](/search?do=process&provider=Member&searchuser=550345)

gchf may be skyrocketting this week . im in 

CHECK MY TE !

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#61](/thread/post/10717336#post10717336 "Post Permalink")

  * Jan 29, 2018 5:20pm  Jan 29, 2018 5:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar301219_1.gif) earlroy63](earlroy63)

  * Joined Oct 2012 | Status: Trader | [605 Posts](/search?do=process&provider=Member&searchuser=301219)

new EA does not work, charts candlesticks dissappear when applied. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#62](/thread/post/10717346#post10717346 "Post Permalink")

  * Jan 29, 2018 5:23pm  Jan 29, 2018 5:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting earlroy63](/thread/post/10717336#post10717336 "View Quoted Post")
> 
> Disliked
> 
> new EA does not work, charts candlesticks dissappear when applied.
> 
> Ignored

Works perfectly.. The ea creates a black background since you are not interested on the candlesticks of the chart you put the EA on.  
We just need a blank chart for the EA so it can draw its figures onto it 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#63](/thread/post/10717398#post10717398 "Post Permalink")

  * Jan 29, 2018 5:41pm  Jan 29, 2018 5:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar301219_1.gif) earlroy63](earlroy63)

  * Joined Oct 2012 | Status: Trader | [605 Posts](/search?do=process&provider=Member&searchuser=301219)

OK Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#64](/thread/post/10717451#post10717451 "Post Permalink")

  * Jan 29, 2018 5:59pm  Jan 29, 2018 5:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546078_1.gif) johnsmith2nd](johnsmith2nd)

  * Joined Jan 2017 | Status: Trader | [530 Posts](/search?do=process&provider=Member&searchuser=546078)

@ebeckers forgive me for pestering you, but for the R:R system to work, it must work off a stop loss. Is this the orderhiddenSL? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#65](/thread/post/10717561#post10717561 "Post Permalink")

  * Jan 29, 2018 6:37pm  Jan 29, 2018 6:37pm 

  * [ RapzyFX](rapzyfx)

  * | Joined Sep 2010  | Status: Trader | [180 Posts](/search?do=process&provider=Member&searchuser=155512)

Hi ebeckers,  
Thanks for the pinbar ea and strat, I have installed all and the dashboard is presently showing a trade on EURNZD but I have noticed that it is not displaying all the pairs stated in the "Pairs To Trade" section.  
On my dashboard it is showing only EURNZD, CADJPY, EURGBP, GBPCAD, GBPAUD, GBPJPY, and GBPNZD and most surprisingly it also includes ASK price variations -- eurgbp_ask, audcad_ask, eurjpy_ask, cadjpy_ask, gbpaud_ask, and gbpcad_ask.  
What am I to do in order to correct this?  
Thanks for your help.  
R  
EDIT: Thought a screen shot would better explain my situation. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Displayed Pairs.png
Size: 62 KB](/attachment/image/2652352/thumbnail?d=1517218963)](/attachment/image/2652352?d=1517218963)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#66](/thread/post/10717608#post10717608 "Post Permalink")

  * Jan 29, 2018 6:51pm  Jan 29, 2018 6:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting RapzyFX](/thread/post/10717561#post10717561 "View Quoted Post")
> 
> Disliked
> 
> Hi ebeckers, Thanks for the pinbar ea and strat, I have installed all and the dashboard is presently showing a trade on EURNZD but I have noticed that it is not displaying all the pairs stated in the "Pairs To Trade" section. On my dashboard it is showing only EURNZD, CADJPY, EURGBP, GBPCAD, GBPAUD, GBPJPY, and GBPNZD and most surprisingly it also includes ASK price variations -- eurgbp_ask, audcad_ask, eurjpy_ask, cadjpy_ask, gbpaud_ask, and gbpcad_ask. What am I to do in order to correct this? Thanks for your help. R EDIT: Thought a screen shot...
> 
> Ignored

As stated in the first post, The EA is only showing the pairs where setups are valid or building up  
Pairs which are not interesting since there is no setup building up at the moment are filtered out and not shown 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#67](/thread/post/10717776#post10717776 "Post Permalink")

  * Jan 29, 2018 7:49pm  Jan 29, 2018 7:49pm 

  * [ RapzyFX](rapzyfx)

  * | Joined Sep 2010  | Status: Trader | [180 Posts](/search?do=process&provider=Member&searchuser=155512)

> [Quoting ebeckers](/thread/post/10717608#post10717608 "View Quoted Post")
> 
> Disliked
> 
> {quote} As stated in the first post, The EA is only showing the pairs where setups are valid or building up Pairs which are not interesting since there is no setup building up at the moment are filtered out and not shown
> 
> Ignored

Oh am really sorry for the disturbance. I actually read that part but can't imagine how it didn't click in my head.  
Thanks for your time.  
Cheers. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#68](/thread/post/10717884#post10717884 "Post Permalink")

  * Jan 29, 2018 8:23pm  Jan 29, 2018 8:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar527771_3.gif) jenbols](jenbols)

  * Joined Nov 2016 | Status: Getting there, but not just yet | [2,430 Posts](/search?do=process&provider=Member&searchuser=527771)

> [Quoting ebeckers](/thread/post/10717608#post10717608 "View Quoted Post")
> 
> Disliked
> 
> {quote} As stated in the first post, The EA is only showing the pairs where setups are valid or building up Pairs which are not interesting since there is no setup building up at the moment are filtered out and not shown
> 
> Ignored

The EA began by opening the EurNzd/Sell yesterday nite, and closed due to reverse signal, we will see later what happens _  
But this is not the point and i wanted to ask why when modifying the mql4 and compiling ...  
it becomes full of errors again ? I generally can do little modifications and i careful not to make any mistakes  
did you do something to it, have you programmed it this way not do allow modifications ?  
Why give the mql4 then, if that is the case _ ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
Well thanks you for clarifying or ... I think best to Pm you then_  
OH btw i did load the Dll and the rest of them but some cannot be found _ thanx 

The arriving better than the arrival, the journey has just started

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#69](/thread/post/10717946#post10717946 "Post Permalink")

  * Jan 29, 2018 8:36pm  Jan 29, 2018 8:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting jenbols](/thread/post/10717884#post10717884 "View Quoted Post")
> 
> Disliked
> 
> {quote} did you do something to it, have you programmed it this way not do allow modifications ?
> 
> Ignored

No offcourse not. Why would i make all source code available if i dont want you guys to compile it ??  
Simply copy all the mqh files to your MQL4/include folder  
and copy the mq4 experts file to your MQL4/experts folder   
and you should be able to compile it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#70](/thread/post/10718008#post10718008 "Post Permalink")

  * Jan 29, 2018 8:53pm  Jan 29, 2018 8:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar527771_3.gif) jenbols](jenbols)

  * Joined Nov 2016 | Status: Getting there, but not just yet | [2,430 Posts](/search?do=process&provider=Member&searchuser=527771)

> [Quoting ebeckers](/thread/post/10717946#post10717946 "View Quoted Post")
> 
> Disliked
> 
> {quote} No offcourse not. Why would i make all source code available if i dont want you guys to compile it ?? Simply copy all the mqh files to your MQL4/include folder and copy the mq4 experts file to your MQL4/experts folder and you should be able to compile it.
> 
> Ignored

Yes i thought so, as you are an honest guy   
also you made available the mql4 and i did try a few times but all errors again.  
i asked cos some times coders put some restrictions, but eventually this was not the case_  
I compiled and only changed name to PinbarTrader2_mod to differentiate the name with the 1st version  
also a couple of the dll were not in the list, .. Damn i should send a screenshot but i can't now   
so later i will do it _ Thanx for assistance ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

The arriving better than the arrival, the journey has just started

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#71](/thread/post/10718209#post10718209 "Post Permalink")

  * Jan 29, 2018 10:05pm  Jan 29, 2018 10:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar527771_3.gif) jenbols](jenbols)

  * Joined Nov 2016 | Status: Getting there, but not just yet | [2,430 Posts](/search?do=process&provider=Member&searchuser=527771)

Situation at the moment ..   
Just trying out this nice Ea which looks promising though i think some rules   
will need to be implemented later on, ex: not to take a hanging man/hammer pin bar,, whatever names  
in a continuation trend up/down or wait for more confirmation to spot fakez and so on _   
Meanwhile i started my trading day and taken some possible trades Non-Auto chart action only  
I am always curious to see differences between Auto/Non-Auto which means (Emotionless Ea -Vs- Emotional human mind decisions) 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Trades by Ea and Non Auto chart action.jpg
Size: 447 KB](/attachment/image/2652684/thumbnail?d=1517230963)](/attachment/image/2652684?d=1517230963)   
[![Click to Enlarge

Name: PATTERNS TAKEN BY THE Ea.jpg
Size: 154 KB](/attachment/image/2652686/thumbnail?d=1517230970)](/attachment/image/2652686?d=1517230970)   

The arriving better than the arrival, the journey has just started

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#72](/thread/post/10718553#post10718553 "Post Permalink")

  * Jan 29, 2018 11:35pm  Jan 29, 2018 11:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

Dank U wel Erwin ! ![](https://resources.faireconomy.media/images/emojis/64/1f4aa.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: en1.png
Size: 100 KB](/attachment/image/2652783/thumbnail?d=1517236516)](/attachment/image/2652783?d=1517236516)   

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#73](/thread/post/10718628#post10718628 "Post Permalink")

  * Jan 29, 2018 11:54pm  Jan 29, 2018 11:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar527771_3.gif) jenbols](jenbols)

  * Joined Nov 2016 | Status: Getting there, but not just yet | [2,430 Posts](/search?do=process&provider=Member&searchuser=527771)

> [Quoting pipsy7](/thread/post/10718553#post10718553 "View Quoted Post")
> 
> Disliked
> 
> Dank U wel Erwin ! ![](https://resources.faireconomy.media/images/emojis/64/1f4aa.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) {image}
> 
> Ignored

Hey Pipsy forgot you are Dutch too  
Ea seem to work is it ! but future is unpredictable you never know ,,  
but we will see what the coding mind of ebeckers has prepared for us  
**Je weet nooit hoe een koe en haas vangt** ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: pintrader update EA.jpg
Size: 279 KB](/attachment/image/2652815/thumbnail?d=1517237687)](/attachment/image/2652815?d=1517237687)   

The arriving better than the arrival, the journey has just started

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#74](/thread/post/10719100#post10719100 "Post Permalink")

  * Jan 30, 2018 1:13am  Jan 30, 2018 1:13am 

  * [ leougo](leougo)

  * | Joined Jul 2010  | Status: Trader | [35 Posts](/search?do=process&provider=Member&searchuser=149780)

Hi ebecks I appreciate your efforts and all your contributions. This looks very promising and am in on this. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#75](/thread/post/10720044#post10720044 "Post Permalink")

  * Jan 30, 2018 6:18am  Jan 30, 2018 6:18am 

  * [ Forexholy](forexholy)

  * Joined Jul 2017 | Status: Trader | [2,403 Posts](/search?do=process&provider=Member&searchuser=591923)

ebeckers  
  
Once again very nice system you have. If people would have gotten in on the very first signal Friday EUR/USD trading it manually, you could have easily made 140 pips.  
I am asking is it possible that you could add the piercing line candle and the engulfing candle I think these would be very nice additions. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#76](/thread/post/10720110#post10720110 "Post Permalink")

  * Jan 30, 2018 6:47am  Jan 30, 2018 6:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar527771_3.gif) jenbols](jenbols)

  * Joined Nov 2016 | Status: Getting there, but not just yet | [2,430 Posts](/search?do=process&provider=Member&searchuser=527771)

> [Quoting Forexholy](/thread/post/10720044#post10720044 "View Quoted Post")
> 
> Disliked
> 
> ebeckers Once again very nice system you have. If people would have gotten in on the very first signal Friday EUR/USD trading it manually, you could have easily made 140 pips. I am asking is it possible that you could add the piercing line candle and the engulfing candle I think these would be very nice additions.
> 
> Ignored

You are quite right there ,,  
the reason i soon liked this Ea made by Erwin it is not only because of a' pin bar.. ;-)  
but mostly because i saw the potential that it could expand in another little Monster Ea  
with more parameters and main patterns _  
I agree with the engulfing, however what i see many many time happening, it's the Pregnant Harami Bearish which can act as bearish reversal  
or bullish continuation .. though often patterns formed in forex charts are confused with stocks non forex charts and have **different shape**  
which are similar but not exactly because of the different stock market conditions and close 

The arriving better than the arrival, the journey has just started

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#77](/thread/post/10720113#post10720113 "Post Permalink")

  * Jan 30, 2018 6:48am  Jan 30, 2018 6:48am 

  * [ shasi12](shasi12)

  * | Joined Jan 2018  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=647219)

How is the winning percentage look like 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#78](/thread/post/10720116#post10720116 "Post Permalink")

  * Jan 30, 2018 6:53am  Jan 30, 2018 6:53am 

  * [ Forexholy](forexholy)

  * Joined Jul 2017 | Status: Trader | [2,403 Posts](/search?do=process&provider=Member&searchuser=591923)

> [Quoting jenbols](/thread/post/10720110#post10720110 "View Quoted Post")
> 
> Disliked
> 
> {quote} You are quite right there ,, the reason i soon liked this Ea made by Erwin it is not only because of a' pin bar.. ;-) but mostly because i saw the potential that it could expand in another little Monster Ea with more parameters and main patterns _ I agree with the engulfing, however what i see many many time happening, it's the Pregnant Harami Bearish which can act as bearish reversal or bullish continuation .. though often patterns formed in forex charts are confused with stocks non forex charts and have different shape which are similar...
> 
> Ignored

  
Yes this could get very big a little at a time, many more reversal candles could be added. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#79](/thread/post/10720260#post10720260 "Post Permalink")

  * Jan 30, 2018 8:27am  Jan 30, 2018 8:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar331979_1.gif) cfudge](cfudge)

  * Joined Apr 2013 | Status: Trader | [1,192 Posts](/search?do=process&provider=Member&searchuser=331979)

You guys should check out Zohebs indicator in the "Price action/system indicator" thread It does exactly what you are requesting. Maybe could be incorporated into your EA nicely Ebeckers.  
  
Chris 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#80](/thread/post/10720272#post10720272 "Post Permalink")

  * Jan 30, 2018 8:35am  Jan 30, 2018 8:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting shasi12](/thread/post/10720113#post10720113 "View Quoted Post")
> 
> Disliked
> 
> How is the winning percentage look like
> 
> Ignored

Professionals focus of setups and not percentage winning rate 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#81](/thread/post/10720757#post10720757 "Post Permalink")

  * Jan 30, 2018 2:53pm  Jan 30, 2018 2:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546078_1.gif) johnsmith2nd](johnsmith2nd)

  * Joined Jan 2017 | Status: Trader | [530 Posts](/search?do=process&provider=Member&searchuser=546078)

> [Quoting 9jatrader](/thread/post/10720272#post10720272 "View Quoted Post")
> 
> Disliked
> 
> {quote} Professionals focus of setups and not percentage winning rate
> 
> Ignored

Precisely. It's amazing what can be done with a little bit of maths. 

Attached Image

![](/attachment/image/2653653?d=1517291566)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#82](/thread/post/10720971#post10720971 "Post Permalink")

  * Jan 30, 2018 4:26pm  Jan 30, 2018 4:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting johnsmith2nd](/thread/post/10720757#post10720757 "View Quoted Post")
> 
> Disliked
> 
> {quote} Precisely. It's amazing what can be done with a little bit of maths. {image}
> 
> Ignored

We need not too much headache. Stay with trading/chart analyses 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#83](/thread/post/10721200#post10721200 "Post Permalink")

  * Jan 30, 2018 5:36pm  Jan 30, 2018 5:36pm 

  * [ maahome](maahome)

  * Joined May 2013 | Status: Trader | [568 Posts](/search?do=process&provider=Member&searchuser=336733)

> [Quoting ebeckers](/thread/post/10717946#post10717946 "View Quoted Post")
> 
> Disliked
> 
> {quote} No offcourse not. Why would i make all source code available if i dont want you guys to compile it ?? Simply copy all the mqh files to your MQL4/include folder and copy the mq4 experts file to your MQL4/experts folder and you should be able to compile it.
> 
> Ignored

Hi @ebeckers,,  
  
The download zip file only contains the ex4 and tpl files. Are you releasing the source code also? The concept you have here is a good one and I think I would like to see a combination of the order placement as an option (retracement/standard/both) instead of either or. For example 50% of risk on the retracement entry and 50% on the standard entry etc. would alloe for the opportunbity to enjoy both.  
  
Thanks for your efforts.  
maahome 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#84](/thread/post/10721254#post10721254 "Post Permalink")

  * Jan 30, 2018 5:50pm  Jan 30, 2018 5:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting maahome](/thread/post/10721200#post10721200 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi @ebeckers,, The download zip file only contains the ex4 and tpl files. Are you releasing the source code also? The concept you have here is a good one and I think I would like to see a combination of the order placement as an option (retracement/standard/both) instead of either or. For example 50% of risk on the retracement entry and 50% on the standard entry etc. would alloe for the opportunbity to enjoy both. Thanks for your efforts. maahome
> 
> Ignored

come on guys, i didnt write a big long post for nothing, did i ??  
If you would have read it you would have seen that the 1st post does contain a link to all sourcecode 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#85](/thread/post/10721282#post10721282 "Post Permalink")

  * Jan 30, 2018 6:02pm  Jan 30, 2018 6:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar527771_3.gif) jenbols](jenbols)

  * Joined Nov 2016 | Status: Getting there, but not just yet | [2,430 Posts](/search?do=process&provider=Member&searchuser=527771)

> [Quoting ebeckers](/thread/post/10721254#post10721254 "View Quoted Post")
> 
> Disliked
> 
> {quote} come on guys, i didnt write a big long post for nothing, did i ?? If you would have read it you would have seen that the 1st post does contain a link to all sourcecode
> 
> Ignored

HI Erwin would be possible just to clarify the functions   
of these parameters what they do ? I Have used few Trailing Ea's in the past   
but different terminology could have a different meaning ,,, Cheers 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Ea closing .jpg
Size: 82 KB](/attachment/image/2653864/thumbnail?d=1517302592)](/attachment/image/2653864?d=1517302592)   

The arriving better than the arrival, the journey has just started

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#86](/thread/post/10721457#post10721457 "Post Permalink")

  * Jan 30, 2018 6:44pm  Jan 30, 2018 6:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting jenbols](/thread/post/10721282#post10721282 "View Quoted Post")
> 
> Disliked
> 
> {quote} HI Erwin would be possible just to clarify the functions of these parameters what they do ? I Have used few Trailing Ea's in the past but different terminology could have a different meaning ,,, Cheers {image}
> 
> Ignored

pls read the first post.   
It Explains exactly how this works ;-) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#87](/thread/post/10721648#post10721648 "Post Permalink")

  * Jan 30, 2018 7:20pm  Jan 30, 2018 7:20pm 

  * [ maahome](maahome)

  * Joined May 2013 | Status: Trader | [568 Posts](/search?do=process&provider=Member&searchuser=336733)

> [Quoting ebeckers](/thread/post/10721254#post10721254 "View Quoted Post")
> 
> Disliked
> 
> {quote} come on guys, i didnt write a big long post for nothing, did i ?? If you would have read it you would have seen that the 1st post does contain a link to all sourcecode
> 
> Ignored

Humblest apologies @ebeckers, I am going blind in my old age I think.  
  
Thanks again  
maahome 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#88](/thread/post/10721928#post10721928 "Post Permalink")

  * Edited 8:44pm  Jan 30, 2018 8:11pm | Edited 8:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

> [Quoting maahome](/thread/post/10721648#post10721648 "View Quoted Post")
> 
> Disliked
> 
> {quote} Humblest apologies @ebeckers, I am going blind in my old age I think. Thanks again maahome
> 
> Ignored

\-------7  
  
think Again , u just toooo fukkin Lazy to read JUST 5 PAGES and there's **more** LAZY fukkers like u 4sure !  
  
but thats OK with me cuz then more $$$$$$$ in d _**Loser's_Pool**_ ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[1 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#89](/thread/post/10722198#post10722198 "Post Permalink")

  * Jan 30, 2018 9:22pm  Jan 30, 2018 9:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar527771_3.gif) jenbols](jenbols)

  * Joined Nov 2016 | Status: Getting there, but not just yet | [2,430 Posts](/search?do=process&provider=Member&searchuser=527771)

> [Quoting ebeckers](/thread/post/10721457#post10721457 "View Quoted Post")
> 
> Disliked
> 
> {quote} pls read the first post. It Explains exactly how this works ;-)
> 
> Ignored

hi read it, okay so tsx trigger/ts1.2.3 were was pretty intuitive as per my draw   
but the second part was not written on 1st page so i assume that must be a parameters   
like Eax dashboard which should be last order trailed how many pips etc .. _ 

The arriving better than the arrival, the journey has just started

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#90](/thread/post/10722353#post10722353 "Post Permalink")

  * Jan 30, 2018 10:10pm  Jan 30, 2018 10:10pm 

  * [ marzinsz](marzinsz)

  * | Joined May 2016  | Status: Trader | [55 Posts](/search?do=process&provider=Member&searchuser=465166)

Hi, i was wondering if that would be reasonable and possible to implement one function to ea, 'open chart on signal'. When sognal is generated on certain pair, ea opens chart with defined template. Temlate is sourced in default mt4 directory. That would help to see chart with any template (defined in ea by name) when signal is generated. Thank U. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#91](/thread/post/10722422#post10722422 "Post Permalink")

  * Jan 30, 2018 10:36pm  Jan 30, 2018 10:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting marzinsz](/thread/post/10722353#post10722353 "View Quoted Post")
> 
> Disliked
> 
> Hi, i was wondering if that would be reasonable and possible to implement one function to ea, 'open chart on signal'. When sognal is generated on certain pair, ea opens chart with defined template. Temlate is sourced in default mt4 directory. That would help to see chart with any template (defined in ea by name) when signal is generated. Thank U.
> 
> Ignored

As described in the first post:  

> Quote
> 
> Disliked
> 
> If you want to look at the chart , then simply click on the name of the currency pair in the 1st column (e.g. EURUSD in the screenshot)  
>  This will open a new chart with the S&R indicator attached so you can take a quick look

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#92](/thread/post/10722433#post10722433 "Post Permalink")

  * Jan 30, 2018 10:38pm  Jan 30, 2018 10:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar400088_33.gif) PayItForward](payitforward)

  * Joined Feb 2015 | Status: Patience | [1,320 Posts](/search?do=process&provider=Member&searchuser=400088)

> [Quoting jenbols](/thread/post/10722198#post10722198 "View Quoted Post")
> 
> Disliked
> 
> {quote} hi read it, okay so tsx trigger/ts1.2.3 were was pretty intuitive as per my draw but the second part was not written on 1st page so i assume that must be a parameters like Eax dashboard which should be last order trailed how many pips etc .. _
> 
> Ignored

"when profit goes above Order TS4 Trigger pips then the rest gets trailed with a Trailing Step" 

When you are successful perhaps give a thought to others ... Kiva dot org

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#93](/thread/post/10722643#post10722643 "Post Permalink")

  * Jan 30, 2018 11:29pm  Jan 30, 2018 11:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar527771_3.gif) jenbols](jenbols)

  * Joined Nov 2016 | Status: Getting there, but not just yet | [2,430 Posts](/search?do=process&provider=Member&searchuser=527771)

> [Quoting PayItForward](/thread/post/10722433#post10722433 "View Quoted Post")
> 
> Disliked
> 
> {quote} "when profit goes above Order TS4 Trigger pips then the rest gets trailed with a Trailing Step"
> 
> Ignored

ok i see, well then i best use the other trailing i got  
cheers Payit 

The arriving better than the arrival, the journey has just started

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#94](/thread/post/10722813#post10722813 "Post Permalink")

  * Jan 31, 2018 12:05am  Jan 31, 2018 12:05am 

  * [ sailorvt](sailorvt)

  * | Joined Jun 2013  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=341480)

Hi, thanks a lot for coding such good EAs and indicators.  
I see you use some very similar codes for this EA as the trend reversal EA, my question is that does the EA has a hard stoploss option?  
I want to place a hard stop, maybe not the same as the hidden sl, because I want to have protection when something like the flash crash of chf pairs several years ago.  
Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#95](/thread/post/10722823#post10722823 "Post Permalink")

  * Jan 31, 2018 12:07am  Jan 31, 2018 12:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting sailorvt](/thread/post/10722813#post10722813 "View Quoted Post")
> 
> Disliked
> 
> Hi, thanks a lot for coding such good EAs and indicators. I see you use some very similar codes for this EA as the trend reversal EA, my question is that does the EA has a hard stoploss option? I want to place a hard stop, maybe not the same as the hidden sl, because I want to have protection when something like the flash crash of chf pairs several years ago. Thanks!
> 
> Ignored

good question!  
not at the moment, but next version will have it 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#96](/thread/post/10723106#post10723106 "Post Permalink")

  * Jan 31, 2018 12:59am  Jan 31, 2018 12:59am 

  * [ sailorvt](sailorvt)

  * | Joined Jun 2013  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=341480)

> [Quoting ebeckers](/thread/post/10722823#post10722823 "View Quoted Post")
> 
> Disliked
> 
> {quote} good question! not at the moment, but next version will have it
> 
> Ignored

Thanks in advance! You're the best! and please also update the trend reversal EA to enable it with the same feature, I know a lot of people may have given up the trend reversal strategy after last week's big drawdown, but I personally still believe it might be a good method, which may only need a little bit more filters or discretion.  
Cheers!  
Happy Trading! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#97](/thread/post/10723399#post10723399 "Post Permalink")

  * Jan 31, 2018 2:05am  Jan 31, 2018 2:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

atm = 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: atm.png
Size: 106 KB](/attachment/image/2654687/thumbnail?d=1517331900)](/attachment/image/2654687?d=1517331900)   

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#98](/thread/post/10723452#post10723452 "Post Permalink")

  * Jan 31, 2018 2:23am  Jan 31, 2018 2:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting pipsy7](/thread/post/10723399#post10723399 "View Quoted Post")
> 
> Disliked
> 
> atm = {image}
> 
> Ignored

damn.. how did you get 29 trades ??  
Mine just took 3 trades so far 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#99](/thread/post/10723493#post10723493 "Post Permalink")

  * Jan 31, 2018 2:37am  Jan 31, 2018 2:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar635214_1.gif) taksistalo](taksistalo)

  * Joined Dec 2017 | Status: Trader | [183 Posts](/search?do=process&provider=Member&searchuser=635214)

Hi Ebeckers,  
  
Congrats on your post bro. Hope all is going well for you. I will defiantly test your system =) Thanks for the hours of work and sharing your system for free. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#100](/thread/post/10723518#post10723518 "Post Permalink")

  * Jan 31, 2018 2:47am  Jan 31, 2018 2:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

"**damn.. how did you get 29 trades ??** " = sofar just 1 trade completed 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: en2.png
Size: 3 KB](/attachment/image/2654739/thumbnail?d=1517334438)](/attachment/image/2654739?d=1517334438)   

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#101](/thread/post/10724154#post10724154 "Post Permalink")

  * Jan 31, 2018 7:04am  Jan 31, 2018 7:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar400088_33.gif) PayItForward](payitforward)

  * Joined Feb 2015 | Status: Patience | [1,320 Posts](/search?do=process&provider=Member&searchuser=400088)

> [Quoting jenbols](/thread/post/10722643#post10722643 "View Quoted Post")
> 
> Disliked
> 
> {quote} ok i see, well then i best use the other trailing i got cheers Payit
> 
> Ignored

Not sure what happens if you just fill in TS1 (leave the rest) and the Trailing Step ... if the Trailing Step will trigger or it needs TS4 to trigger, maybe ebeckers can clear up that picture? 

When you are successful perhaps give a thought to others ... Kiva dot org

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#102](/thread/post/10724155#post10724155 "Post Permalink")

  * Jan 31, 2018 7:06am  Jan 31, 2018 7:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546078_1.gif) johnsmith2nd](johnsmith2nd)

  * Joined Jan 2017 | Status: Trader | [530 Posts](/search?do=process&provider=Member&searchuser=546078)

Anyone else got a GBPCHF BUY signal?  
For some reason the EA is NOT opening an order... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#103](/thread/post/10724171#post10724171 "Post Permalink")

  * Jan 31, 2018 7:10am  Jan 31, 2018 7:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting johnsmith2nd](/thread/post/10724155#post10724155 "View Quoted Post")
> 
> Disliked
> 
> Anyone else got a GBPCHF BUY signal? For some reason the EA is NOT opening an order...
> 
> Ignored

yeah got it!   
ea is not opening a trade at tbis moment since the spread is too high. it will open it when spread is low again 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#104](/thread/post/10724263#post10724263 "Post Permalink")

  * Jan 31, 2018 7:58am  Jan 31, 2018 7:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting ebeckers](/thread/post/10724171#post10724171 "View Quoted Post")
> 
> Disliked
> 
> {quote} yeah got it! ea is not opening a trade at tbis moment since the spread is too high. it will open it when spread is low again
> 
> Ignored

Good feature... 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#105](/thread/post/10724285#post10724285 "Post Permalink")

  * Jan 31, 2018 8:18am  Jan 31, 2018 8:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar614028_5.gif) reo4ua](reo4ua)

  * | Joined Sep 2017  | Status: Thankful | [202 Posts](/search?do=process&provider=Member&searchuser=614028)

> [Quoting ebeckers](/thread/post/10723452#post10723452 "View Quoted Post")
> 
> Disliked
> 
> {quote} damn.. how did you get 29 trades ?? Mine just took 3 trades so far
> 
> Ignored

Pinbar and simple reversal ea's running at same time - 2 different windows - causes them to share the totals. Also does weird things with yours stop loss. I had a trade yesterday with a 5000+ pip stop loss. I'm a terrible trader but not so much that I need a margin for error that large. ;-) 

Blessed is the one who takes refuge in Him.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#106](/thread/post/10724368#post10724368 "Post Permalink")

  * Jan 31, 2018 9:11am  Jan 31, 2018 9:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting johnsmith2nd](/thread/post/10724155#post10724155 "View Quoted Post")
> 
> Disliked
> 
> Anyone else got a GBPCHF BUY signal? For some reason the EA is NOT opening an order...
> 
> Ignored

It's good to indicate the time frame 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#107](/thread/post/10724377#post10724377 "Post Permalink")

  * Jan 31, 2018 9:20am  Jan 31, 2018 9:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

**"Pinbar and simple reversal ea's running at same time - 2 different windows - causes them to share the totals."** = FYI i had just pinbar_EA  
runnin on this tiny Live US acct. 

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#108](/thread/post/10724387#post10724387 "Post Permalink")

  * Jan 31, 2018 9:24am  Jan 31, 2018 9:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar581555_2.gif) mrdfx](mrdfx)

  * Joined May 2017 | Status: Trader | [3,804 Posts](/search?do=process&provider=Member&searchuser=581555)

> [Quoting reo4ua](/thread/post/10724285#post10724285 "View Quoted Post")
> 
> Disliked
> 
> {quote} Pinbar and simple reversal ea's running at same time - 2 different windows - causes them to share the totals. Also does weird things with yours stop loss. I had a trade yesterday with a 5000+ pip stop loss. I'm a terrible trader but not so much that I need a margin for error that large. ;-)
> 
> Ignored

I'm running the SDTR EA and the pin bar EA on the same platform, and there is no issues.  
  
Make sure you are using different magic numbers for each chart and EA. 

Truth is like poetry. And most people f*cking hate poetry.

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#109](/thread/post/10724394#post10724394 "Post Permalink")

  * Jan 31, 2018 9:29am  Jan 31, 2018 9:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: man.png
Size: 116 KB](/attachment/image/2655022/thumbnail?d=1517358546)](/attachment/image/2655022?d=1517358546)   

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#110](/thread/post/10724429#post10724429 "Post Permalink")

  * Jan 31, 2018 9:46am  Jan 31, 2018 9:46am 

  * [ lctrader11](lctrader11)

  * | Joined Mar 2016  | Status: Trader | [297 Posts](/search?do=process&provider=Member&searchuser=454494)

> [Quoting mrdfx](/thread/post/10724387#post10724387 "View Quoted Post")
> 
> Disliked
> 
> {quote} I'm running the SDTR EA and the pin bar EA on the same platform, and there is no issues. Make sure you are using different magic numbers for each chart and EA.
> 
> Ignored

I didn't think I was having a problem, except I wasn't getting any alerts from the Pinbar EA. Come to find out they are both running (by default) the same Magic Numbers. I changed the last digit on each of the magic numbers for the Pinbar EA, saved it, and then removed it from the chart. When trying to reload it, it won't do it.  
I had to shut MT4 down and start it back up again to get it to load. NOWWWW we'll see how the 2 EAs behavior together. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#111](/thread/post/10724469#post10724469 "Post Permalink")

  * Jan 31, 2018 10:03am  Jan 31, 2018 10:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar614028_5.gif) reo4ua](reo4ua)

  * | Joined Sep 2017  | Status: Thankful | [202 Posts](/search?do=process&provider=Member&searchuser=614028)

55 pips total on 2 live trades. Have a 3rd that's currently flat. 

Blessed is the one who takes refuge in Him.

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#112](/thread/post/10724509#post10724509 "Post Permalink")

  * Jan 31, 2018 10:34am  Jan 31, 2018 10:34am 

  * [ lctrader11](lctrader11)

  * | Joined Mar 2016  | Status: Trader | [297 Posts](/search?do=process&provider=Member&searchuser=454494)

Have mine on D1 and no alerts. Here's a pic of the pairs with potential. Does this match up with anyone? 

Attached Image

![](/attachment/image/2655066?d=1517362467)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#113](/thread/post/10724527#post10724527 "Post Permalink")

  * Jan 31, 2018 10:46am  Jan 31, 2018 10:46am 

  * [ billbss](billbss)

  * Joined Apr 2006 | Status: Trader | [4,301 Posts](/search?do=process&provider=Member&searchuser=9243)

> [Quoting lctrader11](/thread/post/10724509#post10724509 "View Quoted Post")
> 
> Disliked
> 
> Have mine on D1 and no alerts. Here's a pic of the pairs with potential. Does this match up with anyone? {image}
> 
> Ignored

It matches mine. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#114](/thread/post/10724745#post10724745 "Post Permalink")

  * Jan 31, 2018 2:12pm  Jan 31, 2018 2:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

EA opened GBPCHF last night.. So far so good + 17pips 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screen Shot 2018-01-31 at 06.13.28.png
Size: 40 KB](/attachment/image/2655146/thumbnail?d=1517375646)](/attachment/image/2655146?d=1517375646)   

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#115](/thread/post/10724798#post10724798 "Post Permalink")

  * Jan 31, 2018 2:35pm  Jan 31, 2018 2:35pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

Hi ebeckers, first thanks for sharing the EA.  
Trying to backtested, but facing this error. Do you happen to know how to resolve? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 34 KB](/attachment/image/2655160/thumbnail?d=1517376886)](/attachment/image/2655160?d=1517376886)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#116](/thread/post/10724831#post10724831 "Post Permalink")

  * Jan 31, 2018 3:03pm  Jan 31, 2018 3:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546078_1.gif) johnsmith2nd](johnsmith2nd)

  * Joined Jan 2017 | Status: Trader | [530 Posts](/search?do=process&provider=Member&searchuser=546078)

> [Quoting 9jatrader](/thread/post/10724368#post10724368 "View Quoted Post")
> 
> Disliked
> 
> {quote} It's good to indicate the time frame
> 
> Ignored

Using daily time frame as per the rules. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#117](/thread/post/10725267#post10725267 "Post Permalink")

  * Jan 31, 2018 5:59pm  Jan 31, 2018 5:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar488242_1.gif) ppwest](ppwest)

  * | Joined Sep 2016  | Status: Trader | [113 Posts](/search?do=process&provider=Member&searchuser=488242)

> [Quoting happytrade38](/thread/post/10724798#post10724798 "View Quoted Post")
> 
> Disliked
> 
> Hi ebeckers, first thanks for sharing the EA. Trying to backtested, but facing this error. Do you happen to know how to resolve? {image}
> 
> Ignored

I'm getting the same error when trying to backtest ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#118](/thread/post/10725270#post10725270 "Post Permalink")

  * Jan 31, 2018 6:00pm  Jan 31, 2018 6:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting ppwest](/thread/post/10725267#post10725267 "View Quoted Post")
> 
> Disliked
> 
> {quote} I'm getting the same error when trying to backtest ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)
> 
> Ignored

yeah found the bug... will upload new version somewhere tonight 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#119](/thread/post/10725800#post10725800 "Post Permalink")

  * Jan 31, 2018 8:40pm  Jan 31, 2018 8:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546078_1.gif) johnsmith2nd](johnsmith2nd)

  * Joined Jan 2017 | Status: Trader | [530 Posts](/search?do=process&provider=Member&searchuser=546078)

GBPCHF - BUY at 0311hrs (+2 GMT)  
Could someone provide some analysis of this lost trade?  
  
This doesn't seem like a great setup to me (please correct me if I'm wrong).  
Quite a distance from the S/R level. The candle on the 26th suggests a bearish price action. Then the 27th there is resistance with a spinning top bullish pattern. Followed by a potential bullish pinbar, and the trade was entered on the next candle.   
  
It seems that that there was something going on at this area, and possibly not the clearest signal for an entry?  
at 1150 (+2 GMT) this was stopped out. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 10 KB](/attachment/image/2655613/thumbnail?d=1517398754)](/attachment/image/2655613?d=1517398754)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#120](/thread/post/10725943#post10725943 "Post Permalink")

  * Jan 31, 2018 9:25pm  Jan 31, 2018 9:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting ebeckers](/thread/post/10725270#post10725270 "View Quoted Post")
> 
> Disliked
> 
> {quote} yeah found the bug... will upload new version somewhere tonight
> 
> Ignored

Can Always update the first post...as long as it has version everyone will know its the latest. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#121](/thread/post/10725949#post10725949 "Post Permalink")

  * Jan 31, 2018 9:28pm  Jan 31, 2018 9:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar183881_58.gif) andoseg2](andoseg2)

  * Joined Jun 2011 | Status: Swing trader using Market Cycles | [2,152 Posts](/search?do=process&provider=Member&searchuser=183881)

> [Quoting johnsmith2nd](/thread/post/10725800#post10725800 "View Quoted Post")
> 
> Disliked
> 
> GBPCHF - BUY at 0311hrs (+2 GMT) Could someone provide some analysis of this lost trade? This doesn't seem like a great setup to me (please correct me if I'm wrong). Quite a distance from the S/R level. The candle on the 26th suggests a bearish price action. Then the 27th there is resistance with a spinning top bullish pattern. Followed by a potential bullish pinbar, and the trade was entered on the next candle. It seems that that there was something going on at this area, and possibly not the clearest signal for an entry? at 1150 (+2 GMT) this...
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_1.png
Size: 24 KB](/attachment/image/2655683/thumbnail?d=1517401682)](/attachment/image/2655683?d=1517401682)   

  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: ggg.png
Size: 42 KB](/attachment/image/2655684/thumbnail?d=1517401918)](/attachment/image/2655684?d=1517401918)   

Money moves the market, not an indicator.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#122](/thread/post/10725962#post10725962 "Post Permalink")

  * Jan 31, 2018 9:32pm  Jan 31, 2018 9:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

@john = still in this trade ! OTOH swissy has Always been Slippery m8 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: there.png
Size: 117 KB](/attachment/image/2655692/thumbnail?d=1517401949)](/attachment/image/2655692?d=1517401949)   

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#123](/thread/post/10726009#post10726009 "Post Permalink")

  * Jan 31, 2018 9:47pm  Jan 31, 2018 9:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting johnsmith2nd](/thread/post/10725800#post10725800 "View Quoted Post")
> 
> Disliked
> 
> GBPCHF - BUY at 0311hrs (+2 GMT) Could someone provide some analysis of this lost trade? This doesn't seem like a great setup to me (please correct me if I'm wrong). Quite a distance from the S/R level. The candle on the 26th suggests a bearish price action. Then the 27th there is resistance with a spinning top bullish pattern. Followed by a potential bullish pinbar, and the trade was entered on the next candle. It seems that that there was something going on at this area, and possibly not the clearest signal for an entry? at 1150 (+2 GMT) this...
> 
> Ignored

There is still a probability that it may work out (**remember not all signals even if it is looking perfect, have to workout positive**), as a signal is only invalidated when the price has broken the tail area where the original risk/protection would have been placed and still valid even if it ranges for days, ranging shakes out those without patience. We should observe what happens at the end of the day, most times when executing on a daily chart traders should look to be in the trade for at least 3 days for argument sake.. When the big boys trade this pattern they don't always move the money protection, until the end of the day or the price made a higher low. We would be surprised to see some of these same signals still valid up to weeks and months away from when they first triggered. It all boils down to the management of the trade.  
For a system like this, lots of big boys would pay heavily for a system like this...I think the reason for sharing here is to have a collective effort in making what already exist even better. ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) & judging from my side it's very good based on my filters and study. (n.b. a lot of signals exist on lower timeframe but the higher timeframe has a lot less noise and takes a whole day to materialize almost like a set and forget system for those who work or go to school etc, and these points of S&R are essential key zones).   
  
For those participating, we all have different perspectives and exposure, whether "new" or at the "been there don't that stage", we should try to constructively point out the little bugs like some have and any advice as to perfecting what can make the difference in whether we make it or not. Many of us look for too much complicated systems and try to make the simple ones more complicated. Trading should not be hard, we should keep it simple.  
Happy there are many persons interested in this very system.  
  
**Ebeckers it is a Good System...Simple and gets the Job Done and i know we will make it better.![](https://resources.faireconomy.media/images/emojis/64/1f4a1.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f4a1.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f4a1.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f4a1.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f4a1.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f3af.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f3af.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f3af.png?v=15.1)**  
**Rinse and repeat=![](https://resources.faireconomy.media/images/emojis/64/1f501.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f501.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f501.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f501.png?v=15.1)**

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#124](/thread/post/10726021#post10726021 "Post Permalink")

  * Jan 31, 2018 9:50pm  Jan 31, 2018 9:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

Started ignoring  
[](https://www.forexfactory.com/davit)[https://cdn-assets.forexfactory.net/...230796_207.gif](https://cdn-assets.forexfactory.net/nfs/customavatars/thumbs/small/avatar230796_207.gif) Davit = _**hmmm, i wonder why ?**_

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#125](/thread/post/10726048#post10726048 "Post Permalink")

  * Jan 31, 2018 9:58pm  Jan 31, 2018 9:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

_**" For a system like this, lots of big boys would pay heavily for a system like this..."**_ = damn Right m8 ! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#126](/thread/post/10726068#post10726068 "Post Permalink")

  * Jan 31, 2018 10:00pm  Jan 31, 2018 10:00pm 

  * [ kentyeoh](kentyeoh)

  * | Joined Oct 2017  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=621125)

Hi Ebeckers,  
  
i have downloaded EA but SMA200 trend filter seems missing. Can you help on this?  
  
Thanks a lot.  
  
Kent 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#127](/thread/post/10726170#post10726170 "Post Permalink")

  * Jan 31, 2018 10:23pm  Jan 31, 2018 10:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar614028_5.gif) reo4ua](reo4ua)

  * | Joined Sep 2017  | Status: Thankful | [202 Posts](/search?do=process&provider=Member&searchuser=614028)

> [Quoting reo4ua](/thread/post/10724469#post10724469 "View Quoted Post")
> 
> Disliked
> 
> 55 pips total on 2 live trades. Have a 3rd that's currently flat.
> 
> Ignored

Make that 3/3. An additional 34 pips on 3rd signal. Nice work EB! 

Blessed is the one who takes refuge in Him.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#128](/thread/post/10726187#post10726187 "Post Permalink")

  * Jan 31, 2018 10:26pm  Jan 31, 2018 10:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

fwiw = 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: fed.png
Size: 8 KB](/attachment/image/2655803/thumbnail?d=1517405198)](/attachment/image/2655803?d=1517405198)   

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#129](/thread/post/10726197#post10726197 "Post Permalink")

  * Jan 31, 2018 10:29pm  Jan 31, 2018 10:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting johnsmith2nd](/thread/post/10725800#post10725800 "View Quoted Post")
> 
> Disliked
> 
> GBPCHF - BUY at 0311hrs (+2 GMT) Could someone provide some analysis of this lost trade? This doesn't seem like a great setup to me (please correct me if I'm wrong). Quite a distance from the S/R level. The candle on the 26th suggests a bearish price action. Then the 27th there is resistance with a spinning top bullish pattern. Followed by a potential bullish pinbar, and the trade was entered on the next candle. It seems that that there was something going on at this area, and possibly not the clearest signal for an entry? at 1150 (+2 GMT) this...
> 
> Ignored

Trade is still running here.  
Yesterday we had a pinbar rejecting the weekly level @ 1.31090  
Today price retraced to +/-50% of the pinbar and now its slowly moving into profit  
  
(in hindsight.. I got in too early, i should have waited for the 50% retrace) 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: gbpchf.jpg
Size: 234 KB](/attachment/image/2655807/thumbnail?d=1517405349)](/attachment/image/2655807?d=1517405349)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#130](/thread/post/10726283#post10726283 "Post Permalink")

  * Jan 31, 2018 10:45pm  Jan 31, 2018 10:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar581555_2.gif) mrdfx](mrdfx)

  * Joined May 2017 | Status: Trader | [3,804 Posts](/search?do=process&provider=Member&searchuser=581555)

My GBPCHF buy trade got stopped out last night. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screen Shot 2018-01-31 at 11.44.47.png
Size: 13 KB](/attachment/image/2655835/thumbnail?d=1517406314)](/attachment/image/2655835?d=1517406314)   

Truth is like poetry. And most people f*cking hate poetry.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#131](/thread/post/10726292#post10726292 "Post Permalink")

  * Jan 31, 2018 10:47pm  Jan 31, 2018 10:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting ebeckers](/thread/post/10726197#post10726197 "View Quoted Post")
> 
> Disliked
> 
> {quote} Trade is still running here. Yesterday we had a pinbar rejecting the weekly level @ 1.31090 Today price retraced to +/-50% of the pinbar and now its slowly moving into profit (in hindsight.. I got in too early, i should have waited for the 50% retrace) {image}
> 
> Ignored

Yes the 50% is the sweet one, though it does not come very often but when it does come it's worth the wait. Usually when this limit order entry is triggered it tends to work out even better than the stop order entry, something for traders to think about. nice one ebeckers...![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#132](/thread/post/10726343#post10726343 "Post Permalink")

  * Jan 31, 2018 10:58pm  Jan 31, 2018 10:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting mrdfx](/thread/post/10726283#post10726283 "View Quoted Post")
> 
> Disliked
> 
> My GBPCHF buy trade got stopped out last night. {image}
> 
> Ignored

On my live account I'm trading manually and using the EA for signals;-)  
On my demo account i'm use the EA for automated trading and that on got stopped out indeed 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#133](/thread/post/10726401#post10726401 "Post Permalink")

  * Jan 31, 2018 11:07pm  Jan 31, 2018 11:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: temp.png
Size: 110 KB](/attachment/image/2655911/thumbnail?d=1517407618)](/attachment/image/2655911?d=1517407618)   

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#134](/thread/post/10726451#post10726451 "Post Permalink")

  * Jan 31, 2018 11:16pm  Jan 31, 2018 11:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar581555_2.gif) mrdfx](mrdfx)

  * Joined May 2017 | Status: Trader | [3,804 Posts](/search?do=process&provider=Member&searchuser=581555)

> [Quoting ebeckers](/thread/post/10726343#post10726343 "View Quoted Post")
> 
> Disliked
> 
> {quote} On my live account I'm trading manually and using the EA for signals;-) On my demo account i'm use the EA for automated trading and that on got stopped out indeed
> 
> Ignored

Not trading this strategy live yet, still testing the waters. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

Truth is like poetry. And most people f*cking hate poetry.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#135](/thread/post/10726751#post10726751 "Post Permalink")

  * Feb 1, 2018 12:11am  Feb 1, 2018 12:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar298742_5.gif) bluejack](bluejack)

  * | Joined Oct 2012  | Status: Trader | [493 Posts](/search?do=process&provider=Member&searchuser=298742)

ebeckers.. Thank You for the EA. Looks very promising. I have been closing the trades manually by checking the 1hr S/R, but EA opens the trade again from where i close. Can we add an option like EA opens trades on only new signals or something that sort of? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#136](/thread/post/10726838#post10726838 "Post Permalink")

  * Feb 1, 2018 12:35am  Feb 1, 2018 12:35am 

  * [ Monty13](monty13)

  * | Joined Aug 2009  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=113946)

> [Quoting bluejack](/thread/post/10726751#post10726751 "View Quoted Post")
> 
> Disliked
> 
> ebeckers.. Thank You for the EA. Looks very promising. I have been closing the trades manually by checking the 1hr S/R, but EA opens the trade again from where i close. Can we add an option like EA opens trades on only new signals or something that sort of?
> 
> Ignored

bluejack.  
The option is already in the EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#137](/thread/post/10726866#post10726866 "Post Permalink")

  * Feb 1, 2018 12:40am  Feb 1, 2018 12:40am 

  * [ Monty13](monty13)

  * | Joined Aug 2009  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=113946)

[quote=ebeckers;10726343]{quote} On my live account I'm trading manually and using the EA for signals;-) On my demo account i'm use the EA for automated trading and that on got stopped out indeed[/q  
  
Hi ebeckers. Thank you for the EA.  
  
Would it be possible to have both, trade opens at the start and as well as the 50% retracement if it occurs.  
  
Just a thought.  
  
Thanks again. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#138](/thread/post/10727030#post10727030 "Post Permalink")

  * Feb 1, 2018 1:15am  Feb 1, 2018 1:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting johnsmith2nd](/thread/post/10724831#post10724831 "View Quoted Post")
> 
> Disliked
> 
> {quote} Using daily time frame as per the rules.
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#139](/thread/post/10727130#post10727130 "Post Permalink")

  * Feb 1, 2018 1:24am  Feb 1, 2018 1:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar298742_5.gif) bluejack](bluejack)

  * | Joined Oct 2012  | Status: Trader | [493 Posts](/search?do=process&provider=Member&searchuser=298742)

> [Quoting Monty13](/thread/post/10726838#post10726838 "View Quoted Post")
> 
> Disliked
> 
> {quote} bluejack. The option is already in the EA.
> 
> Ignored

Thank You, but i believe that "allow reentries on the same pair" is a different function. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#140](/thread/post/10727301#post10727301 "Post Permalink")

  * Feb 1, 2018 2:00am  Feb 1, 2018 2:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 3.png
Size: 126 KB](/attachment/image/2656402/thumbnail?d=1517417996)](/attachment/image/2656402?d=1517417996)   

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#141](/thread/post/10727331#post10727331 "Post Permalink")

  * Feb 1, 2018 2:12am  Feb 1, 2018 2:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

Did anyone see __**NZDJPY**__ yesterday?? 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#142](/thread/post/10727434#post10727434 "Post Permalink")

  * Edited 3:11am  Feb 1, 2018 2:40am | Edited 3:11am 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

> [Quoting johnsmith2nd](/thread/post/10725800#post10725800 "View Quoted Post")
> 
> Disliked
> 
> GBPCHF - BUY at 0311hrs (+2 GMT) Could someone provide some analysis of this lost trade? This doesn't seem like a great setup to me (please correct me if I'm wrong). Quite a distance from the S/R level. The candle on the 26th suggests a bearish price action. Then the 27th there is resistance with a spinning top bullish pattern. Followed by a potential bullish pinbar, and the trade was entered on the next candle. It seems that that there was something going on at this area, and possibly not the clearest signal for an entry? at 1150 (+2 GMT) this...
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 29 KB](/attachment/image/2656452/thumbnail?d=1517420393)](/attachment/image/2656452?d=1517420393)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture2.PNG
Size: 26 KB](/attachment/image/2656464/thumbnail?d=1517420774)](/attachment/image/2656464?d=1517420774)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture3.PNG
Size: 80 KB](/attachment/image/2656504/thumbnail?d=1517421649)](/attachment/image/2656504?d=1517421649)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture4.PNG
Size: 89 KB](/attachment/image/2656515/thumbnail?d=1517421927)](/attachment/image/2656515?d=1517421927)   

  
If she does not close the candle, there is no reason to enter. It could be a breakthrough, but they could be pincers?  
  
Ако не е затворила свещта, няма никакво основание за вход. Може да е пробив, но може да са пинцети? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#143](/thread/post/10727620#post10727620 "Post Permalink")

  * Feb 1, 2018 3:27am  Feb 1, 2018 3:27am 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

> [Quoting 9jatrader](/thread/post/10727331#post10727331 "View Quoted Post")
> 
> Disliked
> 
> Did anyone see NZDJPY yesterday??
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 72 KB](/attachment/image/2656548/thumbnail?d=1517423220)](/attachment/image/2656548?d=1517423220)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#144](/thread/post/10728236#post10728236 "Post Permalink")

  * Feb 1, 2018 6:10am  Feb 1, 2018 6:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting pipsy7](/thread/post/10727301#post10727301 "View Quoted Post")
> 
> Disliked
> 
> {image}
> 
> Ignored

Nice... 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#145](/thread/post/10728242#post10728242 "Post Permalink")

  * Feb 1, 2018 6:11am  Feb 1, 2018 6:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting juraia](/thread/post/10727620#post10727620 "View Quoted Post")
> 
> Disliked
> 
> {quote} {image}
> 
> Ignored

I did. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#146](/thread/post/10728325#post10728325 "Post Permalink")

  * Feb 1, 2018 7:38am  Feb 1, 2018 7:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

Does everyone have 2 signals and 3 possible others=5 signals for the day.  
That being:  
**Eurgbp-Short**  
**Cadchf-Short**  
**Audusd-Possible Short**  
**Gbpcad-Possible Long**  
**Eurnzd-Possible Short**

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#147](/thread/post/10728336#post10728336 "Post Permalink")

  * Feb 1, 2018 7:44am  Feb 1, 2018 7:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting lctrader11](/thread/post/10724509#post10724509 "View Quoted Post")
> 
> Disliked
> 
> Have mine on D1 and no alerts. Here's a pic of the pairs with potential. Does this match up with anyone? {image}
> 
> Ignored

Did you manage to have all these trades trigger? 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#148](/thread/post/10728390#post10728390 "Post Permalink")

  * Feb 1, 2018 8:32am  Feb 1, 2018 8:32am 

  * [ Monty13](monty13)

  * | Joined Aug 2009  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=113946)

> [Quoting PrinceJ58](/thread/post/10728325#post10728325 "View Quoted Post")
> 
> Disliked
> 
> Does everyone have 2 signals and 3 possible others=5 signals for the day. That being: Eurgbp-Short Cadchf-Short Audusd-Possible Short Gbpcad-Possible Long Eurnzd-Possible Short
> 
> Ignored

I have Cad Chf and eur/gbp short triggered. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#149](/thread/post/10730218#post10730218 "Post Permalink")

  * Edited 10:06pm  Feb 1, 2018 9:34pm | Edited 10:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

atm = + Not usin **VPS** and puter **was closed** for 7 hrs [_**00AM-07AM EST**_ (NY time)]  
  
Most likely Will _**close**_ all trades 1hr B4 _**NFP**_ = tmw **_Fri. [07:30 EST]_**  
  
**imagin** what a Nice profit$ if it was _**7bucks**_ /pip instead of .02/pip ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 4.png
Size: 126 KB](/attachment/image/2657684/thumbnail?d=1517488477)](/attachment/image/2657684?d=1517488477)   

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#150](/thread/post/10730438#post10730438 "Post Permalink")

  * Feb 1, 2018 10:17pm  Feb 1, 2018 10:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 4+.png
Size: 134 KB](/attachment/image/2657765/thumbnail?d=1517491045)](/attachment/image/2657765?d=1517491045)   

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#151](/thread/post/10731683#post10731683 "Post Permalink")

  * Feb 2, 2018 1:53am  Feb 2, 2018 1:53am 

  * [ Beertje](beertje)

  * | Joined Oct 2011  | Status: Trader | [446 Posts](/search?do=process&provider=Member&searchuser=198914)

Many thanks for sharing, great system! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#152](/thread/post/10731783#post10731783 "Post Permalink")

  * Feb 2, 2018 2:11am  Feb 2, 2018 2:11am 

  * [ Beertje](beertje)

  * | Joined Oct 2011  | Status: Trader | [446 Posts](/search?do=process&provider=Member&searchuser=198914)

I would like to ask you, what is the difference between the "SimpleDailyTrendReversal" and the "PinBarTrader"? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#153](/thread/post/10731854#post10731854 "Post Permalink")

  * Feb 2, 2018 2:28am  Feb 2, 2018 2:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting Beertje](/thread/post/10731783#post10731783 "View Quoted Post")
> 
> Disliked
> 
> I would like to ask you, what is the difference between the "SimpleDailyTrendReversal" and the "PinBarTrader"?
> 
> Ignored

The ea looks more or less the same, but the underlying trading strategies are completely different 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#154](/thread/post/10731862#post10731862 "Post Permalink")

  * Feb 2, 2018 2:29am  Feb 2, 2018 2:29am 

  * [ sailorvt](sailorvt)

  * | Joined Jun 2013  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=341480)

> [Quoting Beertje](/thread/post/10731783#post10731783 "View Quoted Post")
> 
> Disliked
> 
> I would like to ask you, what is the difference between the "SimpleDailyTrendReversal" and the "PinBarTrader"?
> 
> Ignored

both of them are made by a very generous member **ebeckers** here at FF, so some of the options seem very similar.  
for the difference please read the first page of this thread and first page of  
<https://www.forexfactory.com/showthread.php?t=713593>  
to see the logics behind both EAs. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#155](/thread/post/10732338#post10732338 "Post Permalink")

  * Feb 2, 2018 4:46am  Feb 2, 2018 4:46am 

  * [ Beertje](beertje)

  * | Joined Oct 2011  | Status: Trader | [446 Posts](/search?do=process&provider=Member&searchuser=198914)

> [Quoting sailorvt](/thread/post/10731862#post10731862 "View Quoted Post")
> 
> Disliked
> 
> {quote} both of them are made by a very generous member ebeckers here at FF, so some of the options seem very similar. for the difference please read the first page of this thread and first page of <https://www.forexfactory.com/showthread.php?t=713593> to see the logics behind both EAs.
> 
> Ignored

  
Thank you! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#156](/thread/post/10732356#post10732356 "Post Permalink")

  * Feb 2, 2018 4:53am  Feb 2, 2018 4:53am 

  * [ billbss](billbss)

  * Joined Apr 2006 | Status: Trader | [4,301 Posts](/search?do=process&provider=Member&searchuser=9243)

I'm seeing the sell and buy on some of the pairs, but it isn't opening any trades.  
I have the smiling face- I wonder what I'm doing wrong. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#157](/thread/post/10732487#post10732487 "Post Permalink")

  * Feb 2, 2018 5:26am  Feb 2, 2018 5:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting billbss](/thread/post/10732356#post10732356 "View Quoted Post")
> 
> Disliked
> 
> I'm seeing the sell and buy on some of the pairs, but it isn't opening any trades. I have the smiling face- I wonder what I'm doing wrong.
> 
> Ignored

spread is probably too high atm, ea will open the trade when spread is loeer 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#158](/thread/post/10732620#post10732620 "Post Permalink")

  * Feb 2, 2018 6:13am  Feb 2, 2018 6:13am 

  * [ lctrader11](lctrader11)

  * | Joined Mar 2016  | Status: Trader | [297 Posts](/search?do=process&provider=Member&searchuser=454494)

> [Quoting ebeckers](/thread/post/10731854#post10731854 "View Quoted Post")
> 
> Disliked
> 
> {quote} The ea looks more or less the same, but the underlying trading strategies are completely different
> 
> Ignored

I have them both running and have changed the Magic Numbers to avoid conflict, but the PinBar EA isn't giving me any signals, whereas the TrendReversal is constantly giving me alerts. I'm using defaults for everything...maybe I should change some of the parameters? Any ideas? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#159](/thread/post/10732754#post10732754 "Post Permalink")

  * Feb 2, 2018 7:22am  Feb 2, 2018 7:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

Thats because they are 2 completely different strategies. trend reversal works mostly on H4 and will find much more signals   
Pinbar works on D1 with weekly levels, so expect just a handful signals a week from this 

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#160](/thread/post/10732798#post10732798 "Post Permalink")

  * Feb 2, 2018 7:48am  Feb 2, 2018 7:48am 

  * [ lctrader11](lctrader11)

  * | Joined Mar 2016  | Status: Trader | [297 Posts](/search?do=process&provider=Member&searchuser=454494)

> [Quoting ebeckers](/thread/post/10732754#post10732754 "View Quoted Post")
> 
> Disliked
> 
> Thats because they are 2 completely different strategies. trend reversal works mostly on H4 and will find much more signals Pinbar works on D1 with weekly levels, so expect just a handful signals a week from this
> 
> Ignored

I'd like to make a request to make the alerts for each of those EAs a little more descriptive. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#161](/thread/post/10732905#post10732905 "Post Permalink")

  * Feb 2, 2018 8:39am  Feb 2, 2018 8:39am 

  * [ Monty13](monty13)

  * | Joined Aug 2009  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=113946)

Hi ebeckers. Thank you for the EA.  
  
Would it be possible to have both option, trade opens at the start and as well as the 50% retracement when it occurs.  
  
Just a thought.  
  
Thanks again.![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)  
  
1  

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#162](/thread/post/10733135#post10733135 "Post Permalink")

  * Feb 2, 2018 11:04am  Feb 2, 2018 11:04am 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

> [Quoting ebeckers](/thread/post/10725270#post10725270 "View Quoted Post")
> 
> Disliked
> 
> {quote} yeah found the bug... will upload new version somewhere tonight
> 
> Ignored

  
thanks sir. do update us after update the new version, going to backtest and get the feel. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#163](/thread/post/10733585#post10733585 "Post Permalink")

  * Feb 2, 2018 3:15pm  Feb 2, 2018 3:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting happytrade38](/thread/post/10733135#post10733135 "View Quoted Post")
> 
> Disliked
> 
> {quote} thanks sir. do update us after update the new version, going to backtest and get the feel.
> 
> Ignored

will do, but found 1 other bug i'm currently busy fixing  
Hope to have a new version ready this weekend 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#164](/thread/post/10734163#post10734163 "Post Permalink")

  * Feb 2, 2018 6:23pm  Feb 2, 2018 6:23pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

> [Quoting ebeckers](/thread/post/10733585#post10733585 "View Quoted Post")
> 
> Disliked
> 
> {quote} will do, but found 1 other bug i'm currently busy fixing Hope to have a new version ready this weekend
> 
> Ignored

thanks sir. take your time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#165](/thread/post/10734428#post10734428 "Post Permalink")

  * Feb 2, 2018 7:28pm  Feb 2, 2018 7:28pm 

  * [ thantrang](thantrang)

  * | Joined Jan 2018  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=640232)

Ebeckers I'm subscribed. Your coding skills and generosity is truely amazing!  
Thanks  
  

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#166](/thread/post/10734448#post10734448 "Post Permalink")

  * Feb 2, 2018 7:34pm  Feb 2, 2018 7:34pm 

  * [ mftrader](mftrader)

  * | Joined Sep 2017  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=614434)

Simplicity of the Dashboard is great. Thanks Ebeckes for the EA. Hope to be live and profitable, when time is right. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#167](/thread/post/10734689#post10734689 "Post Permalink")

  * Feb 2, 2018 8:19pm  Feb 2, 2018 8:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar472073_2.gif) ordosgoitia](ordosgoitia)

  * Joined Jun 2016 | Status: Trader | [268 Posts](/search?do=process&provider=Member&searchuser=472073)

> [Quoting pipsy7](/thread/post/10730218#post10730218 "View Quoted Post")
> 
> Disliked
> 
> atm = + Not usin VPS and puter was closed for 7 hrs [00AM-07AM EST (NY time)] Most likely Will close all trades 1hr B4 NFP = tmw Fri. [07:30 EST] imagin what a Nice profit$ if it was 7bucks/pip instead of .02/pip ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) {image}
> 
> Ignored

Hi, what settings are you using? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#168](/thread/post/10735558#post10735558 "Post Permalink")

  * Feb 2, 2018 11:03pm  Feb 2, 2018 11:03pm 

  * [ ohleclaire](ohleclaire)

  * | Joined Sep 2014  | Status: Trader | [40 Posts](/search?do=process&provider=Member&searchuser=384148)

<http://prntscr.com/i95qzm>  
  
Bug? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#169](/thread/post/10735754#post10735754 "Post Permalink")

  * Feb 2, 2018 11:33pm  Feb 2, 2018 11:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

> [Quoting ordosgoitia](/thread/post/10734689#post10734689 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, what settings are you using?
> 
> Ignored

\-------7  
  
= def. 

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#170](/thread/post/10736188#post10736188 "Post Permalink")

  * Edited 3:05am  Feb 3, 2018 12:46am | Edited 3:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1) = 7 ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: flat.png
Size: 304 KB](/attachment/image/2660092/thumbnail?d=1517594586)](/attachment/image/2660092?d=1517594586)   

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#171](/thread/post/10737587#post10737587 "Post Permalink")

  * Edited 7:12am  Feb 3, 2018 6:53am | Edited 7:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting pipsy7](/thread/post/10736188#post10736188 "View Quoted Post")
> 
> Disliked
> 
> ![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1) = 7 ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) {image}
> 
> Ignored

Based on those signals today along with NFP as a factor...Would you have traded those?  
**Audjpy- No-** If using the stop order, it was not triggered.  
**NzdChf** \- **Yes-** If using the 50% (**68-70 pips gain**) or Stop Order (**45-50 pips gain**)  
**GbpChf-Yes-** If using the 50% (**Don't think it would was triggered**) or Stop Order (**45 pips gain**)  
**Eurcad** -**No-** Not valid- It does not have a good signal in terms of pinbar requirements, far from the signal  
**CadChf** -**Yes** If using the 50% (**70-78 pips gain**) or Stop Order (**52-56 pips gain**)  
**AudCad** -No Not valid- It does not have a good signal in terms of pinbar requirements, far from the signal  
  
**3 out of 4 Valid signals and 2 not worthy of trading.**  
**Trades today Resulting in a "_minimum_ " 140 pips minimum for 2 possible limit order trades and a minimum of 142 pips for stop order trades. **  
**Were there any other signals?**

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#172](/thread/post/10737639#post10737639 "Post Permalink")

  * Edited 7:50am  Feb 3, 2018 7:16am | Edited 7:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting PrinceJ58](/thread/post/10737587#post10737587 "View Quoted Post")
> 
> Disliked
> 
> {quote} Based on those signals today along with NFP as a factor...Would you have traded those? Audjpy- No- If using the stop order, it was not triggered. NzdChf- Yes-If using the 50% (68-70 pips gain) or Stop Order (45-50 pips gain) GbpChf-Yes-If using the 50% (Don't think it would was triggered) or Stop Order (45 pips gain) Eurcad-No-Not valid- It does not have a good signal in terms of pinbar requirements, far from the signal CadChf -Yes If using the 50% (70-78 pips gain) or Stop Order (52-56 pips gain) AudCad-No Not valid- It does not have a...
> 
> Ignored

So we have two concerns and thats the two invalid signals- why did it alert to these two bars that are not pinbars? Probably a bug.  
Nevertheless it does filter those signals well...Keep it up. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#173](/thread/post/10738292#post10738292 "Post Permalink")

  * Feb 3, 2018 8:07pm  Feb 3, 2018 8:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

> [Quoting PrinceJ58](/thread/post/10737639#post10737639 "View Quoted Post")
> 
> Disliked
> 
> {quote} So we have two concerns and thats the two invalid signals- why did it alert to these two bars that are not pinbars? Probably a bug. Nevertheless it does filter those signals well...Keep it up.
> 
> Ignored

Hello PrinceJ58  
  
Really appreciated your work here...  
  
I have 2 ideas for this strategy.  
  
There are 4 types of combinations can be recongized as reverse pattern.   
  
Thus, this Pinbar approach is quite rough, sometimes we will miss signals if it is not a pinbar.  
  
Moveover, Daliy candle can be various from different brokers, so as the signals.  
  
Finally, TP and SL issues.  
  
this picture tells everything.  
  
all brokers have same M1 and H1 charts. 

Attached Image

![](/attachment/image/2660573?d=1517655830)

No one wants to be defeated~

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#174](/thread/post/10738293#post10738293 "Post Permalink")

  * Feb 3, 2018 8:09pm  Feb 3, 2018 8:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

Hi guys, so first week has past. Let's see how the EA did so far.  
Like i said before, i use automated trading on a demo account with 0.01 lotsize just to see how the EA is doing in automated trading mode  
_(So don't look at the $ it made, thats pretty low because of the 0.01 lotsize. Instead just look at the pips gained/lost)_  
  
_Note that for my life account i do manual trading only._  
_I do use the EA as an tool which scans the market for me and sends me alerts when something interesting pops up_  
  
So.. first week the EA did pretty well. It made 7 trades with a 71.43% win ratio  
In total it made 105 pips and we have a profit factor of 2.36, which is really good  
And we still have 1 trade running which is currently at +42 pips, so things could be even higher..  
  
Now please note this was with 100% full automated trading  
If you had traded manually and used the EA for signals you could have made much more.  
Simply because we humans are stil better at reading the market then computers are ;-)  
  
So whats up for next week ?  
I'm currently busy developing the next release of the EA. it will fix some small bugs and have some new exciting features  
Things i'm working on is  
\- more candle stick reversal patterns  
\- more candle stick trend continuation patterns and signals  
\- sma 200 trend filter  
\- distributed cloud S&R levels so we have manual spotted S&R levels stored in the cloud which we can all use  
\- and some more stuff 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screen Shot 2018-02-03 at 12.00.38.png
Size: 109 KB](/attachment/image/2660571/thumbnail?d=1517655727)](/attachment/image/2660571?d=1517655727)   

[0 ](javascript:void\(0\);) [9 ](javascript:void\(0\);)

  * [#175](/thread/post/10738298#post10738298 "Post Permalink")

  * Edited 9:08pm  Feb 3, 2018 8:18pm | Edited 9:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

Whatever types of daliy candle reverse the market, is all comes from basic N shape in smaller timeframe. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 25 KB](/attachment/image/2660575/thumbnail?d=1517656728)](/attachment/image/2660575?d=1517656728)   

Attached Image

![](/attachment/image/2660580?d=1517657165)

No one wants to be defeated~

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#176](/thread/post/10738305#post10738305 "Post Permalink")

  * Feb 3, 2018 8:30pm  Feb 3, 2018 8:30pm 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

> [Quoting jonirrenicus](/thread/post/10738298#post10738298 "View Quoted Post")
> 
> Disliked
> 
> Whatever daliy candle reverse the market, is all comes from basic N shape in smaller timeframe. {image} {image}
> 
> Ignored

.... lower low, 1-2-3 pattern, ABCD .... and so on 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#177](/thread/post/10738326#post10738326 "Post Permalink")

  * Feb 3, 2018 8:42pm  Feb 3, 2018 8:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

TP and SL case by case.  
  
Near last Top/bottom, 1618 2618 4236  
  
Far from last Top/bottom, 1618 200 2618  
  
SL si always at Fibo 0.0 level. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 37 KB](/attachment/image/2660600/thumbnail?d=1517657649)](/attachment/image/2660600?d=1517657649)   
[![Click to Enlarge

Name: Screenshot3.png
Size: 27 KB](/attachment/image/2660609/thumbnail?d=1517657953)](/attachment/image/2660609?d=1517657953)   

Attached Image

![](/attachment/image/2660596?d=1517657548)

No one wants to be defeated~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#178](/thread/post/10738432#post10738432 "Post Permalink")

  * Feb 3, 2018 10:45pm  Feb 3, 2018 10:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting jonirrenicus](/thread/post/10738326#post10738326 "View Quoted Post")
> 
> Disliked
> 
> TP and SL case by case. Near last Top/bottom, 1618 2618 4236 Far from last Top/bottom, 1618 200 2618 SL si always at Fibo 0.0 level. {image} {image} {image}
> 
> Ignored

Sorry but i don't understand a bit about what you are trying to explain.  
Also lets try to keep the thread focused on the original strategy.  
There are already way to many threads in this forum where people get enthusiastic and post literaly everything they think  
This cause the few posts about the original strategy to get lost between all those off-topic posts..  
  
**So pls guys lets keep this thread relevant to the original strategy.**  
How to trade it, how to improve it and what your results/ideas/suggestions about it are 

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#179](/thread/post/10738473#post10738473 "Post Permalink")

  * Feb 3, 2018 11:06pm  Feb 3, 2018 11:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

> [Quoting ebeckers](/thread/post/10738432#post10738432 "View Quoted Post")
> 
> Disliked
> 
> {quote} Sorry but i don't understand a bit about what you are trying to explain. Also lets try to keep the thread focused on the original strategy. There are already way to many threads in this forum where people get enthusiastic and post literaly everything they think This cause the few posts about the original strategy to get lost between all those off-topic posts.. So pls guys lets keep this thread relevant to the original strategy. How to trade it, how to improve it and what your results/ideas/suggestions about it are
> 
> Ignored

sorry i just want to improve your strategy, but i may go too far from it.  
  
thanks again for your sharing! Could you pls explain the logic for calculating the weekly SR levels? 

Attached Image

![](/attachment/image/2660674?d=1517666532)

No one wants to be defeated~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#180](/thread/post/10738509#post10738509 "Post Permalink")

  * Feb 3, 2018 11:24pm  Feb 3, 2018 11:24pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

> [Quoting ebeckers](/thread/post/10738293#post10738293 "View Quoted Post")
> 
> Disliked
> 
> Hi guys, so first week has past. Let's see how the EA did so far. Like i said before, i use automated trading on a demo account with 0.01 lotsize just to see how the EA is doing in automated trading mode (So don't look at the $ it made, thats pretty low because of the 0.01 lotsize. Instead just look at the pips gained/lost) Note that for my life account i do manual trading only. I do use the EA as an tool which scans the market for me and sends me alerts when something interesting pops up So.. first week the EA did pretty well. It made 7 trades...
> 
> Ignored

the result is encouraging and looks forward it.  
I agree manual trading would be able to generate relatively higher return, but in certain points EA might outperform than human especially on psychological part such as after consecutive loss, missed the trade due to other commitments and etc, so in my view, EA trading should still be used as part of the trading maybe can allocate the lower capital or lower percentage of risk. this is my personal view. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#181](/thread/post/10739301#post10739301 "Post Permalink")

  * Feb 4, 2018 10:25am  Feb 4, 2018 10:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

Ok I see where some "pinbars" ended up working out to be hanging man = bullish pinbar end up as a bearish result while there was the opposite a grave stone doji/ inverted hammer =bearish pinbar but ended up as a bullish result. Do we ignore those?   
  
I wonder if your update will have any of the following:  
Cloud cover  
Morning star - I prefer  
Evening star- I prefer  
Beovb  
Buovb  
Inside bar  
Harami  
  
Whatever you choose will be good since the pinbar is so good already. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#182](/thread/post/10739534#post10739534 "Post Permalink")

  * Feb 4, 2018 3:57pm  Feb 4, 2018 3:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting PrinceJ58](/thread/post/10739301#post10739301 "View Quoted Post")
> 
> Disliked
> 
> Ok I see where some "pinbars" ended up working out to be hanging man = bullish pinbar end up as a bearish result while there was the opposite a grave stone doji/ inverted hammer =bearish pinbar but ended up as a bullish result. Do we ignore those? I wonder if your update will have any of the following: Cloud cover Morning star - I prefer Evening star- I prefer Beovb Buovb Inside bar Harami Whatever you choose will be good since the pinbar is so good already.
> 
> Ignored

yeah i know all these patterns and sometimes its hard to tell if a candle is a pinbar, a doji , a hanging man, shooting star or ...  
But in my opinion its totally irrelevant if its a pinbar or for example a hanging man.  
What is relevant is that the **price action** **touched a major S &R** level and shows a **strong rejection on that level**.  
Like it says ok.. here's the line, we are NOT going to cross it.  
That reaction may result in one of the various candle stick patterns.  
My idea is that the ea recognises the fact that we have a strong rejection from the S&R level, not that it can perfectly quantify if its a pinbar or a hanging man ;-) 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#183](/thread/post/10739708#post10739708 "Post Permalink")

  * Feb 4, 2018 7:28pm  Feb 4, 2018 7:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting PrinceJ58](/thread/post/10739301#post10739301 "View Quoted Post")
> 
> Disliked
> 
> Ok I see where some "pinbars" ended up working out to be hanging man = bullish pinbar end up as a bearish result while there was the opposite a grave stone doji/ inverted hammer =bearish pinbar but ended up as a bullish result. Do we ignore those? I wonder if your update will have any of the following: Cloud cover Morning star - I prefer Evening star- I prefer Beovb Buovb Inside bar Harami Whatever you choose will be good since the pinbar is so good already.
> 
> Ignored

**By your analyses it means we did not wait to for TF candle to finally close before we took the position. We have to wait for candle to close before final analyses**.**In spite of the strong analyses we might take no setup is 100% safe. And so we keep our risk level low**

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#184](/thread/post/10739719#post10739719 "Post Permalink")

  * Feb 4, 2018 7:33pm  Feb 4, 2018 7:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

> [Quoting PrinceJ58](/thread/post/10739301#post10739301 "View Quoted Post")
> 
> Disliked
> 
> Ok I see where some "pinbars" ended up working out to be hanging man = bullish pinbar end up as a bearish result while there was the opposite a grave stone doji/ inverted hammer =bearish pinbar but ended up as a bullish result. Do we ignore those? I wonder if your update will have any of the following: Cloud cover Morning star - I prefer Evening star- I prefer Beovb Buovb Inside bar Harami Whatever you choose will be good since the pinbar is so good already.
> 
> Ignored

Hi,  
  
All of them may become a reverse point, pin bar is only one type. 

Attached Image

![](/attachment/image/2661201?d=1517740389)

No one wants to be defeated~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#185](/thread/post/10739730#post10739730 "Post Permalink")

  * Feb 4, 2018 7:39pm  Feb 4, 2018 7:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting ebeckers](/thread/post/10739534#post10739534 "View Quoted Post")
> 
> Disliked
> 
> {quote} yeah i know all these patterns and sometimes its hard to tell if a candle is a pinbar, a doji , a hanging man, shooting star or ... But in my opinion its totally irrelevant if its a pinbar or for example a hanging man. What is relevant is that the price action touched a major S&R level and shows a strong rejection on that level. Like it says ok.. here's the line, we are NOT going to cross it. That reaction may result in one of the various candle stick patterns. My idea is that the ea recognises the fact that we have a strong rejection from...
> 
> Ignored

**You hit the point. When they form on S/R you enter with peace of mind. Sometimes they form their own S/R which becomes so important and reference point-S/R**

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#186](/thread/post/10740472#post10740472 "Post Permalink")

  * Feb 5, 2018 4:20am  Feb 5, 2018 4:20am 

  * [ FxMadness](fxmadness)

  * Joined May 2017 | Status: Trader | [1,564 Posts](/search?do=process&provider=Member&searchuser=579828)

> [Quoting jonirrenicus](/thread/post/10739719#post10739719 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, All of them may become a reverse point, pin bar is only one type. {image}
> 
> Ignored

  
**Written Chinese** ([Chinese](https://en.wikipedia.org/wiki/Chinese_language): 中文; [pinyin](https://en.wikipedia.org/wiki/Pinyin): _zhōngwén_) comprises [Chinese characters](https://en.wikipedia.org/wiki/Chinese_character) (汉字/漢字; pinyin: _Hànzì_ , literally "[Han](https://en.wikipedia.org/wiki/Han_people) characters") used to represent the [Chinese language](https://en.wikipedia.org/wiki/Chinese_language). Chinese characters do not constitute an alphabet or a compact [syllabary](https://en.wikipedia.org/wiki/Syllabary). Rather, the writing system is roughly [logosyllabic](https://en.wikipedia.org/wiki/Logogram); that is, a character generally represents one [syllable](https://en.wikipedia.org/wiki/Syllable) of spoken Chinese and may be a word on its own or a part of a polysyllabic word. The characters themselves are often composed of parts that may represent physical objects, abstract notions,[[1]](https://en.wikipedia.org/wiki/Written_Chinese#cite_note-FOOTNOTEWieger1915-1) or pronunciation.[[2]](https://en.wikipedia.org/wiki/Written_Chinese#cite_note-FOOTNOTEDeFrancis198484-2) Literacy requires the memorization of a great many characters: educated Chinese know about 4,000.[[3]](https://en.wikipedia.org/wiki/Written_Chinese#cite_note-FOOTNOTEDeFrancis1968-3)[[4]](https://en.wikipedia.org/wiki/Written_Chinese#cite_note-FOOTNOTENorman198873-4) The large number of Chinese characters has in part led to the adoption of Western alphabets as an auxiliary means of representing Chinese.[[5]](https://en.wikipedia.org/wiki/Written_Chinese#cite_note-FOOTNOTERamsey1987143-5)  
  
  
That's why i did not understand your post. 

I can calculate the movement of stars, but not the madness of men. Isaac N.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#187](/thread/post/10742636#post10742636 "Post Permalink")

  * Feb 5, 2018 9:21pm  Feb 5, 2018 9:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546078_1.gif) johnsmith2nd](johnsmith2nd)

  * Joined Jan 2017 | Status: Trader | [530 Posts](/search?do=process&provider=Member&searchuser=546078)

Anyone else had their dashboard disappear? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 40 KB](/attachment/image/2662489/thumbnail?d=1517833274)](/attachment/image/2662489?d=1517833274)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#188](/thread/post/10742666#post10742666 "Post Permalink")

  * Feb 5, 2018 9:32pm  Feb 5, 2018 9:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar581555_2.gif) mrdfx](mrdfx)

  * Joined May 2017 | Status: Trader | [3,804 Posts](/search?do=process&provider=Member&searchuser=581555)

> [Quoting johnsmith2nd](/thread/post/10742636#post10742636 "View Quoted Post")
> 
> Disliked
> 
> Anyone else had their dashboard disappear? {image}
> 
> Ignored

If there's no valid confirmations on any pair then nothing will be displayed. As soon as one of the criteria becomes valid on a pair it will show on the panel. 

Truth is like poetry. And most people f*cking hate poetry.

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#189](/thread/post/10742712#post10742712 "Post Permalink")

  * Feb 5, 2018 9:51pm  Feb 5, 2018 9:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting mrdfx](/thread/post/10742666#post10742666 "View Quoted Post")
> 
> Disliked
> 
> {quote} If there's no valid confirmations on any pair then nothing will be displayed. As soon as one of the criteria becomes valid on a pair it will show on the panel.
> 
> Ignored

  
That's how trading should always be, if no setup no trade. Sometimes we sit there looking for a reason to get in and this is a good feature of the dashboard. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#190](/thread/post/10742845#post10742845 "Post Permalink")

  * Feb 5, 2018 10:24pm  Feb 5, 2018 10:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546078_1.gif) johnsmith2nd](johnsmith2nd)

  * Joined Jan 2017 | Status: Trader | [530 Posts](/search?do=process&provider=Member&searchuser=546078)

> [Quoting mrdfx](/thread/post/10742666#post10742666 "View Quoted Post")
> 
> Disliked
> 
> {quote} If there's no valid confirmations on any pair then nothing will be displayed. As soon as one of the criteria becomes valid on a pair it will show on the panel.
> 
> Ignored

Cheers for clarification, and agreed with J58! No signal, nothing to look at! Enjoy our day! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#191](/thread/post/10742859#post10742859 "Post Permalink")

  * Feb 5, 2018 10:27pm  Feb 5, 2018 10:27pm 

  * [ Bullilulli](bullilulli)

  * | Joined Jul 2015  | Status: Trader | [83 Posts](/search?do=process&provider=Member&searchuser=419042)

Thx for sharing. I will follow.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#192](/thread/post/10742919#post10742919 "Post Permalink")

  * Feb 5, 2018 10:41pm  Feb 5, 2018 10:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

**fwiw** =  
  

The **significant** announcements and the currencies affected include:

**6th February**

  1. 02:30, AUD, Trade Balance
  2. 05:30, AUD, RBA Cash Rate
  3. 15:30, CAD, Trade Balance
  4. 23:45, NZD, Unemployment Rate
  5. 23:45, NZD, Labour Cost Index

  

**7th February**

  1. 22:00, NZD, Cen Bank Interest Rate

  

**8th February**

  1. 14:00, GBP, BOE Bank Rate
  2. 21:00, MXN, Interest Rate

  

**9th February**

  1. 15:30, CAD, Employment Change
  2. 15:30, CAD, Unemployment Rate

  

*All times are Server Time (GMT+2).

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#193](/thread/post/10743006#post10743006 "Post Permalink")

  * Feb 5, 2018 11:05pm  Feb 5, 2018 11:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting 9jatrader](/thread/post/10739708#post10739708 "View Quoted Post")
> 
> Disliked
> 
> {quote} By your analyses it means we did not wait to for TF candle to finally close before we took the position. We have to wait for candle to close before final analyses.In spite of the strong analyses we might take no setup is 100% safe. And so we keep our risk level low
> 
> Ignored

Actually it was a signal photo that I used and I waited until the signals played out for the most part before saying such a thing. For e.g, the alert came on Wednesday/thursday and I waited for friday to come close to an end for newyork session before making such analysis.   
  
My only Aim is to first understand what the system is doing as there are many pinbars that paint across the market but this system does a process of elimination. I was just looking to see how it did that day. I did it for one day and ebeckers did it for the week as "whole" for both live and demo account also for automated and manual which I really appreciate but I had no images for the signals to do a personal analysis of each signal per day.   
I love pinbars and I like his system concept so that was my reason for going into it a bit more. For me some traders look for one thing, this could be my one thing. So with his help and my interest trading this method my trading can also remain simply what this dashboard offers.  
  
I also like the fact that it was highlighted that the rejection of the area is even more important than the bar itself. I was being very strict with the criteria looking for a specific bar if you understand. Cheers. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#194](/thread/post/10743054#post10743054 "Post Permalink")

  * Feb 5, 2018 11:11pm  Feb 5, 2018 11:11pm 

  * [ shasi12](shasi12)

  * | Joined Jan 2018  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=647219)

It's strange EA works in my Mac not in PC.... anyone can help me with please..... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#195](/thread/post/10743524#post10743524 "Post Permalink")

  * Feb 6, 2018 12:21am  Feb 6, 2018 12:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting shasi12](/thread/post/10743054#post10743054 "View Quoted Post")
> 
> Disliked
> 
> It's strange EA works in my Mac not in PC.... anyone can help me with please.....
> 
> Ignored

Post a screenshot of your mt4 with e.a. loaded open the terminal section and click on expert to see if there are any errors.  
  
Right click chart and save picture choose workspace. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#196](/thread/post/10744613#post10744613 "Post Permalink")

  * Feb 6, 2018 4:14am  Feb 6, 2018 4:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546131_3.gif) pamc](pamc)

  * Joined Jan 2017 | Status: Trader | [1,305 Posts](/search?do=process&provider=Member&searchuser=546131)

> [Quoting shasi12](/thread/post/10743054#post10743054 "View Quoted Post")
> 
> Disliked
> 
> It's strange EA works in my Mac not in PC.... anyone can help me with please.....
> 
> Ignored

Sashi, in the files from Ebeckers, when unzippig there are versions MACOS and PC. you must use the PC version for PC. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#197](/thread/post/10746460#post10746460 "Post Permalink")

  * Feb 6, 2018 2:19pm  Feb 6, 2018 2:19pm 

  * [ shasi12](shasi12)

  * | Joined Jan 2018  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=647219)

Thank you Prince & Pamc it works now ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#198](/thread/post/10750809#post10750809 "Post Permalink")

  * Feb 7, 2018 11:23am  Feb 7, 2018 11:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

first trade on EA 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 42 KB](/attachment/image/2665795/thumbnail?d=1517970157)](/attachment/image/2665795?d=1517970157)   

No one wants to be defeated~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#199](/thread/post/10750888#post10750888 "Post Permalink")

  * Feb 7, 2018 12:37pm  Feb 7, 2018 12:37pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

> [Quoting jonirrenicus](/thread/post/10750809#post10750809 "View Quoted Post")
> 
> Disliked
> 
> first trade on EA {image}
> 
> Ignored

Thought this EA should placed at daily chart? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#200](/thread/post/10750908#post10750908 "Post Permalink")

  * Feb 7, 2018 12:42pm  Feb 7, 2018 12:42pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

this is the recommendation for today (note i have included more pairs)  
However, I found some pairs with pinbar is not shown in dashboard under pinbar column e.g. GJ.  
Anyone can share if i miss out anything? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 16 KB](/attachment/image/2665849/thumbnail?d=1517974905)](/attachment/image/2665849?d=1517974905)   

Attached Image

![](/attachment/image/2665830?d=1517974693)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#201](/thread/post/10750932#post10750932 "Post Permalink")

  * Feb 7, 2018 12:52pm  Feb 7, 2018 12:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar42265_1.gif) huatboyz](huatboyz)

  * Joined Jun 2007 | Status: Trader | [190 Posts](/search?do=process&provider=Member&searchuser=42265)

My ea not opening trades , is it something wrong with my settings ? 

Pips Collector EA, No Martingale, No Grid

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#202](/thread/post/10752656#post10752656 "Post Permalink")

  * Feb 7, 2018 9:33pm  Feb 7, 2018 9:33pm 

  * [ Monty13](monty13)

  * | Joined Aug 2009  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=113946)

> [Quoting huatboyz](/thread/post/10750932#post10750932 "View Quoted Post")
> 
> Disliked
> 
> My ea not opening trades , is it something wrong with my settings ?
> 
> Ignored

There hasn't been any trade signal yet. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Pinbar.D.png
Size: 101 KB](/attachment/image/2666653/thumbnail?d=1518006785)](/attachment/image/2666653?d=1518006785)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#203](/thread/post/10753650#post10753650 "Post Permalink")

  * Feb 8, 2018 1:08am  Feb 8, 2018 1:08am 

  * [ shasi12](shasi12)

  * | Joined Jan 2018  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=647219)

> [Quoting Monty13](/thread/post/10752656#post10752656 "View Quoted Post")
> 
> Disliked
> 
> {quote} There hasn't been any trade signal yet. {image}
> 
> Ignored

same here.... not everyday is a trading day 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#204](/thread/post/10753671#post10753671 "Post Permalink")

  * Feb 8, 2018 1:12am  Feb 8, 2018 1:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

very quiet week... zzzzzZZZZ  
Lets hope things get better soon :-) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#205](/thread/post/10753986#post10753986 "Post Permalink")

  * Feb 8, 2018 2:25am  Feb 8, 2018 2:25am 

  * [ Monty13](monty13)

  * | Joined Aug 2009  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=113946)

> [Quoting ebeckers](/thread/post/10753671#post10753671 "View Quoted Post")
> 
> Disliked
> 
> very quiet week... zzzzzZZZZ Lets hope things get better soon :-)
> 
> Ignored

Hi ebeckers.  
  
How's the new development vertison of pinbar is doing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#206](/thread/post/10754552#post10754552 "Post Permalink")

  * Feb 8, 2018 4:59am  Feb 8, 2018 4:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar42265_1.gif) huatboyz](huatboyz)

  * Joined Jun 2007 | Status: Trader | [190 Posts](/search?do=process&provider=Member&searchuser=42265)

understood. thanks so much ! 

Pips Collector EA, No Martingale, No Grid

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#207](/thread/post/10755382#post10755382 "Post Permalink")

  * Edited 10:26pm  Feb 8, 2018 1:42pm | Edited 10:26pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

this is the recommendation for dated on 7 Feb (i have included more pairs)  
However, I found some pairs with pinbar is not shown in dashboard under pinbar column e.g. GJ.  
Anyone can share if i miss out anything? 

Attached Images

![](/attachment/image/2668735?d=1518096395) ![](/attachment/image/2668737?d=1518096396)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#208](/thread/post/10755803#post10755803 "Post Permalink")

  * Feb 8, 2018 4:43pm  Feb 8, 2018 4:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

> [Quoting happytrade38](/thread/post/10750888#post10750888 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thought this EA should placed at daily chart?
> 
> Ignored

EA= EUR AUD lol...  
  
i use pinbar EA as scanner....  
  
another good signal... 

Attached Image

![](/attachment/image/2668016?d=1518075797)

No one wants to be defeated~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#209](/thread/post/10756682#post10756682 "Post Permalink")

  * Feb 8, 2018 8:12pm  Feb 8, 2018 8:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar445074_1.gif) amirhaq](amirhaq)

  * | Joined Jan 2016  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=445074)

hi sir   
  
my account balance is 1100$ in real ... please share with me good set file and ea i m newbie and lost money please help.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#210](/thread/post/10757003#post10757003 "Post Permalink")

  * Feb 8, 2018 9:28pm  Feb 8, 2018 9:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting amirhaq](/thread/post/10756682#post10756682 "View Quoted Post")
> 
> Disliked
> 
> hi sir my account balance is 1100$ in real ... please share with me good set file and ea i m newbie and lost money please help....
> 
> Ignored

Do you have strategy. Forex is more than placing buy/sell order 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#211](/thread/post/10757046#post10757046 "Post Permalink")

  * Feb 8, 2018 9:35pm  Feb 8, 2018 9:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar439673_6.gif) KeenPips](keenpips)

  * Joined Dec 2015 | Status: Trader | [8,254 Posts](/search?do=process&provider=Member&searchuser=439673)

If I may advise, stop trading live account and save your trading capital. Go on a diet of demo trading for about six months mainly to develop a simple system and strategy that you are comfortable with. Make yourself a master of that system/strategy first before you go back to live trading; operate on a 0.01 lot first (micro) and see how your system/strategy works in real live trading. Just my 2 cents mate.  
  
Trade safe and prosper.  
  
KP  
  

> [Quoting amirhaq](/thread/post/10756682#post10756682 "View Quoted Post")
> 
> Disliked
> 
> hi sir my account balance is 1100$ in real ... please share with me good set file and ea i m newbie and lost money please help....
> 
> Ignored

Do your homework, follow the footprints of smart money

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#212](/thread/post/10757127#post10757127 "Post Permalink")

  * Feb 8, 2018 9:44pm  Feb 8, 2018 9:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting KeenPips](/thread/post/10757046#post10757046 "View Quoted Post")
> 
> Disliked
> 
> If I may advise, stop trading live account and save your trading capital. Go on a diet of demo trading for about six months mainly to develop a simple system and strategy that you are comfortable with. Make yourself a master of that system/strategy first before you go back to live trading; operate on a 0.01 lot first (micro) and see how your system/strategy works in real live trading. Just my 2 cents mate. Trade safe and prosper. KP {quote}
> 
> Ignored

You just hit the point. He should open __**same amount**__ in Demo and practice with it. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#213](/thread/post/10757656#post10757656 "Post Permalink")

  * Feb 8, 2018 11:12pm  Feb 8, 2018 11:12pm 

  * [ Trix7v7](trix7v7)

  * | Joined Feb 2018  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=650568)

Good day!  
Very interesting Advisor. Creator - **Ebeckers** thank you. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#214](/thread/post/10757753#post10757753 "Post Permalink")

  * Feb 8, 2018 11:25pm  Feb 8, 2018 11:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar445074_1.gif) amirhaq](amirhaq)

  * | Joined Jan 2016  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=445074)

> [Quoting 9jatrader](/thread/post/10757127#post10757127 "View Quoted Post")
> 
> Disliked
> 
> {quote} You just hit the point. He should open same amount in Demo and practice with it.
> 
> Ignored

i try many stragies and robots but i lost 2900$ i research good ea and traders any one help me in forex .......  
  
  
sorry my bd english 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#215](/thread/post/10759669#post10759669 "Post Permalink")

  * Feb 9, 2018 6:45am  Feb 9, 2018 6:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting amirhaq](/thread/post/10757753#post10757753 "View Quoted Post")
> 
> Disliked
> 
> {quote} i try many stragies and robots but i lost 2900$ i research good ea and traders any one help me in forex ....... sorry my bd english
> 
> Ignored

Focus on trading around S/R. You're subscribed to this thread. Some would be formed on strong support 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#216](/thread/post/10759700#post10759700 "Post Permalink")

  * Feb 9, 2018 6:51am  Feb 9, 2018 6:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting amirhaq](/thread/post/10757753#post10757753 "View Quoted Post")
> 
> Disliked
> 
> {quote} i try many stragies and robots but i lost 2900$ i research good ea and traders any one help me in forex ....... sorry my bd english
> 
> Ignored

The strategy of building account is to stay with small lot size. When you have successfully closed your position, if it's enough you can use the profit to add to lot size. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#217](/thread/post/10760276#post10760276 "Post Permalink")

  * Feb 9, 2018 12:30pm  Feb 9, 2018 12:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

> [Quoting amirhaq](/thread/post/10757753#post10757753 "View Quoted Post")
> 
> Disliked
> 
> {quote} i try many stragies and robots but i lost 2900$ i research good ea and traders any one help me in forex ....... sorry my bd english
> 
> Ignored

forex trading is harder than any common jobs you can find in the market.  
  
set and forget EA, winning while sleeping... finally end up with blowing up. 

No one wants to be defeated~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#218](/thread/post/10760300#post10760300 "Post Permalink")

  * Feb 9, 2018 12:39pm  Feb 9, 2018 12:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

> [Quoting ebeckers](/thread/post/10753671#post10753671 "View Quoted Post")
> 
> Disliked
> 
> very quiet week... zzzzzZZZZ Lets hope things get better soon :-)
> 
> Ignored

hello sir,  
  
Is there a set file available to make your EA scan all currencies when SR Level was touched?  
  
another good signal in EU session 

Attached Image

![](/attachment/image/2669825?d=1518147594)

No one wants to be defeated~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#219](/thread/post/10760604#post10760604 "Post Permalink")

  * Feb 9, 2018 3:11pm  Feb 9, 2018 3:11pm 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

> [Quoting jonirrenicus](/thread/post/10755803#post10755803 "View Quoted Post")
> 
> Disliked
> 
> {quote} EA= EUR AUD lol... i use pinbar EA as scanner.... another good signal... {image}
> 
> Ignored

Excuse me, but what does yours do to none of the unknown EA with the Pinar Trader EA - Trading pinbars off weekly S & R levels? You got enough stains on the topic. Open your theme and post graphics as you please.  
  
Извинявай, но какво общо има твоето на никой неизвестно EA с темата Pinbar trader EA - Trading pinbars off weekly S&R levels? Достатъчно изцапахте темата. Отворете си ваша тема и си публикувайте графики колкото поискате. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#220](/thread/post/10760666#post10760666 "Post Permalink")

  * Feb 9, 2018 3:49pm  Feb 9, 2018 3:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar42265_1.gif) huatboyz](huatboyz)

  * Joined Jun 2007 | Status: Trader | [190 Posts](/search?do=process&provider=Member&searchuser=42265)

Today had a Gold buy signal, but the EA did not opened any trades, can anyone help please? My Autotrading is turned on, I don't know what's wrong 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 94 KB](/attachment/image/2670045/thumbnail?d=1518158971)](/attachment/image/2670045?d=1518158971)   

Pips Collector EA, No Martingale, No Grid

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#221](/thread/post/10760846#post10760846 "Post Permalink")

  * Feb 9, 2018 4:54pm  Feb 9, 2018 4:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

> [Quoting huatboyz](/thread/post/10760666#post10760666 "View Quoted Post")
> 
> Disliked
> 
> Today had a Gold buy signal, but the EA did not opened any trades, can anyone help please? My Autotrading is turned on, I don't know what's wrong {image}
> 
> Ignored

Probably the spread is to high ?  
You can specify the max spread allowed in the settings 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#222](/thread/post/10761109#post10761109 "Post Permalink")

  * Feb 9, 2018 5:43pm  Feb 9, 2018 5:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

> [Quoting juraia](/thread/post/10760604#post10760604 "View Quoted Post")
> 
> Disliked
> 
> {quote} Excuse me, but what does yours do to none of the unknown EA with the Pinar Trader EA - Trading pinbars off weekly S & R levels? You got enough stains on the topic. Open your theme and post graphics as you please. Извинявай, но какво общо има твоето на никой неизвестно...
> 
> Ignored

I think i have make myself very clear on this topic.  
  
1 Switch to H1 TF and find Zigzag reverse signal between EU-NY session.  
2 use fibo to exit partially  
  
that's all... 

No one wants to be defeated~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#223](/thread/post/10761198#post10761198 "Post Permalink")

  * Feb 9, 2018 6:00pm  Feb 9, 2018 6:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

going to buy... 

Attached Image

![](/attachment/image/2670294?d=1518166760)

No one wants to be defeated~

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#224](/thread/post/10761303#post10761303 "Post Permalink")

  * Feb 9, 2018 6:29pm  Feb 9, 2018 6:29pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

Hi ebeckers, is the pinbar shown in dashboard display for all pairs I put in? Or pinbar at S&R level (which I don't think so). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#225](/thread/post/10761598#post10761598 "Post Permalink")

  * Feb 9, 2018 7:46pm  Feb 9, 2018 7:46pm 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

> [Quoting jonirrenicus](/thread/post/10761109#post10761109 "View Quoted Post")
> 
> Disliked
> 
> {quote} I think i have make myself very clear on this topic. 1 Switch to H1 TF and find Zigzag reverse signal between EU-NY session. 2 use fibo to exit partially that's all...
> 
> Ignored

Friend, something did not understand me. You are testing with another EA, this topic is for Pinar Trader EA - Trading pinbars off weekly S & R levels. The other thing is that the strategy of ebeckers is quite different from yours. Looking for Pinbar, the TF H1 is pretty crazy.  
  
Приятел, нещо не ме разбра. Ти тестваш с друг EA, тази тема е за Pinbar trader EA - Trading pinbars off weekly S&R levels. Другото е, че стратегията на ebeckers е съвсем различна от вашата. Да търсиш Pinbar, на TF H1 е доста налудничаво. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#226](/thread/post/10762635#post10762635 "Post Permalink")

  * Feb 9, 2018 11:14pm  Feb 9, 2018 11:14pm 

  * [ Trix7v7](trix7v7)

  * | Joined Feb 2018  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=650568)

Good day, Colleagues!  
Dear **ebeckers** , I appreciate your development. Thank you very much for your work.  
I wanted to ask you for help, maybe you'll find some precious time.  
In addition to automatic trading, I trade in the standard way (multicurrency trading).  
I really like the implementation of TS in your works.  
You may find it possible to allocate a separate expert Advisor to support open orders on TS (in the standard way or by another expert Advisor), on specific pairs or to accompany a specific order.  
Sori for my English, thank you very much. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#227](/thread/post/10764686#post10764686 "Post Permalink")

  * Feb 10, 2018 3:02pm  Feb 10, 2018 3:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

> [Quoting juraia](/thread/post/10761598#post10761598 "View Quoted Post")
> 
> Disliked
> 
> {quote} Friend, something did not understand me. You are testing with another EA, this topic is for Pinar Trader EA - Trading pinbars off weekly S & R levels. The other thing is that the strategy of ebeckers is quite different from yours. Looking for Pinbar, the TF H1 is pretty crazy. Приятел, нещо не ме разбра. Ти тестваш с друг EA, тази...
> 
> Ignored

hello  
  
Check my previous posts, using H1 ZZ to repalce Pinbars on D1. NOT Looking for Pinbars on H1 TF. 

No one wants to be defeated~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#228](/thread/post/10764813#post10764813 "Post Permalink")

  * Feb 10, 2018 5:59pm  Feb 10, 2018 5:59pm 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

[quote=ebeckers;10714321]=== Pinbar Trader EA === Hi everyone, welcome.... Want to get involved ? you can find all source code for this (and my other ea's & indicators) on GitHub <https://github.com/erwin-beckers/SimpleTrendReversalEA>   
  
Hi there EBeckers: Thanks for this; good stuff!. I went looking for the Source Code for the SupportResistance Indicator but did not find it. Can you make it available as well?.  
  
Thank you.  
  
Krismitt. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#229](/thread/post/10764823#post10764823 "Post Permalink")

  * Feb 10, 2018 6:19pm  Feb 10, 2018 6:19pm 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

[quote=krismitt;10764813]

> [Quoting ebeckers](/thread/post/10714321#post10714321 "View Quoted Post")
> 
> Disliked
> 
> === Pinbar Trader EA === Hi everyone, welcome.... Want to get involved ? you can find all source code for this (and my other ea's & indicators) on GitHub <https://github.com/erwin-beckers/SimpleTrendReversalEA> Hi there EBeckers: Thanks for this; good stuff!. I went looking for the Source Code for the SupportResistance Indicator but did not find it. Can you make it available as well?. Thank you. Krismitt.
> 
> Ignored

@krismitt: That's quite simple to find ! Click at "erwin-beckers" in the first line above in this homepage "github" and you'll see all the stuff he coded + posted at this HP ! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#230](/thread/post/10764828#post10764828 "Post Permalink")

  * Feb 10, 2018 6:29pm  Feb 10, 2018 6:29pm 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

[quote=DerBerliner;10764823]

> [Quoting krismitt](/thread/post/10764813#post10764813 "View Quoted Post")
> 
> Disliked
> 
> {quote} @krismitt: That's quite simple to find ! Click at "erwin-beckers" in the first line above in this homepage "github" and you'll see all the stuff he coded + posted at this HP !
> 
> Ignored

Thanks DerBerliner. Got it!.  
  
Cheers. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#231](/thread/post/10776847#post10776847 "Post Permalink")

  * Feb 14, 2018 5:55pm  Feb 14, 2018 5:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar440253_2.gif) badeel](badeel)

  * Joined Dec 2015 | Status: Trader | [257 Posts](/search?do=process&provider=Member&searchuser=440253)

Why this Threat stop out??????????  
its good EA and template lets make this thread and ea alive 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#232](/thread/post/10776909#post10776909 "Post Permalink")

  * Feb 14, 2018 6:09pm  Feb 14, 2018 6:09pm 

  * [ Monty13](monty13)

  * | Joined Aug 2009  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=113946)

> [Quoting badeel](/thread/post/10776847#post10776847 "View Quoted Post")
> 
> Disliked
> 
> Why this Threat stop out?????????? its good EA and template lets make this thread and ea alive
> 
> Ignored

Agree.  
there is no signals so far this week. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: D1 Pinbar.png
Size: 94 KB](/attachment/image/2676617/thumbnail?d=1518599341)](/attachment/image/2676617?d=1518599341)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#233](/thread/post/10777428#post10777428 "Post Permalink")

  * Feb 14, 2018 9:03pm  Feb 14, 2018 9:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar546078_1.gif) johnsmith2nd](johnsmith2nd)

  * Joined Jan 2017 | Status: Trader | [530 Posts](/search?do=process&provider=Member&searchuser=546078)

> [Quoting Monty13](/thread/post/10776909#post10776909 "View Quoted Post")
> 
> Disliked
> 
> {quote} Agree. there is no signals so far this week. {image}
> 
> Ignored

I've got a buy signal for GBPNZD (50%RT is off)however no trade has been opened by the EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#234](/thread/post/10779653#post10779653 "Post Permalink")

  * Feb 15, 2018 4:43am  Feb 15, 2018 4:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

Holiday for the system... 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#235](/thread/post/10781632#post10781632 "Post Permalink")

  * Feb 15, 2018 6:38pm  Feb 15, 2018 6:38pm 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

> [Quoting PrinceJ58](/thread/post/10779653#post10779653 "View Quoted Post")
> 
> Disliked
> 
> Holiday for the system...
> 
> Ignored

I'm not loving any of these. Anyone keen on any of them?.  
  

Attached Image

![](/attachment/image/2678293?d=1518687451)

  
  
Regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#236](/thread/post/10781848#post10781848 "Post Permalink")

  * Feb 15, 2018 7:42pm  Feb 15, 2018 7:42pm 

  * [ Monty13](monty13)

  * | Joined Aug 2009  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=113946)

> [Quoting krismitt](/thread/post/10781632#post10781632 "View Quoted Post")
> 
> Disliked
> 
> {quote} I'm not loving any of these. Anyone keen on any of them?. {image} Regards.
> 
> Ignored

Strange. I haven't got any signals.  
  
Do you have S R on.??? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: D1.png
Size: 103 KB](/attachment/image/2678393/thumbnail?d=1518691366)](/attachment/image/2678393?d=1518691366)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#237](/thread/post/10781876#post10781876 "Post Permalink")

  * Feb 15, 2018 7:52pm  Feb 15, 2018 7:52pm 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

> [Quoting Monty13](/thread/post/10781848#post10781848 "View Quoted Post")
> 
> Disliked
> 
> {quote} Strange. I haven't got any signals. Do you have S R on.??? {image}
> 
> Ignored

Sure.  
  
Cheers. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#238](/thread/post/10781901#post10781901 "Post Permalink")

  * Feb 15, 2018 8:02pm  Feb 15, 2018 8:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar648613_2.gif) farang007](farang007)

  * | Joined Feb 2018  | Status: Trader | [54 Posts](/search?do=process&provider=Member&searchuser=648613)

Hi ebeckers, thank so much for your kind sharing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#239](/thread/post/10781913#post10781913 "Post Permalink")

  * Feb 15, 2018 8:04pm  Feb 15, 2018 8:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting PrinceJ58](/thread/post/10779653#post10779653 "View Quoted Post")
> 
> Disliked
> 
> Holiday for the system...
> 
> Ignored

No signal/system can give traders setup everyday/week/month. That's the reason Forex is a game of patience 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#240](/thread/post/10781994#post10781994 "Post Permalink")

  * Feb 15, 2018 8:30pm  Feb 15, 2018 8:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar581555_2.gif) mrdfx](mrdfx)

  * Joined May 2017 | Status: Trader | [3,804 Posts](/search?do=process&provider=Member&searchuser=581555)

Looks like things have woken up today and going well so far. ![](https://resources.faireconomy.media/images/emojis/64/1f4aa.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screen Shot 2018-02-15 at 09.29.36.png
Size: 69 KB](/attachment/image/2678478/thumbnail?d=1518694224)](/attachment/image/2678478?d=1518694224)   

Truth is like poetry. And most people f*cking hate poetry.

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#241](/thread/post/10784629#post10784629 "Post Permalink")

  * Feb 16, 2018 12:31pm  Feb 16, 2018 12:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting 9jatrader](/thread/post/10781913#post10781913 "View Quoted Post")
> 
> Disliked
> 
> {quote} No signal/system can give traders setup everyday/week/month. That's the reason Forex is a game of patience
> 
> Ignored

No successful signal service...  
You have a nice percentage, is it based of pinbars? 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#242](/thread/post/10784638#post10784638 "Post Permalink")

  * Feb 16, 2018 12:33pm  Feb 16, 2018 12:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting krismitt](/thread/post/10781632#post10781632 "View Quoted Post")
> 
> Disliked
> 
> {quote} I'm not loving any of these. Anyone keen on any of them?. {image} Regards.
> 
> Ignored

Was that even the pinbar strategy I've never seen a day with so many setups. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#243](/thread/post/10785269#post10785269 "Post Permalink")

  * Feb 16, 2018 5:52pm  Feb 16, 2018 5:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting PrinceJ58](/thread/post/10784629#post10784629 "View Quoted Post")
> 
> Disliked
> 
> {quote} No successful signal service... You have a nice percentage, is it based of pinbars?
> 
> Ignored

You're correct, no successful signal. That's the reason we need to keep the risk so low, however strong the setup might be.  
My trades are based on  
**1. Pin Bar on ranging/sideways**  
**2. Hammer, specially with bullish body on sideways/ranging **  
**market.**  
**3. Shooting Star, Gravestone Doji, specially with bearish body and below resistance**  
**4. Bullish/Bearish Engulfing on sideways/ranging market**

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#244](/thread/post/10786391#post10786391 "Post Permalink")

  * Feb 16, 2018 10:55pm  Feb 16, 2018 10:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting 9jatrader](/thread/post/10785269#post10785269 "View Quoted Post")
> 
> Disliked
> 
> {quote} You're correct, no successful signal. That's the reason we need to keep the risk so low, however strong the setup might be. My trades are based on 1. Pin Bar on ranging/sideways 2. Hammer, specially with bullish body on sideways/ranging market. 3. Shooting Star, Gravestone Doji, specially with bearish body and below resistance 4. Bullish/Bearish Engulfing on sideways/ranging market
> 
> Ignored

Excellent  
**1. Pin Bar on ranging/sideways-So the ones that stick out, you don't trade those ones**  
**2. Hammer, specially with bullish body on sideways/ranging market. -So you ignore the bearish colors even if it **  
**3. Shooting Star, Gravestone Doji, specially with bearish body and below resistance-Goodstuff**  
**4. Bullish/Bearish Engulfing on sideways/ranging market-Price-action on a whole**  
  
  
What timeframes:  
H1  
H4  
D1 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Bearish engulfing.png
Size: 4 KB](/attachment/image/2680166/thumbnail?d=1518789270)](/attachment/image/2680166?d=1518789270)   
[![Click to Enlarge

Name: Bullish engulf.png
Size: 4 KB](/attachment/image/2680168/thumbnail?d=1518789275)](/attachment/image/2680168?d=1518789275)   

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#245](/thread/post/10788860#post10788860 "Post Permalink")

  * Feb 18, 2018 12:14am  Feb 18, 2018 12:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting PrinceJ58](/thread/post/10786391#post10786391 "View Quoted Post")
> 
> Disliked
> 
> {quote} Excellent 1. Pin Bar on ranging/sideways-So the ones that stick out, you don't trade those ones 2. Hammer, specially with bullish body on sideways/ranging market. -So you ignore the bearish colors even if it 3. Shooting Star, Gravestone Doji, specially with bearish body and below resistance-Goodstuff 4. Bullish/Bearish Engulfing on sideways/ranging market-Price-action on a whole What timeframes: H1 H4 D1 {image} {image}
> 
> Ignored

I trade daily, weekly and 4hr. I use the longer time frame like the weekly to see the long term trend. Then get in using the daily and 4hr. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#246](/thread/post/10791071#post10791071 "Post Permalink")

  * Feb 19, 2018 9:44am  Feb 19, 2018 9:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting 9jatrader](/thread/post/10788860#post10788860 "View Quoted Post")
> 
> Disliked
> 
> {quote} I trade daily, weekly and 4hr. I use the longer time frame like the weekly to see the long term trend. Then get in using the daily and 4hr.
> 
> Ignored

Thanks for responding. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#247](/thread/post/10791848#post10791848 "Post Permalink")

  * Feb 19, 2018 5:48pm  Feb 19, 2018 5:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting PrinceJ58](/thread/post/10791071#post10791071 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks for responding.
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#248](/thread/post/10792744#post10792744 "Post Permalink")

  * Edited Feb 20, 2018 1:36am  Feb 19, 2018 10:48pm | Edited Feb 20, 2018 1:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar544022_5.gif) pipsy7](pipsy7)

  * | Membership Revoked  | Joined Jan 2017 | [1,824 Posts](/search?do=process&provider=Member&searchuser=544022)

u still dont know = demo accts. are Rigged by d dealers aka brokers , to reel in **boneheads** !  
  
\- this post will most likely get me banned by mr.twee lol cuz this site is 98% funded by d dealers ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)  
soooo many dealers cuz soooo many boneheads , thats fine with me = more _**$$$**_ in d loser's_pool 4sure 

da n0o0b + $hit_Disturber ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#249](/thread/post/10794768#post10794768 "Post Permalink")

  * Edited 11:29am  Feb 20, 2018 10:21am | Edited 11:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

NZDUSD Triggered 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: NZDUSD.proDaily pinbar.png
Size: 63 KB](/attachment/image/2683542/thumbnail?d=1519093737)](/attachment/image/2683542?d=1519093737)   

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#250](/thread/post/10794847#post10794847 "Post Permalink")

  * Feb 20, 2018 11:02am  Feb 20, 2018 11:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting ebeckers](/thread/post/10739534#post10739534 "View Quoted Post")
> 
> Disliked
> 
> {quote} yeah i know all these patterns and sometimes its hard to tell if a candle is a pinbar, a doji , a hanging man, shooting star or ... But in my opinion its totally irrelevant if its a pinbar or for example a hanging man. What is relevant is that the price action touched a major S&R level and shows a strong rejection on that level. Like it says ok.. here's the line, we are NOT going to cross it. That reaction may result in one of the various candle stick patterns. My idea is that the ea recognises the fact that we have a strong rejection from...
> 
> Ignored

As a follow up to this i was reading a similar thread which was suggesting that for eg. Say one was using h4 chart different brokers may display different closed bar's depend on their gmt chart differences... or where they receive their price feed data from. Etc etc. So i am wondering if different brokers may experience different closes.  
  
I do note the support and resistance info you mentioned. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#251](/thread/post/10794850#post10794850 "Post Permalink")

  * Feb 20, 2018 11:05am  Feb 20, 2018 11:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting krismitt](/thread/post/10781632#post10781632 "View Quoted Post")
> 
> Disliked
> 
> {quote} I'm not loving any of these. Anyone keen on any of them?. {image} Regards.
> 
> Ignored

Your market watchlist has duplicated pairs hence the reason for so many signals appearing on the E. A. Dashboard Window. You would have to remove them to have a true reflection. Yet you observe those that highlight sell and buy.  
  

> [Quoting 9jatrader](/thread/post/10785269#post10785269 "View Quoted Post")
> 
> Disliked
> 
> {quote} You're correct, no successful signal. That's the reason we need to keep the risk so low, however strong the setup might be. My trades are based on 1. Pin Bar on ranging/sideways 2. Hammer, specially with bullish body on sideways/ranging market. 3. Shooting Star, Gravestone Doji, specially with bearish body and below resistance 4. Bullish/Bearish Engulfing on sideways/ranging market
> 
> Ignored

You basically have focused on continuation version or usage of these candle patterns with the aim of going as long as the trend allows you to before retracements or and form of complete  
reversals. Am I right? 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#252](/thread/post/10794861#post10794861 "Post Permalink")

  * Feb 20, 2018 11:11am  Feb 20, 2018 11:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting mrdfx](/thread/post/10781994#post10781994 "View Quoted Post")
> 
> Disliked
> 
> Looks like things have woken up today and going well so far. ![](https://resources.faireconomy.media/images/emojis/64/1f4aa.png?v=15.1) {image}
> 
> Ignored

They triggered nicely, how did they turn out in terms of Risk versus reward?  
  

> [Quoting happytrade38](/thread/post/10761303#post10761303 "View Quoted Post")
> 
> Disliked
> 
> Hi ebeckers, is the pinbar shown in dashboard display for all pairs I put in? Or pinbar at S&R level (which I don't think so).
> 
> Ignored

If he did not answer you, I believe there is an input section for the pairs of choice, just click it to see what is in there and add what you want. It should work on other tradable charts as long as they have a valid signal. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#253](/thread/post/10794877#post10794877 "Post Permalink")

  * Feb 20, 2018 11:21am  Feb 20, 2018 11:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

It would be good if those trading this live or demo share the experience with system as an E.A. or as a means of alerting one to a high probability setup that may bring positive pips. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#254](/thread/post/10794889#post10794889 "Post Permalink")

  * Feb 20, 2018 11:29am  Feb 20, 2018 11:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

Did USDJPY show up yesterday...anyone with screenshots...  
The system uses weekly settings though... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: USDJPY.proDaily pinbar.png
Size: 57 KB](/attachment/image/2683545/thumbnail?d=1519093791)](/attachment/image/2683545?d=1519093791)   

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#255](/thread/post/10802846#post10802846 "Post Permalink")

  * Feb 22, 2018 8:16am  Feb 22, 2018 8:16am 

  * [ Monty13](monty13)

  * | Joined Aug 2009  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=113946)

This is the second week I haven't had any signal yet.  
Has any one has any trade signals. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: D1.png
Size: 106 KB](/attachment/image/2686893/thumbnail?d=1519254991)](/attachment/image/2686893?d=1519254991)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#256](/thread/post/10803626#post10803626 "Post Permalink")

  * Feb 22, 2018 3:22pm  Feb 22, 2018 3:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting Monty13](/thread/post/10802846#post10802846 "View Quoted Post")
> 
> Disliked
> 
> This is the second week I haven't had any signal yet. Has any one has any trade signals. {image}
> 
> Ignored

Some you have to just take manually. Look on eurjpy...Cadjpy. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#257](/thread/post/10806648#post10806648 "Post Permalink")

  * Feb 23, 2018 3:43am  Feb 23, 2018 3:43am 

  * [ Monty13](monty13)

  * | Joined Aug 2009  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=113946)

> [Quoting PrinceJ58](/thread/post/10803626#post10803626 "View Quoted Post")
> 
> Disliked
> 
> {quote} Some you have to just take manually. Look on eurjpy...Cadjpy.
> 
> Ignored

PrinceJ58.  
  
Thanks for the in put.  
  
But I'm just wondering despite the pinbars are forming on D1 ie e/j and c/j. the Pinbar bot would not send alert or execute the trades.  
I hope ebeckers would enlighten us with his thoughts. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#258](/thread/post/10807077#post10807077 "Post Permalink")

  * Feb 23, 2018 7:07am  Feb 23, 2018 7:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting Monty13](/thread/post/10806648#post10806648 "View Quoted Post")
> 
> Disliked
> 
> {quote} PrinceJ58. Thanks for the in put. But I'm just wondering despite the pinbars are forming on D1 ie e/j and c/j. the Pinbar bot would not send alert or execute the trades. I hope ebeckers would enlighten us with his thoughts.
> 
> Ignored

I guess he will..., should all conditions not be met in the algorithm whether it be spread, news etc then it will not issue a signal or a trade, however it may very well work out in manual trading. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#259](/thread/post/10812134#post10812134 "Post Permalink")

  * Feb 24, 2018 10:55pm  Feb 24, 2018 10:55pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

> [Quoting PrinceJ58](/thread/post/10794861#post10794861 "View Quoted Post")
> 
> Disliked
> 
> {quote} They triggered nicely, how did they turn out in terms of Risk versus reward? {quote} If he did not answer you, I believe there is an input section for the pairs of choice, just click it to see what is in there and add what you want. It should work on other tradable charts as long as they have a valid signal.
> 
> Ignored

Yes, i did put in all relevant pairs I want to see, and also confirm there is a pin bar on the selected pair. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#260](/thread/post/10812214#post10812214 "Post Permalink")

  * Feb 24, 2018 11:37pm  Feb 24, 2018 11:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting happytrade38](/thread/post/10812134#post10812134 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes, i did put in all relevant pairs I want to see, and also confirm there is a pin bar on the selected pair.
> 
> Ignored

So far the system was really designed for signals, however those signals maybe automated to trigger a directional trade. Good setups come and do not get triggered and at other times it will be executed. Otherwise its best to just use your discretion at the moment.  
  
Ebeckers tested the robot and it gave positive results for the period. I don't remember if it was the first version or present one. He also said it was created for his personal alerts which he took on a manual basis. The manual basis at the moment is likely to yield more than the automation.  
  
I suggest that until there is a solution for the challenge faced, use the system as an on screen signal system. It is one of the few free system for this method that filters news, support and resistance, swing high and lows and directional based pinbars that the colours have to match the direction. This is an excellent system and if anyome knows of a way to make it better, the thread is open for suggestions with use of clear examples. Test and test your suggestions, share your thoughts and lets work on this edge based system.   
  
Remember the alerts show up at the end of the New York sessions. So where ever a reader is located they can check the chart once for the signals and chill after, if there are none then it did not reach the coded requirements. It's possible there could be a bug or a slight adjustment and the system behaves flawless.   
Nb. The system is open to be modified he made it available which is great. Should anyone be able to assist and not deviate from the original concept then I don't think he would mind. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#261](/thread/post/10818487#post10818487 "Post Permalink")

  * Feb 27, 2018 8:50am  Feb 27, 2018 8:50am 

  * [ Monty13](monty13)

  * | Joined Aug 2009  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=113946)

The pinbar EA opened a long E/J trade. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Pinbar.png
Size: 119 KB](/attachment/image/2693224/thumbnail?d=1519689013)](/attachment/image/2693224?d=1519689013)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#262](/thread/post/10818629#post10818629 "Post Permalink")

  * Feb 27, 2018 11:00am  Feb 27, 2018 11:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting Monty13](/thread/post/10818487#post10818487 "View Quoted Post")
> 
> Disliked
> 
> The pinbar EA opened a long E/J trade. {image}
> 
> Ignored

Seems like you in the game! 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#263](/thread/post/10823860#post10823860 "Post Permalink")

  * Feb 28, 2018 6:08pm  Feb 28, 2018 6:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

signal found... 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 22 KB](/attachment/image/2695522/thumbnail?d=1519807284)](/attachment/image/2695522?d=1519807284)   
[![Click to Enlarge

Name: Screenshot2.png
Size: 22 KB](/attachment/image/2695565/thumbnail?d=1519808633)](/attachment/image/2695565?d=1519808633)   
[![Click to Enlarge

Name: Screenshot3.png
Size: 24 KB](/attachment/image/2695568/thumbnail?d=1519808892)](/attachment/image/2695568?d=1519808892)   

No one wants to be defeated~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#264](/thread/post/10826076#post10826076 "Post Permalink")

  * Mar 1, 2018 2:42am  Mar 1, 2018 2:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting jonirrenicus](/thread/post/10823860#post10823860 "View Quoted Post")
> 
> Disliked
> 
> signal found... {image} {image} {image}
> 
> Ignored

This is very intersting...Is this based on pinbar? 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#265](/thread/post/10826981#post10826981 "Post Permalink")

  * Mar 1, 2018 8:56am  Mar 1, 2018 8:56am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

Pinbar....what do you think?  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Pinbar.png
Size: 42 KB](/attachment/image/2696919/thumbnail?d=1519862149)](/attachment/image/2696919?d=1519862149)   

  
Trade well. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#266](/thread/post/10827487#post10827487 "Post Permalink")

  * Mar 1, 2018 2:53pm  Mar 1, 2018 2:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

> [Quoting PrinceJ58](/thread/post/10826076#post10826076 "View Quoted Post")
> 
> Disliked
> 
> {quote} This is very intersting...Is this based on pinbar?
> 
> Ignored

Hi my friend,  
  
Pinbar is one of the most popular reverse pattern....  
  
but if you switch to smaller Timeframe (H1 is the best, because all brokers share same H1 candle)...  
  
you will find all reverse pattrens have same N structures.  
  
all detials(entry,TP,SL) are clear on following pictures: 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 24 KB](/attachment/image/2697115/thumbnail?d=1519883488)](/attachment/image/2697115?d=1519883488)   
[![Click to Enlarge

Name: Screenshot2.png
Size: 24 KB](/attachment/image/2697116/thumbnail?d=1519883500)](/attachment/image/2697116?d=1519883500)   
[![Click to Enlarge

Name: Screenshot3.png
Size: 36 KB](/attachment/image/2697119/thumbnail?d=1519883514)](/attachment/image/2697119?d=1519883514)   

No one wants to be defeated~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#267](/thread/post/10828547#post10828547 "Post Permalink")

  * Mar 1, 2018 8:20pm  Mar 1, 2018 8:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting krismitt](/thread/post/10826981#post10826981 "View Quoted Post")
> 
> Disliked
> 
> Pinbar....what do you think? {image} Trade well.
> 
> Ignored

Its in a good Place, but you never know until your in... 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#268](/thread/post/10828587#post10828587 "Post Permalink")

  * Mar 1, 2018 8:29pm  Mar 1, 2018 8:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting jonirrenicus](/thread/post/10827487#post10827487 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi my friend, Pinbar is one of the most popular reverse pattern.... but if you switch to smaller Timeframe (H1 is the best, because all brokers share same H1 candle)... you will find all reverse pattrens have same N structures. all detials(entry,TP,SL) are clear on following pictures: {image} {image} {image}
> 
> Ignored

Yes it all boils down to perspective...Good Stuff... 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#269](/thread/post/10831541#post10831541 "Post Permalink")

  * Mar 2, 2018 7:44am  Mar 2, 2018 7:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

Usdjpy and gbpusd....thoughts 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#270](/thread/post/10831652#post10831652 "Post Permalink")

  * Mar 2, 2018 8:46am  Mar 2, 2018 8:46am 

  * [ lctrader11](lctrader11)

  * | Joined Mar 2016  | Status: Trader | [297 Posts](/search?do=process&provider=Member&searchuser=454494)

> [Quoting PrinceJ58](/thread/post/10831541#post10831541 "View Quoted Post")
> 
> Disliked
> 
> Usdjpy and gbpusd....thoughts
> 
> Ignored

Put both on the watch list, but I think it's too early for a reversal. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#271](/thread/post/10831697#post10831697 "Post Permalink")

  * Mar 2, 2018 9:23am  Mar 2, 2018 9:23am 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

> [Quoting PrinceJ58](/thread/post/10831541#post10831541 "View Quoted Post")
> 
> Disliked
> 
> Usdjpy and gbpusd....thoughts
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 71 KB](/attachment/image/2698953/thumbnail?d=1519950192)](/attachment/image/2698953?d=1519950192)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#272](/thread/post/10832027#post10832027 "Post Permalink")

  * Mar 2, 2018 1:03pm  Mar 2, 2018 1:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

> [Quoting PrinceJ58](/thread/post/10828587#post10828587 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes it all boils down to perspective...Good Stuff...
> 
> Ignored

Tools + imagination + Time = all you needed for trading  
  
GJ and EJ break 3 Support lvs on D1, trade cancelled....  
  
EA still holding position 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 15 KB](/attachment/image/2699072/thumbnail?d=1519963022)](/attachment/image/2699072?d=1519963022)   
[![Click to Enlarge

Name: Screenshot2.png
Size: 37 KB](/attachment/image/2699078/thumbnail?d=1519963407)](/attachment/image/2699078?d=1519963407)   

No one wants to be defeated~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#273](/thread/post/10832165#post10832165 "Post Permalink")

  * Mar 2, 2018 2:57pm  Mar 2, 2018 2:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

more signal 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 24 KB](/attachment/image/2699139/thumbnail?d=1519969680)](/attachment/image/2699139?d=1519969680)   
[![Click to Enlarge

Name: Screenshot2.png
Size: 25 KB](/attachment/image/2699144/thumbnail?d=1519970247)](/attachment/image/2699144?d=1519970247)   

No one wants to be defeated~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#274](/thread/post/10832288#post10832288 "Post Permalink")

  * Mar 2, 2018 3:58pm  Mar 2, 2018 3:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting juraia](/thread/post/10831697#post10831697 "View Quoted Post")
> 
> Disliked
> 
> {quote} {image}
> 
> Ignored

The challenge i have with fibs, everyone has a different way of drawing it. The points are subjective to perspective... and yet even if drawn incorrectly people still make money. So as long as it works for you no problem. I wont go into that any deeper...can of worms that one. I like your highlighted candlesticks. Good analysist by the way. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#275](/thread/post/10832323#post10832323 "Post Permalink")

  * Mar 2, 2018 4:16pm  Mar 2, 2018 4:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

So can someone post the signals received from the e.a.  
  
Judging from my mobile usdjpy, usdchf,audjpy moving quite good. Gbpusd struggling at the moment, will see what London and New york will do for that. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#276](/thread/post/10832600#post10832600 "Post Permalink")

  * Mar 2, 2018 5:36pm  Mar 2, 2018 5:36pm 

  * [ Tlx](tlx)

  * | Joined Feb 2016  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=450864)

thanks for sharing.   
I get "weekly SR" on mt4, but I don't get the "trend reversal EA"part on my mt4, is there something wrong? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 105 KB](/attachment/image/2699329/thumbnail?d=1519979716)](/attachment/image/2699329?d=1519979716)   

TLX

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#277](/thread/post/10832744#post10832744 "Post Permalink")

  * Mar 2, 2018 6:16pm  Mar 2, 2018 6:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting PrinceJ58](/thread/post/10794850#post10794850 "View Quoted Post")
> 
> Disliked
> 
> {quote} Your market watchlist has duplicated pairs hence the reason for so many signals appearing on the E. A. Dashboard Window. You would have to remove them to have a true reflection. Yet you observe those that highlight sell and buy. {quote} You basically have focused on continuation version or usage of these candle patterns with the aim of going as long as the trend allows you to before retracements or and form of complete reversals. Am I right?
> 
> Ignored

**They can be used on both reversal and continuation setups**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#278](/thread/post/10833387#post10833387 "Post Permalink")

  * Mar 2, 2018 8:56pm  Mar 2, 2018 8:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting 9jatrader](/thread/post/10832744#post10832744 "View Quoted Post")
> 
> Disliked
> 
> {quote} They can be used on both reversal and continuation setups
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f463.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f463.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f463.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f463.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f463.png?v=15.1) Leave heavy foot prints my friend. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#279](/thread/post/10833400#post10833400 "Post Permalink")

  * Mar 2, 2018 9:01pm  Mar 2, 2018 9:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting Tlx](/thread/post/10832600#post10832600 "View Quoted Post")
> 
> Disliked
> 
> thanks for sharing. I get "weekly SR" on mt4, but I don't get the "trend reversal EA"part on my mt4, is there something wrong? {image}
> 
> Ignored

Ensure that you placed it in the expert folder refresh your mt4 and then look in the navigator panel for the expert advisor if you use the template its possible that the e.a. might ot be attached. So resave it when you attach it with the preferred settings of your choice. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#280](/thread/post/10835953#post10835953 "Post Permalink")

  * Mar 3, 2018 4:45pm  Mar 3, 2018 4:45pm 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

> [Quoting krismitt](/thread/post/10826981#post10826981 "View Quoted Post")
> 
> Disliked
> 
> Pinbar....what do you think? {image} Trade well.
> 
> Ignored

**Pinbars.**  
  
I took this Trade and it was a candy. However, I was unsure about the veracity of the Pinbar so I went in with some uncertainty. I have done some reading since then; sharing some excellent resources that are freely available here.  
  
Krismitt.  
  

Attached File(s)

![File Type: pdf](https://assets.faireconomy.media/images/attach/pdf.gif) [Pin bars-introduction.pdf](/attachment/file/2700840?d=1520062658) 175 KB | 751 downloads 

  

Attached File(s)

![File Type: pdf](https://assets.faireconomy.media/images/attach/pdf.gif) [Pin bars-advanced.pdf](/attachment/file/2700839?d=1520062656) 113 KB | 729 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#281](/thread/post/10838638#post10838638 "Post Permalink")

  * Mar 5, 2018 1:37pm  Mar 5, 2018 1:37pm 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

Not from The Pinbar Trader EA, but a nice Weekly Pinbar on USDCHF  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Weekly Pinbar.jpg
Size: 104 KB](/attachment/image/2702138/thumbnail?d=1520224572)](/attachment/image/2702138?d=1520224572)   

  
  
Cheers. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#282](/thread/post/10838648#post10838648 "Post Permalink")

  * Mar 5, 2018 1:41pm  Mar 5, 2018 1:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar440253_2.gif) badeel](badeel)

  * Joined Dec 2015 | Status: Trader | [257 Posts](/search?do=process&provider=Member&searchuser=440253)

hi  
can someone share Dash SDTR pin??   
thank 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#283](/thread/post/10842218#post10842218 "Post Permalink")

  * Mar 6, 2018 8:51am  Mar 6, 2018 8:51am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

AUDUSD.  
  
Long Trade.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 06.03.18 - AUDUSD Pinbar Trade.jpg
Size: 130 KB](/attachment/image/2703689/thumbnail?d=1520293736)](/attachment/image/2703689?d=1520293736)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: AUDUSD.jpg
Size: 50 KB](/attachment/image/2703697/thumbnail?d=1520293830)](/attachment/image/2703697?d=1520293830)   

  
Cheerz. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#284](/thread/post/10842331#post10842331 "Post Permalink")

  * Mar 6, 2018 9:55am  Mar 6, 2018 9:55am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

Pinbar EA  
  
I have enabled the 50% retracement rule but the EA is still taking market orders.  
Anyone else experiencing this?.  

Attached Image

![](/attachment/image/2703772?d=1520297585)

  
Cheerz. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#285](/thread/post/10850467#post10850467 "Post Permalink")

  * Mar 8, 2018 8:23am  Mar 8, 2018 8:23am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

AUDUSD PINBAR.  
  
Still in (Demo Account)  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: AUDUSD_Trade.png
Size: 45 KB](/attachment/image/2707092/thumbnail?d=1520464964)](/attachment/image/2707092?d=1520464964)   

  
Cheerz 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#286](/thread/post/10850492#post10850492 "Post Permalink")

  * Mar 8, 2018 8:29am  Mar 8, 2018 8:29am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

AUDNZD  
  
Got this signal today and EA opened Trade. Bad location. I will close trade.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: AUDNZD.png
Size: 42 KB](/attachment/image/2707100/thumbnail?d=1520465256)](/attachment/image/2707100?d=1520465256)   

  
Not sure why but EA not doing the 50% retracement and is doing only market entries - even with the 50% enabled.  
Cheerz. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#287](/thread/post/10850498#post10850498 "Post Permalink")

  * Mar 8, 2018 8:33am  Mar 8, 2018 8:33am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

**Open Trades**  
Disclaimer: Please note that this is a demo account and I am therefore trading the EA in "experimental mode".  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Open_Trades.png
Size: 19 KB](/attachment/image/2707103/thumbnail?d=1520465565)](/attachment/image/2707103?d=1520465565)   

  
Cheerz. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#288](/thread/post/10850504#post10850504 "Post Permalink")

  * Mar 8, 2018 8:36am  Mar 8, 2018 8:36am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

**Pinbar Trader EA.**  
  
I like this EA. I have a habit of over-trading and this will keep me in check ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Two or three good trades per week and less headaches.  
  
Cheerz. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#289](/thread/post/10850874#post10850874 "Post Permalink")

  * Mar 8, 2018 2:03pm  Mar 8, 2018 2:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar27846_5.gif) Nut](nut)

  * Joined Dec 2006 | Status: Trader | [410 Posts](/search?do=process&provider=Member&searchuser=27846)

Hi, have just come across this thread and downloaded and installed the EA however it will not load onto the template. The template itself loads fine as does the SupportResistance indicator(a fantastic indy in itself). I must be doing someting wrong but am not sure what, I have followed all of the instructions and all other EA's work fine. Any help offered much appreciated. I am talking about pinbar trader eav1.20  
  
Thanks in advance  
Nut 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#290](/thread/post/10850898#post10850898 "Post Permalink")

  * Mar 8, 2018 2:12pm  Mar 8, 2018 2:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar27846_5.gif) Nut](nut)

  * Joined Dec 2006 | Status: Trader | [410 Posts](/search?do=process&provider=Member&searchuser=27846)

> [Quoting Nut](/thread/post/10850874#post10850874 "View Quoted Post")
> 
> Disliked
> 
> Hi, have just come across this thread and downloaded and installed the EA however it will not load onto the template. The template itself loads fine as does the SupportResistance indicator(a fantastic indy in itself). I must be doing someting wrong but am not sure what, I have followed all of the instructions and all other EA's work fine. Any help offered much appreciated. I am talking about pinbar trader eav1.20 Thanks in advance Nut
> 
> Ignored

Typical I had no sooner posted this when my error became apparent and we are now up and running.  
Thanks to all  
Nut 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#291](/thread/post/10850972#post10850972 "Post Permalink")

  * Mar 8, 2018 2:58pm  Mar 8, 2018 2:58pm 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

> [Quoting Nut](/thread/post/10850898#post10850898 "View Quoted Post")
> 
> Disliked
> 
> {quote} Typical I had no sooner posted this when my error became apparent and we are now up and running. Thanks to all Nut
> 
> Ignored

Sweet.  
  
Best to you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#292](/thread/post/10851625#post10851625 "Post Permalink")

  * Mar 8, 2018 6:57pm  Mar 8, 2018 6:57pm 

  * [ kobra101](kobra101)

  * | Joined Jan 2018  | Status: Trader | [63 Posts](/search?do=process&provider=Member&searchuser=642070)

@ebeckers  
  
Thank you very much for sharing this EA !  
  
may i please ask a few questions :  
  
1\. When i try to add some more pairs, the buffer of "Tradepairs" seems to be limited. Any plans possibly to increase the buffer ?  
2\. Sometimes a buy or sell signal appears but goes away after minutes or hour so . Does this mean the signal is no longer valid ?  
3\. Is there is possiblity to have same EA for trading pinbars from DAILY S&R levels ? Does this require big effort or only one part of the code  
needs to be changed. I would really appreicate your comment on this ?

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#293](/thread/post/10853629#post10853629 "Post Permalink")

  * Mar 9, 2018 3:01am  Mar 9, 2018 3:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar626176_1.gif) ebeckers](ebeckers)

  * Joined Nov 2017 | Status: Trader | [376 Posts](/search?do=process&provider=Member&searchuser=626176)

Hi guys  
  
Sorry for the lack of updates. I've been extremely busy with other stuff lately and sadly didn't had much time for forex trading  
but i'm still visiting this thread a couple of times a week and still got some idea's on how to improve the ea :-)  
If you have any questions, just ask me, or pm me 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#294](/thread/post/10854169#post10854169 "Post Permalink")

  * Mar 9, 2018 5:32am  Mar 9, 2018 5:32am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

> [Quoting ebeckers](/thread/post/10853629#post10853629 "View Quoted Post")
> 
> Disliked
> 
> Hi guys Sorry for the lack of updates. I've been extremely busy with other stuff lately and sadly didn't had much time for forex trading but i'm still visiting this thread a couple of times a week and still got some idea's on how to improve the ea :-) If you have any questions, just ask me, or pm me
> 
> Ignored

Nice to have you around Ebeckers ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Here is a question for you:-  
  
[https://www.forexfactory.com/showthr...1#post10842331](https://www.forexfactory.com/showthread.php?p=10842331#post10842331)  
  
Cheerz. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#295](/thread/post/10854439#post10854439 "Post Permalink")

  * Mar 9, 2018 7:37am  Mar 9, 2018 7:37am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

**EURGBP**  
I do not like the position of the Pinbar and the Body is too much.  
Also, the nose is not much of a Pinocchio ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  

Attached Image

![](/attachment/image/2708750?d=1520548365)

  
Can anyone tell how to stop EA from trading the second pair with the subscript?  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Trade.png
Size: 25 KB](/attachment/image/2708751/thumbnail?d=1520548419)](/attachment/image/2708751?d=1520548419)   

  
Note that EA takes Market Order  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 50.jpg
Size: 89 KB](/attachment/image/2708758/thumbnail?d=1520548582)](/attachment/image/2708758?d=1520548582)   

  
Despite 50% retracement enabled.  
  
Cheerz. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#296](/thread/post/10856046#post10856046 "Post Permalink")

  * Mar 9, 2018 8:07pm  Mar 9, 2018 8:07pm 

  * [ rajandaas](rajandaas)

  * | Joined Jun 2011  | Status: Trader | [176 Posts](/search?do=process&provider=Member&searchuser=182339)

> [Quoting ebeckers](/thread/post/10853629#post10853629 "View Quoted Post")
> 
> Disliked
> 
> Hi guys Sorry for the lack of updates. I've been extremely busy with other stuff lately and sadly didn't had much time for forex trading but i'm still visiting this thread a couple of times a week and still got some idea's on how to improve the ea :-) If you have any questions, just ask me, or pm me
> 
> Ignored

  
Hi Ebeckers,  
  
Can this EA be tweaked to take continuation trades. Hopefully you are already working on it.  
  
Have a great weekend. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#297](/thread/post/10857865#post10857865 "Post Permalink")

  * Mar 10, 2018 2:23am  Mar 10, 2018 2:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar429880_1.gif) sam68](sam68)

  * | Commercial User  | Joined Oct 2015 | [246 Posts](/search?do=process&provider=Member&searchuser=429880)

> [Quoting ebeckers](/thread/post/10714321#post10714321 "View Quoted Post")
> 
> Disliked
> 
> === Pinbar Trader EA === Hi everyone, welcome ! I would like to present my latest EA. It implements a very basic, but very effective strategy. trading pinbars from weekly S&R levels Strategy: - we wait for a pinbar to appear which rejects a weekly support & resistance level - When the candle with the pinbar is closed we open a new buy/sell trade on the next candle The Pinbar trader EA The pinbar trader EA implements the strategy and has lots of extra features: it scans multiple currencies. So load the EA on 1 chart and it will scan all major currencies...
> 
> Ignored

Ebeckers , thank you for your contribution , today I got a loud and clear signal on UC , even though it's NFP but classic combination as such is just a piece of gold.  
  
Definitely a great addition to the arsenal! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 27 KB](/attachment/image/2710281/thumbnail?d=1520616117)](/attachment/image/2710281?d=1520616117)   

What goes up will come down...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#298](/thread/post/10857880#post10857880 "Post Permalink")

  * Mar 10, 2018 2:27am  Mar 10, 2018 2:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar429880_1.gif) sam68](sam68)

  * | Commercial User  | Joined Oct 2015 | [246 Posts](/search?do=process&provider=Member&searchuser=429880)

> [Quoting krismitt](/thread/post/10854439#post10854439 "View Quoted Post")
> 
> Disliked
> 
> EURGBP I do not like the position of the Pinbar and the Body is too much. Also, the nose is not much of a Pinocchio ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) {image} Can anyone tell how to stop EA from trading the second pair with the subscript? {image} Note that EA takes Market Order {image} Despite 50% retracement enabled. Cheerz.
> 
> Ignored

Hi  
  
Did you edit the pairs in the settings? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 35 KB](/attachment/image/2710303/thumbnail?d=1520616432)](/attachment/image/2710303?d=1520616432)   

What goes up will come down...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#299](/thread/post/10858092#post10858092 "Post Permalink")

  * Mar 10, 2018 3:34am  Mar 10, 2018 3:34am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

> [Quoting sam68](/thread/post/10857880#post10857880 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Did you edit the pairs in the settings? {image}
> 
> Ignored

I have, but the pairs in the settings do not have the "subscript" that are listed in the Marketwatch Window.  
  
Cheerz. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#300](/thread/post/10858105#post10858105 "Post Permalink")

  * Mar 10, 2018 3:37am  Mar 10, 2018 3:37am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

**EURGBP UPDATE**  
**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Update EURGBP.jpg
Size: 97 KB](/attachment/image/2710426/thumbnail?d=1520620622)](/attachment/image/2710426?d=1520620622)   

**  
Cheerz. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#301](/thread/post/10858174#post10858174 "Post Permalink")

  * Mar 10, 2018 4:08am  Mar 10, 2018 4:08am 

  * [ Monty13](monty13)

  * | Joined Aug 2009  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=113946)

Hi Ebeckers. Thank you for your time and generosity . Would it possible to have both option on trade open with the signal as well as opening another trade if it retrace at %50 .  
  
Also could the pinbar be more specific than any kind of pinbar.  
  
Thank you in advance. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Pinbar.png
Size: 128 KB](/attachment/image/2710473/thumbnail?d=1520622405)](/attachment/image/2710473?d=1520622405)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#302](/thread/post/10858902#post10858902 "Post Permalink")

  * Mar 10, 2018 9:52am  Mar 10, 2018 9:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,577 Posts](/search?do=process&provider=Member&searchuser=185229)

> [Quoting krismitt](/thread/post/10858092#post10858092 "View Quoted Post")
> 
> Disliked
> 
> {quote} I have, but the pairs in the settings do not have the "subscript" that are listed in the Marketwatch Window. Cheerz.
> 
> Ignored

Does you Marketwatch have both regular and "subscript" pairs?  
  
If so, did you try have only the 28 regular pairs there with any "subscript" pairs?  
  
Just an idea, maybe works, I see a lot of EA have the choice to trade Marketwatch pairs, not this one yet.  
  
Also, most EA have the pairs separated by comma or semicolon, this one is just by spacing, not sure why that is. I wonder if it will read those formats?  
  
EURUSD USDJPY GBPUSD USDCHF USDCAD AUDUSD NZDUSD EURCHF EURGBP EURCAD EURAUD EURNZD EURJPY GBPJPY CHFJPY CADJPY AUDJPY NZDJPY GBPCHF GBPAUD GBPCAD GBPNZD AUDCHF AUDCAD AUDNZD CADCHF NZDCHF NZDCAD  
  
AUDCAD,AUDCHF,AUDJPY,AUDNZD,AUDUSD,CADCHF,CADJPY,CHFJPY,EURAUD,EURCAD,EURCHF,EURGBP,EURJPY,EURNZD,EURUSD,GBPAUD,GBPCAD,GBPCHF,GBPJPY,GBPNZD,GBPUSD,NZDCAD,NZDCHF,NZDJPY,NZDUSD,USDCAD,USDCHF,USDJPY  
  
AUDCAD;AUDCHF;AUDJPY;AUDNZD;AUDUSD;CADCHF;CADJPY;CHFJPY;EURAUD;EURCAD;EURCHF;EURGBP;EURJPY;EURNZD;EURUSD;GBPAUD;GBPCAD;GBPCHF;GBPJPY;GBPNZD;GBPUSD;NZDCAD;NZDCHF;NZDJPY;NZDUSD;USDCAD;USDCHF;USDJPY 

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.7%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#303](/thread/post/10858959#post10858959 "Post Permalink")

  * Mar 10, 2018 11:35am  Mar 10, 2018 11:35am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

> [Quoting Erebus](/thread/post/10858902#post10858902 "View Quoted Post")
> 
> Disliked
> 
> {quote} Does you Marketwatch have both regular and "subscript" pairs? If so, did you try have only the 28 regular pairs there with any "subscript" pairs? Just an idea, maybe works, I see a lot of EA have the choice to trade Marketwatch pairs, not this one yet. Also, most EA have the pairs separated by comma or semicolon, this one is just by spacing, not sure why that is. I wonder if it will read those formats? EURUSD USDJPY GBPUSD USDCHF USDCAD AUDUSD NZDUSD EURCHF EURGBP EURCAD EURAUD EURNZD EURJPY GBPJPY CHFJPY CADJPY AUDJPY NZDJPY GBPCHF GBPAUD...
> 
> Ignored

Thanks Erebus.   
  
My Marketwatch has both regular and subscript; pairs in the EA Inputs are without subscript.  
I noticed that with the market now closed I was able to "right click" and "hide" most of the subscript pairs. A couple just will not go..  
I will try adding the commas etc. at market open and see what happens.  
  
Cheerz. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#304](/thread/post/10859085#post10859085 "Post Permalink")

  * Mar 10, 2018 2:09pm  Mar 10, 2018 2:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,577 Posts](/search?do=process&provider=Member&searchuser=185229)

> [Quoting krismitt](/thread/post/10858959#post10858959 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks Erebus. My Marketwatch has both regular and subscript; pairs in the EA Inputs are without subscript. I noticed that with the market now closed I was able to "right click" and "hide" most of the subscript pairs. A couple just will not go.. I will try adding the commas etc. at market open and see what happens. Cheerz.
> 
> Ignored

It's worth a try but you probably won't know for sure until Monday  
  
When a pair or index will not delete from Marketwatch, there might be a chart open with that pair?  
  
Or close and restart, try again, MT4 is very quirky like that ![](https://resources.faireconomy.media/images/emojis/64/1f644.png?v=15.1)

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.7%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#305](/thread/post/10859744#post10859744 "Post Permalink")

  * Mar 11, 2018 2:00am  Mar 11, 2018 2:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar454965_8.gif) 9jatrader](9jatrader)

  * Joined Mar 2016 | Status: Trader | [6,280 Posts](/search?do=process&provider=Member&searchuser=454965)

> [Quoting PrinceJ58](/thread/post/10833387#post10833387 "View Quoted Post")
> 
> Disliked
> 
> {quote} ![](https://resources.faireconomy.media/images/emojis/64/1f463.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f463.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f463.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f463.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f463.png?v=15.1) Leave heavy foot prints my friend.
> 
> Ignored

**Thanks**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#306](/thread/post/10863014#post10863014 "Post Permalink")

  * Edited 9:04pm  Mar 12, 2018 8:47pm | Edited 9:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

How are the traders using the system?  
Anyone on full auto or trading signals manually? 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#307](/thread/post/10877044#post10877044 "Post Permalink")

  * Mar 16, 2018 3:29am  Mar 16, 2018 3:29am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

**AUDJPY**  
  
Traded this one manually from the Pinbar Trader Signal.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Pinbar_Trader.png
Size: 14 KB](/attachment/image/2719870/thumbnail?d=1521138498)](/attachment/image/2719870?d=1521138498)   

  
Cheerz. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#308](/thread/post/10883364#post10883364 "Post Permalink")

  * Mar 18, 2018 9:02pm  Mar 18, 2018 9:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting krismitt](/thread/post/10877044#post10877044 "View Quoted Post")
> 
> Disliked
> 
> AUDJPY Traded this one manually from the Pinbar Trader Signal. {image} Cheerz.
> 
> Ignored

Awesome trade. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#309](/thread/post/10884872#post10884872 "Post Permalink")

  * Mar 19, 2018 3:54pm  Mar 19, 2018 3:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147030_5.gif) jonirrenicus](jonirrenicus)

  * Joined Jul 2010 | Status: Trader | [1,136 Posts](/search?do=process&provider=Member&searchuser=147030)

> [Quoting krismitt](/thread/post/10877044#post10877044 "View Quoted Post")
> 
> Disliked
> 
> AUDJPY Traded this one manually from the Pinbar Trader Signal. {image} Cheerz.
> 
> Ignored

it was a great trade which i missed....lol 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 23 KB](/attachment/image/2723946/thumbnail?d=1521442279)](/attachment/image/2723946?d=1521442279)   

No one wants to be defeated~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#310](/thread/post/10888667#post10888667 "Post Permalink")

  * Mar 20, 2018 3:48pm  Mar 20, 2018 3:48pm 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

AUDJPY signal from Pinbar Trader.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: AUDJPY.png
Size: 15 KB](/attachment/image/2725749/thumbnail?d=1521528502)](/attachment/image/2725749?d=1521528502)   

  
Saw it a bit late and missed the retracement.  
  
Cheerz. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#311](/thread/post/10891936#post10891936 "Post Permalink")

  * Mar 21, 2018 8:30am  Mar 21, 2018 8:30am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

Still in.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: AUDJPY_2.png
Size: 15 KB](/attachment/image/2727184/thumbnail?d=1521588623)](/attachment/image/2727184?d=1521588623)   

  
Cheerz. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#312](/thread/post/10900929#post10900929 "Post Permalink")

  * Mar 23, 2018 3:13pm  Mar 23, 2018 3:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar429880_1.gif) sam68](sam68)

  * | Commercial User  | Joined Oct 2015 | [246 Posts](/search?do=process&provider=Member&searchuser=429880)

> [Quoting krismitt](/thread/post/10891936#post10891936 "View Quoted Post")
> 
> Disliked
> 
> Still in. {image} Cheerz.
> 
> Ignored

it broke that support , with a very bearish candle more to the down side now IMHO 

What goes up will come down...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#313](/thread/post/10903171#post10903171 "Post Permalink")

  * Mar 24, 2018 1:38am  Mar 24, 2018 1:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar469190_3.gif) theChamp](thechamp)

  * | Joined Jun 2016  | Status: Trader | [29 Posts](/search?do=process&provider=Member&searchuser=469190)

adding **Morning star ,evening star & shooting star** to this system will make it more powerful 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#314](/thread/post/10918445#post10918445 "Post Permalink")

  * Mar 29, 2018 6:55am  Mar 29, 2018 6:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar339829_1.gif) chayon](chayon)

  * | Joined Jun 2013  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=339829)

Why everyone stopped?? How about the ea performance now? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#315](/thread/post/10921788#post10921788 "Post Permalink")

  * Mar 30, 2018 5:16am  Mar 30, 2018 5:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar429880_1.gif) sam68](sam68)

  * | Commercial User  | Joined Oct 2015 | [246 Posts](/search?do=process&provider=Member&searchuser=429880)

> [Quoting chayon](/thread/post/10918445#post10918445 "View Quoted Post")
> 
> Disliked
> 
> Why everyone stopped?? How about the ea performance now?
> 
> Ignored

I am not enabling the EA but dashboard is always on , when I see a signal I evaluate and enter a manual trade  
Will post next ones ! 

What goes up will come down...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#316](/thread/post/10921889#post10921889 "Post Permalink")

  * Mar 30, 2018 6:18am  Mar 30, 2018 6:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting sam68](/thread/post/10921788#post10921788 "View Quoted Post")
> 
> Disliked
> 
> {quote} I am not enabling the EA but dashboard is always on , when I see a signal I evaluate and enter a manual trade Will post next ones !
> 
> Ignored

Awesome...do what works, that is exactly what ebeckers do he uses it as an alert system. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#317](/thread/post/10921893#post10921893 "Post Permalink")

  * Mar 30, 2018 6:22am  Mar 30, 2018 6:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting chayon](/thread/post/10918445#post10918445 "View Quoted Post")
> 
> Disliked
> 
> Why everyone stopped?? How about the ea performance now?
> 
> Ignored

Usually when a system based thread has achieved what it was created for, it is expected that the developer and integral participants exit the building and continue using the too or systeml.  
There is really nothing to write after that. Most times its just issues and updates that will keep most threads going unless it is a discussion based thread. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#318](/thread/post/10921901#post10921901 "Post Permalink")

  * Mar 30, 2018 6:26am  Mar 30, 2018 6:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting theChamp](/thread/post/10903171#post10903171 "View Quoted Post")
> 
> Disliked
> 
> adding Morning star ,evening star & shooting star to this system will make it more powerful
> 
> Ignored

I believe that was the mission, if you go to his resources web page you will observe his further developments that took place in the quiet gifted space he dwells in, cheers. It would be good to post some examples of your statement so we can observe the same high probability setups you look for. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#319](/thread/post/10922109#post10922109 "Post Permalink")

  * Mar 30, 2018 9:37am  Mar 30, 2018 9:37am 

  * [ zackery](zackery)

  * | Joined Nov 2011  | Status: Trader | [701 Posts](/search?do=process&provider=Member&searchuser=205747)

> [Quoting krismitt](/thread/post/10838638#post10838638 "View Quoted Post")
> 
> Disliked
> 
> Not from The Pinbar Trader EA, but a nice Weekly Pinbar on USDCHF {image} Cheers.
> 
> Ignored

@krismitt:  
I am interested where do got those diamond-types over the PinBar-Candles from?  
An Indi or Script oir drawn by your own?  
thanks for an info.  
Reg.Zack 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#320](/thread/post/10922110#post10922110 "Post Permalink")

  * Mar 30, 2018 9:39am  Mar 30, 2018 9:39am 

  * [ zackery](zackery)

  * | Joined Nov 2011  | Status: Trader | [701 Posts](/search?do=process&provider=Member&searchuser=205747)

> [Quoting ebeckers](/thread/post/10853629#post10853629 "View Quoted Post")
> 
> Disliked
> 
> Hi guys Sorry for the lack of updates. I've been extremely busy with other stuff lately and sadly didn't had much time for forex trading but i'm still visiting this thread a couple of times a week and still got some idea's on how to improve the ea :-) If you have any questions, just ask me, or pm me
> 
> Ignored

@ebeckers :  
very interesting idea.  
Came up with 1 small add...is it possible to show the Monthly and Yearly S/R-lines also.  
would be a huge advantage for this Indi I think.  
thanks for an info.  
Reg.Zack 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#321](/thread/post/10922574#post10922574 "Post Permalink")

  * Mar 30, 2018 4:51pm  Mar 30, 2018 4:51pm 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

> [Quoting zackery](/thread/post/10922109#post10922109 "View Quoted Post")
> 
> Disliked
> 
> {quote} @krismitt: I am interested where do got those diamond-types over the PinBar-Candles from? An Indi or Script oir drawn by your own? thanks for an info. Reg.Zack
> 
> Ignored

Fractals.  
  
Cheerz. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [sFractals.mq4](/attachment/file/2741176?d=1522396309) 7 KB | 663 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#322](/thread/post/10926345#post10926345 "Post Permalink")

  * Apr 2, 2018 7:48am  Apr 2, 2018 7:48am 

  * [ zackery](zackery)

  * | Joined Nov 2011  | Status: Trader | [701 Posts](/search?do=process&provider=Member&searchuser=205747)

> [Quoting ebeckers](/thread/post/10853629#post10853629 "View Quoted Post")
> 
> Disliked
> 
> Hi guys Sorry for the lack of updates. I've been extremely busy with other stuff lately and sadly didn't had much time for forex trading but i'm still visiting this thread a couple of times a week and still got some idea's on how to improve the ea :-) If you have any questions, just ask me, or pm me
> 
> Ignored

@ebeckers:  
please contact me via PM.Thanks.  
Could be interesting for both of us i think.  
Reg.Zack 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#323](/thread/post/10926539#post10926539 "Post Permalink")

  * Apr 2, 2018 10:25am  Apr 2, 2018 10:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

Which one is better... at times only 2 or one will present itself. 

Attached Images

![](/attachment/image/2742965?d=1522632294) ![](/attachment/image/2742968?d=1522632302) ![](/attachment/image/2742969?d=1522632314)

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#324](/thread/post/10927906#post10927906 "Post Permalink")

  * Apr 3, 2018 12:23am  Apr 3, 2018 12:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar610921_14.gif) AngelicaMari](angelicamari)

  * Joined Sep 2017 | Status: Trader | [126 Posts](/search?do=process&provider=Member&searchuser=610921)

I have only seen one update on results of the forward testing after week one by Ebeckers. I am wondering if the results have been as positive since last January or have interest in this EA dwindled. Has anyone had positive results with the EA using it in automatic not manual? I ask only because if nobody shows actual results how can you improve on a great tool like this. Ebeckers does a fantastic job of his coding and it would be a shame to let this thread die off.  
  
Cheers 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#325](/thread/post/10928343#post10928343 "Post Permalink")

  * Apr 3, 2018 2:37am  Apr 3, 2018 2:37am 

  * [ zackery](zackery)

  * | Joined Nov 2011  | Status: Trader | [701 Posts](/search?do=process&provider=Member&searchuser=205747)

> [Quoting krismitt](/thread/post/10922574#post10922574 "View Quoted Post")
> 
> Disliked
> 
> {quote} Fractals. Cheerz. {file}
> 
> Ignored

thanks a lot.  
Reg.Zack 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#326](/thread/post/10943354#post10943354 "Post Permalink")

  * Apr 7, 2018 10:02am  Apr 7, 2018 10:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting AngelicaMari](/thread/post/10927906#post10927906 "View Quoted Post")
> 
> Disliked
> 
> I have only seen one update on results of the forward testing after week one by Ebeckers. I am wondering if the results have been as positive since last January or have interest in this EA dwindled. Has anyone had positive results with the EA using it in automatic not manual? I ask only because if nobody shows actual results how can you improve on a great tool like this. Ebeckers does a fantastic job of his coding and it would be a shame to let this thread die off. Cheers
> 
> Ignored

I agree, it will not die...unless mission accomplish. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#327](/thread/post/10943378#post10943378 "Post Permalink")

  * Apr 7, 2018 10:23am  Apr 7, 2018 10:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar608462_3.gif) T4Trade](t4trade)

  * Joined Sep 2017 | Status: Trend Following,Price Action,Grid | [2,484 Posts](/search?do=process&provider=Member&searchuser=608462)

> [Quoting zackery](/thread/post/10928343#post10928343 "View Quoted Post")
> 
> Disliked
> 
> {quote} thanks a lot. Reg.Zack
> 
> Ignored

this fractals do repaint ,i tried and dump it like zigzag arrows etc,let me know your experince and way of trading with sfractals please. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#328](/thread/post/10943835#post10943835 "Post Permalink")

  * Apr 7, 2018 8:27pm  Apr 7, 2018 8:27pm 

  * [ friday13](friday13)

  * Joined Aug 2015 | Status: Trader | [85 Posts](/search?do=process&provider=Member&searchuser=424557)

> [Quoting T4Trade](/thread/post/10943378#post10943378 "View Quoted Post")
> 
> Disliked
> 
> {quote} this fractals do repaint ,i tried and dump it like zigzag arrows etc,let me know your experince and way of trading with sfractals please.
> 
> Ignored

Fractals always repaint, or actually, they simply appear late because of the way fractals are formed.  
To learn the math behind fractals you can read [here](https://trader.exposed/bill-williams-fractals/).  
The way to trade according to fractals, any sort of fractals is this:  
You always scan 9 bars backwards, and stop your scan on the first fractal you encounter.  
If you're a manual trader - that's easy.  
If you're a programmer, this is the way to do it (more or less):  
  

Inserted Code
    
    
    double fractalUp=0,fractalDn=0;
    i=1;
    while(i<Bars && (fractalUp==0 || fractalDn==0))
    {
       if(fractalUp==0)
          fractalUp=iCustom(NULL,0,"sfractals.ex4",0,i);
       if(fractalDn==0)
          fractalDn=iCustom(NULL,0,"sfractals.ex4",1,i);
       i++;
    }

  
After this code segment, fractalUp and fractalDn will contain the most recent fractal prices it encountered, then you can use any trading strategy you want - stop orders or wait and market order, or anything else. 

[Thunder OM Flex Secondary](friday13#07 "View Trade Explorer") All Time Return: -18.2%

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#329](/thread/post/10944824#post10944824 "Post Permalink")

  * Apr 8, 2018 3:23pm  Apr 8, 2018 3:23pm 

  * [ Megahead](megahead)

  * | Joined Aug 2014  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=379872)

Hello, I was trying to install the EA but for some reason it is all squished. Can someone please help me fix it? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Pinbartrader.jpg
Size: 437 KB](/attachment/image/2751709/thumbnail?d=1523168600)](/attachment/image/2751709?d=1523168600)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#330](/thread/post/10969060#post10969060 "Post Permalink")

  * Apr 16, 2018 10:38pm  Apr 16, 2018 10:38pm 

  * [ Monty13](monty13)

  * | Joined Aug 2009  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=113946)

Is this forum dead.??????????????????????????????????????????????????????????????????? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#331](/thread/post/10970495#post10970495 "Post Permalink")

  * Apr 17, 2018 6:44am  Apr 17, 2018 6:44am 

  * [ friday13](friday13)

  * Joined Aug 2015 | Status: Trader | [85 Posts](/search?do=process&provider=Member&searchuser=424557)

> [Quoting Monty13](/thread/post/10969060#post10969060 "View Quoted Post")
> 
> Disliked
> 
> Is this forum dead.???????????????????????????????????????????????????????????????????
> 
> Ignored

If you keep spamming, yes it will surely die. 

[Thunder OM Flex Secondary](friday13#07 "View Trade Explorer") All Time Return: -18.2%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#332](/thread/post/10974912#post10974912 "Post Permalink")

  * Apr 18, 2018 3:16pm  Apr 18, 2018 3:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar392811_4.gif) fleurdelys](fleurdelys)

  * Joined Dec 2014 | Status: Trader | [246 Posts](/search?do=process&provider=Member&searchuser=392811)

Hello  
After thousands of hours spent on my graphs, I apply a similar method since early 2017  
I expect a pinbar when it is outside the 70-30 area of the RSI 14.  
I open 50% of the wick for a better ratio.  
I apply to TF> H1  
  
I have great ratios and excellent signals!  
Often there is an appointment at this place with institutions..  
  
That's why I'm curious with this similar method. I wanted to try to backtester this EA, but I'm full of error messages. Is this normal?  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Journal.jpg
Size: 140 KB](/attachment/image/2765170/thumbnail?d=1524032180)](/attachment/image/2765170?d=1524032180)   

  
  
Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#333](/thread/post/10977890#post10977890 "Post Permalink")

  * Apr 19, 2018 4:19am  Apr 19, 2018 4:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar339829_1.gif) chayon](chayon)

  * | Joined Jun 2013  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=339829)

> [Quoting sam68](/thread/post/10921788#post10921788 "View Quoted Post")
> 
> Disliked
> 
> {quote} I am not enabling the EA but dashboard is always on , when I see a signal I evaluate and enter a manual trade Will post next ones !
> 
> Ignored

Good to know...post some result then![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#334](/thread/post/10984930#post10984930 "Post Permalink")

  * Apr 21, 2018 1:53am  Apr 21, 2018 1:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar429880_1.gif) sam68](sam68)

  * | Commercial User  | Joined Oct 2015 | [246 Posts](/search?do=process&provider=Member&searchuser=429880)

> [Quoting chayon](/thread/post/10977890#post10977890 "View Quoted Post")
> 
> Disliked
> 
> {quote} Good to know...post some result then![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

Ok , here is a heads up for GA, pinbar @ weekly S/R level ON THU  
Fri is retesting & now waiting to see a good PA on smaller frames next week in order to pull the trigger ... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 16 KB](/attachment/image/2769439/thumbnail?d=1524243131)](/attachment/image/2769439?d=1524243131)   

What goes up will come down...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#335](/thread/post/11005499#post11005499 "Post Permalink")

  * Apr 27, 2018 7:16pm  Apr 27, 2018 7:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar429880_1.gif) sam68](sam68)

  * | Commercial User  | Joined Oct 2015 | [246 Posts](/search?do=process&provider=Member&searchuser=429880)

> [Quoting sam68](/thread/post/10984930#post10984930 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ok , here is a heads up for GA, pinbar @ weekly S/R level ON THU Fri is retesting & now waiting to see a good PA on smaller frames next week in order to pull the trigger ... {image}
> 
> Ignored

Was out all day as i am not a big fan of trading on Friday to see this ...  
big fat bearish candle , lets see if it will take out previous low so we sell comfortably.  
Have a good weekend everybody! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 15 KB](/attachment/image/2778669/thumbnail?d=1524824123)](/attachment/image/2778669?d=1524824123)   

What goes up will come down...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#336](/thread/post/11017613#post11017613 "Post Permalink")

  * May 2, 2018 12:56pm  May 2, 2018 12:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar429880_1.gif) sam68](sam68)

  * | Commercial User  | Joined Oct 2015 | [246 Posts](/search?do=process&provider=Member&searchuser=429880)

> [Quoting sam68](/thread/post/11005499#post11005499 "View Quoted Post")
> 
> Disliked
> 
> {quote} Was out all day as i am not a big fan of trading on Friday to see this ... big fat bearish candle , lets see if it will take out previous low so we sell comfortably. Have a good weekend everybody! {image}
> 
> Ignored

So after carefully listening to Mr. Price , I decide to go short on GA after previous lows were taken.  
Target is next daily level , and stop is the high of 34EMA/ coinciding with previous S/R level  
Let's see how it plays out in this game of patience... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 14 KB](/attachment/image/2784123/thumbnail?d=1525233369)](/attachment/image/2784123?d=1525233369)   

What goes up will come down...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#337](/thread/post/11017787#post11017787 "Post Permalink")

  * May 2, 2018 3:31pm  May 2, 2018 3:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar429880_1.gif) sam68](sam68)

  * | Commercial User  | Joined Oct 2015 | [246 Posts](/search?do=process&provider=Member&searchuser=429880)

> [Quoting sam68](/thread/post/11017613#post11017613 "View Quoted Post")
> 
> Disliked
> 
> {quote} So after carefully listening to Mr. Price , I decide to go short on GA after previous lows were taken. Target is next daily level , and stop is the high of 34EMA/ coinciding with previous S/R level Let's see how it plays out in this game of patience... {image}
> 
> Ignored

GA obediently fell and now it is a risk free trade with +30 pips already... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 15 KB](/attachment/image/2784225/thumbnail?d=1525242693)](/attachment/image/2784225?d=1525242693)   

What goes up will come down...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#338](/thread/post/11018178#post11018178 "Post Permalink")

  * May 2, 2018 5:24pm  May 2, 2018 5:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar429880_1.gif) sam68](sam68)

  * | Commercial User  | Joined Oct 2015 | [246 Posts](/search?do=process&provider=Member&searchuser=429880)

GA  
Taken out with +5 pips  
Will keep watching for another chance to sell after PA confirms. 

What goes up will come down...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#339](/thread/post/11094832#post11094832 "Post Permalink")

  * May 24, 2018 10:00pm  May 24, 2018 10:00pm 

  * [ kobra101](kobra101)

  * | Joined Jan 2018  | Status: Trader | [63 Posts](/search?do=process&provider=Member&searchuser=642070)

@ebeckers:  
  
Many Thanks for sharing your experience !  
I know you are quite busy..  
  
Once you find some time, it would be very much appreciated if there would be a possibility to:  
  
\- add an additional choice on top of Use50PercentRetracementEntry, to set a pending order (buy stop) on top of bullish pinbar or (sell stop) at the bottom of bearish pinbar.  
  
\- Also if there would be a possibility to add a field where one could add additional pip on top or bottom of the pinbar.  
  
Thank you very much for your time and support. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#340](/thread/post/11164358#post11164358 "Post Permalink")

  * Jun 14, 2018 6:50am  Jun 14, 2018 6:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar687444_5.gif) zeeftrader](zeeftrader)

  * | Joined Jun 2018  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=687444)

> [Quoting ebeckers](/thread/post/10714321#post10714321 "View Quoted Post")
> 
> Disliked
> 
> === Pinbar Trader EA === Hi everyone, welcome ! I would like to present my latest EA. It implements a very basic, but very effective strategy. trading pinbars from weekly S&R levels Strategy: - we wait for a pinbar to appear which rejects a weekly support & resistance level - When the candle with the pinbar is closed we open a new buy/sell trade on the next candle The Pinbar trader EA The pinbar trader EA implements the strategy and has lots of extra features: it scans multiple currencies. So load the EA on 1 chart and it will scan all major currencies...
> 
> Ignored

Hello ebeckers,  
  
Where can I get hold of your Dashboard. Couldn't find the download link. It looks great and I wish to have it. Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#341](/thread/post/11240895#post11240895 "Post Permalink")

  * Jul 9, 2018 6:32am  Jul 9, 2018 6:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting ebeckers](/thread/post/10724745#post10724745 "View Quoted Post")
> 
> Disliked
> 
> EA opened GBPCHF last night.. So far so good + 17pips {image}
> 
> Ignored

This indicator looks pretty nice... 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#342](/thread/post/11240939#post11240939 "Post Permalink")

  * Jul 9, 2018 6:49am  Jul 9, 2018 6:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting ebeckers](/thread/post/10714321#post10714321 "View Quoted Post")
> 
> Disliked
> 
> === Pinbar Trader EA === Hi everyone, welcome ! I would like to present my latest EA. It implements a very basic, but very effective strategy. trading pinbars from weekly S&R levels Strategy: - we wait for a pinbar to appear which rejects a weekly support & resistance level - When the candle with the pinbar is closed we open a new buy/sell trade on the next candle The Pinbar trader EA The pinbar trader EA implements the strategy and has lots of extra features: it scans multiple currencies. So load the EA on 1 chart and it will scan all major currencies...
> 
> Ignored

The systems that are slow based on the timeframe traded and have great potential over the long hall, don't receive much attention. It's quite weird, yet I always see this happening and the systems that have quick and more entry frequency in the market are the ones that are always flooded.![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) Good Stuff Ebeckers... 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#343](/thread/post/11270729#post11270729 "Post Permalink")

  * Jul 18, 2018 3:14am  Jul 18, 2018 3:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar687444_5.gif) zeeftrader](zeeftrader)

  * | Joined Jun 2018  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=687444)

> [Quoting zeeftrader](/thread/post/11164358#post11164358 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello ebeckers, Where can I get hold of your Dashboard. Couldn't find the download link. It looks great and I wish to have it. Thanks.
> 
> Ignored

Hello ebeckers,  
I am still waiting for the link to download the Dashboard  
Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#344](/thread/post/11275731#post11275731 "Post Permalink")

  * Edited Jul 20, 2018 4:42am  Jul 19, 2018 8:41am | Edited Jul 20, 2018 4:42am 

  * [ NickIfill](nickifill)

  * | Joined Jun 2018  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=690971)

Hey Paul im curious about your EA youve used for your Supply and Demand Strategy and im wondering if you can possibly share it with, as im trying to use a similar strategy. The EA that duplicates the first order into 10 orders. It would be greatly appreciated. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#345](/thread/post/11541243#post11541243 "Post Permalink")

  * Oct 3, 2018 11:24am  Oct 3, 2018 11:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

@ebeckers I read through this thread once more and it is amazing I know you still around but you keep comments few. Keep well... 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#346](/thread/post/11566346#post11566346 "Post Permalink")

  * Oct 10, 2018 4:53pm  Oct 10, 2018 4:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

Signals still flow...  
**Daily**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: October 10, 2018 22653 AM GMT-0500.png
Size: 210 KB](/attachment/image/3032629/thumbnail?d=1539157888)](/attachment/image/3032629?d=1539157888)   

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#347](/thread/post/11566360#post11566360 "Post Permalink")

  * Oct 10, 2018 4:56pm  Oct 10, 2018 4:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

**Weekly**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: October 10, 2018 22735 AM GMT-0500.png
Size: 158 KB](/attachment/image/3032642/thumbnail?d=1539158129)](/attachment/image/3032642?d=1539158129)   

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#348](/thread/post/11566363#post11566363 "Post Permalink")

  * Oct 10, 2018 4:57pm  Oct 10, 2018 4:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

**Monthly**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: October 10, 2018 22817 AM GMT-0500.png
Size: 231 KB](/attachment/image/3032645/thumbnail?d=1539158235)](/attachment/image/3032645?d=1539158235)   

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#349](/thread/post/11566457#post11566457 "Post Permalink")

  * Oct 10, 2018 5:20pm  Oct 10, 2018 5:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

Patience, money management and discipline can do a lot for:

  1. New traders
  2. Experienced traders
  3. Traders who seem lost
  4. Traders who have given up
  5. Traders who chase every new strategy

**Earn the right for the next trade opportunity, control the risk so the account can survive the tides of the market. Winning & losing trades, comes in and goes out like the sea.**  
_**N.B. Never let your risk be the tsunami that kills your account but the one to let your account last through the test of times.**_

Attached Image

![](/attachment/image/3032674?d=1539159369)

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#350](/thread/post/11575067#post11575067 "Post Permalink")

  * Oct 12, 2018 11:08am  Oct 12, 2018 11:08am 

  * [ Phil1234](phil1234)

  * | Joined Mar 2016  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=455863)

> [Quoting zeeftrader](/thread/post/11270729#post11270729 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello ebeckers, I am still waiting for the link to download the Dashboard Thanks.
> 
> Ignored

It's in the zip file........first few posts 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#351](/thread/post/11575301#post11575301 "Post Permalink")

  * Oct 12, 2018 1:12pm  Oct 12, 2018 1:12pm 

  * [ nave](nave)

  * | Joined Dec 2013  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=357970)

Anyone dashboard is showing any pairs? Mine is empty for the last 6hrs. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#352](/thread/post/11576925#post11576925 "Post Permalink")

  * Oct 12, 2018 8:49pm  Oct 12, 2018 8:49pm 

  * [ Hukman](hukman)

  * | Joined Oct 2018  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=725748)

Thanks for the EA. Looking forward to testing it!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#353](/thread/post/11577334#post11577334 "Post Permalink")

  * Oct 12, 2018 10:17pm  Oct 12, 2018 10:17pm 

  * [ nave](nave)

  * | Joined Dec 2013  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=357970)

Yesterday still got signal and a trade on GY pair. But today until now the dash is blank and nothing shown. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#354](/thread/post/11577365#post11577365 "Post Permalink")

  * Oct 12, 2018 10:22pm  Oct 12, 2018 10:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting nave](/thread/post/11575301#post11575301 "View Quoted Post")
> 
> Disliked
> 
> Anyone dashboard is showing any pairs? Mine is empty for the last 6hrs.
> 
> Ignored

Daily will give you time off periods for trading...this is one depending on the pairs you have implemented.  
No trade unless there is a setup. You don't lose and you don't win. In fact some setups are still running from previous signals. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#355](/thread/post/11577368#post11577368 "Post Permalink")

  * Oct 12, 2018 10:23pm  Oct 12, 2018 10:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting nave](/thread/post/11577334#post11577334 "View Quoted Post")
> 
> Disliked
> 
> Yesterday still got signal and a trade on GY pair. But today until now the dash is blank and nothing shown.
> 
> Ignored

Precisely...holiday for that setup...probably h4 or h1 may have setups. You could try it out at lower risk. On occasions like this.  
From M15 to Monthly can be traded you just have to be open to more volatility or noise. It might be less on the accuracy or you might be surprised to find good results just the same. However create your rules and stick to them, Know them inside out. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#356](/thread/post/11577371#post11577371 "Post Permalink")

  * Oct 12, 2018 10:23pm  Oct 12, 2018 10:23pm 

  * [ nave](nave)

  * | Joined Dec 2013  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=357970)

Like this for the whole of today. Tried reload still like that. Anybody got any idea? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: MetaTrader 4.png
Size: 120 KB](/attachment/image/3037550/thumbnail?d=1539350604)](/attachment/image/3037550?d=1539350604)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#357](/thread/post/11577431#post11577431 "Post Permalink")

  * Oct 12, 2018 10:35pm  Oct 12, 2018 10:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting nave](/thread/post/11577371#post11577371 "View Quoted Post")
> 
> Disliked
> 
> Like this for the whole of today. Tried reload still like that. Anybody got any idea? {image}
> 
> Ignored

It just simply means no setup on that timeframe go to m30, h1 and h4 on days like this, remember it takes a while day before the possibility of a new setup on daily timeframe. Remember losses or profits incurred on other timeframes are in your hands. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: October 12, 2018 83723 AM GMT-0500.png
Size: 214 KB](/attachment/image/3037587/thumbnail?d=1539351343)](/attachment/image/3037587?d=1539351343)   
[![Click to Enlarge

Name: October 12, 2018 83924 AM GMT-0500.png
Size: 300 KB](/attachment/image/3037590/thumbnail?d=1539351377)](/attachment/image/3037590?d=1539351377)   

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#358](/thread/post/11577459#post11577459 "Post Permalink")

  * Oct 12, 2018 10:41pm  Oct 12, 2018 10:41pm 

  * [ nave](nave)

  * | Joined Dec 2013  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=357970)

I am just confused. I just start loading it up yesterday with some pairs showing on the dash and today is totally empty. So I thought something is wrong. Anyway I am letting it run on autotrade with 0.01 lot on a real account to see how it fair.  
  
Thanks for the information. Will check back again next week. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#359](/thread/post/11586392#post11586392 "Post Permalink")

  * Oct 16, 2018 6:25am  Oct 16, 2018 6:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting nave](/thread/post/11577459#post11577459 "View Quoted Post")
> 
> Disliked
> 
> I am just confused. I just start loading it up yesterday with some pairs showing on the dash and today is totally empty. So I thought something is wrong. Anyway I am letting it run on autotrade with 0.01 lot on a real account to see how it fair. Thanks for the information. Will check back again next week.
> 
> Ignored

How are you now, when there is no setup on daily usually I would get on m15 back up to weekly. For e.g. Usdjpy lastweek and eurusd this week. M15, m30, H1, H4. Sometimes even monthly look on silver (xagusd).  
  
What would be good is:

  1. Inside bar
  2. Outside bar
  3. Engulfing
  4. Harami

As potential continuation and reversal signals when pinbar is not present. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: October 15, 2018 12507 PM GMT-0500.png
Size: 1.0 MB](/attachment/image/3041797/thumbnail?d=1539638500)](/attachment/image/3041797?d=1539638500)   
[![Click to Enlarge

Name: October 15, 2018 43011 PM GMT-0500.png
Size: 316 KB](/attachment/image/3041798/thumbnail?d=1539638646)](/attachment/image/3041798?d=1539638646)   

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#360](/thread/post/11591716#post11591716 "Post Permalink")

  * Oct 17, 2018 9:38am  Oct 17, 2018 9:38am 

  * [ nave](nave)

  * | Joined Dec 2013  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=357970)

I got a bug where the EA took a trade immediately on closing of the day despite setting the 50%retracement=true. The dash board also showed the 50%rt=true when it is not. I need to switch timeframe then the dash board goes back to normal. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#361](/thread/post/11592135#post11592135 "Post Permalink")

  * Oct 17, 2018 1:48pm  Oct 17, 2018 1:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

I enabled late... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: October 16, 2018 115659 PM GMT-0500.png
Size: 642 KB](/attachment/image/3044341/thumbnail?d=1539751817)](/attachment/image/3044341?d=1539751817)   

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#362](/thread/post/11593478#post11593478 "Post Permalink")

  * Oct 17, 2018 6:44pm  Oct 17, 2018 6:44pm 

  * [ nave](nave)

  * | Joined Dec 2013  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=357970)

Did you use auto-trade? If yes, did you disable and enable everyday??  
  
  
I closed my EU trade at 20+ pips seeing it stalled. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#363](/thread/post/11601596#post11601596 "Post Permalink")

  * Oct 19, 2018 5:58am  Oct 19, 2018 5:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar289531_6.gif) Soros](soros)

  * Joined Sep 2012 | Status: Edge,Phsycology And Money Managemen | [951 Posts](/search?do=process&provider=Member&searchuser=289531)

its a sound system, just dont understant why anyone hasnt backtested it yet 

I am what Many Dream to be but only a few can achieve, im a part of the 1%

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#364](/thread/post/11601869#post11601869 "Post Permalink")

  * Oct 19, 2018 9:23am  Oct 19, 2018 9:23am 

  * [ nave](nave)

  * | Joined Dec 2013  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=357970)

The 50% retrace don’t seems to work. I set it to true but the EA still opens the trade at the open of the new day candle. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#365](/thread/post/11602004#post11602004 "Post Permalink")

  * Edited 11:09am  Oct 19, 2018 10:55am | Edited 11:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting nave](/thread/post/11593478#post11593478 "View Quoted Post")
> 
> Disliked
> 
> Did you use auto-trade? If yes, did you disable and enable everyday?? I closed my EU trade at 20+ pips seeing it stalled.
> 
> Ignored

I had another pinbar method On, which covers other time frames... I love the system hence the reason I posted here the trade since some persons were having difficulty with the system having alerts. It was meant for feedback to those individuals more than anything else. In a daily basis there are numerous opportunities from m15 to h4 while daily requires 24 hours of cycle for a new alert. While several other signals may trigger within the same 24 hour wih similar results...  
However these significant zones of support and resistance based on a weekly weighted factor, plays a vital role in the zones being actual reactionary zones beyond just a pinbar pattern. At these zones almost any rejections can be traded from these levels. So the system can be accepting of other candle patterns of reversal or continuation reactions.  
Cheers...  
  
Multi timeframe may just have mix results while h4 to weekly may have more of a solid response to the patterns expected reaction as a higher probability trade.  
On this system the Trades are not often but worth the patience. Daily have more potency since banks, hedge funds, money managers and other institutions utilize the new yorks daily close for their trading decision hence the results are more potent.  
  
One trade example I love is December 12 I believe on gold and a couple weeks before that coming down September 8th 2017. When you observe those trades you will realize the importance of these levels identified by the pinbars, since pinbars usually form at levels of expected breakouts that triggered a Lot buys or sells with stoplosses being triggered and lots of limit orders being activated on the wick zones. After seeing these trades you will think twice about closing trades so fast and let them run for as long as the can in your favour but do you have the patience to let these soldiers fight for you... front line duty is not easy but could lead the way to capturing large profits with little or no risk. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#366](/thread/post/11602030#post11602030 "Post Permalink")

  * Oct 19, 2018 11:12am  Oct 19, 2018 11:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting Soros](/thread/post/11601596#post11601596 "View Quoted Post")
> 
> Disliked
> 
> its a sound system, just dont understant why anyone hasnt backtested it yet
> 
> Ignored

I realise people flood the threads which require a Lot more work and those that are out right profitable but slow are more on the ghost town, that has lots of spider Webs on their titles. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#367](/thread/post/11602038#post11602038 "Post Permalink")

  * Oct 19, 2018 11:21am  Oct 19, 2018 11:21am 

  * [ nave](nave)

  * | Joined Dec 2013  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=357970)

So you are using the s/r that show on the dashboard and look for trades on lower time frame? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#368](/thread/post/11602109#post11602109 "Post Permalink")

  * Oct 19, 2018 12:02pm  Oct 19, 2018 12:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting nave](/thread/post/11602038#post11602038 "View Quoted Post")
> 
> Disliked
> 
> So you are using the s/r that show on the dashboard and look for trades on lower time frame?
> 
> Ignored

It's a different system alltogether... however it picks up the same pinbars...all you would have to do is have the dash board with different magic numbers on h1 h4 daily and weekly. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#369](/thread/post/11605918#post11605918 "Post Permalink")

  * Oct 20, 2018 12:33pm  Oct 20, 2018 12:33pm 

  * [ nave](nave)

  * | Joined Dec 2013  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=357970)

I like to see what s/r you are using. Do you using monthly pivots or weekly pivots values as s/r too?  
Maybe you could post some trades whether done or ongoing to shed some lights for me to further learn and understand. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#370](/thread/post/11607843#post11607843 "Post Permalink")

  * Oct 22, 2018 1:06am  Oct 22, 2018 1:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting nave](/thread/post/11605918#post11605918 "View Quoted Post")
> 
> Disliked
> 
> I like to see what s/r you are using. Do you using monthly pivots or weekly pivots values as s/r too? Maybe you could post some trades whether done or ongoing to shed some lights for me to further learn and understand.
> 
> Ignored

I would love to however this thread is for weekly support and resistance hence it cannot be discussed in this thread. I respect Ebeckers. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#371](/thread/post/11608660#post11608660 "Post Permalink")

  * Oct 22, 2018 10:33am  Oct 22, 2018 10:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting nave](/thread/post/11605918#post11605918 "View Quoted Post")
> 
> Disliked
> 
> I like to see what s/r you are using. Do you using monthly pivots or weekly pivots values as s/r too? Maybe you could post some trades whether done or ongoing to shed some lights for me to further learn and understand.
> 
> Ignored

Just compared signals and ebeckers signals match even on the m30 currently. ☺![](https://resources.faireconomy.media/images/emojis/64/1f917.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f60e.png?v=15.1)

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#372](/thread/post/11686882#post11686882 "Post Permalink")

  * Nov 13, 2018 3:41pm  Nov 13, 2018 3:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar707416_2.gif) Mardin](mardin)

  * | Commercial User  | Joined Aug 2018 | [12 Posts](/search?do=process&provider=Member&searchuser=707416)

> [Quoting ebeckers](/thread/post/10714321#post10714321 "View Quoted Post")
> 
> Disliked
> 
> === Pinbar Trader EA === Hi everyone, welcome ! I would like to present my latest EA. It implements a very basic, but very effective strategy. trading pinbars from weekly S&R levels Strategy: - we wait for a pinbar to appear which rejects a weekly support & resistance level - When the candle with the pinbar is closed we open a new buy/sell trade on the next candle The Pinbar trader EA The pinbar trader EA implements the strategy and has lots of extra features: it scans multiple currencies. So load the EA on 1 chart and it will scan all major currencies...
> 
> Ignored

Hi ebeckers, can i request the mq4 file for you? I have asked to take on Github, but an error , please help me friend, thanks 

Get profit together

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#373](/thread/post/11996116#post11996116 "Post Permalink")

  * Feb 13, 2019 5:13pm  Feb 13, 2019 5:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar768340_3.gif) nyakzin](nyakzin)

  * | Joined Feb 2019  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=768340)

> [Quoting zackery](/thread/post/10926345#post10926345 "View Quoted Post")
> 
> Disliked
> 
> {quote} @ebeckers: please contact me via PM.Thanks. Could be interesting for both of us i think. Reg.Zack
> 
> Ignored

Hi Zack,  
  
I would like t get in touch with @ebeckers relating to this EA.  
  
Please help how I would go about doing this?  
  
Regards, 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#374](/thread/post/11996460#post11996460 "Post Permalink")

  * Feb 13, 2019 6:32pm  Feb 13, 2019 6:32pm 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

> [Quoting nyakzin](/thread/post/11996116#post11996116 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Zack, I would like t get in touch with @ebeckers relating to this EA. Please help how I would go about doing this? Regards,
> 
> Ignored

Easy!.  
  
Post here; he will see it.  
  
Cheers. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#375](/thread/post/11996498#post11996498 "Post Permalink")

  * Feb 13, 2019 6:43pm  Feb 13, 2019 6:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar768340_3.gif) nyakzin](nyakzin)

  * | Joined Feb 2019  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=768340)

Thanks @krismitt.  
  
What is the latest version on the EA? Is it available for download and testing?   
  
I only just found the thread and would like to explore this fabulous idea.  
  
Does anyone have results generally on the EA? @PrinceJ58 maybe? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#376](/thread/post/12000420#post12000420 "Post Permalink")

  * Feb 14, 2019 3:03pm  Feb 14, 2019 3:03pm 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

> [Quoting nyakzin](/thread/post/11996498#post11996498 "View Quoted Post")
> 
> Disliked
> 
> Thanks @krismitt. What is the latest version on the EA? Is it available for download and testing? I only just found the thread and would like to explore this fabulous idea. Does anyone have results generally on the EA? @PrinceJ58 maybe?
> 
> Ignored

Everything is in Post No 1, including link to the Source Code, which you can modify as you wish.  
  
Cheers. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#377](/thread/post/12010072#post12010072 "Post Permalink")

  * Feb 16, 2019 7:02pm  Feb 16, 2019 7:02pm 

  * [ Dramti](dramti)

  * | Joined Feb 2019  | Status: Trader | [30 Posts](/search?do=process&provider=Member&searchuser=766813)

Hi all,  
  
It is a great thread.  
  
Does anyone consider the body of Pin Bar ?  
  
I am looking for an EA make an alert when Smallest body candle within X candles (include Pin bar)/ or Largest range within X candles (whole price range, also include Pin Bar).  
  
  
If anyone has any information about similar indicator, please let me know about it.  
  
Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#378](/thread/post/12037541#post12037541 "Post Permalink")

  * Feb 23, 2019 4:03am  Feb 23, 2019 4:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar768340_3.gif) nyakzin](nyakzin)

  * | Joined Feb 2019  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=768340)

Guys,  
  
I've been testing this EA on H1 (AutoTrade), 420 pips today alone. Would like to see it do for a sustainable period but I'm fairly impressed nonetheless.  
  
Thanks for this EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#379](/thread/post/12037727#post12037727 "Post Permalink")

  * Feb 23, 2019 5:10am  Feb 23, 2019 5:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar64206_3.gif) ChicagoRob](chicagorob)

  * | Joined Mar 2008  | Status: Trader | [901 Posts](/search?do=process&provider=Member&searchuser=64206)

> [Quoting nyakzin](/thread/post/12037541#post12037541 "View Quoted Post")
> 
> Disliked
> 
> Guys, I've been testing this EA on H1 (AutoTrade), 420 pips today alone. Would like to see it do for a sustainable period but I'm fairly impressed nonetheless. Thanks for this EA.
> 
> Ignored

Did you run it with defaults? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#380](/thread/post/12038010#post12038010 "Post Permalink")

  * Feb 23, 2019 8:00am  Feb 23, 2019 8:00am 

  * [ artic118](artic118)

  * | Joined Mar 2012  | Status: Trader | [159 Posts](/search?do=process&provider=Member&searchuser=238199)

> [Quoting nyakzin](/thread/post/12037541#post12037541 "View Quoted Post")
> 
> Disliked
> 
> Guys, I've been testing this EA on H1 (AutoTrade), 420 pips today alone. Would like to see it do for a sustainable period but I'm fairly impressed nonetheless. Thanks for this EA.
> 
> Ignored

i try also in H1,..but not very lucky,.what is your settings for h1,.????? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#381](/thread/post/12114226#post12114226 "Post Permalink")

  * Mar 14, 2019 8:55pm  Mar 14, 2019 8:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar681848_1.gif) Boo15](boo15)

  * | Joined May 2018  | Status: Forever Hopeful!! | [257 Posts](/search?do=process&provider=Member&searchuser=681848)

Lets see how this goes.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: AUDUSDDaily1.png
Size: 66 KB](/attachment/image/3267130/thumbnail?d=1552564512)](/attachment/image/3267130?d=1552564512)   

From tiny pips mighty oaks grow

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#382](/thread/post/12118831#post12118831 "Post Permalink")

  * Mar 15, 2019 9:28pm  Mar 15, 2019 9:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar681848_1.gif) Boo15](boo15)

  * | Joined May 2018  | Status: Forever Hopeful!! | [257 Posts](/search?do=process&provider=Member&searchuser=681848)

> [Quoting nyakzin](/thread/post/12037541#post12037541 "View Quoted Post")
> 
> Disliked
> 
> Guys, I've been testing this EA on H1 (AutoTrade), 420 pips today alone. Would like to see it do for a sustainable period but I'm fairly impressed nonetheless. Thanks for this EA.
> 
> Ignored

  
Did you change the magic number to run it on h1?? 

From tiny pips mighty oaks grow

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#383](/thread/post/12254630#post12254630 "Post Permalink")

  * May 5, 2019 1:16pm  May 5, 2019 1:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

Good threads hibernate early... 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#384](/thread/post/12255068#post12255068 "Post Permalink")

  * May 6, 2019 2:11am  May 6, 2019 2:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135523_1.gif) blamshakk](blamshakk)

  * Joined Mar 2010 | Status: Trader | [2,240 Posts](/search?do=process&provider=Member&searchuser=135523)

hey PrinceJ58  
  
i tried this EA but couldn't get any consisten tresults. have you any advise / settings that you could share?  
  
blam  
  

> [Quoting PrinceJ58](/thread/post/12254630#post12254630 "View Quoted Post")
> 
> Disliked
> 
> Good threads hibernate early...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#385](/thread/post/12261472#post12261472 "Post Permalink")

  * May 8, 2019 11:56pm  May 8, 2019 11:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting blamshakk](/thread/post/12255068#post12255068 "View Quoted Post")
> 
> Disliked
> 
> hey PrinceJ58 i tried this EA but couldn't get any consisten tresults. have you any advise / settings that you could share? blam {quote}
> 
> Ignored

Was it on daily? 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#386](/thread/post/12262187#post12262187 "Post Permalink")

  * May 9, 2019 8:35am  May 9, 2019 8:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135523_1.gif) blamshakk](blamshakk)

  * Joined Mar 2010 | Status: Trader | [2,240 Posts](/search?do=process&provider=Member&searchuser=135523)

Possibly.. or h4 i can't quite remember, I just know i had to discontinue the demo after some time testing  
  
blam  
  

> [Quoting PrinceJ58](/thread/post/12261472#post12261472 "View Quoted Post")
> 
> Disliked
> 
> {quote} Was it on daily?
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#387](/thread/post/12263743#post12263743 "Post Permalink")

  * May 9, 2019 11:58pm  May 9, 2019 11:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting blamshakk](/thread/post/12262187#post12262187 "View Quoted Post")
> 
> Disliked
> 
> Possibly.. or h4 i can't quite remember, I just know i had to discontinue the demo after some time testing blam {quote}
> 
> Ignored

I would say which ever pattern you are interested in:

  1. It has to be non repainting
  2. have a coder add a risk to reward factor to it
  3. Check the different ratios win-rate and that will determine which setup or Risk to Reward is best for your strategy.

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#388](/thread/post/12265924#post12265924 "Post Permalink")

  * May 10, 2019 10:39pm  May 10, 2019 10:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar558821_5.gif) tzic](tzic)

  * | Joined Feb 2017  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=558821)

My broker displays valid pairs like this EURUSD.E AUDCAD.E etc. If I use this in the EAs options I get a message that "no pairs found"Any ideas? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#389](/thread/post/12266199#post12266199 "Post Permalink")

  * May 11, 2019 1:01am  May 11, 2019 1:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting tzic](/thread/post/12265924#post12265924 "View Quoted Post")
> 
> Disliked
> 
> My broker displays valid pairs like this EURUSD.E AUDCAD.E etc. If I use this in the EAs options I get a message that "no pairs found"Any ideas?
> 
> Ignored

I believe pages 30 and 31 spoke to that issue about subscripts it would be good to check the mq4 file to see if it is there in the code or delete the list of other currencies that are not being used in the watch list. Ensure to read pages 30 and 31. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#390](/thread/post/12266258#post12266258 "Post Permalink")

  * May 11, 2019 1:47am  May 11, 2019 1:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar558821_5.gif) tzic](tzic)

  * | Joined Feb 2017  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=558821)

Pages 30 and 31 from which thread? OP is not monitoring the thread? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#391](/thread/post/12266430#post12266430 "Post Permalink")

  * May 11, 2019 4:32am  May 11, 2019 4:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting tzic](/thread/post/12266258#post12266258 "View Quoted Post")
> 
> Disliked
> 
> Pages 30 and 31 from which thread? OP is not monitoring the thread?
> 
> Ignored

This same thread. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#392](/thread/post/12266449#post12266449 "Post Permalink")

  * May 11, 2019 4:47am  May 11, 2019 4:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar558821_5.gif) tzic](tzic)

  * | Joined Feb 2017  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=558821)

> [Quoting PrinceJ58](/thread/post/12266430#post12266430 "View Quoted Post")
> 
> Disliked
> 
> {quote} This same thread.
> 
> Ignored

I can only see 20 pages in this thread..... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#393](/thread/post/12266883#post12266883 "Post Permalink")

  * May 11, 2019 6:44pm  May 11, 2019 6:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting tzic](/thread/post/12266449#post12266449 "View Quoted Post")
> 
> Disliked
> 
> {quote} I can only see 20 pages in this thread.....
> 
> Ignored

Please read post:  
[https://www.forexfactory.com/showthr...2#post10858902](https://www.forexfactory.com/showthread.php?p=10858902#post10858902)

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#394](/thread/post/12516172#post12516172 "Post Permalink")

  * Sep 21, 2019 4:11pm  Sep 21, 2019 4:11pm 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

[Attachment g](https://www.forexfactory.com/attachment/file/3445585)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#395](/thread/post/12516695#post12516695 "Post Permalink")

  * Sep 22, 2019 7:33am  Sep 22, 2019 7:33am 

  * [ essyessy](essyessy)

  * | Joined Sep 2019  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=856453)

Is the zip file of this EA removed? I cannot find anything to download.  
  
Could anyone with this great system share the zip file again please. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#396](/thread/post/12584148#post12584148 "Post Permalink")

  * Edited 8:35pm  Oct 27, 2019 8:23pm | Edited 8:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting essyessy](/thread/post/12516695#post12516695 "View Quoted Post")
> 
> Disliked
> 
> Is the zip file of this EA removed? I cannot find anything to download. Could anyone with this great system share the zip file again please.
> 
> Ignored

[https://github.com/erwin-beckers/Sim...master/Experts](https://github.com/erwin-beckers/SimpleTrendReversalEA/tree/master/Experts)  
  
Hope this helps... its a nice e.a.  
Ensure to use a broker with good spread, like an Ecn or Stp, absolutely no market makers... the reason for that is that if the [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") are too large, the positions will have poor entries and this will impact the risk to reward ratio of the strategy.  
  
Note well though, this type of trading requires what most traders don't have= patience. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#397](/thread/post/12601200#post12601200 "Post Permalink")

  * Nov 6, 2019 6:44am  Nov 6, 2019 6:44am 

  * [ laharjaya](laharjaya)

  * | Joined Jun 2008  | Status: Trader | [136 Posts](/search?do=process&provider=Member&searchuser=72657)

got message unable to download news ...  
  
what supposed to do ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#398](/thread/post/12696062#post12696062 "Post Permalink")

  * Jan 10, 2020 6:12am  Jan 10, 2020 6:12am 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

**AUDJPY**  
  
Been away from the Charts for a while!.  
  
Haven't traded Pinbars for a long time but been looking at this Pinbar Trader this week. Here is one that I think is worth the risk (this is a demo Account).  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Signal.png
Size: 18 KB](/attachment/image/3525647/thumbnail?d=1578604149)](/attachment/image/3525647?d=1578604149)   

  
  
And the Entry (was a Limit Order at the High of the Pinbar)  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Trade.png
Size: 30 KB](/attachment/image/3525648/thumbnail?d=1578604224)](/attachment/image/3525648?d=1578604224)   

.  
  
Trade well. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#399](/thread/post/12704027#post12704027 "Post Permalink")

  * Jan 15, 2020 10:05pm  Jan 15, 2020 10:05pm 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

**AUDJPY - UPDATE:**  
  
**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: AUDJPY.png
Size: 36 KB](/attachment/image/3529635/thumbnail?d=1579093540)](/attachment/image/3529635?d=1579093540)   

**  
  
Trade well. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#400](/thread/post/12724984#post12724984 "Post Permalink")

  * Jan 28, 2020 9:09pm  Jan 28, 2020 9:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting krismitt](/thread/post/12704027#post12704027 "View Quoted Post")
> 
> Disliked
> 
> AUDJPY - UPDATE: {image} Trade well.
> 
> Ignored

Great stuff krismitt... I am actually testing a mtf pinbar system too, through pending orders.  
<https://t.me/joinchat/AAAAAFixP49h5XGkuravkg>  
Prior to now i was testing other things but i decided to go ahead with pinbars, Filtering them is the hard part. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#401](/thread/post/12892137#post12892137 "Post Permalink")

  * Apr 22, 2020 2:35pm  Apr 22, 2020 2:35pm 

  * [ krismitt](krismitt)

  * Joined Nov 2009 | Status: Trader | [864 Posts](/search?do=process&provider=Member&searchuser=123567)

**EURJPY**  
  
**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURJPY.jpg
Size: 126 KB](/attachment/image/3613004/thumbnail?d=1587533627)](/attachment/image/3613004?d=1587533627)   

**  
  
**Entry (bounce off 50%)**  
  
**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURJPY Entry.jpg
Size: 51 KB](/attachment/image/3613006/thumbnail?d=1587533663)](/attachment/image/3613006?d=1587533663)   

**  
  
**Trade well.**

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#402](/thread/post/12892916#post12892916 "Post Permalink")

  * Apr 22, 2020 7:28pm  Apr 22, 2020 7:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar817367_1.gif) ecryptom](ecryptom)

  * | Joined Jun 2019  | Status: Trader | [140 Posts](/search?do=process&provider=Member&searchuser=817367)

How about the ea performance now? 

Everything flows. Learn to Earn.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#403](/thread/post/12914737#post12914737 "Post Permalink")

  * May 2, 2020 1:31am  May 2, 2020 1:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar886548_1.gif) Dizza](dizza)

  * | Joined Nov 2019  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=886548)

These are profits using this system.I started to check **Pinbar trader EA** three days ago.It has opened six trades. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Profits \(1\).png
Size: 82 KB](/attachment/image/3622856/thumbnail?d=1588350557)](/attachment/image/3622856?d=1588350557)   
[![Click to Enlarge

Name: Profits \(2\).png
Size: 16 KB](/attachment/image/3622857/thumbnail?d=1588350558)](/attachment/image/3622857?d=1588350558)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#404](/thread/post/12914934#post12914934 "Post Permalink")

  * May 2, 2020 3:26am  May 2, 2020 3:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting Dizza](/thread/post/12914737#post12914737 "View Quoted Post")
> 
> Disliked
> 
> These are profits using this system.I started to check Pinbar trader EA three days ago.It has opened six trades. {image} {image}
> 
> Ignored

Yeah a little patience is worth it, is it default settings?  
Apart from the 50% retrace being activated.![](https://resources.faireconomy.media/images/emojis/64/1f60f.png?v=15.1) limit orders, these sometimes miss potential entries, that the stop orders would pick up.   
  
Ever thought of activating one chart as stop orders= buystop sellstop, market orders versus another chart with limit orders, these retracement entries. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#405](/thread/post/12915366#post12915366 "Post Permalink")

  * May 2, 2020 2:24pm  May 2, 2020 2:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar886548_1.gif) Dizza](dizza)

  * | Joined Nov 2019  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=886548)

> [Quoting PrinceJ58](/thread/post/12914934#post12914934 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yeah a little patience is worth it, is it default settings? Apart from the 50% retrace being activated.![](https://resources.faireconomy.media/images/emojis/64/1f60f.png?v=15.1) limit orders, these sometimes miss potential entries, that the stop orders would pick up. Ever thought of activating one chart as stop orders= buystop sellstop, market orders versus another chart with limit orders, these retracement entries.
> 
> Ignored

I just only changed the lot size and used fix lot size. That is all i changed.all others are default settings. I do not know what will happened in the future.will see... 

[1 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#406](/thread/post/12915851#post12915851 "Post Permalink")

  * May 3, 2020 5:03am  May 3, 2020 5:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting Dizza](/thread/post/12915366#post12915366 "View Quoted Post")
> 
> Disliked
> 
> {quote} I just only changed the lot size and used fix lot size. That is all i changed.all others are default settings. I do not know what will happened in the future.will see...
> 
> Ignored

Well basically with this method you can basically check 15 minutes before the new trading day, based on the timeframe being daily. Otherwise book a vps to test it so you get a fair evaluation. Best if you have low [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") from your broker end like ecn or stp. Then you'd have to check each pair to see the maximum spread on those being monitored during regular market condition, so you don't miss a trade or filter them out with the spread. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#407](/thread/post/12916099#post12916099 "Post Permalink")

  * May 3, 2020 2:08pm  May 3, 2020 2:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar886548_1.gif) Dizza](dizza)

  * | Joined Nov 2019  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=886548)

> [Quoting PrinceJ58](/thread/post/12915851#post12915851 "View Quoted Post")
> 
> Disliked
> 
> {quote} Well basically with this method you can basically check 15 minutes before the new trading day, based on the timeframe being daily. Otherwise book a vps to test it so you get a fair evaluation. Best if you have low spreads from your broker end like ecn or stp. Then you'd have to check each pair to see the maximum spread on those being monitored during regular market condition, so you don't miss a trade or filter them out with the spread.
> 
> Ignored

  
I have a problem.Help me to resolve it. I put **Pinbar trader EA** in to two different mt4 platforms in one VPS. Two different mt4 platforms are **[Pepperstone](/brokers/pepperstone "View Pepperstone Broker Profile") **and **Icmarkets**.   
  
**Pepperstone mt4 is taking positions.already six trades.but when it comes to Icmarkets its not taking positions.no any trade yet. should i change the magic number when i run same ea with two mt4 in one vps?**  
  
**PS : No any errors.all settings are ok.smile face also smiling![](https://resources.faireconomy.media/images/emojis/64/1f603.png?v=15.1)**  
  
**Thanks**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#408](/thread/post/12916910#post12916910 "Post Permalink")

  * May 4, 2020 7:05am  May 4, 2020 7:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting Dizza](/thread/post/12916099#post12916099 "View Quoted Post")
> 
> Disliked
> 
> {quote} I have a problem.Help me to resolve it. I put Pinbar trader EA in to two different mt4 platforms in one VPS. Two different mt4 platforms are Pepperstone and Icmarkets. Pepperstone mt4 is taking positions.already six trades.but when it comes to Icmarkets its not taking positions.no any trade yet. should i change the magic number when i run same ea with two mt4 in one vps? PS : No any errors.all settings are ok.smile face also smiling ![](https://resources.faireconomy.media/images/emojis/64/1f603.png?v=15.1) Thanks
> 
> Ignored

Remember the same spread settings, there are about 2 mt4 types that icmarkets carry, one with commissions and swap and the other i believe incorporate those into the spread. So check that first. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#409](/thread/post/12916911#post12916911 "Post Permalink")

  * May 4, 2020 7:06am  May 4, 2020 7:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

Lots of pins on Aussie pairs. Weekly. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#410](/thread/post/12917805#post12917805 "Post Permalink")

  * May 4, 2020 7:06pm  May 4, 2020 7:06pm 

  * [ minhquan](minhquan)

  * | Joined Apr 2020  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=944701)

Hello every one!  
I followed this thread a long time, but the interaction here doesn't seem to be much.  
Base on the strategy of the Pinbar EA trader, I developed it with more pattern such as Engulfing, inside bar, reversal 02 candle, reversal 03 candle, Fakey. Besides, I added hull moving, RSIoMA with purpose trade follow trend. I tested on M5,M15,M30, and H1 and see result is good on 04 time frames. However, there is one problem that: when i use iCustom, sometime EA was lag, so the entry point be late. I don't know convert Indicators to file *mqh to attached to EA to speed up of trading. If anyone good coding and interesting by this EA, you can help me and people convert indicator to speed up for EA.  
Thank you very much!  
I posted 04 files related update this EA. The remaining files remain the same as Ebeckers posted.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: picture.png
Size: 119 KB](/attachment/image/3624502/thumbnail?d=1588586692)](/attachment/image/3624502?d=1588586692)   

Attached File(s)

![File Type: mqh](https://assets.faireconomy.media/images/attach/mqh.gif) [CPriceActionStrategy3.mqh](/attachment/file/3624480?d=1588586076) 52 KB | 556 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Price Action2.mq4](/attachment/file/3624482?d=1588586115) 19 KB | 662 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [master trend v.2.mq4](/attachment/file/3624484?d=1588586212) 8 KB | 601 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [MasterTrendRSI.mq4](/attachment/file/3624485?d=1588586213) 5 KB | 571 downloads 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#411](/thread/post/12919156#post12919156 "Post Permalink")

  * May 5, 2020 8:48am  May 5, 2020 8:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting minhquan](/thread/post/12917805#post12917805 "View Quoted Post")
> 
> Disliked
> 
> Hello every one! I followed this thread a long time, but the interaction here doesn't seem to be much. Base on the strategy of the Pinbar EA trader, I developed it with more pattern such as Engulfing, inside bar, reversal 02 candle, reversal 03 candle, Fakey. Besides, I added hull moving, RSIoMA with purpose trade follow trend. I tested on M5,M15,M30, and H1 and see result is good on 04 time frames. However, there is one problem that: when i use iCustom, sometime EA was lag, so the entry point be late. I don't know convert Indicators to file *mqh...
> 
> Ignored

Interesting very interesting.... 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#412](/thread/post/12919302#post12919302 "Post Permalink")

  * May 5, 2020 12:34pm  May 5, 2020 12:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar934248_1.gif) Jonhathan123](jonhathan123)

  * | Joined Apr 2020  | Status: Trader | [144 Posts](/search?do=process&provider=Member&searchuser=934248)

> [Quoting minhquan](/thread/post/12917805#post12917805 "View Quoted Post")
> 
> Disliked
> 
> Hello every one! I followed this thread a long time, but the interaction here doesn't seem to be much. Base on the strategy of the Pinbar EA trader, I developed it with more pattern such as Engulfing, inside bar, reversal 02 candle, reversal 03 candle, Fakey. Besides, I added hull moving, RSIoMA with purpose trade follow trend. I tested on M5,M15,M30, and H1 and see result is good on 04 time frames. However, there is one problem that: when i use iCustom, sometime EA was lag, so the entry point be late. I don't know convert Indicators to file *mqh...
> 
> Ignored

Can I ask how to install it? I cannot install .mqh and EA files on my MT4! Thank 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#413](/thread/post/12919316#post12919316 "Post Permalink")

  * May 5, 2020 12:49pm  May 5, 2020 12:49pm 

  * [ minhquan](minhquan)

  * | Joined Apr 2020  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=944701)

> [Quoting Jonhathan123](/thread/post/12919302#post12919302 "View Quoted Post")
> 
> Disliked
> 
> {quote} Can I ask how to install it? I cannot install .mqh and EA files on my MT4! Thank
> 
> Ignored

File *.mqh was attached in EA. You should copy file *.mqh to folder "include", then EA will detect and run.  
I send more template file for you. 

Attached File(s)

![File Type: tpl](https://assets.faireconomy.media/images/attach/tpl.gif) [pinbartrader.tpl](/attachment/file/3625276?d=1588650462) 9 KB | 404 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#414](/thread/post/12933215#post12933215 "Post Permalink")

  * May 12, 2020 11:52am  May 12, 2020 11:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375355_1.gif) FX5Star](fx5star)

  * | Joined Jun 2014  | Status: Trader | [200 Posts](/search?do=process&provider=Member&searchuser=375355)

> [Quoting ebeckers](/thread/post/10714321#post10714321 "View Quoted Post")
> 
> Disliked
> 
> === Pinbar Trader EA === Hi everyone, welcome ! I would like to present my latest EA. It implements a very basic, but very effective strategy. trading pinbars from weekly S&R levels Strategy: - we wait for a pinbar to appear which rejects a weekly support & resistance level - When the candle with the pinbar is closed we open a new buy/sell trade on the next candle The Pinbar trader EA The pinbar trader EA implements the strategy and has lots of extra features: it scans multiple currencies. So load the EA on 1 chart and it will scan all major currencies...
> 
> Ignored

  
  
Hi, ebeckers  
Can you share the setting of the results of a 2-year backtest on EURUSD you attached ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#415](/thread/post/12946217#post12946217 "Post Permalink")

  * Edited 4:10pm  May 18, 2020 1:51pm | Edited 4:10pm 

  * [ timidave](timidave)

  * | Joined Nov 2007  | Status: Trader | [460 Posts](/search?do=process&provider=Member&searchuser=54383)

> [Quoting minhquan](/thread/post/12917805#post12917805 "View Quoted Post")
> 
> Disliked
> 
> Hello every one! I followed this thread a long time, but the interaction here doesn't seem to be much. Base on the strategy of the Pinbar EA trader, I developed it with more pattern such as Engulfing, inside bar, reversal 02 candle, reversal 03 candle, Fakey. Besides, I added hull moving, RSIoMA with purpose trade follow trend. I tested on M5,M15,M30, and H1 and see result is good on 04 time frames. However, there is one problem that: when i use iCustom, sometime EA was lag, so the entry point be late. I don't know convert Indicators to file *mqh...
> 
> Ignored

Thank you so much for your input on this EA. I have installed all 3 new indicators plus the file to be installed at the 'include' folder and here my template still remains the same as old. pls, what could be the problem? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURUSDDaily.png
Size: 33 KB](/attachment/image/3638079/thumbnail?d=1589777465)](/attachment/image/3638079?d=1589777465)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#416](/thread/post/12948668#post12948668 "Post Permalink")

  * May 19, 2020 12:14pm  May 19, 2020 12:14pm 

  * [ timidave](timidave)

  * | Joined Nov 2007  | Status: Trader | [460 Posts](/search?do=process&provider=Member&searchuser=54383)

> [Quoting timidave](/thread/post/12946217#post12946217 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thank you so much for your input on this EA. I have installed all 3 new indicators plus the file to be installed at the 'include' folder and here my template still remains the same as old. pls, what could be the problem? {image}
> 
> Ignored

i think the problem is that the Price Action2.mq4 indicator is not detected by the EA. Can someone pls tell me how to fix this problem? It says 'cannot open file'. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Untitled.png
Size: 101 KB](/attachment/image/3639265/thumbnail?d=1589858078)](/attachment/image/3639265?d=1589858078)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#417](/thread/post/12949483#post12949483 "Post Permalink")

  * May 19, 2020 6:57pm  May 19, 2020 6:57pm 

  * [ minhquan](minhquan)

  * | Joined Apr 2020  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=944701)

> [Quoting timidave](/thread/post/12948668#post12948668 "View Quoted Post")
> 
> Disliked
> 
> {quote} i think the problem is that the Price Action2.mq4 indicator is not detected by the EA. Can someone pls tell me how to fix this problem? It says 'cannot open file'. {image}
> 
> Ignored

file Price Action2.mq4 is EA, not indicator! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#418](/thread/post/12949881#post12949881 "Post Permalink")

  * May 19, 2020 9:35pm  May 19, 2020 9:35pm 

  * [ moomooCow](moomoocow)

  * | Joined Jun 2016  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=468925)

> [Quoting Dizza](/thread/post/12914737#post12914737 "View Quoted Post")
> 
> Disliked
> 
> These are profits using this system.I started to check Pinbar trader EA three days ago.It has opened six trades. {image} {image}
> 
> Ignored

Could you elaborate on how you got it running? What timeframe are you using? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#419](/thread/post/12950029#post12950029 "Post Permalink")

  * Edited 10:45pm  May 19, 2020 10:29pm | Edited 10:45pm 

  * [ timidave](timidave)

  * | Joined Nov 2007  | Status: Trader | [460 Posts](/search?do=process&provider=Member&searchuser=54383)

> [Quoting minhquan](/thread/post/12949483#post12949483 "View Quoted Post")
> 
> Disliked
> 
> {quote} file Price Action2.mq4 is EA, not indicator!
> 
> Ignored

Thanks, i've installed in the experts but the same problem persisted. I'm surprised i'm the only one talking about this problem. Also, it could'nt be attached to my chart. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#420](/thread/post/12953896#post12953896 "Post Permalink")

  * May 21, 2020 5:31am  May 21, 2020 5:31am 

  * [ moomooCow](moomoocow)

  * | Joined Jun 2016  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=468925)

> [Quoting timidave](/thread/post/12950029#post12950029 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks, i've installed in the experts but the same problem persisted. I'm surprised i'm the only one talking about this problem. Also, it could'nt be attached to my chart.
> 
> Ignored

He hasn't provided his actual EA that is why it's breaking 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

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

[5/13/50 with pinbars](/thread/68263-51350-with-pinbars "I have been following this for quite awhile, it is not perfect, but seems to give decent setups on the 30/60 min nzd/jpy aud/jpy  charts 
 ...") 5 replies

[Price action topics on pinbars?](/thread/375369-price-action-topics-on-pinbars "Where I can find topics on price action on pinbars? How to trade with them, what is inside pinbar? Please tell best sources \( not promo for...") 2 replies

[PinBar Trading](/thread/381949-pinbar-trading "So I've been discussing this with my friends for some time and no matter how bad scenarios we apply, we still find this method profitable....") 7 replies

[Pinbar's live trading journal](/thread/252015-pinbars-live-trading-journal "Pinbar's trading journal. 
 
After demoing the J16 systems for 3 months, I have started to trade small lots on my live account. I would...") 30 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)
  * Subscribe
  * [156](javascript:void\(0\);)

Attachments: Pinbar trader EA - Trading pinbars off weekly S&R levels

Tags: Pinbar trader EA - Trading pinbars off weekly S&R levels

#  [](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly)Pinbar trader EA - Trading pinbars off weekly S&R levels 

  * 

  * [#421](/thread/post/12953910#post12953910 "Post Permalink")

  * May 21, 2020 5:45am  May 21, 2020 5:45am 

  * [ timidave](timidave)

  * | Joined Nov 2007  | Status: Trader | [460 Posts](/search?do=process&provider=Member&searchuser=54383)

> [Quoting moomooCow](/thread/post/12953896#post12953896 "View Quoted Post")
> 
> Disliked
> 
> {quote} He hasn't provided his actual EA that is why it's breaking
> 
> Ignored

Oh no, thanks for that observation. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#422](/thread/post/13057746#post13057746 "Post Permalink")

  * Jul 14, 2020 1:40pm  Jul 14, 2020 1:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar978440_1.gif) cutbankfx](cutbankfx)

  * | Joined Jul 2020  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=978440)

I have attached Ea MT4 2 Day but not Open Order Why..? can you help..?? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#423](/thread/post/13066742#post13066742 "Post Permalink")

  * Jul 19, 2020 4:43pm  Jul 19, 2020 4:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting cutbankfx](/thread/post/13057746#post13057746 "View Quoted Post")
> 
> Disliked
> 
> I have attached Ea MT4 2 Day but not Open Order Why..? can you help..??
> 
> Ignored

Sometimes the day will not have a pinbar and other times alot will be around especially after an impactful news releases. Stophunts etc etc 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#424](/thread/post/13067127#post13067127 "Post Permalink")

  * Jul 20, 2020 4:36am  Jul 20, 2020 4:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting cutbankfx](/thread/post/13057746#post13057746 "View Quoted Post")
> 
> Disliked
> 
> I have attached Ea MT4 2 Day but not Open Order Why..? can you help..??
> 
> Ignored

You can take out a cheap vps to test it for a period.

  1. Change timeframes,
  2. check minimum spread,
  3. check if news filters are on.

Lots of settings can cause it but when you change to lower timeframe it will show if the e.a would definitely trigger a trade when daily conditions are met, this doesn't happen very often since you have to wait one whole day. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#425](/thread/post/13067266#post13067266 "Post Permalink")

  * Edited 9:28am  Jul 20, 2020 9:06am | Edited 9:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

Made the post at the wrong location... I apologize. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#426](/thread/post/13194256#post13194256 "Post Permalink")

  * Oct 2, 2020 3:56am  Oct 2, 2020 3:56am 

  * [ maplefu0601](maplefu0601)

  * | Joined Sep 2020  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=1005040)

Thanks Ebeckers. It's a great system.  
  
I Downloaded the EA and tried to run.  
  
I ran two EAs on different pair, and I found the result were different. I'm using the same EA so why the results are different? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 75 KB](/attachment/image/3755059/thumbnail?d=1601578431)](/attachment/image/3755059?d=1601578431)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#427](/thread/post/13229523#post13229523 "Post Permalink")

  * Oct 26, 2020 6:57pm  Oct 26, 2020 6:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar430267_1.gif) PrinceJ58](princej58)

  * Joined Oct 2015 | Status: Focused on the Results | [1,482 Posts](/search?do=process&provider=Member&searchuser=430267)

> [Quoting maplefu0601](/thread/post/13194256#post13194256 "View Quoted Post")
> 
> Disliked
> 
> Thanks Ebeckers. It's a great system. I Downloaded the EA and tried to run. I ran two EAs on different pair, and I found the result were different. I'm using the same EA so why the results are different? {image}
> 
> Ignored

Question should also cover whether its the same broker. Each broker sometimes vary in the close bars of h4 and daily based on the gmt offset differences. 

R:R "Percentage Focus"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#428](/thread/post/13237113#post13237113 "Post Permalink")

  * Oct 30, 2020 7:22am  Oct 30, 2020 7:22am 

  * [ LadyAmira](ladyamira)

  * Joined May 2016 | Status: Trader | [51 Posts](/search?do=process&provider=Member&searchuser=465501)

Any updates? How are the results? ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#429](/thread/post/13316010#post13316010 "Post Permalink")

  * Dec 17, 2020 12:50am  Dec 17, 2020 12:50am 

  * [ traderjane](traderjane)

  * | Joined May 2006  | Status: Trader | [35 Posts](/search?do=process&provider=Member&searchuser=9265)

> [Quoting minhquan](/thread/post/12917805#post12917805 "View Quoted Post")
> 
> Disliked
> 
> Hello every one! I followed this thread a long time, but the interaction here doesn't seem to be much. Base on the strategy of the Pinbar EA trader, I developed it with more pattern such as Engulfing, inside bar, reversal 02 candle, reversal 03 candle, Fakey. Besides, I added hull moving, RSIoMA with purpose trade follow trend. I tested on M5,M15,M30, and H1 and see result is good on 04 time frames. However, there is one problem that: when i use iCustom, sometime EA was lag, so the entry point be late. I don't know convert Indicators to file *mqh...
> 
> Ignored

Thanks Ebeckers and minhquan for the additional indicators. Is there an updated ea for the system?  
Appreciate your assistance. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#430](/thread/post/13321265#post13321265 "Post Permalink")

  * Dec 20, 2020 12:08am  Dec 20, 2020 12:08am 

  * [ minhquan](minhquan)

  * | Joined Apr 2020  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=944701)

I updated EA it with more pattern such as Engulfing, inside bar, reversal 02 candle, reversal 03 candle, Fakey and hull moving, rsi without any indicator attached. Ea run faster and more effective. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#431](/thread/post/13321428#post13321428 "Post Permalink")

  * Dec 20, 2020 4:52am  Dec 20, 2020 4:52am 

  * [ marzinsz](marzinsz)

  * | Joined May 2016  | Status: Trader | [55 Posts](/search?do=process&provider=Member&searchuser=465166)

> [Quoting minhquan](/thread/post/13321265#post13321265 "View Quoted Post")
> 
> Disliked
> 
> I updated EA it with more pattern such as Engulfing, inside bar, reversal 02 candle, reversal 03 candle, Fakey and hull moving, rsi without any indicator attached. Ea run faster and more effective.
> 
> Ignored

Hei, minhquan, where can I find updated version? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#432](/thread/post/13328791#post13328791 "Post Permalink")

  * Dec 24, 2020 10:19am  Dec 24, 2020 10:19am 

  * [ minhquan](minhquan)

  * | Joined Apr 2020  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=944701)

> [Quoting marzinsz](/thread/post/13321428#post13321428 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hei, minhquan, where can I find updated version?
> 
> Ignored

I have not update new EA on here because I see the result not as I want. Besides, now I focus trade by manual instead of EA. I take time more than 01 year code EA but almost them that is not effective. So I decide stop coding. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#433](/thread/post/14021381#post14021381 "Post Permalink")

  * Jun 4, 2022 3:09pm  Jun 4, 2022 3:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar723593_4.gif) Klausi](klausi)

  * | Joined Oct 2018  | Status: Trader | [425 Posts](/search?do=process&provider=Member&searchuser=723593)

Hi guys. Thanks for the brilliant EA and addons here. I got a question: what is the name of the standalone support/resistance indicator used in the pinbartrader? the one that shows historical week, daily, monthlly S/R Levels like in post one? A time ago i have know the name and im pretty sure i got it in the archives somewhere. But cant recall the name.  
  
Thanks and have a great one!  
  
Klausi 

Stick to the plan!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#434](/thread/post/14026274#post14026274 "Post Permalink")

  * Jun 9, 2022 7:03pm  Jun 9, 2022 7:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135037_2.gif) CamaRon](camaron)

  * | Joined Mar 2010  | Status: Forex Trader & Kali Fighter | [63 Posts](/search?do=process&provider=Member&searchuser=135037)

> [Quoting Klausi](/thread/post/14021381#post14021381 "View Quoted Post")
> 
> Disliked
> 
> Hi guys. Thanks for the brilliant EA and addons here. I got a question: what is the name of the standalone support/resistance indicator used in the pinbartrader? the one that shows historical week, daily, monthlly S/R Levels like in post one? A time ago i have know the name and im pretty sure i got it in the archives somewhere. But cant recall the name. Thanks and have a great one! Klausi
> 
> Ignored

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [SupportResistance.mq4](/attachment/file/4220750?d=1654769013) 7 KB | 272 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#435](/thread/post/14539303#post14539303 "Post Permalink")

  * Aug 17, 2023 6:50pm  Aug 17, 2023 6:50pm 

  * [ kentyeoh](kentyeoh)

  * | Joined Oct 2017  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=621125)

Hi ebeckers,  
  
Your EA is fantastic!  
Would it possible to change option to either trade with pinbar or without?  
  
Thanks a lot! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#436](/thread/post/14552042#post14552042 "Post Permalink")

  * Last Post: Aug 28, 2023 7:42am  Aug 28, 2023 7:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,577 Posts](/search?do=process&provider=Member&searchuser=185229)

> [Quoting kentyeoh](/thread/post/14539303#post14539303 "View Quoted Post")
> 
> Disliked
> 
> Hi ebeckers, Your EA is fantastic! Would it possible to change option to either trade with pinbar or without? Thanks a lot!
> 
> Ignored

More details required...  
  
Assuming you want to trade simply the breakout of weekly highs or lows, there are plenty of existing EA's for that already.  
  
Good Luck ![](https://resources.faireconomy.media/images/emojis/64/1f340.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f340.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f340.png?v=15.1)

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.7%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Pinbar trader EA - Trading pinbars off weekly S&R levels
  *   * [ **Reply to Thread** ](/thread/733891-pinbar-trader-ea-trading-pinbars-off-weekly/reply#reply)

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)
