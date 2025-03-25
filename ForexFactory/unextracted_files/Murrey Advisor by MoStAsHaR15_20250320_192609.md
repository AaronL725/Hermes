

  * 

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#1](/thread/255584-murrey-advisor-by-mostashar15 "Post Permalink")

  * First Post: Edited Sep 20, 2010 12:10pm  Sep 13, 2010 1:41am | Edited Sep 20, 2010 12:10pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

  
  
**_MURREY ADVISOR V2.3 ![](https://resources.faireconomy.media/images/emojis/64/00a9-fe0f.png?v=15.1) MoStAsHaR15 2010_**  
  
**_Timeframe_** : 4 Hrs  
**_Pairs_** : EURUSD, GBPUSD, USDJPY, USDCAD, AUDUSD, NZDUSD, and EURGBP.  
  
I have developed this indicator based on my observations. It is based on the principles of Support and Resistance using Murrey Lines and Trend strength & direction using ADX.  
The indicator will plot Murrey lines. It will highlight areas from -2/8P to 0/8 AND 8/8 to +2/8P with a red color to indicate that these two areas follow additional rule. The rule is that only LONG positions will be allowed below 0/8 and only SHORT positions will be allowed above 8/8.  
The indicator can automatically recognize the current Murrey support and resistance and will show how many pips still there to reach the levels.   
  
**_BUY ENTRY_**  
The indicator looks for the following:

  1. EMA(5,close) > EMA(6,open) by 5 points at least AND close of last candle Close[1] is no more than 25 pips above EMA(5,close).
  2. Current candle open (Open[0]) > support by 3 points at least.
  3. Main ADX > 21 and increasing while ADX(+) > ADX(-) by 3 points at least.
  4. High of both current and last candles (H[0,1]) < resistance by 10 points at least.
  5. Price should be below 8/8 Murrey level

  
**_SELL ENTRY_**  
The indicator looks for the following:

  1. EMA(5,close) < EMA(6,open) by 5 points at least AND close of last candle Close[1] is no more than 25 pips below EMA(5,close).
  2. Current candle open (Open[0]) > resistance by 3 points at least.
  3. Main ADX > 21 and increasing while ADX(-) > ADX(+) by 3 points at least.
  4. Low of both current and last candles (L[0,1]) < resistance by 10 points at least.
  5. Price should be above 0/8 Murrey level

  
The indicator shows status of each condition on real-time. Once conditions achieved, recommendations will be shown as “Go Long” or “Go Short” while “Hold!” is shown if any of the conditions is not satisfied. The indicator gives an alert once a signal is generated.  
  
Once you get in LONG position, then your TP = next resistance (usually from 30 to 60 points based on Murrey span) and SL = -30 points.  
  
**_RESULTS_**  
So far, I am getting around 75% success rate and overall it is making good money based on manual trading on both Demo and Real accounts. I have been developing this strategy since 2005 and it evolved from different indicators and timeframes until it is in this form in this version (v2.3).   
  
**_MURREY ADVISOR EA V1.0_**  
We have produced the 1st version of EA that uses this strategy. Highlights are as follows:  
  

  1. You have to attach both EA V1.0 and Murrey Advisor V2.3 to the same chart as the EA imports the data through the chart.
  2. EA will trade one position per pair max as long as there is enough money.
  3. Lot size is 0.1 and can be changed (external variable).
  4. Take Profit (TP) will be next Murrey Support/Resistance as per strategy.
  5. Stop Loss (SL) will be -30 points and can be changed (external variable).
  6. Trailing Stop (TS) is 15 and can be turned off if set to 0 (external variable).
  7. Open positions will be closed automatically either by: (i) TP, (ii) SL, (iii) TS, (iv) if close of last candle close[1] is less than EMA(6,o) by 15 points as it is likely for the pair to go in reverse.
  8. Murrey Advisor v1.0 can support only 4-digit brokers as of now. Work in progress to support 5-digit brokers as well.

  
  
**_ATTACHMENTS:_**  
Attached is the latest version v2.3. You need to pick up the right version for you based on your broker digits either 4 or 5. EA v1.0 can only support 4 digit brokers as of now.  
  
Below is a snapshot of the indicator showing SELL entry for EURGBP:  

  

<http://img214.imageshack.us/img214/5652/eurgbpsell.gif>

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Murrey Advisor EA 4dig v1.0.mq4](/attachment/file/544860?d=1284672875) 5 KB | 1,213 downloads | Uploaded Sep 17, 2010 6:34am 

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [Murrey Advisor v2.3 4dig.zip](/attachment/file/544873?d=1284675357) 9 KB | 1,670 downloads | Uploaded Sep 17, 2010 7:15am 

  * [#2](/thread/post/4016257#post4016257 "Post Permalink")

  * Sep 13, 2010 2:52am  Sep 13, 2010 2:52am 

  * [ Indrek](indrek)

  * Joined Jun 2009 | Status: Trader | [2,430 Posts](/search?do=process&provider=Member&searchuser=106754)

Very interesting indicator. Do you wait for the h4 candle to close for entry or you enter as soon as there is a signal? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#3](/thread/post/4016262#post4016262 "Post Permalink")

  * Sep 13, 2010 2:58am  Sep 13, 2010 2:58am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting Indrek](/thread/post/4016257#post4016257 "View Quoted Post")
> 
> Disliked
> 
> Very interesting indicator. Do you wait for the h4 candle to close for entry or you enter as soon as there is a signal?
> 
> Ignored

What I have been doing is that I get in immediately whenever there is a signal even if the candle did not close with exception after weekend. I usually wait at least for the close of one new candle to confirm the direction during the opening of Asian market after the weekend.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#4](/thread/post/4016296#post4016296 "Post Permalink")

  * Sep 13, 2010 3:42am  Sep 13, 2010 3:42am 

  * [ aelimian](aelimian)

  * | Joined Oct 2004  | Status: Trader | [438 Posts](/search?do=process&provider=Member&searchuser=1172)

> [Quoting mostashar15](/thread/post/4016262#post4016262 "View Quoted Post")
> 
> Disliked
> 
> What I have been doing is that I get in immediately whenever there is a signal even if the candle did not close with exception after weekend. I usually wait at least for the close of one new candle to confirm the direction during the opening of Asian market after the weekend.
> 
> Ignored

Please post the remaining required indicators. Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#5](/thread/post/4016300#post4016300 "Post Permalink")

  * Sep 13, 2010 3:47am  Sep 13, 2010 3:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar146979_2.gif) 219](219)

  * | Joined Jun 2010  | Status: Trader | [76 Posts](/search?do=process&provider=Member&searchuser=146979)

Il try it for next few weeks now. Thanks dude ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#6](/thread/post/4016303#post4016303 "Post Permalink")

  * Sep 13, 2010 4:02am  Sep 13, 2010 4:02am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting aelimian](/thread/post/4016296#post4016296 "View Quoted Post")
> 
> Disliked
> 
> Please post the remaining required indicators. Thanks
> 
> Ignored

There is no other indicators required. You just install the MQL4 file and insert the template. You should get it setup. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#7](/thread/post/4016306#post4016306 "Post Permalink")

  * Sep 13, 2010 4:04am  Sep 13, 2010 4:04am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting 219](/thread/post/4016300#post4016300 "View Quoted Post")
> 
> Disliked
> 
> Il try it for next few weeks now. Thanks dude ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

Thanks buddy 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#8](/thread/post/4016332#post4016332 "Post Permalink")

  * Sep 13, 2010 4:35am  Sep 13, 2010 4:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar113359_3.gif) Precap2](precap2)

  * | Joined Aug 2009  | Status: Non-graduating student | [575 Posts](/search?do=process&provider=Member&searchuser=113359)

subscribed. Would want to do a test of your indi and respond.  
  
Peace! 

Mystery Is The Final Product Of Ignorance. Hey! What's ma chart doin' ![](https://resources.faireconomy.media/images/emojis/64/1f621.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#9](/thread/post/4016356#post4016356 "Post Permalink")

  * Sep 13, 2010 4:58am  Sep 13, 2010 4:58am 

  * [ zeCarvalho](zecarvalho)

  * | Joined Sep 2009  | Status: Trader | [68 Posts](/search?do=process&provider=Member&searchuser=115276)

good work... thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#10](/thread/post/4016358#post4016358 "Post Permalink")

  * Sep 13, 2010 5:00am  Sep 13, 2010 5:00am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting Precap2](/thread/post/4016332#post4016332 "View Quoted Post")
> 
> Disliked
> 
> subscribed. Would want to do a test of your indi and respond.  
>    
>  Peace!
> 
> Ignored

Thanks for dropping by and waiting for your results. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#11](/thread/post/4016365#post4016365 "Post Permalink")

  * Sep 13, 2010 5:07am  Sep 13, 2010 5:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar146979_2.gif) 219](219)

  * | Joined Jun 2010  | Status: Trader | [76 Posts](/search?do=process&provider=Member&searchuser=146979)

So it cant be used on 15 min or 30 min timeframes ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#12](/thread/post/4016389#post4016389 "Post Permalink")

  * Sep 13, 2010 5:31am  Sep 13, 2010 5:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar64206_3.gif) ChicagoRob](chicagorob)

  * | Joined Mar 2008  | Status: Trader | [901 Posts](/search?do=process&provider=Member&searchuser=64206)

> [Quoting mostashar15](/thread/post/4016194#post4016194 "View Quoted Post")
> 
> Disliked
> 
> The rule is that only LONG positions will be allowed below 0/8 and only SHORT positions will be allowed above 8/8.
> 
> Ignored

The example violates the above rules, since you're going short at the 4/8 pivot, instead of MM levels above 8/8.   
  
Please advise.  
  
Rob 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#13](/thread/post/4016395#post4016395 "Post Permalink")

  * Sep 13, 2010 5:33am  Sep 13, 2010 5:33am 

  * [ Invisible](invisible)

  * | Joined Nov 2009  | Status: Trader | [469 Posts](/search?do=process&provider=Member&searchuser=124048)

Excellent work, mostashar15.  
  
I have been playing around with Murrey on the D1 for a while recently and it is interesting how price tends to respect these lines quite a lot. This is definitely a good candidate for an EA. I wonder if Sir Steve Hopwood would be interested... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
I would like to add that it would also be useful to have Steve's Trade Manager EA manage the trades. When I was trying to some trading off the D1 Murreys, I was using this EA to manage the trade. I found the following features useful, and you might want to try them as this may improve the profitability in the case where the price reverses without quite touching the TP line:

  1.  _Instant trailing stop_ : As soon as the trade starts moving in the direction of the trade, this feature the starts trailing the SL. So if your SL is set at 30, then it will trail at 30 pips.
  2. _Tightening SL_ : Once the trailing SL reaches certain levels, then the Trade Manager EA tightens the trailing stop. The two points are at 50% of the TP level and 80% of the TP level. So if you have a trailing 30 pip stop, then you could have this tightened to 15 pips when the trade reaches 50% of the TP and then to 7 pips when the trade reaches 80% of the TP level. In other words as you get closer to the TP, then you lock in progressively more profit.

I hope this is a help to you. Thank you very much for sharing.  
  
Invisible 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#14](/thread/post/4016398#post4016398 "Post Permalink")

  * Sep 13, 2010 5:34am  Sep 13, 2010 5:34am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting 219](/thread/post/4016365#post4016365 "View Quoted Post")
> 
> Disliked
> 
> So it cant be used on 15 min or 30 min timeframes ?
> 
> Ignored

I don't recommend other time frames than 4 hrs. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#15](/thread/post/4016401#post4016401 "Post Permalink")

  * Sep 13, 2010 5:37am  Sep 13, 2010 5:37am 

  * [ Invisible](invisible)

  * | Joined Nov 2009  | Status: Trader | [469 Posts](/search?do=process&provider=Member&searchuser=124048)

@ ChicagoRob  
  
The way I understand it is between 0 and 8 levels, then you can go either long or short. If price is above 8/8 then you can only go short, and below 0/8 you can only go long.  
  
@ mostashar15  
  
Sometimes Murreys will suddenly change. Does your indicator automatically do that, or do we need to refresh the chart by changing to another TF and back again to see that? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#16](/thread/post/4016406#post4016406 "Post Permalink")

  * Sep 13, 2010 5:40am  Sep 13, 2010 5:40am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting ChicagoRob](/thread/post/4016389#post4016389 "View Quoted Post")
> 
> Disliked
> 
> The example violates the above rules, since you're going short at the 4/8 pivot, instead of MM levels above 8/8.   
>    
>  Please advise.  
>    
>  Rob
> 
> Ignored

No it does not.  
  
8/8 to +2/8P => go for SELL signals only.  
0/8 to 8/8 => go for both BUY and SELL signals.  
-2/8 to 0/8 => go for BUY signals only.  
  
I hope this clarifies it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#17](/thread/post/4016415#post4016415 "Post Permalink")

  * Sep 13, 2010 5:48am  Sep 13, 2010 5:48am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting Invisible](/thread/post/4016401#post4016401 "View Quoted Post")
> 
> Disliked
> 
> @ ChicagoRob  
>    
>  The way I understand it is between 0 and 8 levels, then you can go either long or short. If price is above 8/8 then you can only go short, and below 0/8 you can only go long.  
>    
>  @ mostashar15  
>    
>  Sometimes Murreys will suddenly change. Does your indicator automatically do that, or do we need to refresh the chart by changing to another TF and back again to see that?
> 
> Ignored

Yes, your understanding is correct.  
  
Regarding sudden change of Murrey Levels, if you use 4hr time frame as proposed by this strategy then the change will not happen before days and sometimes weeks.Therefore, what I suggest is that to refresh the chart everyday just in case. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#18](/thread/post/4016429#post4016429 "Post Permalink")

  * Sep 13, 2010 6:07am  Sep 13, 2010 6:07am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting Invisible](/thread/post/4016395#post4016395 "View Quoted Post")
> 
> Disliked
> 
> Excellent work, mostashar15.  
>    
>  I have been playing around with Murrey on the D1 for a while recently and it is interesting how price tends to respect these lines quite a lot. This is definitely a good candidate for an EA. I wonder if Sir Steve Hopwood would be interested... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>    
>  I would like to add that it would also be useful to have Steve's Trade Manager EA manage the trades. When I was trying to some trading off the D1 Murreys, I was using this EA to manage the trade. I found the following features useful, and you might want to try them as...
> 
> Ignored

Sorry Invisible, I overlooked your post.  
  
I like your suggestions and sure will be considered during EA developments.  
  
I appreciate the time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#19](/thread/post/4016463#post4016463 "Post Permalink")

  * Sep 13, 2010 6:48am  Sep 13, 2010 6:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar64206_3.gif) ChicagoRob](chicagorob)

  * | Joined Mar 2008  | Status: Trader | [901 Posts](/search?do=process&provider=Member&searchuser=64206)

> [Quoting mostashar15](/thread/post/4016406#post4016406 "View Quoted Post")
> 
> Disliked
> 
> No it does not.  
>    
>  8/8 to +2/8P => go for SELL signals only.  
>  0/8 to 8/8 => go for both BUY and SELL signals.  
>  -2/8 to 0/8 => go for BUY signals only.  
>    
>  I hope this clarifies it.
> 
> Ignored

Yes, it does. Sorry for the confusion, since there is another MM system floating around that advises to only initiate trades at the extreme levels.  
The analogy is price equates to a rubber band: the farther away it gets from the mean, the higher the force to return to the mean.  
  
Rob 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#20](/thread/post/4016529#post4016529 "Post Permalink")

  * Sep 13, 2010 7:43am  Sep 13, 2010 7:43am 

  * [ aelimian](aelimian)

  * | Joined Oct 2004  | Status: Trader | [438 Posts](/search?do=process&provider=Member&searchuser=1172)

> [Quoting mostashar15](/thread/post/4016303#post4016303 "View Quoted Post")
> 
> Disliked
> 
> There is no other indicators required. You just install the MQL4 file and insert the template. You should get it setup.
> 
> Ignored

  
The Murray and recommendations portion are not showing up on my platform FXDD. Any suggestions? Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#21](/thread/post/4016660#post4016660 "Post Permalink")

  * Sep 13, 2010 9:33am  Sep 13, 2010 9:33am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting aelimian](/thread/post/4016529#post4016529 "View Quoted Post")
> 
> Disliked
> 
> The Murray and recommendations portion are not showing up on my platform FXDD. Any suggestions? Thanks
> 
> Ignored

I am not sure why, but try to add the indicator from custom indicators list manually without the template. Also, please PM me with a snapshot of your screen to hep further. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#22](/thread/post/4016743#post4016743 "Post Permalink")

  * Sep 13, 2010 10:25am  Sep 13, 2010 10:25am 

  * [ aelimian](aelimian)

  * | Joined Oct 2004  | Status: Trader | [438 Posts](/search?do=process&provider=Member&searchuser=1172)

> [Quoting mostashar15](/thread/post/4016660#post4016660 "View Quoted Post")
> 
> Disliked
> 
> I am not sure why, but try to add the indicator from custom indicators list manually without the template. Also, please PM me with a snapshot of your screen to hep further.
> 
> Ignored

  
Please post the respective indicators. Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#23](/thread/post/4016841#post4016841 "Post Permalink")

  * Sep 13, 2010 12:08pm  Sep 13, 2010 12:08pm 

  * [ Blackeagle](blackeagle)

  * Joined Aug 2005 | Status: Trader | [1,188 Posts](/search?do=process&provider=Member&searchuser=3166)

> [Quoting mostashar15](/thread/post/4016262#post4016262 "View Quoted Post")
> 
> Disliked
> 
> What I have been doing is that I get in immediately whenever there is a signal even if the candle did not close with exception after weekend. I usually wait at least for the close of one new candle to confirm the direction during the opening of Asian market after the weekend.
> 
> Ignored

Since you are not waiting for the candle close and your indi shows real time status, is it possible to add a feature to indi which shows the price the signal is given so that if a trader is not in front of the screen while the signal is given, he/she can open the position later on especially if the position is in a loss?  
  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#24](/thread/post/4016911#post4016911 "Post Permalink")

  * Sep 13, 2010 1:35pm  Sep 13, 2010 1:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

nice thread...subscribed...  
waiting for results ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#25](/thread/post/4016969#post4016969 "Post Permalink")

  * Sep 13, 2010 2:34pm  Sep 13, 2010 2:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar86393_9.gif) J e M y](j*e*m*y)

  * | Joined Nov 2008  | Status: Trader | [76 Posts](/search?do=process&provider=Member&searchuser=86393)

Eur/usd buy signal 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#26](/thread/post/4017345#post4017345 "Post Permalink")

  * Sep 13, 2010 5:53pm  Sep 13, 2010 5:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar61335_2.gif) courtneywild](courtneywild)

  * | Joined Feb 2008  | Status: Trader | [678 Posts](/search?do=process&provider=Member&searchuser=61335)

Thank you for posting this. I have been using MM lines for some time and they are very helpful and your system appears to be a very nice way to intergrate them. Started demo this morning +26 EUR/USD so a nice start.  
  
Once again thank you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#27](/thread/post/4017398#post4017398 "Post Permalink")

  * Sep 13, 2010 6:26pm  Sep 13, 2010 6:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar136638_2.gif) xfiles](xfiles)

  * | Joined Mar 2010  | Status: Buy, Sell, Buy, Sell | [30 Posts](/search?do=process&provider=Member&searchuser=136638)

Thank you for system.  
  
Regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#28](/thread/post/4017458#post4017458 "Post Permalink")

  * Sep 13, 2010 7:00pm  Sep 13, 2010 7:00pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

I would like to share my results so far with this version 2.2 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: MurreyAdvisor_v2.2_reults_13092010.PNG
Size: 17 KB](/attachment/image/542421/thumbnail?d=1365648967)](/attachment/image/542421?d=1284371988)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#29](/thread/post/4017464#post4017464 "Post Permalink")

  * Sep 13, 2010 7:03pm  Sep 13, 2010 7:03pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting courtneywild](/thread/post/4017345#post4017345 "View Quoted Post")
> 
> Disliked
> 
> Thank you for posting this. I have been using MM lines for some time and they are very helpful and your system appears to be a very nice way to intergrate them. Started demo this morning +26 EUR/USD so a nice start.  
>    
>  Once again thank you.
> 
> Ignored

I am glad that was successful. I was away from my platform and thus I could not get in otherwise, it would have even improved the indicator success statistics.  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#30](/thread/post/4017487#post4017487 "Post Permalink")

  * Sep 13, 2010 7:13pm  Sep 13, 2010 7:13pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting Blackeagle](/thread/post/4016841#post4016841 "View Quoted Post")
> 
> Disliked
> 
> Since you are not waiting for the candle close and your indi shows real time status, is it possible to add a feature to indi which shows the price the signal is given so that if a trader is not in front of the screen while the signal is given, he/she can open the position later on especially if the position is in a loss?  
>    
>  Regards
> 
> Ignored

I am not so good with MQL4. I have very basic and limited knowledge. I will see what I can do with this regard. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#31](/thread/post/4017498#post4017498 "Post Permalink")

  * Sep 13, 2010 7:22pm  Sep 13, 2010 7:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

lets see this short signal 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: cad short.png
Size: 60 KB](/attachment/image/542431/thumbnail?d=1365648967)](/attachment/image/542431?d=1284373307)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#32](/thread/post/4017541#post4017541 "Post Permalink")

  * Sep 13, 2010 7:46pm  Sep 13, 2010 7:46pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting tahshoon](/thread/post/4017498#post4017498 "View Quoted Post")
> 
> Disliked
> 
> lets see this short signal
> 
> Ignored

Your entry will be interesting to me since you are using different broker platform than mine. I am using FxSol which uses USA eastern time.  
  
My new candles are @ 8:00, 12:00, 16:00, 20:00 and 4:00 ET therefore, I still have about 73 minutes till new candle. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#33](/thread/post/4017606#post4017606 "Post Permalink")

  * Sep 13, 2010 8:17pm  Sep 13, 2010 8:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

EA buggy ?  
attached on chart but nothing happens : p 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#34](/thread/post/4017607#post4017607 "Post Permalink")

  * Sep 13, 2010 8:17pm  Sep 13, 2010 8:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting mostashar15](/thread/post/4017541#post4017541 "View Quoted Post")
> 
> Disliked
> 
> Your entry will be interesting to me since you are using different broker platform than mine. I am using FxSol which uses USA eastern time.  
>    
>  My new candles are @ 8:00, 12:00, 16:00, 20:00 and 4:00 ET therefore, I still have about 73 minutes till new candle.
> 
> Ignored

thnx for ur reply... a nice work , as u said ,we r testing , i hope that it will works fine ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#35](/thread/post/4017617#post4017617 "Post Permalink")

  * Sep 13, 2010 8:22pm  Sep 13, 2010 8:22pm 

  * [ vince](vince)

  * | Joined Mar 2009  | Status: Trader | [162 Posts](/search?do=process&provider=Member&searchuser=95373)

So in case with CAD you wait for close of the candle?  
  

> [Quoting mostashar15](/thread/post/4016262#post4016262 "View Quoted Post")
> 
> Disliked
> 
> What I have been doing is that I get in immediately whenever there is a signal even if the candle did not close with exception after weekend. I usually wait at least for the close of one new candle to confirm the direction during the opening of Asian market after the weekend.
> 
> Ignored

Are yours MM levels any different form the ones tahshoon posted? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#36](/thread/post/4017641#post4017641 "Post Permalink")

  * Sep 13, 2010 8:32pm  Sep 13, 2010 8:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

this is my clasic chart .. to compare 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 4 h trend.png
Size: 52 KB](/attachment/image/542473/thumbnail?d=1365648997)](/attachment/image/542473?d=1284377553)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#37](/thread/post/4017758#post4017758 "Post Permalink")

  * Sep 13, 2010 9:24pm  Sep 13, 2010 9:24pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

After my close of 4Hr candle, now I have Go Short on USDCAD.  
  
Let us see 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: usdcad_13092010_0820_sell.gif
Size: 29 KB](/attachment/image/542497/thumbnail?d=1365648997)](/attachment/image/542497?d=1284380669)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#38](/thread/post/4017766#post4017766 "Post Permalink")

  * Sep 13, 2010 9:28pm  Sep 13, 2010 9:28pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting vince](/thread/post/4017617#post4017617 "View Quoted Post")
> 
> Disliked
> 
> So in case with CAD you wait for close of the candle?  
>    
>  Are yours MM levels any different form the ones tahshoon posted?
> 
> Ignored

Simply, once you see Go Short, just get in.  
  
I am not sure what tahshoon used to plot Murrey Lines but for my case I used one existing code for Murrey (I just forgot who originally developed it) then I added the additional required indicators. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#39](/thread/post/4017771#post4017771 "Post Permalink")

  * Sep 13, 2010 9:31pm  Sep 13, 2010 9:31pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting PhAnTi'](/thread/post/4017606#post4017606 "View Quoted Post")
> 
> Disliked
> 
> EA buggy ?  
>  attached on chart but nothing happens : p
> 
> Ignored

This is strange. It should work. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#40](/thread/post/4017906#post4017906 "Post Permalink")

  * Sep 13, 2010 10:39pm  Sep 13, 2010 10:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

we have a long signal , watching ... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: euro long.png
Size: 64 KB](/attachment/image/542541/thumbnail?d=1365648997)](/attachment/image/542541?d=1284385167)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#41](/thread/post/4017922#post4017922 "Post Permalink")

  * Sep 13, 2010 10:44pm  Sep 13, 2010 10:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

wow so far this is working out out lovely, later this week i will post my results. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#42](/thread/post/4017967#post4017967 "Post Permalink")

  * Sep 13, 2010 11:03pm  Sep 13, 2010 11:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

Do you think you can update this thread like daily to show the trades you have made each day using this.   
  
Although i do find the tool really really easy to use (nice interface) I think it would be useful because for those of us using this tool now we can check to see if we are making the right trades with you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#43](/thread/post/4017990#post4017990 "Post Permalink")

  * Sep 13, 2010 11:15pm  Sep 13, 2010 11:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar132525_2.gif) Centu](centu)

  * | Joined Feb 2010  | Status: Trader | [54 Posts](/search?do=process&provider=Member&searchuser=132525)

Also installed the system and give it a try.  
  
Maybe some mistake/MT bug/my user setting ?  
I see the "Pips till ..." in 3 digit way.  
  
Anyone else with same "bug" ? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eurusd4h.gif
Size: 177 KB](/attachment/image/542563/thumbnail?d=1365649033)](/attachment/image/542563?d=1284387306)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#44](/thread/post/4018010#post4018010 "Post Permalink")

  * Sep 13, 2010 11:22pm  Sep 13, 2010 11:22pm 

  * [ fxpilot](fxpilot)

  * | Joined Aug 2008  | Status: Surf The Waves | [177 Posts](/search?do=process&provider=Member&searchuser=77895)

Great work Mostashar15. Very nice indicator and simple to use. Will try it out and provide feedback. Thanks for sharing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#45](/thread/post/4018072#post4018072 "Post Permalink")

  * Sep 13, 2010 11:41pm  Sep 13, 2010 11:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

Hi  
  
On my 4 hour chart EUR/USD its also saying PIPS to resistance 332.   
  
I dont know, but I think its the way my MT4 is setup with decimal placing.   
  
I think it should be read as 33 pips. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: murray.png
Size: 69 KB](/attachment/image/542582/thumbnail?d=1365649033)](/attachment/image/542582?d=1284388874)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#46](/thread/post/4018077#post4018077 "Post Permalink")

  * Sep 13, 2010 11:42pm  Sep 13, 2010 11:42pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting tahshoon](/thread/post/4017906#post4017906 "View Quoted Post")
> 
> Disliked
> 
> we have a long signal , watching ...
> 
> Ignored

Who is your broker? It is interesting because you are getting the entry signal ahead of us. This should give you better position and profit than us. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#47](/thread/post/4018087#post4018087 "Post Permalink")

  * Sep 13, 2010 11:45pm  Sep 13, 2010 11:45pm 

  * [ fxpilot](fxpilot)

  * | Joined Aug 2008  | Status: Surf The Waves | [177 Posts](/search?do=process&provider=Member&searchuser=77895)

> [Quoting tahshoon](/thread/post/4017641#post4017641 "View Quoted Post")
> 
> Disliked
> 
> this is my clasic chart .. to compare
> 
> Ignored

Nice chart Tahshoon. I notice your 4 hour MACD is different from mine. Which MACD are you using. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#48](/thread/post/4018088#post4018088 "Post Permalink")

  * Sep 13, 2010 11:45pm  Sep 13, 2010 11:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135988_2.gif) Goldflight](goldflight)

  * | Joined Mar 2010  | Status: Trader | [263 Posts](/search?do=process&provider=Member&searchuser=135988)

Very nice work. Will follow along......... 

I AM WHAT I AM, AND THATS ALL THAT I AM

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#49](/thread/post/4018092#post4018092 "Post Permalink")

  * Sep 13, 2010 11:46pm  Sep 13, 2010 11:46pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting DrLobo](/thread/post/4017967#post4017967 "View Quoted Post")
> 
> Disliked
> 
> Do you think you can update this thread like daily to show the trades you have made each day using this.   
>    
>  Although i do find the tool really really easy to use (nice interface) I think it would be useful because for those of us using this tool now we can check to see if we are making the right trades with you.
> 
> Ignored

Sure, I will do. As I said I cannot watch all trades as I might be away from my platform. I think if everybody shares his results, we will be able to cover most of them. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#50](/thread/post/4018095#post4018095 "Post Permalink")

  * Sep 13, 2010 11:46pm  Sep 13, 2010 11:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

This is due to the way you have MT4 leverage setup.  
  
The way you need to read this is by placing decimal spot one place to the left.  
  
  
  

> [Quoting Centu](/thread/post/4017990#post4017990 "View Quoted Post")
> 
> Disliked
> 
> Also installed the system and give it a try.  
>    
>  Maybe some mistake/MT bug/my user setting ?  
>  I see the "Pips till ..." in 3 digit way.  
>    
>  Anyone else with same "bug" ?
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#51](/thread/post/4018098#post4018098 "Post Permalink")

  * Sep 13, 2010 11:47pm  Sep 13, 2010 11:47pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting Centu](/thread/post/4017990#post4017990 "View Quoted Post")
> 
> Disliked
> 
> Also installed the system and give it a try.  
>    
>  Maybe some mistake/MT bug/my user setting ?  
>  I see the "Pips till ..." in 3 digit way.  
>    
>  Anyone else with same "bug" ?
> 
> Ignored

I guess, because the code is made for 4 digit broker. I will modify and share to suit 5 digit brokers as well. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#52](/thread/post/4018100#post4018100 "Post Permalink")

  * Sep 13, 2010 11:48pm  Sep 13, 2010 11:48pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting fxpilot](/thread/post/4018010#post4018010 "View Quoted Post")
> 
> Disliked
> 
> Great work Mostashar15. Very nice indicator and simple to use. Will try it out and provide feedback. Thanks for sharing.
> 
> Ignored

Thanks for the nice words. I'll be waiting for your results. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#53](/thread/post/4018105#post4018105 "Post Permalink")

  * Sep 13, 2010 11:49pm  Sep 13, 2010 11:49pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting DrLobo](/thread/post/4018072#post4018072 "View Quoted Post")
> 
> Disliked
> 
> Hi  
>    
>  On my 4 hour chart EUR/USD its also saying PIPS to resistance 332.   
>    
>  I dont know, but I think its the way my MT4 is setup with decimal placing.   
>    
>  I think it should be read as 33 pips.
> 
> Ignored

It is because your are using 5 decimal broker. I will be modifying the code to suit everybody. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#54](/thread/post/4018136#post4018136 "Post Permalink")

  * Sep 14, 2010 12:00am  Sep 14, 2010 12:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar85797_8.gif) goldsurfer](goldsurfer)

  * | Joined Nov 2008  | Status: Trader | [575 Posts](/search?do=process&provider=Member&searchuser=85797)

_mostashar15_  
  
Hi There  
  
Good Work it appears![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Curious as to the selection of pairs that you trade?   
  
You had best results on these vs. other currency pairs?  
  
cheers 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#55](/thread/post/4018153#post4018153 "Post Permalink")

  * Sep 14, 2010 12:04am  Sep 14, 2010 12:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar64206_3.gif) ChicagoRob](chicagorob)

  * | Joined Mar 2008  | Status: Trader | [901 Posts](/search?do=process&provider=Member&searchuser=64206)

> [Quoting mostashar15](/thread/post/4017458#post4017458 "View Quoted Post")
> 
> Disliked
> 
> I would like to share my results so far with this version 2.2
> 
> Ignored

If you can maintain this level of consistency, you will be a rich man, indeed.  
  
Rob 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#56](/thread/post/4018162#post4018162 "Post Permalink")

  * Sep 14, 2010 12:06am  Sep 14, 2010 12:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting mostashar15](/thread/post/4018077#post4018077 "View Quoted Post")
> 
> Disliked
> 
> Who is your broker? It is interesting because you are getting the entry signal ahead of us. This should give you better position and profit than us.
> 
> Ignored

mr.mostashar ... i see that ur rang is higher than mostashar to be... a nice work, more than excellent , my broker is uranus investment -dubai 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: close to close.png
Size: 72 KB](/attachment/image/542603/thumbnail?d=1365649033)](/attachment/image/542603?d=1284390393)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#57](/thread/post/4018205#post4018205 "Post Permalink")

  * Sep 14, 2010 12:18am  Sep 14, 2010 12:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting fxpilot](/thread/post/4018087#post4018087 "View Quoted Post")
> 
> Disliked
> 
> Nice chart Tahshoon. I notice your 4 hour MACD is different from mine. Which MACD are you using.
> 
> Ignored

the macd u saw in my chart is down there(attachment)  
if u want it to be like mine make the setting to show histo=true  
u r welcome 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [MACD_OsMA_4ColorH_2LVar_mtf.ex4](/attachment/file/542613?d=1284391095) 8 KB | 304 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#58](/thread/post/4018217#post4018217 "Post Permalink")

  * Sep 14, 2010 12:21am  Sep 14, 2010 12:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar61335_2.gif) courtneywild](courtneywild)

  * | Joined Feb 2008  | Status: Trader | [678 Posts](/search?do=process&provider=Member&searchuser=61335)

mostashar15  
  
Closed my trades for the day...  
  
3 trades...  
  
EUR USD +26  
EUR GBP +19  
USD CAD +16  
  
Total for day +61   
  
To be honest the EURGB USDCAD have more miles in them but thats my day done.  
  
Qs   
Do you hold overnight ever?  
If in a trade and the signal turns to hold do you exit?  
If you exit and the trend regains original path, when will the EA send a new signal?  
Sorry if these are junior school questions.  
  
Thanks for 61 pips.  
  
Abiento. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#59](/thread/post/4018243#post4018243 "Post Permalink")

  * Sep 14, 2010 12:36am  Sep 14, 2010 12:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar132525_2.gif) Centu](centu)

  * | Joined Feb 2010  | Status: Trader | [54 Posts](/search?do=process&provider=Member&searchuser=132525)

> [Quoting mostashar15](/thread/post/4018098#post4018098 "View Quoted Post")
> 
> Disliked
> 
> I guess, because the code is made for 4 digit broker. I will modify and share to suit 5 digit brokers as well.
> 
> Ignored

Thx ! Great work btw ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
Closed Trades:  
EUR/USD +32  
USD/CAD +11  
  
Still open:  
USD/JPY and another USD/CAD 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#60](/thread/post/4018296#post4018296 "Post Permalink")

  * Sep 14, 2010 12:56am  Sep 14, 2010 12:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

a nice job done ... mostashar thnx very much 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: euro closed.png
Size: 62 KB](/attachment/image/542651/thumbnail?d=1365649033)](/attachment/image/542651?d=1284393370)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#61](/thread/post/4018314#post4018314 "Post Permalink")

  * Sep 14, 2010 1:03am  Sep 14, 2010 1:03am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting tahshoon](/thread/post/4018162#post4018162 "View Quoted Post")
> 
> Disliked
> 
> mr.mostashar ... i see that ur rang is higher than mostashar to be... a nice work, more than excellent , my broker is uranus investment -dubai
> 
> Ignored

Target Achieved, +22 pips 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#62](/thread/post/4018324#post4018324 "Post Permalink")

  * Sep 14, 2010 1:06am  Sep 14, 2010 1:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

I turned 100 pound account (it still a demo account) into 150 pounds today with 0.50 per PIP. Here were my trades.  
  
Eur/USD = 40 pips  
USD/CHF = 32 pips  
USD/JPY = 31 pips  
USD/CAD = 8 pips (not sure if this trade was done on a 4h time chart looks odd to me)  
  
I am still running another trade on the USD/CAD which I am shorting and I am 8 pips up.   
  
  
Anyway 111 PIPS banked today !!  
  
Honestly I have never ever made 111 PIPS in my wildest dreams !   
  
I am in total shock its a bit insane i expecting some turn of events to even up the scores this week and bring me back to reality.  
  
Big thanks from me ! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#63](/thread/post/4018345#post4018345 "Post Permalink")

  * Sep 14, 2010 1:14am  Sep 14, 2010 1:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar136638_2.gif) xfiles](xfiles)

  * | Joined Mar 2010  | Status: Buy, Sell, Buy, Sell | [30 Posts](/search?do=process&provider=Member&searchuser=136638)

26+15+15=56 pips. I use signal same scalping.  
Thank you friend. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#64](/thread/post/4018352#post4018352 "Post Permalink")

  * Sep 14, 2010 1:18am  Sep 14, 2010 1:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar132525_2.gif) Centu](centu)

  * | Joined Feb 2010  | Status: Trader | [54 Posts](/search?do=process&provider=Member&searchuser=132525)

> [Quoting Centu](/thread/post/4018243#post4018243 "View Quoted Post")
> 
> Disliked
> 
> Closed Trades:  
>  EUR/USD +32  
>  USD/CAD +11  
>    
>  Still open:  
>  USD/JPY and another USD/CAD
> 
> Ignored

Done for the day  
  
USD/JPY +20,5  
USD/CAD be  
  
total 63,5 - not that bad ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#65](/thread/post/4018381#post4018381 "Post Permalink")

  * Sep 14, 2010 1:32am  Sep 14, 2010 1:32am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting mostashar15](/thread/post/4018098#post4018098 "View Quoted Post")
> 
> Disliked
> 
> I guess, because the code is made for 4 digit broker. I will modify and share to suit 5 digit brokers as well.
> 
> Ignored

This version should work with 5 digit brokers. Please let me know once you try it and works fine for you so that I will update post #1 to include this version as well. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [murrey advisor 5dec.zip](/attachment/file/542669?d=1284395597) 9 KB | 381 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#66](/thread/post/4018392#post4018392 "Post Permalink")

  * Sep 14, 2010 1:36am  Sep 14, 2010 1:36am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting DrLobo](/thread/post/4018324#post4018324 "View Quoted Post")
> 
> Disliked
> 
> I turned 100 pound account (it still a demo account) into 150 pounds today with 0.50 per PIP. Here were my trades.  
>    
>  Eur/USD = 40 pips  
>  USD/CHF = 32 pips  
>  USD/JPY = 31 pips  
>  USD/CAD = 8 pips (not sure if this trade was done on a 4h time chart looks odd to me)  
>    
>  I am still running another trade on the USD/CAD which I am shorting and I am 8 pips up.   
>    
>    
>  Anyway 111 PIPS banked today !!  
>    
>  Honestly I have never ever made 111 PIPS in my wildest dreams !   
>    
>  I am in total shock its a bit insane i expecting some turn of events to even up the scores...
> 
> Ignored

Wo0o0o0oW  
  
Very glad to see this numer of pips earned by this code. I think today was a good day for trading which triggered this much of signals. Typical days maybe you will see around 60 pips as an average.  
  
Congrats 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#67](/thread/post/4018483#post4018483 "Post Permalink")

  * Sep 14, 2010 2:30am  Sep 14, 2010 2:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

setup for 5 digit broker is working very nice,all thnx for our mostashar for a great well done job ... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 5 digit broker.png
Size: 58 KB](/attachment/image/542693/thumbnail?d=1365649075)](/attachment/image/542693?d=1284398994)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#68](/thread/post/4018511#post4018511 "Post Permalink")

  * Sep 14, 2010 2:46am  Sep 14, 2010 2:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting Invisible](/thread/post/4016395#post4016395 "View Quoted Post")
> 
> Disliked
> 
> Excellent work, mostashar15.  
>    
>  I have been playing around with Murrey on the D1 for a while recently and it is interesting how price tends to respect these lines quite a lot. This is definitely a good candidate for an EA. I wonder if Sir Steve Hopwood would be interested... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

Yes, he is.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#69](/thread/post/4018530#post4018530 "Post Permalink")

  * Sep 14, 2010 3:05am  Sep 14, 2010 3:05am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting SteveHopwood](/thread/post/4018511#post4018511 "View Quoted Post")
> 
> Disliked
> 
> Yes, he is.  
>    
>  ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

Wo00o0oW  
  
Look who is here.  
  
Thanks Steve for dropping by. I will be curios to see what your hands will do for us. I just cannot wait. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#70](/thread/post/4018534#post4018534 "Post Permalink")

  * Sep 14, 2010 3:06am  Sep 14, 2010 3:06am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting tahshoon](/thread/post/4018483#post4018483 "View Quoted Post")
> 
> Disliked
> 
> setup for 5 digit broker is working very nice,all thnx for our mostashar for a great well done job ...
> 
> Ignored

Thanks for the trial. I will update the Post #1 accordingly. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#71](/thread/post/4018546#post4018546 "Post Permalink")

  * Sep 14, 2010 3:15am  Sep 14, 2010 3:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

I do not really understand indicators, but do know this: rather than have separate indis for 4 and 5 digit crims, have one that will identify the number of digits in the quote and take things from there.  
  
I _think_ the attached does this. When you are sure it works equally well on 4 digit crim accounts (I have only tested it on 5 digit), then simply delete the 'Mod Steve' from the indi name and replace the current versions with this single one.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#72](/thread/post/4018551#post4018551 "Post Permalink")

  * Sep 14, 2010 3:17am  Sep 14, 2010 3:17am 

  * [ ejikz](ejikz)

  * | Joined Jan 2010  | Status: Trader | [124 Posts](/search?do=process&provider=Member&searchuser=131860)

You are welcome to this thread....and we believe you will make this new strategy a masterpiece with your EA  
Thank you once again for all your support in the forum 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#73](/thread/post/4018552#post4018552 "Post Permalink")

  * Sep 14, 2010 3:18am  Sep 14, 2010 3:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

Oops. Forgot to attach it. Here it is. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Murrey Advisor V2.2 Mod Steve.mq4](/attachment/file/542722?d=1284402057) 48 KB | 318 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#74](/thread/post/4018554#post4018554 "Post Permalink")

  * Sep 14, 2010 3:20am  Sep 14, 2010 3:20am 

  * [ Invisible](invisible)

  * | Joined Nov 2009  | Status: Trader | [469 Posts](/search?do=process&provider=Member&searchuser=124048)

Sir Steve's in the house. Woot!  
  
BTW, just closed a demo long on EURGBP using Steve's MPTM to manage it: $23 Monopoly dollars profit on 0.1 lot. Could possibly have been left to run for longer, but I had the trailing stop tightening to lock in profits and it did just that.  
  
Cheers!  
  
Invisible 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#75](/thread/post/4018572#post4018572 "Post Permalink")

  * Sep 14, 2010 3:33am  Sep 14, 2010 3:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting Invisible](/thread/post/4018554#post4018554 "View Quoted Post")
> 
> Disliked
> 
> Sir Steve's in the house. Woot!
> 
> Ignored

Yes he is, and very, _very_ interested.   
  
mostashar15, anyone who spends 5 years developing a system then shares it with others deserves some attention.  
  
In order to code an ea to trade signals from the indi, it needs to store something in a buffer that the ea can interrogate to see what the current status is.  
  
Looking through the code, there is no such buffer but I see these three lines of code:  
string advisor = "HOLD!";  
advisor = "Go Long";  
advisor = "Go Short";  
  
If someone here can add a buffer that holds:

  1. 0 for "HOLD!"
  2. 1 for "Go Long"
  3. 2 for "Go Short"

at these points, then I can take things from there.  
  
Ok, so I am going to play with this, but an indi coder can probably save me a shed-load of chaos and confusion.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#76](/thread/post/4018616#post4018616 "Post Permalink")

  * Sep 14, 2010 4:05am  Sep 14, 2010 4:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> Quote
> 
> Disliked
> 
> Once you get in LONG position, then your TP = next resistance (usually from 30 to 60 points based on Murrey span) and SL = -30 points.

  
there's no automatic sl/tp when i go short?   
or did i miss s.th?  
  
  
thank you so much for your content and ideas and your development.. 5 years of work and we just have to download 2 files in 10 seconds and start trading...  
  
uhhm that's pretty unfair...  
I'd voucher for you but still can't ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
best regards  
Phanti 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#77](/thread/post/4018629#post4018629 "Post Permalink")

  * Sep 14, 2010 4:12am  Sep 14, 2010 4:12am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

I was watching some of the failing signals. As you see once there is a trend up, the candle will move above EMA(5,close) {the green line} and after some time, it will retrace back to test EMA(5,close) and continue moving up.  
  
I noticed whenever the prices is over 25 pips above EMA(5,close), then it re-traces back. Therefore, I am thinking to add a new condition which is Close[0] is not more than 20 pips above EMA(5,close) in case of long and not more than 20 pips below EMA(5,close) in case of short.  
  
I believe this will not affect number of trades dramatically. but rather will improve profitability further.  
  
Any suggestions and thoughts? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eurusd_newcond.gif
Size: 31 KB](/attachment/image/542742/thumbnail?d=1365649075)](/attachment/image/542742?d=1284405139)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#78](/thread/post/4018640#post4018640 "Post Permalink")

  * Sep 14, 2010 4:18am  Sep 14, 2010 4:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting mostashar15](/thread/post/4018629#post4018629 "View Quoted Post")
> 
> Disliked
> 
> I was watching some of the failing signals. As you see once there is a trend up, the candle will move above EMA(5,close) {the green line} and after some time, it will retrace back to test EMA(5,close) and continue moving up.  
>    
>  I noticed whenever the prices is over 25 pips above EMA(5,close), then it re-traces back. Therefore, I am thinking to add a new condition which is Close[0] is not more than 20 pips above EMA(5,close) in case of long and not more than 20...
> 
> Ignored

> Quote
> 
> Disliked
> 
> **I believe this will not affect number of trades dramatically. but rather will improve profitability further.**

  
I think we should try whether number of trades is being damaged...  
less trades + better profit > more trades and less profit...  
  
let's give it a try  
  
got another question:  
why exactly those 7 pairs and no other pairs?  
do u have special reasons ?  
  
best regards  
Phanti 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#79](/thread/post/4018662#post4018662 "Post Permalink")

  * Sep 14, 2010 4:36am  Sep 14, 2010 4:36am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting PhAnTi'](/thread/post/4018640#post4018640 "View Quoted Post")
> 
> Disliked
> 
> I think we should try whether number of trades is being damaged...  
>  less trades + better profit > more trades and less profit...  
>    
>  let's give it a try  
>    
>  got another question:  
>  why exactly those 7 pairs and no other pairs?  
>  do u have special reasons ?  
>    
>  best regards  
>  Phanti
> 
> Ignored

Ok, we will keep using the current version for more time and collect more feedback.  
  
Regarding the 7 pairs, there are two reasons:

  1. They gave me better results with old versions but to be honest with you I did not test on this version.  

  2. The other reason, is that I like to take pairs with no more than 5 pips max spread and as per my broker FxSol, it is those pairs.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#80](/thread/post/4018670#post4018670 "Post Permalink")

  * Sep 14, 2010 4:40am  Sep 14, 2010 4:40am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting PhAnTi'](/thread/post/4018616#post4018616 "View Quoted Post")
> 
> Disliked
> 
> there's no automatic sl/tp when i go short?   
>  or did i miss s.th?  
>    
>    
>  thank you so much for your content and ideas and your development.. 5 years of work and we just have to download 2 files in 10 seconds and start trading...  
>    
>  uhhm that's pretty unfair...  
>  I'd voucher for you but still can't ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
>    
>  best regards  
>  Phanti
> 
> Ignored

This indicator will not do any trading for you. It is all manual. Our friend Steve is working on developing EA to do it on Auto. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#81](/thread/post/4018679#post4018679 "Post Permalink")

  * Sep 14, 2010 4:48am  Sep 14, 2010 4:48am 

  * [ Indrek](indrek)

  * Joined Jun 2009 | Status: Trader | [2,430 Posts](/search?do=process&provider=Member&searchuser=106754)

> [Quoting mostashar15](/thread/post/4018629#post4018629 "View Quoted Post")
> 
> Disliked
> 
> Therefore, I am thinking to add a new condition which is Close[0] is not more than 20 pips above EMA(5,close) in case of long and not more than 20 pips below EMA(5,close) in case of short.  
>    
>  I believe this will not affect number of trades dramatically. but rather will improve profitability further.  
>    
>  Any suggestions and thoughts?
> 
> Ignored

Different pairs have different volatility, so I would not suggest to use the same number of pips for all. The same refers to SL.  
I personally use ATR to define the values. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#82](/thread/post/4018701#post4018701 "Post Permalink")

  * Sep 14, 2010 5:01am  Sep 14, 2010 5:01am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting courtneywild](/thread/post/4018217#post4018217 "View Quoted Post")
> 
> Disliked
> 
> mostashar15  
>    
>  Closed my trades for the day...  
>    
>  3 trades...  
>    
>  EUR USD +26  
>  EUR GBP +19  
>  USD CAD +16  
>    
>  Total for day +61   
>    
>  To be honest the EURGB USDCAD have more miles in them but thats my day done.  
>    
>  Qs   
>  Do you hold overnight ever?  
>  If in a trade and the signal turns to hold do you exit?  
>  If you exit and the trend regains original path, when will the EA send a new signal?  
>  Sorry if these are junior school questions.  
>    
>  Thanks for 61 pips.  
>    
>  Abiento.
> 
> Ignored

> Quote
> 
> Disliked
> 
> Do you hold overnight ever?

Yes, I do in particular for AUDUSD and NZDUSD as they see some good moves during Asian market.  
  

> Quote
> 
> Disliked
> 
> If in a trade and the signal turns to hold do you exit?

No I don't. It is either TP or SL.  
  

> Quote
> 
> Disliked
> 
> If you exit and the trend regains original path, when will the EA send a new signal?

Yes, it will give another signal. But you may want to look at this observation before you try to decide to get in again. We have not incorporated this yet in the code becasue we want to run the current version (v2.2) more time then we collect feedback.  
  
[http://www.forexfactory.com/showpost...9&postcount=77](http://www.forexfactory.com/showpost.php?p=4018629&postcount=77)  
  

> Quote
> 
> Disliked
> 
> Sorry if these are junior school questions.

Do not worry. We are all here to learn, buddy.  
  

> Quote
> 
> Disliked
> 
> Thanks for 61 pips.

Enjoy it 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#83](/thread/post/4018709#post4018709 "Post Permalink")

  * Sep 14, 2010 5:06am  Sep 14, 2010 5:06am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting Indrek](/thread/post/4018679#post4018679 "View Quoted Post")
> 
> Disliked
> 
> Different pairs have different volatility, so I would not suggest to use the same number of pips for all. The same refers to SL.  
>  I personally use ATR to define the values.
> 
> Ignored

I don't like the idea of having high SL because now if the trade hits your SL, then it will more likely eat profit of two or three winning trades. Therefore, what I see is to hold whever you are away from EMA(5,close) by more than 20 pips and allow some retrace then get in with much lower SL. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#84](/thread/post/4018712#post4018712 "Post Permalink")

  * Sep 14, 2010 5:08am  Sep 14, 2010 5:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> Quote
> 
> Disliked
> 
> The other reason, is that I like to take pairs with no more than 5 pips max spread and as per my broker FxSol, it is those pairs.

  
well okay let's see...  
more pairs = more trades = more profit...  
but big [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") minimize wins or even don't make any sense to start trading with a low tp etc.  
  
let's see  
this thread just needs more feedback to improve system ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#85](/thread/post/4018732#post4018732 "Post Permalink")

  * Sep 14, 2010 5:21am  Sep 14, 2010 5:21am 

  * [ Invisible](invisible)

  * | Joined Nov 2009  | Status: Trader | [469 Posts](/search?do=process&provider=Member&searchuser=124048)

> Quote
> 
> Disliked
> 
> "If you exit and the trend regains original path, when will the EA send a new signal?"  
>    
>  Yes, it will give another signal. But you may want to look at this observation before you try to decide to get in again. We have not incorporated this yet in the code becasue we want to run the current version (v2.2) more time then we collect feedback.

This is an important point for Steve's EA. I think there are two ways forward:

  1. The EA could just take the first signal after a breach of the Murray line and then ignore any subsequent ones until there was another Murray line breach.
  2. The EA could take every signal, even if there are several after the same Murray line has been breached.

Personally, I would tend to favor the former, as the risk with taking subsequent entries is that the market might be ranging rather than powering towards the TP, so it is less likely to produce a good trade. Also, the price is much more likely to be closer to the TP area on the second trade signal (I just saw 3 on the hour just now and this was the case with all of them), so the R:R is going to be much poorer.  
  

> Quote
> 
> Disliked
> 
> "If in a trade and the signal turns to hold do you exit?"  
>    
>  No I don't. It is either TP or SL.

Perhaps this could be an option in the EA: When in a trade, ignore any changes to the status and just let it run, or to close the trade when status changes to "hold". In fact, it would be very useful to be able to test these two in parallel to see which was more profitable. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#86](/thread/post/4018745#post4018745 "Post Permalink")

  * Sep 14, 2010 5:29am  Sep 14, 2010 5:29am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting PhAnTi'](/thread/post/4018712#post4018712 "View Quoted Post")
> 
> Disliked
> 
> well okay let's see...  
>  more pairs = more trades = more profit...  
>  but big spreads minimize wins or even don't make any sense to start trading with a low tp etc.  
>    
>  let's see  
>  **_this thread just needs more feedback to improve system_** ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)
> 
> Ignored

I strongly agree. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#87](/thread/post/4018751#post4018751 "Post Permalink")

  * Sep 14, 2010 5:33am  Sep 14, 2010 5:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar147096_19.gif) tradpat](tradpat)

  * | Joined Jul 2010  | Status: I LOVE MACD | [511 Posts](/search?do=process&provider=Member&searchuser=147096)

> [Quoting tahshoon](/thread/post/4017641#post4017641 "View Quoted Post")
> 
> Disliked
> 
> this is my clasic chart .. to compare
> 
> Ignored

Can you share yours colorful MACD?  
It is easy to read, isn't it?  
Cheers 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#88](/thread/post/4018755#post4018755 "Post Permalink")

  * Sep 14, 2010 5:35am  Sep 14, 2010 5:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> Quote
> 
> Disliked
> 
> In fact, it would be very useful to be able to test these two in parallel to see which was more profitable.

  
don't know but maybe we can set a ts or s.th like that when conditions are changing 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#89](/thread/post/4018801#post4018801 "Post Permalink")

  * Sep 14, 2010 5:58am  Sep 14, 2010 5:58am 

  * [ Invisible](invisible)

  * | Joined Nov 2009  | Status: Trader | [469 Posts](/search?do=process&provider=Member&searchuser=124048)

> [Quoting PhAnTi'](/thread/post/4018755#post4018755 "View Quoted Post")
> 
> Disliked
> 
> don't know but maybe we can set a ts or s.th like that when conditions are changing
> 
> Ignored

The beauty of having this encoded in an EA would be that we can run different scenarios in both back and forward testing to see which are best.   
  
mostashar15 has already given us a good 5 years of work on this, so we know what we are starting with is very solid. Then with Steve's automation it should be possible make it even better. If it can at least follow mostashar15's rules, then we already know it is 75% accurate with good R:R for him on live and demo, so that would be very nice to replicate in itself. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#90](/thread/post/4018832#post4018832 "Post Permalink")

  * Sep 14, 2010 6:12am  Sep 14, 2010 6:12am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting tahshoon](/thread/post/4018162#post4018162 "View Quoted Post")
> 
> Disliked
> 
> mr.mostashar ... i see that ur rang is higher than mostashar to be... a nice work, more than excellent , **my broker is uranus investment -dubai**
> 
> Ignored

I have downloaded their platform and opened a demo account with them. I will be testing their platform. Hopefully, this will yield more pips since their 4 hr candle is closing 1 hour ahead of FxSol. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#91](/thread/post/4018834#post4018834 "Post Permalink")

  * Sep 14, 2010 6:12am  Sep 14, 2010 6:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting tradpat](/thread/post/4018751#post4018751 "View Quoted Post")
> 
> Disliked
> 
> Can you share yours colorful MACD?  
>  It is easy to read, isn't it?  
>  Cheers
> 
> Ignored

its here ... no problem  
[http://www.forexfactory.com/showpost...5&postcount=57](http://www.forexfactory.com/showpost.php?p=4018205&postcount=57)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#92](/thread/post/4018932#post4018932 "Post Permalink")

  * Edited 7:18am  Sep 14, 2010 7:06am | Edited 7:18am 

  * [ plind](plind)

  * | Joined Jun 2006  | Status: Trader | [135 Posts](/search?do=process&provider=Member&searchuser=12124)

Loaded Steve's ver on FXDD (EUR/USD H4),4digit, and IamFX (EUR/USD H4) 5 digit. I don't have Daily Range Statistics on either chart. Also the +,- on each Murray line is "0". I switched time frames to try for reset but still no data. Any ideas? Paul 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#93](/thread/post/4018951#post4018951 "Post Permalink")

  * Sep 14, 2010 7:19am  Sep 14, 2010 7:19am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting plind](/thread/post/4018932#post4018932 "View Quoted Post")
> 
> Disliked
> 
> Loaded Steve's ver on FXDD (EUR/USD H4) and IamFX (EUR/USD H4). I don't have Daily Range Statistics on either chart. Also the +,- on each Murray line is "0". I switched time frames to try for reset but still no data. Any ideas? Paul
> 
> Ignored

I tried it but did not work with me either. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#94](/thread/post/4018959#post4018959 "Post Permalink")

  * Sep 14, 2010 7:22am  Sep 14, 2010 7:22am 

  * [ Invisible](invisible)

  * | Joined Nov 2009  | Status: Trader | [469 Posts](/search?do=process&provider=Member&searchuser=124048)

Could a coder familiar with indicators follow up Steve's request here?  
  

> Quote
> 
> Disliked
> 
> If someone here can add a buffer that holds:
> 
>   1. 0 for "HOLD!"
>   2. 1 for "Go Long"
>   3. 2 for "Go Short"
> 

> 
> at these points, then I can take things from there.

  
[http://www.forexfactory.com/showpost...2&postcount=75](http://www.forexfactory.com/showpost.php?p=4018572&postcount=75)  
  
Thanks  
  
Invisible 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#95](/thread/post/4018980#post4018980 "Post Permalink")

  * Sep 14, 2010 7:35am  Sep 14, 2010 7:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting plind](/thread/post/4018932#post4018932 "View Quoted Post")
> 
> Disliked
> 
> Loaded Steve's ver on FXDD (EUR/USD H4),4digit, and IamFX (EUR/USD H4) 5 digit. I don't have Daily Range Statistics on either chart. Also the +,- on each Murray line is "0". I switched time frames to try for reset but still no data. Any ideas? Paul
> 
> Ignored

Mine have gone too.  
  
As I pointed out earlier, I do not understand indis.  
  
Over to you lot. Produce on that I can interrogate to produce figures that an ea can use and I can code the ea. Until someone does this, there is nothing I can do.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#96](/thread/post/4018986#post4018986 "Post Permalink")

  * Sep 14, 2010 7:38am  Sep 14, 2010 7:38am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

Among all the winning trades today, I have seen two losses:  
1\. EURUSD (-29 pips)  
2\. USDJPY (-33 pips)  
  
The common between the two trades is what I talked about before. There was a very long candle that breached a Murrey level but as the new candle opens, it retraces back.  
  
This can be filtered easily by looking for EMA(5,close) is no more than 25 pips below the close of last candle Close[1] in case of LONG and no more than 25 pips above Close[1].  
  
To be honest, I have already modified the code to incorporate this change in v2.3 but I will not share now. However, I will share some results from both to compare.  
  
Regards 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: jpyusd_newcond.gif
Size: 28 KB](/attachment/image/542817/thumbnail?d=1365649111)](/attachment/image/542817?d=1284417503)   
[![Click to Enlarge

Name: eurusd_newcond.gif
Size: 31 KB](/attachment/image/542818/thumbnail?d=1365649111)](/attachment/image/542818?d=1284417503)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#97](/thread/post/4019032#post4019032 "Post Permalink")

  * Sep 14, 2010 8:11am  Sep 14, 2010 8:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar24884_5.gif) camvcvoo](camvcvoo)

  * | Joined Nov 2006  | Status: Trader | [678 Posts](/search?do=process&provider=Member&searchuser=24884)

> [Quoting mostashar15](/thread/post/4018986#post4018986 "View Quoted Post")
> 
> Disliked
> 
>   
>  To be honest, I have already modified the code to incorporate this change in v2.3 but I will not share now.  
>    
>  Regards
> 
> Ignored

Why?  
  
Will you share with us later?  
  
This improved version will be helpful, at least i think, for Steve's coding of your system into a profitable EA.  
  
Do you have intention to sell it later? I really hope not. If i've misunderstood your intention, please forgive me.![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1)  
  
Cheers.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Ã§Â¦Â Ã¥Â­Â Victor V

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#98](/thread/post/4019073#post4019073 "Post Permalink")

  * Sep 14, 2010 8:48am  Sep 14, 2010 8:48am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting camvcvoo](/thread/post/4019032#post4019032 "View Quoted Post")
> 
> Disliked
> 
> Why?  
>    
>  Will you share with us later?  
>    
>  This improved version will be helpful, at least i think, for Steve's coding of your system into a profitable EA.  
>    
>  Do you have intention to sell it later? I really hope not. If i've misunderstood your intention, please forgive me.![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1)  
>    
>  Cheers.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

If I have intentions to sell, I would not have told you with the change. I believe with the current performance, there are some people who maybe willing to buy it if I sell it for US$ 30 and only if I manage to sell 1000 copies, this is US$ 30,000. ![](https://resources.faireconomy.media/images/emojis/64/263a-fe0f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f4ad.png?v=15.1)  
  
You know, it is not a bad idea at the end. ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)  
  
I am just kidding  
  
This code is no longer mine now, because it will contain thoughts, suggestions and experience of everybody here in this thread. If I decide one day to use it commercially, then I will have first to get your permission. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#99](/thread/post/4019104#post4019104 "Post Permalink")

  * Sep 14, 2010 9:14am  Sep 14, 2010 9:14am 

  * [ heaveyrain](heaveyrain)

  * | Joined Sep 2009  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=114832)

> [Quoting mostashar15](/thread/post/4018709#post4018709 "View Quoted Post")
> 
> Disliked
> 
> I don't like the idea of having high SL because now if the trade hits your SL, then it will more likely eat profit of two or three winning trades. Therefore, what I see is to hold whever you are away from EMA(5,close) by more than 20 pips and allow some retrace then get in with much lower SL.
> 
> Ignored

a suggestion you can use a certain % of the ATR as yr SL. e.g 50% or 70% 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [ATR Pips.ex4](/attachment/file/542846?d=1284423227) 2 KB | 284 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#100](/thread/post/4019163#post4019163 "Post Permalink")

  * Sep 14, 2010 9:48am  Sep 14, 2010 9:48am 

  * [ Pardy](pardy)

  * | Joined Jan 2008  | Status: Trader | [615 Posts](/search?do=process&provider=Member&searchuser=57656)

> [Quoting mostashar15](/thread/post/4018986#post4018986 "View Quoted Post")
> 
> Disliked
> 
> Among all the winning trades today, I have seen two losses:  
>  1\. EURUSD (-29 pips)  
>  2\. USDJPY (-33 pips)  
>    
>  The common between the two trades is what I talked about before. There was a very long candle that breached a Murrey level but as the new candle opens, it retraces back.  
>    
>  This can be filtered easily by looking for EMA(5,close) is no more than 25 pips below the close of last candle Close[1] in case of LONG and no more than 25 pips above Close[1].  
>    
>  To be honest, I have already modified the code to incorporate this change in v2.3 but I will not...
> 
> Ignored

Hi, you might find this indicator useful - It simply displays the distance of price to the ma, so you can easily tell if it is higher than 25 pips.  
For 5 digit brokers, it'll show 10 pips as 100.  
  
Pardy 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [MADistance.mq4](/attachment/file/542865?d=1284425287) 5 KB | 430 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#101](/thread/post/4019642#post4019642 "Post Permalink")

  * Sep 14, 2010 4:13pm  Sep 14, 2010 4:13pm 

  * [ skoda2008](skoda2008)

  * | Joined Mar 2010  | Status: Trader | [224 Posts](/search?do=process&provider=Member&searchuser=137969)

> [Quoting SteveHopwood](/thread/post/4018980#post4018980 "View Quoted Post")
> 
> Disliked
> 
>   
>  As I pointed out earlier, I do not understand indis.  
>    
>  Over to you lot. Produce on that I can interrogate to produce figures that an ea can use and I can code the ea. Until someone does this, there is nothing I can do.  
>    
>  ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

This should do the trick. In honesty I haven't tested it yet though...  
  
If you call it with iCustom with an offset of 0 it should return:  
  
0 for Hold  
1 for long  
2 for short  
  
I could also code the EA, but since you seem to be able to pump them out quicker than I can turn my PC on I'll leave it to you. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Murrey Advisor V2.2 5dec.mq4](/attachment/file/543015?d=1284448327) 48 KB | 358 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#102](/thread/post/4019850#post4019850 "Post Permalink")

  * Sep 14, 2010 5:58pm  Sep 14, 2010 5:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> Quote
> 
> Disliked
> 
> Among all the winning trades today, I have seen two losses:  
>  1\. EURUSD (-29 pips)  
>  2\. USDJPY (-33 pips)

  
USD/CAD as well 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#103](/thread/post/4019880#post4019880 "Post Permalink")

  * Sep 14, 2010 6:08pm  Sep 14, 2010 6:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting PhAnTi'](/thread/post/4019850#post4019850 "View Quoted Post")
> 
> Disliked
> 
> USD/CAD as well
> 
> Ignored

Einstein>Chuck Norris>**Steve Hopwood** >Lindsay Lohan> **mostashar15**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#104](/thread/post/4019884#post4019884 "Post Permalink")

  * Sep 14, 2010 6:09pm  Sep 14, 2010 6:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

Hi,  
  
I did not see these losses.  
Where did you place your stop loss for these trades ?  
Did it retrace back more than 30 pips or were you using the next S/R lines as your SL ?  
  
I saw a loss of around 50 Pips on Euro/Jpy.  
  
I got buy signal at 00:01 at 14th when price was at 107.838. The price then retraced way back taking out my SL at 107.410.   
  
Here is the action on the 4 hour chart I recieved the buy signal at the very start of the 4 hour bar.   
  
  
  
  
  
  
  
  

> [Quoting mostashar15](/thread/post/4018986#post4018986 "View Quoted Post")
> 
> Disliked
> 
> Among all the winning trades today, I have seen two losses:  
>  1\. EURUSD (-29 pips)  
>  2\. USDJPY (-33 pips)  
>    
>  The common between the two trades is what I talked about before. There was a very long candle that breached a Murrey level but as the new candle opens, it retraces back.  
>    
>  This can be filtered easily by looking for EMA(5,close) is no more than 25 pips below the close of last candle Close[1] in case of LONG and no more than 25 pips above Close[1].  
>    
>  To be honest, I have already modified the code to incorporate this change in v2.3 but I will not share...
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: buy signal.jpg
Size: 220 KB](/attachment/image/543067/thumbnail?d=1365649176)](/attachment/image/543067?d=1284455302)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#105](/thread/post/4019889#post4019889 "Post Permalink")

  * Sep 14, 2010 6:10pm  Sep 14, 2010 6:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting skoda2008](/thread/post/4019642#post4019642 "View Quoted Post")
> 
> Disliked
> 
> This should do the trick. In honesty I haven't tested it yet though...  
>    
>  If you call it with iCustom with an offset of 0 it should return:  
>    
>  0 for Hold  
>  1 for long  
>  2 for short  
>    
>  I could also code the EA, but since you seem to be able to pump them out quicker than I can turn my PC on I'll leave it to you. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

Fantastic. Thanks very muich.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#106](/thread/post/4019892#post4019892 "Post Permalink")

  * Sep 14, 2010 6:11pm  Sep 14, 2010 6:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting DrLobo](/thread/post/4019884#post4019884 "View Quoted Post")
> 
> Disliked
> 
> Hi,  
>    
>  I did not see these losses.  
>  Where did you place your stop loss for these trades ?  
>  Did it retrace back more than 30 pips or were you using the next S/R lines as your SL ?  
>    
>  I saw a loss of around 50 Pips on Euro/Jpy.  
>    
>  I got buy signal at 00:01 at 14th when price was at 107.838. The price then retraced way back taking out my SL at 107.410.   
>    
>  Here is the action on the 4 hour chart I recieved the buy signal at the very start of the 4 hour bar.
> 
> Ignored

sl/tp -30/30  
  
  
  

> Quote
> 
> Disliked
> 
> Einstein>Chuck Norris>Steve Hopwood>Lindsay Lohan> mostashar15

  
Lindsay Lohan> mostashar15????   
![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#107](/thread/post/4019911#post4019911 "Post Permalink")

  * Sep 14, 2010 6:17pm  Sep 14, 2010 6:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting PhAnTi'](/thread/post/4019892#post4019892 "View Quoted Post")
> 
> Disliked
> 
> sl/tp -30/30  
>    
>    
>    
>    
>    
>  Lindsay Lohan> mostashar15????   
>  ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)
> 
> Ignored

PhAnTi' ...![](https://resources.faireconomy.media/images/emojis/64/1f44e.png?v=15.1)  
u r in mostashar15 thread 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#108](/thread/post/4019912#post4019912 "Post Permalink")

  * Sep 14, 2010 6:18pm  Sep 14, 2010 6:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

Also got a buy signal on Eur/GBP as it passed the 0.8361 but there is big resistance here. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: buy signal.jpg
Size: 221 KB](/attachment/image/543071/thumbnail?d=1365649176)](/attachment/image/543071?d=1284455906)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#109](/thread/post/4019914#post4019914 "Post Permalink")

  * Sep 14, 2010 6:19pm  Sep 14, 2010 6:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting tahshoon](/thread/post/4019911#post4019911 "View Quoted Post")
> 
> Disliked
> 
> PhAnTi' ...![](https://resources.faireconomy.media/images/emojis/64/1f44e.png?v=15.1)  
>  **u r in mostashar15 thread**
> 
> Ignored

exactly... and Lindsay Lohan isn't better than mostashar...  
  
  

> Quote
> 
> Disliked
> 
> Lindsay Lohan> mostashar15????

  
...  
  
plz back to topic! 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#110](/thread/post/4019926#post4019926 "Post Permalink")

  * Sep 14, 2010 6:23pm  Sep 14, 2010 6:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting PhAnTi'](/thread/post/4019914#post4019914 "View Quoted Post")
> 
> Disliked
> 
> exactly... and Lindsay Lohan isn't better than mostashar...  
>    
>    
>    
>    
>  ...  
>    
>  plz back to topic!
> 
> Ignored

u can go to that Lindsay Lohan...thread and sing with him 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#111](/thread/post/4019938#post4019938 "Post Permalink")

  * Sep 14, 2010 6:27pm  Sep 14, 2010 6:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

Why do i get a sell signal here when TP would only be 8 PIPS away (next support level) and SL would be 52 PIPS (next resistance level) ?  
  
Thanks 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: sell signal.jpg
Size: 213 KB](/attachment/image/543078/thumbnail?d=1365649176)](/attachment/image/543078?d=1284456363)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#112](/thread/post/4019945#post4019945 "Post Permalink")

  * Sep 14, 2010 6:28pm  Sep 14, 2010 6:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

i had this signal just before the german news... then said its not wise to trade before the news ... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: euro german.png
Size: 67 KB](/attachment/image/543079/thumbnail?d=1365649176)](/attachment/image/543079?d=1284456435)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#113](/thread/post/4019962#post4019962 "Post Permalink")

  * Sep 14, 2010 6:33pm  Sep 14, 2010 6:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting DrLobo](/thread/post/4019938#post4019938 "View Quoted Post")
> 
> Disliked
> 
> Why do i get a sell signal here when TP would only be 8 PIPS away (next support level) and SL would be 52 PIPS (next resistance level) ?  
>    
>  Thanks
> 
> Ignored

hmm take tp the support after the support and sl the next resistance ?! 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#114](/thread/post/4019990#post4019990 "Post Permalink")

  * Sep 14, 2010 6:43pm  Sep 14, 2010 6:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

i wonder why i did not recieve this signal ..  
  

> [Quoting tahshoon](/thread/post/4019945#post4019945 "View Quoted Post")
> 
> Disliked
> 
> i had this signal just before the german news... then said its not wise to trade before the news ...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#115](/thread/post/4019997#post4019997 "Post Permalink")

  * Sep 14, 2010 6:45pm  Sep 14, 2010 6:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

i don't have Daily Range statistics....  
  
0  
0  
0  
0  
0  
0  
? 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#116](/thread/post/4020013#post4020013 "Post Permalink")

  * Sep 14, 2010 6:53pm  Sep 14, 2010 6:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting DrLobo](/thread/post/4019990#post4019990 "View Quoted Post")
> 
> Disliked
> 
> i wonder why i did not recieve this signal ..
> 
> Ignored

i think, its because of time,candles in my broker system is faster than urs 1 hour ,mostashar15 noticed that yesterday... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#117](/thread/post/4020046#post4020046 "Post Permalink")

  * Sep 14, 2010 7:09pm  Sep 14, 2010 7:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

so does that mean you will get different signals and trades ?  
Did you get same signals that I recieved ?  
I just got one to short Eur/Jpy  
  
  

> [Quoting tahshoon](/thread/post/4020013#post4020013 "View Quoted Post")
> 
> Disliked
> 
> i think, its because of time,candles in my broker system is faster than urs 1 hour ,mostashar15 noticed that yesterday...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#118](/thread/post/4020067#post4020067 "Post Permalink")

  * Edited 7:30pm  Sep 14, 2010 7:16pm | Edited 7:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar144900_4.gif) gspe](gspe)

  * | Joined Jun 2010  | Status: Trader | [191 Posts](/search?do=process&provider=Member&searchuser=144900)

> [Quoting PhAnTi'](/thread/post/4019997#post4019997 "View Quoted Post")
> 
> Disliked
> 
> i don't have Daily Range statistics....  
>    
>  0  
>  0  
>  0  
>  0  
>  0  
>  0  
>  ?
> 
> Ignored

Hi,  
try this version i modified it for 4/5 digts brokers. The only thing that doesn't work is the clock, i can't still find the code in the indy to modify it.  
  
Tell me if it works for you  
gspe 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Murrey Advisor V2.2.mq4](/attachment/file/543099?d=1284459378) 48 KB | 244 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#119](/thread/post/4020073#post4020073 "Post Permalink")

  * Sep 14, 2010 7:19pm  Sep 14, 2010 7:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting DrLobo](/thread/post/4020046#post4020046 "View Quoted Post")
> 
> Disliked
> 
> so does that mean you will get different signals and trades ?  
>  Did you get same signals that I recieved ?  
>  I just got one to short Eur/Jpy
> 
> Ignored

plz,see this post ...  
[http://www.forexfactory.com/showpost...7&postcount=46](http://www.forexfactory.com/showpost.php?p=4018077&postcount=46)  
i dont have croses in my platform( didnt put them )... i didnt see that . 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#120](/thread/post/4020116#post4020116 "Post Permalink")

  * Sep 14, 2010 7:37pm  Sep 14, 2010 7:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting skoda2008](/thread/post/4019642#post4019642 "View Quoted Post")
> 
> Disliked
> 
> This should do the trick. In honesty I haven't tested it yet though...  
>    
>  If you call it with iCustom with an offset of 0 it should return:  
>    
>  0 for Hold  
>  1 for long  
>  2 for short  
>    
>  I could also code the EA, but since you seem to be able to pump them out quicker than I can turn my PC on I'll leave it to you. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

This does not display any data, so I am not sure if this means it is not calculating any results.  
  
Whilst you are fixing it, could you adapt it to cater for x digit criminals so we do not have to muck around with separate indicators?  
  
Cheers  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#121](/thread/post/4020131#post4020131 "Post Permalink")

  * Sep 14, 2010 7:45pm  Sep 14, 2010 7:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting gspe](/thread/post/4020067#post4020067 "View Quoted Post")
> 
> Disliked
> 
> Hi,  
>  try this version i modified it for 4/5 digts brokers. The only thing that doesn't work is the clock, i can't still find the code in the indy to modify it.  
>    
>  Tell me if it works for you  
>  gspe
> 
> Ignored

It works...  
thank you very much ![](https://resources.faireconomy.media/images/emojis/64/270c-fe0f.png?v=15.1)

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#122](/thread/post/4020173#post4020173 "Post Permalink")

  * Sep 14, 2010 8:05pm  Sep 14, 2010 8:05pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting PhAnTi'](/thread/post/4019850#post4019850 "View Quoted Post")
> 
> Disliked
> 
> USD/CAD as well
> 
> Ignored

USDCAD is still LIVE with me. It is now +24 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#123](/thread/post/4020188#post4020188 "Post Permalink")

  * Sep 14, 2010 8:11pm  Sep 14, 2010 8:11pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

I was planning to keep it hidden little bit further, but I have noticed most of the bad signals are similar and could have been filtered out.  
  
I am attaching v2.3 for trial purposes and compare performance to v2.2.  
  
I have used the modified version by gspe as a basis so that this new version suits both 4 and 5 digit brokers. Thanks gspe  
  
It is not for SALE yet ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [MURREY ADVISOR v2.3.zip](/attachment/file/543126?d=1284462637) 9 KB | 353 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#124](/thread/post/4020193#post4020193 "Post Permalink")

  * Sep 14, 2010 8:16pm  Sep 14, 2010 8:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar113359_3.gif) Precap2](precap2)

  * | Joined Aug 2009  | Status: Non-graduating student | [575 Posts](/search?do=process&provider=Member&searchuser=113359)

This MM H4 indy seems to work normally like an indicator, late signal. But it's support and resistance areas are quite good. So I take trades when I see multiple failure, and also when I see things like in the posted chart, an inside bar was broken after failure to move up, I go with the break. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: pix.gif
Size: 23 KB](/attachment/image/543127/thumbnail?d=1365649176)](/attachment/image/543127?d=1284462980)   

Mystery Is The Final Product Of Ignorance. Hey! What's ma chart doin' ![](https://resources.faireconomy.media/images/emojis/64/1f621.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#125](/thread/post/4020195#post4020195 "Post Permalink")

  * Sep 14, 2010 8:17pm  Sep 14, 2010 8:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting gspe](/thread/post/4020067#post4020067 "View Quoted Post")
> 
> Disliked
> 
> Hi,  
>  try this version i modified it for 4/5 digts brokers. The only thing that doesn't work is the clock, i can't still find the code in the indy to modify it.  
>    
>  Tell me if it works for you  
>  gspe
> 
> Ignored

Are you able to fix this? When I add Skoda's code to return the status of the indi as either 0, 1 or 2 the display stops. The indi still generates signals (just picked up an eu 'Go short' alert on the H1) but does not display the figures.  
  
The problem is caused by ExtBuffer[0] = 0; Comment this out and re-compile and the display is fine.  
  
I can even code the EA with the indi like this as I really only need to know if the buffer holds a value of either 1 or 2; it would just be good to know the indi is working properly.  
  
Cheers  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Murrey Advisor V2.2.mq4](/attachment/file/543125?d=1284462564) 48 KB | 195 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#126](/thread/post/4020214#post4020214 "Post Permalink")

  * Sep 14, 2010 8:24pm  Sep 14, 2010 8:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

USD/CAD worked for me aswel.   
I had it open since yesterday and just closed it (approaching 0/8 and there is not much range in last few days) with 20 PIPS profit.  
  

> [Quoting mostashar15](/thread/post/4020173#post4020173 "View Quoted Post")
> 
> Disliked
> 
> USDCAD is still LIVE with me. It is now +24
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#127](/thread/post/4020218#post4020218 "Post Permalink")

  * Sep 14, 2010 8:26pm  Sep 14, 2010 8:26pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting heaveyrain](/thread/post/4019104#post4019104 "View Quoted Post")
> 
> Disliked
> 
> a suggestion you can use a certain % of the ATR as yr SL. e.g 50% or 70%
> 
> Ignored

I am not familiar with ATR. Can you explain how you can use 50% or 70%?  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#128](/thread/post/4020219#post4020219 "Post Permalink")

  * Sep 14, 2010 8:27pm  Sep 14, 2010 8:27pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting Pardy](/thread/post/4019163#post4019163 "View Quoted Post")
> 
> Disliked
> 
> Hi, you might find this indicator useful - It simply displays the distance of price to the ma, so you can easily tell if it is higher than 25 pips.  
>  For 5 digit brokers, it'll show 10 pips as 100.  
>    
>  Pardy
> 
> Ignored

Thanks buddy, I have modified the code already. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#129](/thread/post/4020225#post4020225 "Post Permalink")

  * Sep 14, 2010 8:29pm  Sep 14, 2010 8:29pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting skoda2008](/thread/post/4019642#post4019642 "View Quoted Post")
> 
> Disliked
> 
> This should do the trick. In honesty I haven't tested it yet though...  
>    
>  If you call it with iCustom with an offset of 0 it should return:  
>    
>  0 for Hold  
>  1 for long  
>  2 for short  
>    
>  I could also code the EA, but since you seem to be able to pump them out quicker than I can turn my PC on I'll leave it to you. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

Thanks Skoda for jumping just in the right time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#130](/thread/post/4020239#post4020239 "Post Permalink")

  * Sep 14, 2010 8:34pm  Sep 14, 2010 8:34pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting SteveHopwood](/thread/post/4019889#post4019889 "View Quoted Post")
> 
> Disliked
> 
> Fantastic. Thanks very muich.  
>    
>  ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

Now, we will be waiting for your EA, Good Luck 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#131](/thread/post/4020248#post4020248 "Post Permalink")

  * Sep 14, 2010 8:38pm  Sep 14, 2010 8:38pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting DrLobo](/thread/post/4019938#post4019938 "View Quoted Post")
> 
> Disliked
> 
> Why do i get a sell signal here when TP would only be 8 PIPS away (next support level) and SL would be 52 PIPS (next resistance level) ?  
>    
>  Thanks
> 
> Ignored

Hi  
  
The code will look for any opportunity that can give you more than 10 pips. But, you have to make decision whether you want to get in or not based on Reward/Loss ratio.  
  
I believe V2.3 (if works fine) will increase the probability of a trade to go in your direction. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#132](/thread/post/4020250#post4020250 "Post Permalink")

  * Sep 14, 2010 8:40pm  Sep 14, 2010 8:40pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting tahshoon](/thread/post/4019945#post4019945 "View Quoted Post")
> 
> Disliked
> 
> i had this signal just before the german news... then said its not wise to trade before the news ...
> 
> Ignored

I believe this would have been filtered out in the new version, let us see upcoming similar entries. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#133](/thread/post/4020257#post4020257 "Post Permalink")

  * Sep 14, 2010 8:44pm  Sep 14, 2010 8:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting mostashar15](/thread/post/4020250#post4020250 "View Quoted Post")
> 
> Disliked
> 
> I believe this would have been filtered out in the new version, let us see upcoming similar entries.
> 
> Ignored

im sure that u r doing a great job,thnx for sharing ur experience with us 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#134](/thread/post/4020268#post4020268 "Post Permalink")

  * Sep 14, 2010 8:47pm  Sep 14, 2010 8:47pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting PhAnTi'](/thread/post/4019962#post4019962 "View Quoted Post")
> 
> Disliked
> 
> hmm take tp the support after the support and sl the next resistance ?!
> 
> Ignored

To me the most accurate SL should be if the 4Hr candle closes below EMA(5,close) in case of LONG which means the uptrend is broken and vise versa in SHORT. As I said before, the pair will tend to move above EMA(5,close) the green line but after sometime will tend to retrace to test this line and continue moving up.  
  
However, if EMA(5,close) is so close or far then, you may use 25 - 30 pips as SL.  
  
In conclusion, I believe SL setting needs further optimization and feedback about how to further improve. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#135](/thread/post/4020272#post4020272 "Post Permalink")

  * Sep 14, 2010 8:50pm  Sep 14, 2010 8:50pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting DrLobo](/thread/post/4020046#post4020046 "View Quoted Post")
> 
> Disliked
> 
> so does that mean you will get different signals and trades ?  
>  Did you get same signals that I recieved ?  
>  I just got one to short Eur/Jpy
> 
> Ignored

In most of the cases, you will both receive the same signal, however, since he is one hour in advance, he will get better position in the entry.  
  
Since this strategy is based on observations and trial & error, I have downloaded his platform to check both. I believe there might be an incentive. But, we need to test on the long term at least. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#136](/thread/post/4020275#post4020275 "Post Permalink")

  * Sep 14, 2010 8:51pm  Sep 14, 2010 8:51pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting gspe](/thread/post/4020067#post4020067 "View Quoted Post")
> 
> Disliked
> 
> Hi,  
>  try this version i modified it for 4/5 digts brokers. The only thing that doesn't work is the clock, i can't still find the code in the indy to modify it.  
>    
>  Tell me if it works for you  
>  gspe
> 
> Ignored

Great Work, thanks buddy.  
  
I have captured your name in V2.3 in the THANKS section since I used your version as a basis for developing 2.3. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#137](/thread/post/4020305#post4020305 "Post Permalink")

  * Sep 14, 2010 9:00pm  Sep 14, 2010 9:00pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting DrLobo](/thread/post/4020214#post4020214 "View Quoted Post")
> 
> Disliked
> 
> USD/CAD worked for me aswel.   
>  I had it open since yesterday and just closed it (approaching 0/8 and there is not much range in last few days) with 20 PIPS profit.
> 
> Ignored

You did the right move ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#138](/thread/post/4020324#post4020324 "Post Permalink")

  * Sep 14, 2010 9:07pm  Sep 14, 2010 9:07pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

After those big moves which were against the trend, most likely we will not see entry signal before next candle after 4 hrs from now. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#139](/thread/post/4020376#post4020376 "Post Permalink")

  * Sep 14, 2010 9:27pm  Sep 14, 2010 9:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

how to set sl/tp? 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#140](/thread/post/4020418#post4020418 "Post Permalink")

  * Sep 14, 2010 9:45pm  Sep 14, 2010 9:45pm 

  * [ skoda2008](skoda2008)

  * | Joined Mar 2010  | Status: Trader | [224 Posts](/search?do=process&provider=Member&searchuser=137969)

Sorry about the blank display on the previous version. Here is the latest version (2.3) updated to put out values to the external buffer for an EA to use.  
  
This time it has been tested and works. The number next to "MA" in the indicator window is the value it is sending out. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Murrey Advisor V2.3 dual with ext buffer.mq4](/attachment/file/543183?d=1284468292) 48 KB | 412 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#141](/thread/post/4020565#post4020565 "Post Permalink")

  * Sep 14, 2010 10:33pm  Sep 14, 2010 10:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

Meet Louise, named as the contributor who told me to come here wished. Nothing sophisticated yet - just a straight tp and sl.  
  
A few points:

  1. you need to have the attached version of the indi in your indicator's folder. This returns the value of the current indi signal as hold, go long or go short. The version in post 1 does not have this.
  2. you need to run the ea on a separate chart to the indi, otherwise the flashing screen will drive you to drink 'n drugs.
  3. your Journal tab will fill to overflowing with 'unknown subwindow' errors:

    1. I know, so don't tell me about them.
    2. There is nothing I can do about them, so don't tell me about them.
    3. I do not know what causes them, so don't tell me about them.
    4. I do not know how to cure them, so don't tell me about them.
    5. Anyone who _does_ tell me about them proves conclusively they have not been bothered to read this and gets a blast from me. Possibly followed by a visit from a hitman.
    6. Over to the indi-coders for this one.

  4. Louise automatically accommodates to x digit criminals, so enter tp and sl as proper pips, not piplets.
  5. set CriminalIsECN to true if your criminal insists on two-stage order sending. This now includes IBFX.
  6. make sure your indicator inputs are the same as those you input into Murray Advisor. The colours were an attempt to stop the flashing; they do not work.

As usual, the code is my copyright only because this is the state of the law here in the UK. I hereby give full permission to coders to use it in any way. Feel free to add sophisticated mm functionality and anything else you might find useful.  
  
Let's see if Louise has staying-power.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Louise.mq4](/attachment/file/543210?d=1284470313) 9 KB | 296 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Murrey Advisor V2.2.mq4](/attachment/file/543213?d=1284470519) 48 KB | 283 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#142](/thread/post/4020651#post4020651 "Post Permalink")

  * Sep 14, 2010 10:56pm  Sep 14, 2010 10:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting SteveHopwood](/thread/post/4020565#post4020565 "View Quoted Post")
> 
> Disliked
> 
> Meet Louise, named as the contributor who told me to come here wished. Nothing sophisticated yet - just a straight tp and sl.  
>    
>  A few points:  
>  [list=1][*]you need to have the attached version of the indi in your indicator's folder. This returns the value of the current indi signal as hold, go long or go short. The version in post 1 does not have this.[*]you need to run the ea on a separate chart to the indi, otherwise the flashing screen will drive you to drink 'n drugs.[*]your Journal tab will fill to overflowing with 'unknown subwindow'...
> 
> Ignored

ohh yes Baby!  
Thank you so much!  
  
ohh Steve...Lindsay is starting to make movies again... ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#143](/thread/post/4020677#post4020677 "Post Permalink")

  * Sep 14, 2010 11:03pm  Sep 14, 2010 11:03pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

USDCAD now closed with me +40 pips. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#144](/thread/post/4020689#post4020689 "Post Permalink")

  * Sep 14, 2010 11:07pm  Sep 14, 2010 11:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting mostashar15](/thread/post/4020677#post4020677 "View Quoted Post")
> 
> Disliked
> 
> USDCAD now closed with me +40 pips.
> 
> Ignored

when did you enter? i got in yesterday evening and got -30 loss with sl/tp -30/30 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#145](/thread/post/4020701#post4020701 "Post Permalink")

  * Sep 14, 2010 11:09pm  Sep 14, 2010 11:09pm 

  * [ ranger_lp](ranger_lp)

  * | Joined Oct 2008  | Status: Trader | [436 Posts](/search?do=process&provider=Member&searchuser=82547)

Last night two signals.....  
  
USDCAD -30  
USDJPY -30  
  
Looking @ updated indicator now..... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#146](/thread/post/4020723#post4020723 "Post Permalink")

  * Sep 14, 2010 11:15pm  Sep 14, 2010 11:15pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

I am attaching here my latest results with v2.2.  
  
As you see we are achieving almost 70% success rate and we were able to earn a total of +188 pips ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) but we lost -131 pips ![](https://resources.faireconomy.media/images/emojis/64/1f624.png?v=15.1) which leaves us with a net of +57 pips.  
  
If we filter out last two losing trades as v2.3 would have done then we would had lost only -74 pips leaving a net profit of +114 pips.  
  
Thanks 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: MurreyAdvisor_v2.2_reults_14092010.PNG
Size: 28 KB](/attachment/image/543252/thumbnail?d=1365649208)](/attachment/image/543252?d=1284473685)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#147](/thread/post/4020784#post4020784 "Post Permalink")

  * Sep 14, 2010 11:32pm  Sep 14, 2010 11:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

the yesterday cad-usd short signal cant be a loser in any way ...  
take a look here,plz  
[http://www.forexfactory.com/showpost...8&postcount=31](http://www.forexfactory.com/showpost.php?p=4017498&postcount=31)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#148](/thread/post/4020801#post4020801 "Post Permalink")

  * Sep 14, 2010 11:36pm  Sep 14, 2010 11:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting tahshoon](/thread/post/4020784#post4020784 "View Quoted Post")
> 
> Disliked
> 
> the yesterday cad-usd short signal cant be a loser in any way ...  
>  take a look here,plz  
>  [http://www.forexfactory.com/showpost...8&postcount=31](http://www.forexfactory.com/showpost.php?p=4017498&postcount=31)
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: grrr.JPG
Size: 8 KB](/attachment/image/543273/thumbnail?d=1365649208)](/attachment/image/543273?d=1284474969)   

  
  
went it immediately when signal came ...yesterday eve... 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#149](/thread/post/4020838#post4020838 "Post Permalink")

  * Sep 14, 2010 11:43pm  Sep 14, 2010 11:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting skoda2008](/thread/post/4020418#post4020418 "View Quoted Post")
> 
> Disliked
> 
> Sorry about the blank display on the previous version. Here is the latest version (2.3) updated to put out values to the external buffer for an EA to use.  
>    
>  This time it has been tested and works. The number next to "MA" in the indicator window is the value it is sending out.
> 
> Ignored

Ma 0.00000  
?! 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#150](/thread/post/4020839#post4020839 "Post Permalink")

  * Sep 14, 2010 11:43pm  Sep 14, 2010 11:43pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting PhAnTi'](/thread/post/4020801#post4020801 "View Quoted Post")
> 
> Disliked
> 
> [Attachment ](https://www.forexfactory.com/attachment/file/543273)  
>    
>  went it immediately when signal came ...yesterday eve...
> 
> Ignored

My SL was 1.0292  
  
It is only 5 pips that made me make +40 and you lose -30  
  
Sorry 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#151](/thread/post/4020871#post4020871 "Post Permalink")

  * Sep 14, 2010 11:49pm  Sep 14, 2010 11:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting mostashar15](/thread/post/4020839#post4020839 "View Quoted Post")
> 
> Disliked
> 
> My SL was 1.0292  
>    
>  It is only 5 pips that made me make +40 and you lose -30  
>    
>  _**Sorry**_
> 
> Ignored

no problem buddy : D  
but let me plz know for the future...  
how do you set sl tp? 40/40 ? 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#152](/thread/post/4020888#post4020888 "Post Permalink")

  * Sep 14, 2010 11:52pm  Sep 14, 2010 11:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

sorry bit of a noob question when it comes to setting up the EA.  
  
Is the procedure, to open all the charts that i want to trade to 4H TF, then attach louise to them and select live trading and see that there is a smiley face top right corner ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#153](/thread/post/4020895#post4020895 "Post Permalink")

  * Sep 14, 2010 11:54pm  Sep 14, 2010 11:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting DrLobo](/thread/post/4020888#post4020888 "View Quoted Post")
> 
> Disliked
> 
> sorry bit of a noob question when it comes to setting up the EA.  
>    
>  Is the procedure, to open all the charts that i want to trade to 4H TF, then attach louise to them and select live trading and see that there is a smiley face top right corner ?
> 
> Ignored

> Quote
> 
> Disliked
> 
> you need to run the ea on a separate chart to the indi, otherwise the flashing screen will drive you to drink 'n drugs.

  
open Charts as usual... open template and start EA...but on another chart of the same pair as Steve recommended... 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#154](/thread/post/4021022#post4021022 "Post Permalink")

  * Sep 15, 2010 12:18am  Sep 15, 2010 12:18am 

  * [ skoda2008](skoda2008)

  * | Joined Mar 2010  | Status: Trader | [224 Posts](/search?do=process&provider=Member&searchuser=137969)

> [Quoting SteveHopwood](/thread/post/4020565#post4020565 "View Quoted Post")
> 
> Disliked
> 
>   1. you need to have the attached version of the indi in your indicator's folder. This returns the value of the current indi signal as hold, go long or go short. The version in post 1 does not have this.
>   2. you need to run the ea on a separate chart to the indi, otherwise the flashing screen will drive you to drink 'n drugs.
>   3. your Journal tab will fill to overflowing with 'unknown subwindow' errors:
> 
>     1. I know, so don't tell me about them.
>     2. There is nothing I can do about them, so don't tell me about them.
>     3. I do not know what...
> 
> 

> 
> Ignored

The errors in the journal are caused because the indicator is trying to display it's info in a sub-window, but when the indicator is called by the iCustom function there is no sub-window for it to write to. The only way out that I can see is to open the indicator & ea on the same chart (the journal errors then stop), but then you are left with problem 2 as mentioned above. Over time the journal will create a large file on your hard disk... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#155](/thread/post/4021070#post4021070 "Post Permalink")

  * Sep 15, 2010 12:31am  Sep 15, 2010 12:31am 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

Yesterday I came across this thread and was impressed..I downloaded fer 2.2 and installed. Last evening @ 7:45 pm EST I recvd a short gor USD/CAD and a long for EUR/GBP, and never recvd another signal. This AM I downloaded and installed ver 2.3, since then I have recvd no signal at all. Helppp from anyone..  
regards  
sfg7th 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#156](/thread/post/4021137#post4021137 "Post Permalink")

  * Sep 15, 2010 12:49am  Sep 15, 2010 12:49am 

  * [ Invisible](invisible)

  * | Joined Nov 2009  | Status: Trader | [469 Posts](/search?do=process&provider=Member&searchuser=124048)

Great work, guys and thanks for the EA, Steve. Will be testing as usual. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#157](/thread/post/4021233#post4021233 "Post Permalink")

  * Sep 15, 2010 1:13am  Sep 15, 2010 1:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

i might be wrong, but i think this EA will really kick in, by making   
  
Shorts TP = <Pips till support value>  
Long TP = <Pips till reistance value>  
  
Also vice versa for the SL.  
  
I have no idea how to program Mq4 one day i will learn. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#158](/thread/post/4021658#post4021658 "Post Permalink")

  * Sep 15, 2010 4:22am  Sep 15, 2010 4:22am 

  * [ Invisible](invisible)

  * | Joined Nov 2009  | Status: Trader | [469 Posts](/search?do=process&provider=Member&searchuser=124048)

Hi Steve  
  
Backtesting is slow, but it seems that it is doing OK with 30 TP and 30 SL on EURUSD. Thanks for taking on Louise!  
  
I was wondering whether it might be possible to have the TP at the next Murrey line and whether it would be possible to integrate some of the MPTM functions to lock in profits?  
  
Cheers  
  
Invisible 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#159](/thread/post/4021685#post4021685 "Post Permalink")

  * Edited 5:11am  Sep 15, 2010 4:37am | Edited 5:11am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

I believe now we have a LONG entry signal by v2.2 while v2.3 is not giving this signal. V2.3 says EURUSD has to retrace at least 25 points (above EMA(5,close)) then entry is possible.  
  
Let us see 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: eurusd_2.2.gif
Size: 27 KB](/attachment/image/543466/thumbnail?d=1365649280)](/attachment/image/543466?d=1284493054)   
[![Click to Enlarge

Name: eurusd_2.3.gif
Size: 27 KB](/attachment/image/543467/thumbnail?d=1365649280)](/attachment/image/543467?d=1284493054)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#160](/thread/post/4021732#post4021732 "Post Permalink")

  * Sep 15, 2010 5:05am  Sep 15, 2010 5:05am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

Both V2.2 and V2.3 say SHORT for USDJPY. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: usdjpy_13092010_1600_short.gif
Size: 28 KB](/attachment/image/543477/thumbnail?d=1365649280)](/attachment/image/543477?d=1284494714)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#161](/thread/post/4021772#post4021772 "Post Permalink")

  * Sep 15, 2010 5:22am  Sep 15, 2010 5:22am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

I think v2.3 is doing fine. The faulty signal from v2.2 has just hit SL. V2.3 has saved me -30 pips.  
  
This is very good start.  
  
Let us keep watching. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eurusd_2.3_update.gif
Size: 27 KB](/attachment/image/543482/thumbnail?d=1365649280)](/attachment/image/543482?d=1284495716)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#162](/thread/post/4021820#post4021820 "Post Permalink")

  * Sep 15, 2010 5:44am  Sep 15, 2010 5:44am 

  * [ vinesh](vinesh)

  * | Joined Jun 2008  | Status: Trader | [625 Posts](/search?do=process&provider=Member&searchuser=72907)

> [Quoting skoda2008](/thread/post/4021022#post4021022 "View Quoted Post")
> 
> Disliked
> 
> [/list][/list] The errors in the journal are caused because the indicator is trying to display it's info in a sub-window, but when the indicator is called by the iCustom function there is no sub-window for it to write to. The only way out that I can see is to open the indicator & ea on the same chart (the journal errors then stop), but then you are left with problem 2 as mentioned above. Over time the journal will create a large file on your hard disk...
> 
> Ignored

Surprisingly I do NOT have that problem if I load the indi on the same chart with EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#163](/thread/post/4021847#post4021847 "Post Permalink")

  * Sep 15, 2010 5:54am  Sep 15, 2010 5:54am 

  * [ vinesh](vinesh)

  * | Joined Jun 2008  | Status: Trader | [625 Posts](/search?do=process&provider=Member&searchuser=72907)

See the picture. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: problem 2.gif
Size: 81 KB](/attachment/image/543492/thumbnail?d=1365649280)](/attachment/image/543492?d=1284497676)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#164](/thread/post/4021902#post4021902 "Post Permalink")

  * Sep 15, 2010 6:15am  Sep 15, 2010 6:15am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting SteveHopwood](/thread/post/4020565#post4020565 "View Quoted Post")
> 
> Disliked
> 
> Meet Louise, named as the contributor who told me to come here wished. Nothing sophisticated yet - just a straight tp and sl.  
>    
>  A few points:  
>  [list=1][*]you need to have the attached version of the indi in your indicator's folder. This returns the value of the current indi signal as hold, go long or go short. The version in post 1 does not have this.[*]you need to run the ea on a separate chart to the indi, otherwise the flashing screen will drive you to drink 'n drugs.[*]your Journal tab will fill to overflowing with 'unknown subwindow'...
> 
> Ignored

Thanks Steve. I appreciate your work to get this done.  
  
May I suggest the path forward:  
  
1\. We need a volunteer to test the EA continuously preferably if someone has VPN.   
  
2\. We need to continue developing this code further to capture what was proposed in "Next Developments", if you don't mind Steve. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#165](/thread/post/4021937#post4021937 "Post Permalink")

  * Sep 15, 2010 6:30am  Sep 15, 2010 6:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

I'm short on usdjpy with 35/35 sl/tp ...hope this time it works : P  
what tp/sl do u prefer guys? 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#166](/thread/post/4022005#post4022005 "Post Permalink")

  * Sep 15, 2010 7:00am  Sep 15, 2010 7:00am 

  * [ skoda2008](skoda2008)

  * | Joined Mar 2010  | Status: Trader | [224 Posts](/search?do=process&provider=Member&searchuser=137969)

> [Quoting vinesh](/thread/post/4021820#post4021820 "View Quoted Post")
> 
> Disliked
> 
> Surprisingly I do NOT have that problem if I load the indi on the same chart with EA.
> 
> Ignored

Neither do I, it's probably got to do with the colours people are using, if they are using the provided template etc. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#167](/thread/post/4022007#post4022007 "Post Permalink")

  * Sep 15, 2010 7:00am  Sep 15, 2010 7:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting skoda2008](/thread/post/4021022#post4021022 "View Quoted Post")
> 
> Disliked
> 
> [/list][/list] The errors in the journal are caused because the indicator is trying to display it's info in a sub-window, but when the indicator is called by the iCustom function there is no sub-window for it to write to. The only way out that I can see is to open the indicator & ea on the same chart (the journal errors then stop), but then you are left with problem 2 as mentioned above. Over time the journal will create a large file on your hard disk...
> 
> Ignored

Another solution is to import the indi code into Louise. I might look at this tomorrow.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#168](/thread/post/4022009#post4022009 "Post Permalink")

  * Sep 15, 2010 7:01am  Sep 15, 2010 7:01am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting PhAnTi'](/thread/post/4021937#post4021937 "View Quoted Post")
> 
> Disliked
> 
> I'm short on usdjpy with 35/35 sl/tp ...hope this time it works : P  
>  what tp/sl do u prefer guys?
> 
> Ignored

My SL = 83.38  
  
You are on demo, aren't you? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#169](/thread/post/4022011#post4022011 "Post Permalink")

  * Sep 15, 2010 7:02am  Sep 15, 2010 7:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting mostashar15](/thread/post/4021902#post4021902 "View Quoted Post")
> 
> Disliked
> 
> 2\. We need to continue developing this code further to capture what was proposed in "Next Developments", if you don't mind Steve.
> 
> Ignored

Of course not. Anyone can adapt my code and carry it forward.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#170](/thread/post/4022016#post4022016 "Post Permalink")

  * Sep 15, 2010 7:04am  Sep 15, 2010 7:04am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting SteveHopwood](/thread/post/4022011#post4022011 "View Quoted Post")
> 
> Disliked
> 
> Of course not. Anyone can adapt my code and carry it forward.  
>    
>  ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

Thanks. I will be looking into it if I can do something. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#171](/thread/post/4022017#post4022017 "Post Permalink")

  * Sep 15, 2010 7:04am  Sep 15, 2010 7:04am 

  * [ skoda2008](skoda2008)

  * | Joined Mar 2010  | Status: Trader | [224 Posts](/search?do=process&provider=Member&searchuser=137969)

> [Quoting SteveHopwood](/thread/post/4022007#post4022007 "View Quoted Post")
> 
> Disliked
> 
> Another solution is to import the indi code into Louise. I might look at this tomorrow.  
>    
>  ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

Exactly what I was thinking. So it's a race then! ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#172](/thread/post/4022049#post4022049 "Post Permalink")

  * Sep 15, 2010 7:33am  Sep 15, 2010 7:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

Left the EA running for last 6 hours on my demo account but results are not looking too good right now there are a number of trades going pear shaped and the two that have completed have both hit a 30 pips SL which I set.   
  
However I believe in both these cases (EUR/USD AUD/USD) may have been avoided if the EA was running on version 2.3 ? In both cases the Buy signal was given after a very large bullish last session which looks like there is more than 25 points past the 5 ema  
  
Is it possible to update the v2.3 for this EA ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#173](/thread/post/4022082#post4022082 "Post Permalink")

  * Sep 15, 2010 8:16am  Sep 15, 2010 8:16am 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

so from what i understand the current Ea based on 2.2 version ?   
  
i will try 2.3 until the new Ea appear 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#174](/thread/post/4022134#post4022134 "Post Permalink")

  * Sep 15, 2010 8:56am  Sep 15, 2010 8:56am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting DrLobo](/thread/post/4022049#post4022049 "View Quoted Post")
> 
> Disliked
> 
> Left the EA running for last 6 hours on my demo account but results are not looking too good right now there are a number of trades going pear shaped and the two that have completed have both hit a 30 pips SL which I set.   
>    
>  However I believe in both these cases (EUR/USD AUD/USD) may have been avoided if the EA was running on version 2.3 ? In both cases the Buy signal was given after a very large bullish last session which looks like there is more than 25 points past the 5 ema  
>    
>  Is it possible to update the v2.3 for this EA ?
> 
> Ignored

I am not that pro in EA making, but I believe the enclosed files should work based on v2.3.  
  
Please let me know. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [Murrey Advisor EA based on v2.3.zip](/attachment/file/543551?d=1284508594) 64 KB | 298 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#175](/thread/post/4022140#post4022140 "Post Permalink")

  * Sep 15, 2010 9:02am  Sep 15, 2010 9:02am 

  * [ Invisible](invisible)

  * | Joined Nov 2009  | Status: Trader | [469 Posts](/search?do=process&provider=Member&searchuser=124048)

Would it be worth having the EA take the trade only the first time a signal is generated after a breach of the Murray? Otherwise there can be new signals arising which are not as profitable as the price bounces between the Murray lines. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#176](/thread/post/4022210#post4022210 "Post Permalink")

  * Sep 15, 2010 10:03am  Sep 15, 2010 10:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar107454_2.gif) phover](phover)

  * | Joined Jun 2009  | Status: Coder | [226 Posts](/search?do=process&provider=Member&searchuser=107454)

> [Quoting SteveHopwood](/thread/post/4022007#post4022007 "View Quoted Post")
> 
> Disliked
> 
> Another solution is to import the indi code into Louise. I might look at this tomorrow.  
>    
>  [http://cdn.forexfactory.com/images/s...m/big_grin.gif](http://cdn.forexfactory.com/images/smilies/yim/big_grin.gif)
> 
> Ignored

Hi Steve,  
  
I have isolated the code for murray calculation from the indicator.   
  
Attached a function that you can use directly in your ea (the indicator won't be need for the ea to work).  
  
Prototype of the function is:   
int GetMurraySignal(int P, int StepBack)  
  
return   
0: hold  
-1: go short  
1: go buy  
  
Didn't test it, but you'll tell me if it works. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Function will work on 4 and 5 digits crim.  
  
Cheers,  
  
Mart 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Murrey Advisor function isolated.mq4](/attachment/file/543567?d=1284512556) 48 KB | 241 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#177](/thread/post/4022713#post4022713 "Post Permalink")

  * Sep 15, 2010 12:32pm  Sep 15, 2010 12:32pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

Oh my God, this Japanese news flipped the table.  
  
SL hit.  
  
I think losses due to news will be inevitable no matter what your indicators are. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#178](/thread/post/4022868#post4022868 "Post Permalink")

  * Sep 15, 2010 2:02pm  Sep 15, 2010 2:02pm 

  * [ thor68](thor68)

  * | Joined Oct 2007  | Status: Trader | [114 Posts](/search?do=process&provider=Member&searchuser=51486)

You can't account for everything. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#179](/thread/post/4023175#post4023175 "Post Permalink")

  * Sep 15, 2010 5:00pm  Sep 15, 2010 5:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting mostashar15](/thread/post/4022009#post4022009 "View Quoted Post")
> 
> Disliked
> 
> My SL = 83.38  
>    
>  You are on demo, aren't you?
> 
> Ignored

no I'm live...but microaccount...don't like to test on demo ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
3 trades : 3 losses (35/35 sl/tp).... but I still trust this system ; p 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#180](/thread/post/4023244#post4023244 "Post Permalink")

  * Sep 15, 2010 5:29pm  Sep 15, 2010 5:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

mostashar , im afraid that all these changes will damage the basic thought of the indicator ,and for a while we have nothing ....like many threads before in the forum ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#181](/thread/post/4023350#post4023350 "Post Permalink")

  * Sep 15, 2010 6:05pm  Sep 15, 2010 6:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting phover](/thread/post/4022210#post4022210 "View Quoted Post")
> 
> Disliked
> 
> Hi Steve,  
>    
>  I have isolated the code for murray calculation from the indicator.   
>    
>  Attached a function that you can use directly in your ea (the indicator won't be need for the ea to work).  
>    
>  Prototype of the function is:   
>  int GetMurraySignal(int P, int StepBack)  
>    
>  return   
>  0: hold  
>  -1: go short  
>  1: go buy  
>    
>  Didn't test it, but you'll tell me if it works. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>  Function will work on 4 and 5 digits crim.  
>    
>  Cheers,  
>    
>  Mart
> 
> Ignored

Absolutely fantastic Mart. Stunning contribution. About a gazillion thanks. ![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)  
  
Ok guys, dump your adulterated indi's and go back to post 1 to re-download the one appropriate to your criminal that we _know_ works properly.  
  
I will add Mart's code to Louise, do a quick backtest to make sure and release the update asap.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#182](/thread/post/4023363#post4023363 "Post Permalink")

  * Sep 15, 2010 6:10pm  Sep 15, 2010 6:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

Actually, Mart, it looks as though you have simply attached the indi with a different name.  
  
Have I missed something?  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#183](/thread/post/4023429#post4023429 "Post Permalink")

  * Sep 15, 2010 6:31pm  Sep 15, 2010 6:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

Hi  
  
I tried testing this 2.3 v of the EA, so I found a buy signal on 15 min chart (just for testing purposes) and attached Louise to the chart and i got the following errors please see attached.  
  
  

> [Quoting mostashar15](/thread/post/4022134#post4022134 "View Quoted Post")
> 
> Disliked
> 
> I am not that pro in EA making, but I believe the enclosed files should work based on v2.3.  
>    
>  Please let me know.
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: error.png
Size: 71 KB](/attachment/image/543832/thumbnail?d=1365649376)](/attachment/image/543832?d=1284543008)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#184](/thread/post/4023484#post4023484 "Post Permalink")

  * Sep 15, 2010 7:00pm  Sep 15, 2010 7:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting skoda2008](/thread/post/4020418#post4020418 "View Quoted Post")
> 
> Disliked
> 
> Sorry about the blank display on the previous version. Here is the latest version (2.3) updated to put out values to the external buffer for an EA to use.  
>    
>  This time it has been tested and works. The number next to "MA" in the indicator window is the value it is sending out.
> 
> Ignored

skoda, sorry, I completely missed this first time around. I just had a look at 'attachments' to see why people are talking about V2.3  
  
Many apologies.  
  
I am keeping this in reserve, and waiting on Mart's reply to my latest. Louise will be a lot quicker if we can incorporate the indi code within hers.  
  
Cheers  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#185](/thread/post/4023485#post4023485 "Post Permalink")

  * Sep 15, 2010 7:01pm  Sep 15, 2010 7:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting DrLobo](/thread/post/4023429#post4023429 "View Quoted Post")
> 
> Disliked
> 
> Hi  
>    
>  I tried testing this 2.3 v of the EA, so I found a buy signal on 15 min chart (just for testing purposes) and attached Louise to the chart and i got the following errors please see attached.
> 
> Ignored

Your ea's are not enabled.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#186](/thread/post/4023526#post4023526 "Post Permalink")

  * Sep 15, 2010 7:18pm  Sep 15, 2010 7:18pm 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

there something i don't understand here   
  
see this pic:  
  
<http://img823.imageshack.us/img823/8147/123vn.gif>  
  
it shows here that the 5 EMA didn't came over the 6 EMA   
  
but it dose  
  
  
or this a new condition :EMA(5.c) & EMA (6.o) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#187](/thread/post/4023600#post4023600 "Post Permalink")

  * Sep 15, 2010 7:51pm  Sep 15, 2010 7:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting tarek95](/thread/post/4023526#post4023526 "View Quoted Post")
> 
> Disliked
> 
> there something i don't understand here   
>    
>  see this pic:  
>    
>  <http://img823.imageshack.us/img823/8147/123vn.gif>  
>    
>  it shows here that the 5 EMA didn't came over the 6 EMA   
>    
>  but it dose  
>    
>    
>  or this a new condition :EMA(5.c) & EMA (6.o)
> 
> Ignored

good point...hmmm  
,is this demo or live? with time u r using? 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#188](/thread/post/4023606#post4023606 "Post Permalink")

  * Sep 15, 2010 7:54pm  Sep 15, 2010 7:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar107454_2.gif) phover](phover)

  * | Joined Jun 2009  | Status: Coder | [226 Posts](/search?do=process&provider=Member&searchuser=107454)

> [Quoting SteveHopwood](/thread/post/4023363#post4023363 "View Quoted Post")
> 
> Disliked
> 
> Actually, Mart, it looks as though you have simply attached the indi with a different name.  
>    
>  Have I missed something?  
>    
>  ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

Oups so sorry! That's what happen when you go sleeping all day at 3h00am ![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1)  
  
Find attached the corrected file ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Cheers,  
  
Mart 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Murrey Advisor function isolated.mq4](/attachment/file/543875?d=1284548040) 10 KB | 267 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#189](/thread/post/4023621#post4023621 "Post Permalink")

  * Sep 15, 2010 8:00pm  Sep 15, 2010 8:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting phover](/thread/post/4023606#post4023606 "View Quoted Post")
> 
> Disliked
> 
> Oups so sorry! That's what happen when you go sleeping all day at 3h00am ![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1)  
>    
>  Find attached the corrected file ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
>    
>  Cheers,  
>    
>  Mart
> 
> Ignored

Fantastic Mart. You are one of the stars of FF.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#190](/thread/post/4023623#post4023623 "Post Permalink")

  * Sep 15, 2010 8:01pm  Sep 15, 2010 8:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

short signal on NZDUSD, sl/tp 35/35...  
Let's see whether this is gonna be my first profit trade with this system : P 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#191](/thread/post/4023691#post4023691 "Post Permalink")

  * Sep 15, 2010 8:26pm  Sep 15, 2010 8:26pm 

  * [ Caillou](caillou)

  * | Joined Apr 2010  | Status: Trader | [1,404 Posts](/search?do=process&provider=Member&searchuser=140687)

> [Quoting PhAnTi'](/thread/post/4023623#post4023623 "View Quoted Post")
> 
> Disliked
> 
> short signal on NZDUSD, sl/tp 35/35...  
>  Let's see whether this is gonna be my first profit trade with this system : P
> 
> Ignored

Hi all,  
  
First of all, thanks mostashar15 for sharing your system. Phanti, this signal in NZD/USD is with v2.3 or v2.2 because I´m testing v2.3 and I don´t have this signal yet, I think it´s coming soon but not yet..... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#192](/thread/post/4023700#post4023700 "Post Permalink")

  * Sep 15, 2010 8:29pm  Sep 15, 2010 8:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting Caillou](/thread/post/4023691#post4023691 "View Quoted Post")
> 
> Disliked
> 
> Hi all,  
>    
>  First of all, thanks mostashar15 for sharing your system. Phanti, this signal in NZD/USD is with v2.3 or v2.2 because I´m testing v2.3 and I don´t have this signal yet, I think it´s coming soon but not yet.....
> 
> Ignored

welli do use v2.3 ....which broker u use? what time u have? 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#193](/thread/post/4023706#post4023706 "Post Permalink")

  * Sep 15, 2010 8:32pm  Sep 15, 2010 8:32pm 

  * [ Caillou](caillou)

  * | Joined Apr 2010  | Status: Trader | [1,404 Posts](/search?do=process&provider=Member&searchuser=140687)

I use IBFX, now all conditions are ok for Short, only EMA 5 & EMA 6 is not ready (False)..... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#194](/thread/post/4023711#post4023711 "Post Permalink")

  * Sep 15, 2010 8:34pm  Sep 15, 2010 8:34pm 

  * [ iamboston](iamboston)

  * | Joined May 2010  | Status: Trader | [199 Posts](/search?do=process&provider=Member&searchuser=142435)

i do indeed like this system - much like the one (below) i've enjoyed trading with for some time ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screen shot 2010-09-15 at 9.32.08 PM.png
Size: 45 KB](/attachment/image/543895/thumbnail?d=1365649407)](/attachment/image/543895?d=1284550415)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#195](/thread/post/4023726#post4023726 "Post Permalink")

  * Sep 15, 2010 8:36pm  Sep 15, 2010 8:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting Caillou](/thread/post/4023706#post4023706 "View Quoted Post")
> 
> Disliked
> 
> I use IBFX, now all conditions are ok for Short, only EMA 5 & EMA 6 is not ready (False).....
> 
> Ignored

hmm let's see .... I personally triggered 3 trades last 2 days, all stopped out by sl 35/35 ... hope this one is going to work now ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#196](/thread/post/4023729#post4023729 "Post Permalink")

  * Sep 15, 2010 8:37pm  Sep 15, 2010 8:37pm 

  * [ Caillou](caillou)

  * | Joined Apr 2010  | Status: Trader | [1,404 Posts](/search?do=process&provider=Member&searchuser=140687)

I hope too, but I don´t understand why I don´t have these signal..... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#197](/thread/post/4023739#post4023739 "Post Permalink")

  * Sep 15, 2010 8:39pm  Sep 15, 2010 8:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting Caillou](/thread/post/4023729#post4023729 "View Quoted Post")
> 
> Disliked
> 
> I hope too, but I don´t understand why I don´t have these signal.....
> 
> Ignored

don't know...  
but seems like another fail....sl will be hit soon : S  
  
4 trades, 4 failes....hmm... 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#198](/thread/post/4023906#post4023906 "Post Permalink")

  * Sep 15, 2010 9:38pm  Sep 15, 2010 9:38pm 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

> [Quoting PhAnTi'](/thread/post/4023600#post4023600 "View Quoted Post")
> 
> Disliked
> 
> good point...hmmm  
>  ,is this demo or live? with time u r using?
> 
> Ignored

Its a demo account on Al trade   
  
well i still don't under stand the function of the Ema   
  
i mean i know what the EMA do in the 2.2 version 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#199](/thread/post/4024009#post4024009 "Post Permalink")

  * Sep 15, 2010 10:15pm  Sep 15, 2010 10:15pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting PhAnTi'](/thread/post/4023600#post4023600 "View Quoted Post")
> 
> Disliked
> 
> good point...hmmm  
>  ,is this demo or live? with time u r using?
> 
> Ignored

In v2.2, it used to show TRUE only when EMA(5,c) > EMA(6,o) by 5 pips but now in v2.3, it will only show TRUE if:  
1\. EMA(5,c) > EMA(6,o) by 5 pips, AND  
2\. Close of last candle is no more than 25 pips above EMA(5,c).  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#200](/thread/post/4024041#post4024041 "Post Permalink")

  * Sep 15, 2010 10:25pm  Sep 15, 2010 10:25pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

I appreciate all the efforts to develop the EA but I have to say this. Unless, we use support and resistance in considerations, this might not give real picture of the strategy. As of now, EA is sending buy/sell orders with 30 pips TP and SL. However, maybe the next resistance/support is only 20 points, therefore, you will see the pair going in your favor direction but not able to reach to your TP point. Therefore, we need someone to export the value of Sup and Res to EA as well through the buffer. TP then will be equal to Res in case of BUY and equal to Sup in case of SELL. SL can be taken simply as 30points since this version v2.3 will not give entry unless you are not more than 25 pips away from EMA(5,c), therefore 30 points is good enough for SL.  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#201](/thread/post/4024053#post4024053 "Post Permalink")

  * Sep 15, 2010 10:29pm  Sep 15, 2010 10:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting mostashar15](/thread/post/4024041#post4024041 "View Quoted Post")
> 
> Disliked
> 
> I appreciate all the efforts to develop the EA but I have to say this. Unless, we use support and resistance in considerations, this might not give real picture of the strategy. As of now, EA is sending buy/sell orders with 30 pips TP and SL. However, maybe the next resistance/support is only 20 points, therefore, you will see the pair going in your favor direction but not able to reach to your TP point. Therefore, we need someone to export the value of Sup and Res to EA as well through...
> 
> Ignored

> Quote
> 
> Disliked
> 
> herefore, we need someone to export the value of Sup and Res to EA as well through the buffer

That's why my trades aren't succesful so far i think : )  
hope s.o. can do this 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#202](/thread/post/4024057#post4024057 "Post Permalink")

  * Sep 15, 2010 10:30pm  Sep 15, 2010 10:30pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting PhAnTi'](/thread/post/4023739#post4023739 "View Quoted Post")
> 
> Disliked
> 
> don't know...  
>  but seems like another fail....sl will be hit soon : S  
>    
>  4 trades, 4 failes....hmm...
> 
> Ignored

I was reviewing chart but I did not see any potential signals over 4 Hr chart. Can you confirm that you are using 4H chart. Can you please attach a snapshot of your chart and indicate th candle that triggered entry for you? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#203](/thread/post/4024095#post4024095 "Post Permalink")

  * Sep 15, 2010 10:40pm  Sep 15, 2010 10:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting mostashar15](/thread/post/4024057#post4024057 "View Quoted Post")
> 
> Disliked
> 
> I was reviewing chart but I did not see any potential signals over 4 Hr chart. Can you confirm that you are using 4H chart. Can you please attach a snapshot of your chart and indicate th candle that triggered entry for you?
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: lifecanbeeasy.gif
Size: 38 KB](/attachment/image/543977/thumbnail?d=1365649407)](/attachment/image/543977?d=1284557993)   

  
  
hm using v2.3  
went short on vertical line as signal appeared 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#204](/thread/post/4024116#post4024116 "Post Permalink")

  * Sep 15, 2010 10:47pm  Sep 15, 2010 10:47pm 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

> [Quoting PhAnTi'](/thread/post/4024095#post4024095 "View Quoted Post")
> 
> Disliked
> 
> [Attachment ](https://www.forexfactory.com/attachment/file/543977)  
>    
>  hm using v2.3  
>  went short on vertical line as signal appeared
> 
> Ignored

  
hmm i think ADX wasn't increasing 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#205](/thread/post/4024187#post4024187 "Post Permalink")

  * Sep 15, 2010 11:14pm  Sep 15, 2010 11:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar132525_2.gif) Centu](centu)

  * | Joined Feb 2010  | Status: Trader | [54 Posts](/search?do=process&provider=Member&searchuser=132525)

> [Quoting mostashar15](/thread/post/4024057#post4024057 "View Quoted Post")
> 
> Disliked
> 
> I was reviewing chart but I did not see any potential signals over 4 Hr chart.
> 
> Ignored

there are/were no signals for majors all day.  
but EUR/CHF - EUR/JPY and USD/JPY look promising.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f617.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f3b6.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#206](/thread/post/4024277#post4024277 "Post Permalink")

  * Sep 15, 2010 11:48pm  Sep 15, 2010 11:48pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting PhAnTi'](/thread/post/4024095#post4024095 "View Quoted Post")
> 
> Disliked
> 
> [Attachment ](https://www.forexfactory.com/attachment/file/543977)  
>    
>  hm using v2.3  
>  went short on vertical line as signal appeared
> 
> Ignored

I wonder if some mql4 GURU can help us show status of signal by putting the cursor over any previous candles, just like attached snapshot. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: historical data.PNG
Size: 107 KB](/attachment/image/544008/thumbnail?d=1365649445)](/attachment/image/544008?d=1284562097)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#207](/thread/post/4024304#post4024304 "Post Permalink")

  * Edited Sep 16, 2010 12:21am  Sep 15, 2010 11:57pm | Edited Sep 16, 2010 12:21am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

I see it is almost like a pattern that every pair which goes away from EMA(5,C) will retrace back to test EMA(5,C) again. Look at the beautiful chart of EURUSD. I am sure we can develop some strategy to get some pips as well in case of retracing. So, if you miss the big candle at least you will get some from its retrace. It needs more observations but hopefully not another five years. Anyway for those who like only to follow the trend once retracing happens and bounced back from EMA(5,C) then this is a very good signal that the pair will continue its direction. I am sorry if I repeated this so many times and I am very sorry if you already know this.  
  
Regards 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: retrace example.gif
Size: 29 KB](/attachment/image/544016/thumbnail?d=1365649445)](/attachment/image/544016?d=1284562715)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#208](/thread/post/4024319#post4024319 "Post Permalink")

  * Sep 16, 2010 12:02am  Sep 16, 2010 12:02am 

  * [ billbss](billbss)

  * Joined Apr 2006 | Status: Trader | [4,301 Posts](/search?do=process&provider=Member&searchuser=9243)

> [Quoting Centu](/thread/post/4024187#post4024187 "View Quoted Post")
> 
> Disliked
> 
> there are/were no signals for majors all day.  
>  but EUR/CHF - EUR/JPY and USD/JPY look promising.  
>    
>  ![](https://resources.faireconomy.media/images/emojis/64/1f617.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f3b6.png?v=15.1)
> 
> Ignored

  
I don't know what you mean by "all day" and I don't know what you mean by "majors".  
  
_There was a losing short on USD/JPY_ taken at 21:00   
09/14.  
  
  
_There was a winning long on EUR/GBP_ at 01:00 09/15.  
  
  
_There was a losing short on NZD/USD_ at 11:00 09/15.  
  
  
I exited the EUR/GBP trade at resistance. If I had tried for 35 pips, it would have lost. I made 15 pips on it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#209](/thread/post/4024403#post4024403 "Post Permalink")

  * Sep 16, 2010 12:30am  Sep 16, 2010 12:30am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting billbss](/thread/post/4024319#post4024319 "View Quoted Post")
> 
> Disliked
> 
> I exited the EUR/GBP trade at resistance. If I had tried for 35 pips, it would have lost. I made 15 pips on it.
> 
> Ignored

Exactly, this is what I said. It will be always a weak point in the current EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#210](/thread/post/4024492#post4024492 "Post Permalink")

  * Sep 16, 2010 1:06am  Sep 16, 2010 1:06am 

  * [ Caillou](caillou)

  * | Joined Apr 2010  | Status: Trader | [1,404 Posts](/search?do=process&provider=Member&searchuser=140687)

No signals for me with v2.3 all day, and for me it´s a "good signal"......![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#211](/thread/post/4024666#post4024666 "Post Permalink")

  * Sep 16, 2010 2:19am  Sep 16, 2010 2:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar114404_1.gif) Forest-Sea](forest-sea)

  * | Joined Aug 2009  | Status: Trader | [561 Posts](/search?do=process&provider=Member&searchuser=114404)

Wonderful job Mostashar. Congratulations.  
  
  
Am I right that your indicator browses the ADX? It must do so to make its buy, sell, hold recommendations.  
  
I ask so that I can eliminate it from the bottom of my chart. I don't think using that space for ADX is of any purpose, is it? Already in the calculation.  
  
Best to you, Forest 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#212](/thread/post/4024718#post4024718 "Post Permalink")

  * Sep 16, 2010 2:44am  Sep 16, 2010 2:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

I wonder ... is it possible to make the SL a variable whereby you run it through the back test and MT4 can tell you which level SL yielded the best results ?   
  
Is that what people call magic number ? (I heard that reffered to a couple of times)  
  
  

> [Quoting mostashar15](/thread/post/4024041#post4024041 "View Quoted Post")
> 
> Disliked
> 
> I appreciate all the efforts to develop the EA but I have to say this. Unless, we use support and resistance in considerations, this might not give real picture of the strategy. As of now, EA is sending buy/sell orders with 30 pips TP and SL. However, maybe the next resistance/support is only 20 points, therefore, you will see the pair going in your favor direction but not able to reach to your TP point. Therefore, we need someone to export the value of Sup and Res to EA as well through...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#213](/thread/post/4024720#post4024720 "Post Permalink")

  * Sep 16, 2010 2:44am  Sep 16, 2010 2:44am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting Forest-Sea](/thread/post/4024666#post4024666 "View Quoted Post")
> 
> Disliked
> 
> Wonderful job Mostashar. Congratulations.  
>    
>    
>  Am I right that your indicator browses the ADX? It must do so to make its buy, sell, hold recommendations.  
>    
>  I ask so that I can eliminate it from the bottom of my chart. I don't think using that space for ADX is of any purpose, is it? Already in the calculation.  
>    
>  Best to you, Forest
> 
> Ignored

Yes, you are correct. You can remove ADX from your screen as it is being calculated in the code itself. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#214](/thread/post/4024731#post4024731 "Post Permalink")

  * Sep 16, 2010 2:51am  Sep 16, 2010 2:51am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

Wo0o0o0oW ![](https://resources.faireconomy.media/images/emojis/64/1f973.png?v=15.1)  
  
I just managed to establish communication between the indicator and EA I am trying to make. I just managed to call current Support, Resistance and current Signal. See below snap. I used some command to read the data directly from the chart which indeed worked. The comments at the left were printed by EA.  
  
Now, I will be completing the EA so that once it triggers an order, it will immediately have its correct TP and SL as per the strategy.   
  
**_HELP!_**  
Can somebody share the code to allow multiple trades but on different pairs? I kind of struggle to make it with my limited knowledge ![](https://resources.faireconomy.media/images/emojis/64/1f612.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/231b.png?v=15.1). 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: ea v1.0 printscreen.gif
Size: 29 KB](/attachment/image/544121/thumbnail?d=1365649445)](/attachment/image/544121?d=1284573049)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#215](/thread/post/4024811#post4024811 "Post Permalink")

  * Sep 16, 2010 3:44am  Sep 16, 2010 3:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting mostashar15](/thread/post/4024731#post4024731 "View Quoted Post")
> 
> Disliked
> 
> Now, I will be completing the EA so that once it triggers an order, it will immediately have its correct TP and SL as per the strategy.   
>    
>  **_HELP!_**  
>  Can somebody share the code to allow multiple trades but on different pairs? I kind of struggle to make it with my limited knowledge ![](https://resources.faireconomy.media/images/emojis/64/1f612.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/231b.png?v=15.1).
> 
> Ignored

Fantastic. I find that someone who understands their own indi _and_ can code the trading ea to go with it is better placed to do the coding, so I am gracefully stepping aside.  
  
Turning a single-trade ea into a multi-pair trader is complicated. I have attached one of the Boris Schlossberg multi-pair traders I wrote a few months ago. Have a look when you are ready, and see if there is anything that will help you.  
  
Chief requirements are:

  1. a method of allowing the user to input the trade pairs in one input, and dividing that up into a pairs array.
  2. creating variables that hold the Symbol(), Point, Digit, Ask and Bid for each pair via the MarketInfo function

If all this gets a bit complicated for you, I can always do the conversion and you can take matters from there.  
  
So, just sing out if you need any help. Once you see how it is done, coding multi-traders is only a bit more complicated than single-pair traders.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Steve Hopwood's BS 5 minute momo multi-pair.mq4](/attachment/file/544133?d=1284575809) 49 KB | 292 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#216](/thread/post/4024851#post4024851 "Post Permalink")

  * Sep 16, 2010 4:17am  Sep 16, 2010 4:17am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting SteveHopwood](/thread/post/4024811#post4024811 "View Quoted Post")
> 
> Disliked
> 
> Fantastic. I find that someone who understands their own indi _and_ can code the trading ea to go with it is better placed to do the coding, so I am gracefully stepping aside.  
>    
>  Turning a single-trade ea into a multi-pair trader is complicated. I have attached one of the Boris Schlossberg multi-pair traders I wrote a few months ago. Have a look when you are ready, and see if there is anything that will help you.  
>    
>  Chief requirements are:  
>  [list][*]a method of allowing the user to input the trade pairs in one input, and dividing that up...
> 
> Ignored

Thanks Steve for jumping to help as usual.   
  
Why does it have to be this complicated?  
  
Why can't you make something that does the follwoing:  
1\. Once EA initiated on EURUSD for example.  
2\. It will wait for the trigger.  
3\. It will scan open oredrs and if there is no open EURUSD positions, then  
4\. It will do Buy or Sell  
  
I believe this can be made simple but I don't know how to make. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#217](/thread/post/4024864#post4024864 "Post Permalink")

  * Sep 16, 2010 4:31am  Sep 16, 2010 4:31am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting mostashar15](/thread/post/4024851#post4024851 "View Quoted Post")
> 
> Disliked
> 
> Thanks Steve for jumping to help as usual.   
>    
>  Why does it have to be this complicated?  
>    
>  Why can't you make something that does the follwoing:  
>  1\. Once EA initiated on EURUSD for example.  
>  2\. It will wait for the trigger.  
>  3\. It will scan open oredrs and if there is no open EURUSD positions, then  
>  4\. It will do Buy or Sell  
>    
>  I believe this can be made simple but I don't know how to make.
> 
> Ignored

After some Googling, I have done something but it looks there is still a mistake somewhere.  
  
Can you look into it and figure out why it did not work?  
  
By the way, I put the BUY conditions in this version to be Hold! just to test the code if it will trigger and Buy orders since we have no signals as of now.  
  
You can see how I called the data from the indicator:  
  
  

Inserted Code
    
    
    string CurrentResTxt = ObjectDescription("TSR7");
       string CurrentSupTxt = ObjectDescription("TSR5");
       string TradingStatus = ObjectDescription("25");
       
       double CurrentRes = StrToDouble(CurrentResTxt);
       double CurrentSup = StrToDouble(CurrentSupTxt);
       
       Comment("MoStAsHaR15 FoReX - Murrey Advisor EA v1.0",
        "n","Only use with 4Hr timeframe",
        "n","Current Resistance - ",CurrentResTxt,
        "n","Current Support     - ",CurrentSupTxt,
        "n","Current Signal       - ",TradingStatus);

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Murrey Advisor EA v1.0 DEMO.mq4](/attachment/file/544152?d=1284579047) 5 KB | 217 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#218](/thread/post/4024966#post4024966 "Post Permalink")

  * Sep 16, 2010 5:51am  Sep 16, 2010 5:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting mostashar15](/thread/post/4024864#post4024864 "View Quoted Post")
> 
> Disliked
> 
> After some Googling, I have done something but it looks there is still a mistake somewhere.  
>    
>  Can you look into it and figure out why it did not work?  
>    
>  By the way, I put the BUY conditions in this version to be Hold! just to test the code if it will trigger and Buy orders since we have no signals as of now.  
>    
>  You can see how I called the data from the indicator:...
> 
> Ignored

A few things.  
  
First, add a couple of routines to tell you what is going on immediately. So, I have added:  

Inserted Code
    
    
    int init()
    {
    //----
       Comment(".........................Waiting for the first tick");
    //----
       return(0);
    }
    
    int deinit()
    {
    //----
       Comment("");
    //----
       return(0);
    }

The first tells you that there has not been a tick yet. The second clears the comment so you know you have not forgotten to re-compile - and you _will_ forget and wonder why the screen has not changed. Guess how I know? ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)  
  
Futher down, these three lines stop your code executing further:  

Inserted Code
    
    
       if(buys > 0) return(buys);
       else if(sells > 0) return(-sells);
       else return(0);

One way or another, _everything_ ends in return, which means the code can go no further.  
  
Use the Alert() function in debugging. I have added Alert(TradingStatus); immediately after the lines I described earlier but commented out. This shows that TradingStatus is empty on my chart, so your OrderSend() commands cannot execute. If you have an object called "25" on your chart called "HOLD!" or "Go Short" for testing purposes, then it is the above 3 lines that are stopping the trade executing.  
  
Incidentally, notice the #include statements I added to the start of your code. Then see the error code I added to your if(TradingStatus == "HOLD!") code block. The #include statements allow the error reporting. Error reporting is essential for the developer to know when things are going wrong.  
  
It seems to me that you are trying to do too much too early. Tackle one problem at a time so: 

  1. learn to extract and display information from the indi
  2. learn to use this info to send trades
  3. third learn how to know when trades already exists so that step 2 is avoided when unnecessary
  4. add mm facilities

I hope this helps. Sing out when you need more info. Fell free to pinch my code for your own use.  
  
You are doing the right thing here. In the absence of being a trained programmer, the only way to learn to code is to do it.  
  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Murrey Advisor EA v1.0 DEMO.mq4](/attachment/file/544170?d=1284582856) 6 KB | 208 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#219](/thread/post/4024997#post4024997 "Post Permalink")

  * Sep 16, 2010 6:11am  Sep 16, 2010 6:11am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

I think I did it. I just tried it and worked fine.  
  
Please try on a demo account and let me know so that we can proceed further improvements if the basic functions work properly.  
  
Both the indicator and EA have to be added to to each chart simultaneously.  
  
Regards 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Murrey Advisor EA v1.0.mq4](/attachment/file/544181?d=1284585098) 5 KB | 294 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#220](/thread/post/4025011#post4025011 "Post Permalink")

  * Sep 16, 2010 6:21am  Sep 16, 2010 6:21am 

  * [ Invisible](invisible)

  * | Joined Nov 2009  | Status: Trader | [469 Posts](/search?do=process&provider=Member&searchuser=124048)

mostashar15 and Sir Steve.... Go Team EA!  
  
Thanks guys. Will be testing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#221](/thread/post/4025053#post4025053 "Post Permalink")

  * Sep 16, 2010 6:43am  Sep 16, 2010 6:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting mostashar15](/thread/post/4024997#post4024997 "View Quoted Post")
> 
> Disliked
> 
> I think I did it. I just tried it and worked fine.  
>    
>  Please try on a demo account and let me know so that we can proceed further improvements if the basic functions work properly.  
>    
>  Both the indicator and EA have to be added to to each chart simultaneously.  
>    
>  Regards
> 
> Ignored

Wonderful. I didn't realise we can get the value of a label this way; this will make my life easier in the future.  
  
Your stop loss calculations will not work for 5 digit criminals. It will always be a tenth of what is required; this will often result in a stop that is too close to the market to be allowed, and throw up 'invalid stops' errors.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#222](/thread/post/4025182#post4025182 "Post Permalink")

  * Sep 16, 2010 8:13am  Sep 16, 2010 8:13am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting SteveHopwood](/thread/post/4025053#post4025053 "View Quoted Post")
> 
> Disliked
> 
> Wonderful. I didn't realise we can get the value of a label this way; this will make my life easier in the future.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

Mmmmm, at least you found one thing new to you in my code.  
  

> Quote
> 
> Disliked
> 
> Your stop loss calculations will not work for 5 digit criminals. It will always be a tenth of what is required; this will often result in a stop that is too close to the market to be allowed, and throw up 'invalid stops' errors.

  
How do you propose to fix it? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#223](/thread/post/4025307#post4025307 "Post Permalink")

  * Sep 16, 2010 10:06am  Sep 16, 2010 10:06am 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

great work   
  
So how this new Ea put the take profit and Sl lvls   
  
next support/resistance ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#224](/thread/post/4025693#post4025693 "Post Permalink")

  * Edited 3:47pm  Sep 16, 2010 2:41pm | Edited 3:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting mostashar15](/thread/post/4024997#post4024997 "View Quoted Post")
> 
> Disliked
> 
> I think I did it. I just tried it and worked fine.  
>    
>  Please try on a demo account and let me know so that we can proceed further improvements if the basic functions work properly.  
>    
>  Both the indicator and EA have to be added to to each chart simultaneously.  
>    
>  Regards
> 
> Ignored

good work mostashar , but,**which indicator to be added(v2.2 or v2.3) with ea plz ??** ,its working fine now with v2.2 until u tell me and i have nzd short signal now triggered ... thnx 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#225](/thread/post/4025740#post4025740 "Post Permalink")

  * Sep 16, 2010 3:22pm  Sep 16, 2010 3:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting mostashar15](/thread/post/4025182#post4025182 "View Quoted Post")
> 
> Disliked
> 
> Mmmmm, at least you found one thing new to you in my code.  
>    
>    
>    
>  How do you propose to fix it?
> 
> Ignored

You make the stop loss a variable. Either  
  
extern int StopLoss = 30;  
  
if you want to make it a user input, or  
  
int StopLoss = 30;  
  
if you want to keep it internal.  
  
Then you put this snippet in your init() function:  
  

Inserted Code
    
    
       //Accommodate different quote sizes
       double multiplier;
       if(Digits == 2 || Digits == 4) multiplier = 1;
       if(Digits == 3 || Digits == 5) multiplier = 10;
       if(Digits == 6) multiplier = 100;   
       StopLoss*= multiplier;

This automatically adapts the stop loss to x digit accounts. Lunatic as it sounds, apparently some wally-plonker-utter-tosspot crims are quoting 6 ditits these days.  
  
Then your buy code becomes:  

Inserted Code
    
    
    ticket=OrderSend(Symbol(),OP_BUY,Lots,Ask,3,NormalizeDouble(Ask - (StopLoss * Point), Digits),CurrentRes,"Murrey Advisor EA v1.0",1070,0,Green);

and your sell code:  

Inserted Code
    
    
    ticket=OrderSend(Symbol(),OP_SELL,Lots,Bid,3,NormalizeDouble(Bid+(StopLoss*Point), Digits),CurrentSup,"Murrey Advisor EA v1.0",1070,0,Red);

Edited version attached.  
  
There is some extra code to add if there is a possibility of a zero stop loss, but you can worry about that later on. You can see what is required if you look at Louise's code.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Murrey Advisor EA v1.0.mq4](/attachment/file/544364?d=1284618052) 6 KB | 284 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#226](/thread/post/4025780#post4025780 "Post Permalink")

  * Sep 16, 2010 3:45pm  Sep 16, 2010 3:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar61335_2.gif) courtneywild](courtneywild)

  * | Joined Feb 2008  | Status: Trader | [678 Posts](/search?do=process&provider=Member&searchuser=61335)

HI  
  
I took 20 pips from the USDJPY on signal yesterday.  
Funny it was off the **retrace** candle.   
There was a bull spike candle 0.00 hours  
Followed by another uptick candle at 04.00  
Then the 08:00 hour candle retraced. I got a buy signal in the candle at 11:00 at took 20 pips. I am on GMT +1 but my charts show + 2 I.E 8am for me my chart show 6.00am...   
  
Now upgraded to version 3 and today is will see if any trades triggerd. Lot of NEWs out today so...ooooohhhh. ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)  
  
Results for week (demo) so far, though I'm not around to trade every signal.  
  
13th EUR USD +26  
13th USD CAD +16  
13th EUR GBP +19  
14th EUR GBP -35  
15th USD JPY +20  
Total +46  
  
Thank you Mostashar15 ![](https://resources.faireconomy.media/images/emojis/64/1f47c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#227](/thread/post/4026152#post4026152 "Post Permalink")

  * Sep 16, 2010 6:16pm  Sep 16, 2010 6:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting courtneywild](/thread/post/4025780#post4025780 "View Quoted Post")
> 
> Disliked
> 
> HI  
>    
>  I took 20 pips from the USDJPY on signal yesterday.  
>  Funny it was off the **retrace** candle.   
>  There was a bull spike candle 0.00 hours  
>  Followed by another uptick candle at 04.00  
>  Then the 08:00 hour candle retraced. I got a buy signal in the candle at 11:00 at took 20 pips....
> 
> Ignored

uhhm completely different results than mine....what sl/tp u use? 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#228](/thread/post/4026159#post4026159 "Post Permalink")

  * Sep 16, 2010 6:19pm  Sep 16, 2010 6:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting tahshoon](/thread/post/4025693#post4025693 "View Quoted Post")
> 
> Disliked
> 
> good work mostashar , but,**which indicator to be added(v2.2 or v2.3) with ea plz ??** ,its working fine now with v2.2 until u tell me and i have nzd short signal now triggered ... thnx
> 
> Ignored

i think 3.2 to have the added condition to filter out those ''retracement-trades'' 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#229](/thread/post/4026182#post4026182 "Post Permalink")

  * Sep 16, 2010 6:28pm  Sep 16, 2010 6:28pm 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

just closed eurusd + 30   
  
this is the first signal for me with 2.3 version   
  
but it was about hit the stop loss after 5 pips   
  
my stop loss was -40   
  
but i think it was much safer to make SL the Previous support   
  
see this pic i entered on the vertical line  
  
<http://img842.imageshack.us/img842/6409/123ri.gif>  
  
also it hit the next Resistance ...and it retrace from the the EMA very good  

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#230](/thread/post/4026304#post4026304 "Post Permalink")

  * Sep 16, 2010 7:10pm  Sep 16, 2010 7:10pm 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

its really annoying something wrong with the indi its 2.3 its disappear   
  
<http://img580.imageshack.us/img580/7138/123eqw.gif>  
  
Its on Altrade  
  
and there another qus   
  
I have two accounts fxopen and altrade ....the problem is both gave diffrent signal i may got signal on altrade but not on fxopen   
  
i dono why maybe due diff time in both servers ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#231](/thread/post/4026332#post4026332 "Post Permalink")

  * Sep 16, 2010 7:22pm  Sep 16, 2010 7:22pm 

  * [ skoda2008](skoda2008)

  * | Joined Mar 2010  | Status: Trader | [224 Posts](/search?do=process&provider=Member&searchuser=137969)

> [Quoting tarek95](/thread/post/4026304#post4026304 "View Quoted Post")
> 
> Disliked
> 
> its really annoying something wrong with the indi its 2.3 its disappear
> 
> Ignored

If you use the version I posted earlier in this thread it should not disappear:  
  
<http://www.forexfactory.com/showpost.php?p=4020418>  
  
Make sure you rename the file to be the same as the one you were using (so that the EA knows where to find it). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#232](/thread/post/4026368#post4026368 "Post Permalink")

  * Sep 16, 2010 7:40pm  Sep 16, 2010 7:40pm 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

> [Quoting skoda2008](/thread/post/4026332#post4026332 "View Quoted Post")
> 
> Disliked
> 
> If you use the version I posted earlier in this thread it should not disappear:  
>    
>  <http://www.forexfactory.com/showpost.php?p=4020418>  
>    
>  Make sure you rename the file to be the same as the one you were using (so that the EA knows where to find it).
> 
> Ignored

thx buddy im gona try 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#233](/thread/post/4026416#post4026416 "Post Permalink")

  * Sep 16, 2010 8:00pm  Sep 16, 2010 8:00pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting SteveHopwood](/thread/post/4025740#post4025740 "View Quoted Post")
> 
> Disliked
> 
> You make the stop loss a variable. Either  
>    
>  extern int StopLoss = 30;  
>    
>  if you want to make it a user input, or  
>    
>  int StopLoss = 30;  
>    
>  if you want to keep it internal.  
>    
>  Then you put this snippet in your init() function:  
>    
>  [code]...
> 
> Ignored

Thanks my master 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#234](/thread/post/4026427#post4026427 "Post Permalink")

  * Sep 16, 2010 8:04pm  Sep 16, 2010 8:04pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

Yesterday, I got in with EURUSD after it bounced back from EMA(5,c) even though thee was no signal but I wanted to test this strategy and today got up with **+100 pips** in account.  
  
This never happened to me.  
  
I will try to see if I can incorporate this in new versions if it works most of the times. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#235](/thread/post/4026430#post4026430 "Post Permalink")

  * Sep 16, 2010 8:06pm  Sep 16, 2010 8:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting mostashar15](/thread/post/4026427#post4026427 "View Quoted Post")
> 
> Disliked
> 
> Yesterday, I got in with EURUSD after it bounced back from EMA(5,c) even though thee was no signal but I wanted to test this strategy and today got up with **+100 pips** in account.  
>    
>  This never happened to me.  
>    
>  I will try to see if I can incorporate this in new versions if it works most of the times.
> 
> Ignored

i just attached EA to the named pairs...let's see how it will work 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#236](/thread/post/4026432#post4026432 "Post Permalink")

  * Sep 16, 2010 8:06pm  Sep 16, 2010 8:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

shot nzdusd btw 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#237](/thread/post/4026434#post4026434 "Post Permalink")

  * Sep 16, 2010 8:06pm  Sep 16, 2010 8:06pm 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

what is the difference between your system and mer07198's which works on daily time frame..I see that sometime back you were posting on his thread??? also do we have all the bugs out of it, I lost on all three trades last week???  
sfg7th 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#238](/thread/post/4026444#post4026444 "Post Permalink")

  * Sep 16, 2010 8:09pm  Sep 16, 2010 8:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting sfg7th](/thread/post/4026434#post4026434 "View Quoted Post")
> 
> Disliked
> 
> what is the difference between your system and mer07198's which works on daily time frame..I see that sometime back you were posting on his thread??? also do we have all the bugs out of it, I lost on all three trades last week???  
>  sfg7th
> 
> Ignored

> Quote
> 
> Disliked
> 
> I lost on all three trades last week

  
me as well 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#239](/thread/post/4026448#post4026448 "Post Permalink")

  * Sep 16, 2010 8:11pm  Sep 16, 2010 8:11pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting tarek95](/thread/post/4025307#post4025307 "View Quoted Post")
> 
> Disliked
> 
> great work   
>    
>  So how this new Ea put the take profit and Sl lvls   
>    
>  next support/resistance ?
> 
> Ignored

TP: Next Support  
SL: -30 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#240](/thread/post/4026455#post4026455 "Post Permalink")

  * Sep 16, 2010 8:12pm  Sep 16, 2010 8:12pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting tahshoon](/thread/post/4025693#post4025693 "View Quoted Post")
> 
> Disliked
> 
> good work mostashar , but,**which indicator to be added(v2.2 or v2.3) with ea plz ??** ,its working fine now with v2.2 until u tell me and i have nzd short signal now triggered ... thnx
> 
> Ignored

It can work with either version. But, use it with v2.3. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#241](/thread/post/4026457#post4026457 "Post Permalink")

  * Sep 16, 2010 8:13pm  Sep 16, 2010 8:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar61335_2.gif) courtneywild](courtneywild)

  * | Joined Feb 2008  | Status: Trader | [678 Posts](/search?do=process&provider=Member&searchuser=61335)

_[Hi PhAnTi'](http://www.forexfactory.com/member.php?u=151785)  
  
_My stop loss was 30 my TP is 30 but any doubt and I'm out. If you drop the chart to hourly you will see the entry bar and the following bull bar where profit came from (though I don't trade hourly only 4 hour, sticking with system)._  
  
Could someone explain the following (at the risk of looking dumb - still, no ego)  
  
_The indi status  
Long Status Current Open>Sup (+3p) OK so I read open greater than support +3 pips. Which support is this? Is it the Murry line because the price is often way above ML+3 and yet it still does not trigger.   
  
Its the one indi that seems to take an age to turn positive._  
  
Much appreciation to everyone.  
  
Thnx  
  
_

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#242](/thread/post/4026555#post4026555 "Post Permalink")

  * Sep 16, 2010 8:56pm  Sep 16, 2010 8:56pm 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

> [Quoting mostashar15](/thread/post/4026448#post4026448 "View Quoted Post")
> 
> Disliked
> 
> TP: Next Support  
>  SL: -30
> 
> Ignored

very nice so in EURUSD today i shouldn't get with 30+ only i could take 54+ but no problem 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#243](/thread/post/4026659#post4026659 "Post Permalink")

  * Sep 16, 2010 9:27pm  Sep 16, 2010 9:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

hi everyone,  
  
are we testing on the Murray EA advisor v1 or are we trading using the 2.3 template (post 1) ?  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#244](/thread/post/4026660#post4026660 "Post Permalink")

  * Sep 16, 2010 9:27pm  Sep 16, 2010 9:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar132525_2.gif) Centu](centu)

  * | Joined Feb 2010  | Status: Trader | [54 Posts](/search?do=process&provider=Member&searchuser=132525)

> [Quoting billbss](/thread/post/4024319#post4024319 "View Quoted Post")
> 
> Disliked
> 
> I don't know what you mean by "all day" and I don't know what you mean by "majors".  
>    
>  _There was a losing short on USD/JPY_ taken at 21:00   
>  09/14.  
>    
>  _There was a winning long on EUR/GBP_ at 01:00 09/15.  
>    
>  _There was a losing short on NZD/USD_ at 11:00 09/15.  
>    
>    
>  I exited the EUR/GBP trade at resistance. If I had tried for 35 pips, it would have lost. I made 15 pips on it.
> 
> Ignored

i trade only london and early ny session so i didn´t notice the first two and kiwi.  
  
sry for that ![](https://resources.faireconomy.media/images/emojis/64/270c-fe0f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#245](/thread/post/4026705#post4026705 "Post Permalink")

  * Sep 16, 2010 9:38pm  Sep 16, 2010 9:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting DrLobo](/thread/post/4026659#post4026659 "View Quoted Post")
> 
> Disliked
> 
> hi everyone,  
>    
>  are we testing on the Murray EA advisor v1 or are we trading **using the 2.3 template** (post 1) ?  
>    
>  Thanks
> 
> Ignored

best regards 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#246](/thread/post/4026895#post4026895 "Post Permalink")

  * Sep 16, 2010 10:33pm  Sep 16, 2010 10:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

usdjpy long  
let's see : p 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#247](/thread/post/4026940#post4026940 "Post Permalink")

  * Sep 16, 2010 10:45pm  Sep 16, 2010 10:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

guys something wrong with my system here and i did not get this long call on usd/jpy.  
  
I am using version 2.3.  
  
I also tried strategy test on the EA advisor 1 and did not get a single trade opportunity in the last month.  
  

> [Quoting PhAnTi'](/thread/post/4026895#post4026895 "View Quoted Post")
> 
> Disliked
> 
> usdjpy long  
>  let's see : p
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2.jpg
Size: 178 KB](/attachment/image/544616/thumbnail?d=1365649569)](/attachment/image/544616?d=1284644655)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#248](/thread/post/4026966#post4026966 "Post Permalink")

  * Sep 16, 2010 10:50pm  Sep 16, 2010 10:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3317_4.gif) pipsacker](pipsacker)

  * | Joined Aug 2005  | Status: Trader | [127 Posts](/search?do=process&provider=Member&searchuser=3317)

Hi All,  
  
No signal here. I have 2.3 without ea., using IBFX demo.  
  
pipsacker 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#249](/thread/post/4026975#post4026975 "Post Permalink")

  * Sep 16, 2010 10:52pm  Sep 16, 2010 10:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: lifecanbeeasy.gif
Size: 41 KB](/attachment/image/544622/thumbnail?d=1365649569)](/attachment/image/544622?d=1284645162)   

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#250](/thread/post/4026986#post4026986 "Post Permalink")

  * Sep 16, 2010 10:55pm  Sep 16, 2010 10:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

Can u check to see which version u have installed ?  
maybe you are still using 2.2 ?  
  
  

> [Quoting PhAnTi'](/thread/post/4026975#post4026975 "View Quoted Post")
> 
> Disliked
> 
> [Attachment ](https://www.forexfactory.com/attachment/file/544622)
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#251](/thread/post/4026991#post4026991 "Post Permalink")

  * Sep 16, 2010 10:57pm  Sep 16, 2010 10:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting DrLobo](/thread/post/4026986#post4026986 "View Quoted Post")
> 
> Disliked
> 
> Can u check to see which version u have installed ?  
>  maybe you are still using 2.2 ?
> 
> Ignored

tpl ma 2.3 and EA v.1 and indicator 2.3 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#252](/thread/post/4027004#post4027004 "Post Permalink")

  * Sep 16, 2010 11:00pm  Sep 16, 2010 11:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

very strange we should have the same setup and the same readings ...  
  
i will reinstall and start again.  
  
  

> [Quoting PhAnTi'](/thread/post/4026991#post4026991 "View Quoted Post")
> 
> Disliked
> 
> tpl ma 2.3 and EA v.1 and indicator 2.3
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#253](/thread/post/4027008#post4027008 "Post Permalink")

  * Sep 16, 2010 11:02pm  Sep 16, 2010 11:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting DrLobo](/thread/post/4027004#post4027004 "View Quoted Post")
> 
> Disliked
> 
> very strange we should have the same setup and the same readings ...  
>    
>  i will reinstall and start again.
> 
> Ignored

do oyu use H4 timeframe? 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#254](/thread/post/4027012#post4027012 "Post Permalink")

  * Sep 16, 2010 11:03pm  Sep 16, 2010 11:03pm 

  * [ Caillou](caillou)

  * | Joined Apr 2010  | Status: Trader | [1,404 Posts](/search?do=process&provider=Member&searchuser=140687)

Not signal for me, V2.3, IBFX Demo, still waiting...... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#255](/thread/post/4027014#post4027014 "Post Permalink")

  * Sep 16, 2010 11:03pm  Sep 16, 2010 11:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting Caillou](/thread/post/4027012#post4027012 "View Quoted Post")
> 
> Disliked
> 
> Not signal for me, V2.3, IBFX Demo, still waiting......
> 
> Ignored

I'm on FXopen.com live 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#256](/thread/post/4027075#post4027075 "Post Permalink")

  * Sep 16, 2010 11:22pm  Sep 16, 2010 11:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

I reinstalled everything but i still have Hold signal on H4 timeframe.  
  
The long signal is failing on account of the EMA5&6  
  
  

> [Quoting PhAnTi'](/thread/post/4027008#post4027008 "View Quoted Post")
> 
> Disliked
> 
> do oyu use H4 timeframe?
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#257](/thread/post/4027084#post4027084 "Post Permalink")

  * Sep 16, 2010 11:25pm  Sep 16, 2010 11:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting DrLobo](/thread/post/4027075#post4027075 "View Quoted Post")
> 
> Disliked
> 
> I reinstalled everything but i still have Hold signal on H4 timeframe.  
>    
>  The long signal is failing on account of the EMA5&6
> 
> Ignored

I don't know what's the matter... using v3.2 , EA v1  
  
uhhmm maybe systeminventor got an idea ; D 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#258](/thread/post/4027089#post4027089 "Post Permalink")

  * Sep 16, 2010 11:28pm  Sep 16, 2010 11:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

just for clarrity i am assuming thats a typo and you meant 2.3 not 3.2 ?  
  
anyway good luck in your trade ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  

> [Quoting PhAnTi'](/thread/post/4027084#post4027084 "View Quoted Post")
> 
> Disliked
> 
> I don't know what's the matter... using v3.2 , EA v1  
>    
>  uhhmm maybe systeminventor got an idea ; D
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#259](/thread/post/4027092#post4027092 "Post Permalink")

  * Sep 16, 2010 11:28pm  Sep 16, 2010 11:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting DrLobo](/thread/post/4027089#post4027089 "View Quoted Post")
> 
> Disliked
> 
> just for clarrity i am assuming thats a typo and you meant 2.3 not 3.2 ?  
>    
>  anyway good luck in your trade ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

> Quote
> 
> Disliked
> 
> typo and you meant 2.3 not 3.2 ?

yes it is,  
sry ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#260](/thread/post/4027251#post4027251 "Post Permalink")

  * Sep 17, 2010 12:12am  Sep 17, 2010 12:12am 

  * [ Invisible](invisible)

  * | Joined Nov 2009  | Status: Trader | [469 Posts](/search?do=process&provider=Member&searchuser=124048)

I tried backtesting the updated version of the EA (1.0) yesterday, but had no trades at all for 2010 to end of July on EURUSD. This does not seem right. There were no errors in the journal. As anyone else been able to backtest successfully (this latest one, not the original Steve H one)? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#261](/thread/post/4027345#post4027345 "Post Permalink")

  * Sep 17, 2010 12:47am  Sep 17, 2010 12:47am 

  * [ intersis](intersis)

  * | Joined Sep 2010  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=155135)

> [Quoting Invisible](/thread/post/4027251#post4027251 "View Quoted Post")
> 
> Disliked
> 
> I tried backtesting the updated version of the EA (1.0) yesterday, but had no trades at all for 2010 to end of July on EURUSD. This does not seem right. There were no errors in the journal. As anyone else been able to backtest successfully (this latest one, not the original Steve H one)?
> 
> Ignored

did tried for backtest but same thing to me. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#262](/thread/post/4027748#post4027748 "Post Permalink")

  * Sep 17, 2010 3:39am  Sep 17, 2010 3:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar134150_1.gif) greenius](greenius)

  * | Joined Feb 2010  | Status: Harmonic Trader | [513 Posts](/search?do=process&provider=Member&searchuser=134150)

ياعطيك العافية هنا افضل من المتداول على الاقل تلاقي ناس تساعد بي المواضيع تفضل زور المواضي التي عرضها بي فوريكس فاكتوري 

GREENIUS

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#263](/thread/post/4027792#post4027792 "Post Permalink")

  * Sep 17, 2010 4:02am  Sep 17, 2010 4:02am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting Invisible](/thread/post/4027251#post4027251 "View Quoted Post")
> 
> Disliked
> 
> I tried backtesting the updated version of the EA (1.0) yesterday, but had no trades at all for 2010 to end of July on EURUSD. This does not seem right. There were no errors in the journal. As anyone else been able to backtest successfully (this latest one, not the original Steve H one)?
> 
> Ignored

Backtesting does not work, because you cannot get historical data for the signals. It can only work on forward testing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#264](/thread/post/4027794#post4027794 "Post Permalink")

  * Sep 17, 2010 4:03am  Sep 17, 2010 4:03am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting greenius](/thread/post/4027748#post4027748 "View Quoted Post")
> 
> Disliked
> 
> ياعطيك العافية هنا افضل من المتداول على الاقل تلاقي ناس تساعد بي المواضيع تفضل زور المواضي التي...
> 
> Ignored

شكرا لك ولكل منتدى متعته. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#265](/thread/post/4027805#post4027805 "Post Permalink")

  * Sep 17, 2010 4:07am  Sep 17, 2010 4:07am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting courtneywild](/thread/post/4025780#post4025780 "View Quoted Post")
> 
> Disliked
> 
> HI  
>    
>  I took 20 pips from the USDJPY on signal yesterday.  
>  Funny it was off the **retrace** candle.   
>  There was a bull spike candle 0.00 hours  
>  Followed by another uptick candle at 04.00  
>  Then the 08:00 hour candle retraced. I got a buy signal in the candle at 11:00 at took 20 pips....
> 
> Ignored

I am happy to see such positive results.   
  
Wish you green pips continue 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#266](/thread/post/4027812#post4027812 "Post Permalink")

  * Sep 17, 2010 4:09am  Sep 17, 2010 4:09am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting tarek95](/thread/post/4026182#post4026182 "View Quoted Post")
> 
> Disliked
> 
> just closed eurusd + 30   
>    
>  this is the first signal for me with 2.3 version   
>    
>  but it was about hit the stop loss after 5 pips   
>    
>  my stop loss was -40   
>    
>  but i think it was much safer to make SL the Previous support   
>    
>  see this pic i entered on the vertical line  
>    
>  <http://img842.imageshack.us/img842/6409/123ri.gif>  
>    
>  also it hit the next Resistance ...and it retrace from the the EMA very good  
> 
> 
> Ignored

Sometimes, it happens to hit SL and immediately next candle, you will get another entry signal. You just go again and might be get lucky this time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#267](/thread/post/4027821#post4027821 "Post Permalink")

  * Sep 17, 2010 4:11am  Sep 17, 2010 4:11am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting tarek95](/thread/post/4026304#post4026304 "View Quoted Post")
> 
> Disliked
> 
> its really annoying something wrong with the indi its 2.3 its disappear   
>    
>  <http://img580.imageshack.us/img580/7138/123eqw.gif>  
>    
>  Its on Altrade  
>    
>  and there another qus   
>    
>  I have two accounts fxopen and altrade ....the problem is both gave diffrent signal i may got signal on altrade but not on fxopen   
>    
>  i dono why maybe due diff time in both servers ?
> 
> Ignored

The official EA is the one I posted here as it applies the strategy in terms of TP and SL.  
  
Unfortunately, until now it works only with 4 digit brokers.  
  
[http://cdn.forexfactory.com/attachme...1&d=1284585098](http://cdn.forexfactory.com/attachment.php?attachmentid=544181&d=1284585098)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#268](/thread/post/4027829#post4027829 "Post Permalink")

  * Sep 17, 2010 4:14am  Sep 17, 2010 4:14am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting sfg7th](/thread/post/4026434#post4026434 "View Quoted Post")
> 
> Disliked
> 
> what is the difference between your system and mer07198's which works on daily time frame..I see that sometime back you were posting on his thread??? also do we have all the bugs out of it, I lost on all three trades last week???  
>  sfg7th
> 
> Ignored

Main difference:  
  
(1) He is using daily timeframe while I use 4Hr timeframe.  
(2) He depends only on Murrey while I depend on other indicators such as ADX and EMA(5,C) and EMA(6,O). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#269](/thread/post/4027835#post4027835 "Post Permalink")

  * Sep 17, 2010 4:15am  Sep 17, 2010 4:15am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting PhAnTi'](/thread/post/4026444#post4026444 "View Quoted Post")
> 
> Disliked
> 
> me as well
> 
> Ignored

I am sure v2.3 does better job. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#270](/thread/post/4027865#post4027865 "Post Permalink")

  * Sep 17, 2010 4:30am  Sep 17, 2010 4:30am 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

> [Quoting mostashar15](/thread/post/4027821#post4027821 "View Quoted Post")
> 
> Disliked
> 
> The official EA is the one I posted here as it applies the strategy in terms of TP and SL.  
>    
>  Unfortunately, until now it works only with 4 digit brokers.  
>    
>  [http://cdn.forexfactory.com/attachme...1&d=1284585098](http://cdn.forexfactory.com/attachment.php?attachmentid=544181&d=1284585098)
> 
> Ignored

hmm im sorry what is the 4 digit brokers and 5 digit brokers   
  
just a small explain   
  
so is ALtrade works with the EA or FXopen? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#271](/thread/post/4027903#post4027903 "Post Permalink")

  * Sep 17, 2010 4:46am  Sep 17, 2010 4:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting mostashar15](/thread/post/4027835#post4027835 "View Quoted Post")
> 
> Disliked
> 
> I am sure v2.3 does better job.
> 
> Ignored

looks like yes ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#272](/thread/post/4027948#post4027948 "Post Permalink")

  * Sep 17, 2010 5:06am  Sep 17, 2010 5:06am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting DrLobo](/thread/post/4026986#post4026986 "View Quoted Post")
> 
> Disliked
> 
> Can u check to see which version u have installed ?  
>  maybe you are still using 2.2 ?
> 
> Ignored

To clarify it:  
  
If 2.3 gives a signal then by default 2.2 will give the same signal. But, If 2.2 gives a signal, then not necessarily 2.3 will give this signal. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#273](/thread/post/4027954#post4027954 "Post Permalink")

  * Sep 17, 2010 5:10am  Sep 17, 2010 5:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

i have now another signal ( nzd ),yen signal before ...  
two signals triggered now ,v2.3 with ea ... 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: nzd triggered.png
Size: 51 KB](/attachment/image/544837/thumbnail?d=1365649641)](/attachment/image/544837?d=1284667822)   
[![Click to Enlarge

Name: yen triggered.png
Size: 60 KB](/attachment/image/544838/thumbnail?d=1365649641)](/attachment/image/544838?d=1284667822)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#274](/thread/post/4027963#post4027963 "Post Permalink")

  * Sep 17, 2010 5:14am  Sep 17, 2010 5:14am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

Now at 16:00 EST candle, I have the following:  
  
EURUSD - LONG - TP = 1.3123 - SL: -30  
NZDUSD - SHORT - TP = 0.7202 - SL = -30  
  
Also, I am in already with past signal for USDJPY - LONG - TP = 85.94 (Now it is HOLD)  
  
Let us see ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#275](/thread/post/4027970#post4027970 "Post Permalink")

  * Sep 17, 2010 5:15am  Sep 17, 2010 5:15am 

  * [ Invisible](invisible)

  * | Joined Nov 2009  | Status: Trader | [469 Posts](/search?do=process&provider=Member&searchuser=124048)

> [Quoting mostashar15](/thread/post/4027792#post4027792 "View Quoted Post")
> 
> Disliked
> 
> Backtesting does not work, because you cannot get historical data for the signals. It can only work on forward testing.
> 
> Ignored

I'm surprised you say this, as the point of running an EA through the strategy tester is to run it against past price data to see how the strategy would have fared. Of course, the results are not perfect, but if you have an equity line straight down to zero, you know you have a problem. Another warning sign is a lot of errors in the journal. In the case of this EA, it did not produce any results, but also no errors.  
  
I have not written EAs, but I have modified EAs and have seen this kind of thing before where I have accidentally set the logic up so that it would be impossible to ever get a trade. (You can imagine how this could happen: Only sell when the price is over the 5EMA and below the 5EMA, for example. Obviously logic like this will result in no trades.) We know from your manual trading that there should be some trades being taken over an 7-month period, so it makes me wonder whether there is a logic issue in the conditions required for a buy or sell in the EA which is not right and which is therefore causing this situation where no trades are ever sent, but that there are also no errors. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#276](/thread/post/4027972#post4027972 "Post Permalink")

  * Sep 17, 2010 5:16am  Sep 17, 2010 5:16am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting tahshoon](/thread/post/4027954#post4027954 "View Quoted Post")
> 
> Disliked
> 
> i have now another signal ( nzd ),yen signal before ...  
>  two signals triggered now ,v2.3 with ea ...
> 
> Ignored

What about EURUSD signal? Did you get anything? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#277](/thread/post/4027988#post4027988 "Post Permalink")

  * Sep 17, 2010 5:27am  Sep 17, 2010 5:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting mostashar15](/thread/post/4027972#post4027972 "View Quoted Post")
> 
> Disliked
> 
> What about EURUSD signal? Did you get anything?
> 
> Ignored

yes...1 min ago ... u r right 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#278](/thread/post/4027989#post4027989 "Post Permalink")

  * Sep 17, 2010 5:27am  Sep 17, 2010 5:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

Hi,  
  
Yeah i know, you enhanced the 2.3.  
But the problem I and a few other users are seeing is that we are not getting any signals on 2.3 and some other people are seeing signals.  
  
For example today I got no signals on Euro/USD or USD/JPY.  
  
But from posts here i take it that some people have.  
  
I am not sure why this is (maybe broker).  
  
  
  

> [Quoting mostashar15](/thread/post/4027948#post4027948 "View Quoted Post")
> 
> Disliked
> 
> To clarify it:  
>    
>  If 2.3 gives a signal then by default 2.2 will give the same signal. But, If 2.2 gives a signal, then not necessarily 2.3 will give this signal.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#279](/thread/post/4028000#post4028000 "Post Permalink")

  * Sep 17, 2010 5:32am  Sep 17, 2010 5:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

Backtesting does not work with me too ,huge errors in the journal ...  
im going to find another way to do so ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#280](/thread/post/4028003#post4028003 "Post Permalink")

  * Sep 17, 2010 5:33am  Sep 17, 2010 5:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

as you can see my eur/usd is hold.  
  
On this chart, what do i have to manually measure to see if it satisfies the distance ? is it the close of the previous bar (green hammer) with the blue line or with the red line ?  
  
Anyway results are  
  
Blue line = 16 pips  
Red line = 38 pips  
  
unless the problem is because my broker is using 5 digits and not 4 ? Because on the crosshair it read 160 pips ? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2.jpg
Size: 210 KB](/attachment/image/544844/thumbnail?d=1365649641)](/attachment/image/544844?d=1284668956)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#281](/thread/post/4028018#post4028018 "Post Permalink")

  * Sep 17, 2010 5:44am  Sep 17, 2010 5:44am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting DrLobo](/thread/post/4027989#post4027989 "View Quoted Post")
> 
> Disliked
> 
> Hi,  
>    
>  Yeah i know, you enhanced the 2.3.  
>  But the problem I and a few other users are seeing is that we are not getting any signals on 2.3 and some other people are seeing signals.  
>    
>  For example today I got no signals on Euro/USD or USD/JPY.  
>    
>  But from posts here i take it that some people have.  
>    
>  I am not sure why this is (maybe broker).
> 
> Ignored

Are you having any signals now? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#282](/thread/post/4028028#post4028028 "Post Permalink")

  * Sep 17, 2010 5:50am  Sep 17, 2010 5:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

nope ...  
I wonder if it is the 5 digit issue ?  
  

> [Quoting mostashar15](/thread/post/4028018#post4028018 "View Quoted Post")
> 
> Disliked
> 
> Are you having any signals now?
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#283](/thread/post/4028033#post4028033 "Post Permalink")

  * Sep 17, 2010 5:55am  Sep 17, 2010 5:55am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting DrLobo](/thread/post/4028003#post4028003 "View Quoted Post")
> 
> Disliked
> 
> as you can see my eur/usd is hold.  
>    
>  On this chart, what do i have to manually measure to see if it satisfies the distance ? is it the close of the previous bar (green hammer) with the blue line or with the red line ?  
>    
>  Anyway results are  
>    
>  Blue line = 16 pips  
>  Red line = 38 pips  
>    
>  unless the problem is because my broker is using 5 digits and not 4 ? Because on the crosshair it read 160 pips ?
> 
> Ignored

Yes, you are correct. It has to do with the 5 digits. I thought we solved this problem but seems it did not work. You may use the enclosed version and see if you get the signal. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Murrey Advisor 5dig v2.3.mq4](/attachment/file/544853?d=1284670494) 48 KB | 464 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#284](/thread/post/4028038#post4028038 "Post Permalink")

  * Sep 17, 2010 5:59am  Sep 17, 2010 5:59am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting mostashar15](/thread/post/4028033#post4028033 "View Quoted Post")
> 
> Disliked
> 
> Yes, you are correct. It has to do with the 5 digits. I thought we solved this problem but seems it did not work. You may use the enclosed version and see if you get the signal.
> 
> Ignored

By the way MURREY ADVISOR EA v1.0 does **_NOT_** support 5 digit brokers but being revised to do so. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#285](/thread/post/4028050#post4028050 "Post Permalink")

  * Sep 17, 2010 6:09am  Sep 17, 2010 6:09am 

  * [ Caillou](caillou)

  * | Joined Apr 2010  | Status: Trader | [1,404 Posts](/search?do=process&provider=Member&searchuser=140687)

Hi,  
  
Same problem for me, not signal with v2.3 yesterday and today, I´ve download your last indicator, let´s see (I´m 5 digit broker too).... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#286](/thread/post/4028053#post4028053 "Post Permalink")

  * Sep 17, 2010 6:09am  Sep 17, 2010 6:09am 

  * [ Invisible](invisible)

  * | Joined Nov 2009  | Status: Trader | [469 Posts](/search?do=process&provider=Member&searchuser=124048)

> [Quoting mostashar15](/thread/post/4028038#post4028038 "View Quoted Post")
> 
> Disliked
> 
> By the way MURREY ADVISOR EA v1.0 does **_NOT_** support 5 digit brokers but being revised to do so.
> 
> Ignored

Ah! That explains the backtesting results (or lack of). Thanks for noticing that. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#287](/thread/post/4028058#post4028058 "Post Permalink")

  * Sep 17, 2010 6:13am  Sep 17, 2010 6:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting Caillou](/thread/post/4028050#post4028050 "View Quoted Post")
> 
> Disliked
> 
> Hi,  
>    
>  Same problem for me, not signal with v2.3 yesterday and today, I´ve download your last indicator, let´s see (I´m 5 digit broker too)....
> 
> Ignored

do you use the EA? 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#288](/thread/post/4028059#post4028059 "Post Permalink")

  * Sep 17, 2010 6:13am  Sep 17, 2010 6:13am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting Caillou](/thread/post/4028050#post4028050 "View Quoted Post")
> 
> Disliked
> 
> Hi,  
>    
>  Same problem for me, not signal with v2.3 yesterday and today, I´ve download your last indicator, let´s see (I´m 5 digit broker too)....
> 
> Ignored

Did you try this revised version?  
  
[http://cdn.forexfactory.com/attachme...3&d=1284670494](http://cdn.forexfactory.com/attachment.php?attachmentid=544853&d=1284670494)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#289](/thread/post/4028087#post4028087 "Post Permalink")

  * Sep 17, 2010 6:38am  Sep 17, 2010 6:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3317_4.gif) pipsacker](pipsacker)

  * | Joined Aug 2005  | Status: Trader | [127 Posts](/search?do=process&provider=Member&searchuser=3317)

Hi All,  
  
Anyone have any trades open. Downloaded the revised version, no trades now.  
  
pipsacker 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#290](/thread/post/4028104#post4028104 "Post Permalink")

  * Sep 17, 2010 6:53am  Sep 17, 2010 6:53am 

  * [ kapybara](kapybara)

  * | Joined Aug 2010  | Status: Trader | [167 Posts](/search?do=process&provider=Member&searchuser=151152)

Hi folks,  
  
I'm testing on 2 demo accounts w/ 2 brokers (Capital Market Services UK Ltd -> got 2 orders = eurusd, nzdusd - MAv2.2.5digit; [Gain Capital](/brokers/forexcom "View FOREX.com Broker Profile") \- Forex.com UK -> got 1 order = nzdusd - MAv2.3dual). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#291](/thread/post/4028106#post4028106 "Post Permalink")

  * Sep 17, 2010 6:55am  Sep 17, 2010 6:55am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

I have revised Post #1 to include latest versions. Please refer to and get the correct version. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#292](/thread/post/4028110#post4028110 "Post Permalink")

  * Sep 17, 2010 6:57am  Sep 17, 2010 6:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

I can confirm this new revised 2.3 is now working for me !   
I found a "Go Long" signal on 15 min USD/CHF (not that you are supposed to trade on 15 min signals).  
  
However the MA EA does not seem to work with it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#293](/thread/post/4028122#post4028122 "Post Permalink")

  * Edited 7:50am  Sep 17, 2010 7:05am | Edited 7:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102352_6.gif) Inbox](inbox)

  * | Joined May 2009  | Status: Trader | [65 Posts](/search?do=process&provider=Member&searchuser=102352)

Thanks for this great system! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#294](/thread/post/4028133#post4028133 "Post Permalink")

  * Sep 17, 2010 7:19am  Sep 17, 2010 7:19am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

I have added the templates as well in Post #1. 5-digit broker clients may want to re-download the file, I think there might have been a mistake. I tried it with [FXCM](/brokers/fxcm "View FXCM Broker Profile") 5-digit platform and it worked on EURUSD 4Hr.  
  
I am sorry. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: snapshot_5digit_ok.gif
Size: 26 KB](/attachment/image/544875/thumbnail?d=1365649678)](/attachment/image/544875?d=1284675577)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#295](/thread/post/4028143#post4028143 "Post Permalink")

  * Sep 17, 2010 7:29am  Sep 17, 2010 7:29am 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

just recvd long signal for pound/yen and dollar/yen and short for nsd/usd...anyone else get same 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#296](/thread/post/4028147#post4028147 "Post Permalink")

  * Sep 17, 2010 7:33am  Sep 17, 2010 7:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102352_6.gif) Inbox](inbox)

  * | Joined May 2009  | Status: Trader | [65 Posts](/search?do=process&provider=Member&searchuser=102352)

With the last 2.3 version, signals are working good on 5 digits.  
Thanks mostashar15! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#297](/thread/post/4028155#post4028155 "Post Permalink")

  * Sep 17, 2010 7:39am  Sep 17, 2010 7:39am 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

Hi Mostashar,  
Any idea why i get signals Go long for for usdjpy and eurusd on one broker (GCI) and yet nothing on Alpari? i am using the v2.3 manual version. it seems like its sensitive to broker or am i doing something wrongz/ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#298](/thread/post/4028164#post4028164 "Post Permalink")

  * Sep 17, 2010 7:46am  Sep 17, 2010 7:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102352_6.gif) Inbox](inbox)

  * | Joined May 2009  | Status: Trader | [65 Posts](/search?do=process&provider=Member&searchuser=102352)

> [Quoting juzgood1978](/thread/post/4028155#post4028155 "View Quoted Post")
> 
> Disliked
> 
> Hi Mostashar,  
>  Any idea why i get signals Go long for for usdjpy and eurusd on one broker (GCI) and yet nothing on Alpari? i am using the v2.3 manual version. it seems like its sensitive to broker or am i doing something wrongz/
> 
> Ignored

Are you using the last version? Alpari is working with the last 2.3 version... update from 1st post. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#299](/thread/post/4028166#post4028166 "Post Permalink")

  * Sep 17, 2010 7:47am  Sep 17, 2010 7:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

I am with Alpari aswel, and if you compare your 4 hour chart with that of Mostashar you will be suprised to know that it looks quite different.   
  
So my guess is that this must be sensitive to broker (i.e. the data they give) and therefore is leading to different signals.  
  
  
  

> [Quoting juzgood1978](/thread/post/4028155#post4028155 "View Quoted Post")
> 
> Disliked
> 
> Hi Mostashar,  
>  Any idea why i get signals Go long for for usdjpy and eurusd on one broker (GCI) and yet nothing on Alpari? i am using the v2.3 manual version. it seems like its sensitive to broker or am i doing something wrongz/
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#300](/thread/post/4028167#post4028167 "Post Permalink")

  * Sep 17, 2010 7:47am  Sep 17, 2010 7:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37993_2.gif) SteveHopwood](stevehopwood)

  * | Commercial User  | Joined Apr 2007 | [8,331 Posts](/search?do=process&provider=Member&searchuser=37993)

> [Quoting juzgood1978](/thread/post/4028155#post4028155 "View Quoted Post")
> 
> Disliked
> 
> Hi Mostashar,  
>  Any idea why i get signals Go long for for usdjpy and eurusd on one broker (GCI) and yet nothing on Alpari? i am using the v2.3 manual version. it seems like its sensitive to broker or am i doing something wrongz/
> 
> Ignored

Hehe Motasher, the joys of managing a thread are manifold. ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)  
  
juzgood, you are dead right. Different criminal = different feed = different everything else.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#301](/thread/post/4028174#post4028174 "Post Permalink")

  * Sep 17, 2010 7:55am  Sep 17, 2010 7:55am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting juzgood1978](/thread/post/4028155#post4028155 "View Quoted Post")
> 
> Disliked
> 
> Hi Mostashar,  
>  Any idea why i get signals Go long for for usdjpy and eurusd on one broker (GCI) and yet nothing on Alpari? i am using the v2.3 manual version. it seems like its sensitive to broker or am i doing something wrongz/
> 
> Ignored

I guess one of them is 5 digit broker who has the signal while other broker is 5 digit broker. If so, please refer to Post #1 and get the correct versions for each broker. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#302](/thread/post/4028176#post4028176 "Post Permalink")

  * Sep 17, 2010 7:58am  Sep 17, 2010 7:58am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting sfg7th](/thread/post/4028143#post4028143 "View Quoted Post")
> 
> Disliked
> 
> just recvd long signal for pound/yen and dollar/yen and short for nsd/usd...anyone else get same
> 
> Ignored

GBP/JPY is not part of the recommended currency but it is up to you to try it. NZDUSD has SHORT signal on my platform as well. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#303](/thread/post/4028178#post4028178 "Post Permalink")

  * Sep 17, 2010 8:01am  Sep 17, 2010 8:01am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting juzgood1978](/thread/post/4028155#post4028155 "View Quoted Post")
> 
> Disliked
> 
> Hi Mostashar,  
>  Any idea why i get signals Go long for for usdjpy and eurusd on one broker (GCI) and yet nothing on Alpari? i am using the v2.3 manual version. it seems like its sensitive to broker or am i doing something wrongz/
> 
> Ignored

Yes, it does depend on broker supplied data. In particular closing price of last candles beside high and low. Can you attach both charts to compare data? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#304](/thread/post/4028179#post4028179 "Post Permalink")

  * Sep 17, 2010 8:01am  Sep 17, 2010 8:01am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting Inbox](/thread/post/4028147#post4028147 "View Quoted Post")
> 
> Disliked
> 
> With the last 2.3 version, signals are working good on 5 digits.  
>  Thanks mostashar15!
> 
> Ignored

Good News finally. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#305](/thread/post/4028217#post4028217 "Post Permalink")

  * Sep 17, 2010 8:29am  Sep 17, 2010 8:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3317_4.gif) pipsacker](pipsacker)

  * | Joined Aug 2005  | Status: Trader | [127 Posts](/search?do=process&provider=Member&searchuser=3317)

Hi All,  
  
My IBFX demo is now showing signals with latest revision.  
  
pipsacker  
![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#306](/thread/post/4028258#post4028258 "Post Permalink")

  * Sep 17, 2010 9:06am  Sep 17, 2010 9:06am 

  * [ intersis](intersis)

  * | Joined Sep 2010  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=155135)

so far usdjpy & nzdusd go long and short for me. I did counter more long for usdjpy. hope to see more green pips. eurjpy did open today. actually i like to trade gbpjpy & eurjpy. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#307](/thread/post/4028263#post4028263 "Post Permalink")

  * Sep 17, 2010 9:13am  Sep 17, 2010 9:13am 

  * [ intersis](intersis)

  * | Joined Sep 2010  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=155135)

montashar15.. why you develop your indi at TF4? any specific reason for that?  
Is it because at TF4 is a almost confirm signal. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#308](/thread/post/4028294#post4028294 "Post Permalink")

  * Sep 17, 2010 9:47am  Sep 17, 2010 9:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3317_4.gif) pipsacker](pipsacker)

  * | Joined Aug 2005  | Status: Trader | [127 Posts](/search?do=process&provider=Member&searchuser=3317)

Hi All,  
  
Took the NZD/USD & EUR/USD signals. Down a little, but they look like they should go in the right direction.  
Thanks, mostashar15.  
  
pipsacker  
![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#309](/thread/post/4028389#post4028389 "Post Permalink")

  * Sep 17, 2010 11:17am  Sep 17, 2010 11:17am 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

Fantastic, and thanks for the help. I assume stoploss for this system is always at 30pips and tp is at the support is go short and resistance is go long. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#310](/thread/post/4028485#post4028485 "Post Permalink")

  * Sep 17, 2010 12:23pm  Sep 17, 2010 12:23pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

It looks Asian session might not be good for the strategy. We need to keep it running and optimize performance based on different sessions.  
  
Let us see ....  
  
By the way, is there anyone following us here who can keep the EA running 24 hrs to give us 360 panorama view of EA performance? I will need this person to run SPECIAL EDITION for trial purposes while we keep tracking of v2.3 on this thread. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#311](/thread/post/4028574#post4028574 "Post Permalink")

  * Sep 17, 2010 1:15pm  Sep 17, 2010 1:15pm 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

Yes i am running all 7 pairs with the EA for 24hrs 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#312](/thread/post/4028578#post4028578 "Post Permalink")

  * Sep 17, 2010 1:17pm  Sep 17, 2010 1:17pm 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

Will it be a good idea to exit if the signal changed back to hold? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#313](/thread/post/4028624#post4028624 "Post Permalink")

  * Sep 17, 2010 1:36pm  Sep 17, 2010 1:36pm 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

guys how i can know if my broker is 4 or 5 digit to pick the right EA 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#314](/thread/post/4028650#post4028650 "Post Permalink")

  * Sep 17, 2010 1:54pm  Sep 17, 2010 1:54pm 

  * [ intersis](intersis)

  * | Joined Sep 2010  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=155135)

currently running 7 pairs plus ej n gj. hope to see gud result from this EA & indi. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#315](/thread/post/4028654#post4028654 "Post Permalink")

  * Sep 17, 2010 1:57pm  Sep 17, 2010 1:57pm 

  * [ intersis](intersis)

  * | Joined Sep 2010  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=155135)

> [Quoting intersis](/thread/post/4028263#post4028263 "View Quoted Post")
> 
> Disliked
> 
> montashar15.. why you develop your indi at TF4? any specific reason for that?  
>  Is it because at TF4 is a almost confirm signal.
> 
> Ignored

Mostashar15... any specific answer for this question??? TQ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#316](/thread/post/4028704#post4028704 "Post Permalink")

  * Sep 17, 2010 2:24pm  Sep 17, 2010 2:24pm 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

buy signal on USD/CHF 20 min ago 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#317](/thread/post/4028718#post4028718 "Post Permalink")

  * Sep 17, 2010 2:34pm  Sep 17, 2010 2:34pm 

  * [ Caillou](caillou)

  * | Joined Apr 2010  | Status: Trader | [1,404 Posts](/search?do=process&provider=Member&searchuser=140687)

Hi all,  
  
I´ve just downloaded last version in post 1, let´s see how it works today.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#318](/thread/post/4028745#post4028745 "Post Permalink")

  * Sep 17, 2010 2:48pm  Sep 17, 2010 2:48pm 

  * [ xman](xman)

  * | Joined Sep 2009  | Status: Trader | [212 Posts](/search?do=process&provider=Member&searchuser=114906)

It will be less confuse for users if indicator will have name indicator not advisor.   
  
rgsd 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#319](/thread/post/4029106#post4029106 "Post Permalink")

  * Sep 17, 2010 5:20pm  Sep 17, 2010 5:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

for me it doesn't work....got problems with sl/tp   
8 tardes, 7 loss 1 win...  
  
don't know 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#320](/thread/post/4029117#post4029117 "Post Permalink")

  * Sep 17, 2010 5:25pm  Sep 17, 2010 5:25pm 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

> [Quoting PhAnTi'](/thread/post/4029106#post4029106 "View Quoted Post")
> 
> Disliked
> 
> for me it doesn't work....got problems with sl/tp   
>  8 tardes, 7 loss 1 win...  
>    
>  don't know
> 
> Ignored

  
![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) how this could happen   
  
u mean -30 pip isn't enough -50 maybe better? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#321](/thread/post/4029151#post4029151 "Post Permalink")

  * Sep 17, 2010 5:41pm  Sep 17, 2010 5:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting tarek95](/thread/post/4029117#post4029117 "View Quoted Post")
> 
> Disliked
> 
> ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) how this could happen   
>    
>  u mean -30 pip isn't enough -50 maybe better?
> 
> Ignored

I don't know....it's curious....  
maybe u guys can post results to compare?  
  
would be appreciate 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#322](/thread/post/4029258#post4029258 "Post Permalink")

  * Sep 17, 2010 6:26pm  Sep 17, 2010 6:26pm 

  * [ FxHope](fxhope)

  * | Joined Sep 2010  | Status: Trader | [69 Posts](/search?do=process&provider=Member&searchuser=155218)

hi all  
maybe some one can help  
on backtest the EA i get this line   
"10:45:06 TestGenerator: unmatched data error (low value 1.2764 at 2010.09.07 12:02 and price 1.2758 mismatched)"  
my broker is 4 digits.  
thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#323](/thread/post/4029260#post4029260 "Post Permalink")

  * Sep 17, 2010 6:28pm  Sep 17, 2010 6:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

Guys we should all be using 2.3 by now.  
  
Maybe would be a good idea to post daily results and to compare trades ? Will be interesting to know how it plays out.  
  
Because of the different brokers we may get different results (which is interesting) so try to do a screen grab when you do a entry.  
  
  
  
  
  

> [Quoting PhAnTi'](/thread/post/4029151#post4029151 "View Quoted Post")
> 
> Disliked
> 
> I don't know....it's curious....  
>  maybe u guys can post results to compare?  
>    
>  would be appreciate
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#324](/thread/post/4029313#post4029313 "Post Permalink")

  * Sep 17, 2010 6:52pm  Sep 17, 2010 6:52pm 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

i gess you are right we need to see some daily results   
  
but the problem is different brokers   
  
im mean here different 4 hours candle close cause diff signle   
  
if it was on 1 hour there was no way to get different results 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#325](/thread/post/4029520#post4029520 "Post Permalink")

  * Sep 17, 2010 7:59pm  Sep 17, 2010 7:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

mr.mostashar ,do u think that trading with 4H chart to win 30 points is the goal of the system???bec. trading with large time frame is to get more points than a smaller time frame chart... just think about it plz...thnx 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2 losers.png
Size: 11 KB](/attachment/image/545185/thumbnail?d=1365649740)](/attachment/image/545185?d=1284721295)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#326](/thread/post/4029560#post4029560 "Post Permalink")

  * Sep 17, 2010 8:12pm  Sep 17, 2010 8:12pm 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

On 9/12 I had 4 trades 3 were losers, 9/15 3 trades all were losers, 9/16 3 trades all were losers..??????all trades were manual live??? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#327](/thread/post/4029571#post4029571 "Post Permalink")

  * Sep 17, 2010 8:18pm  Sep 17, 2010 8:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

> [Quoting sfg7th](/thread/post/4029560#post4029560 "View Quoted Post")
> 
> Disliked
> 
> On 9/12 I had 4 trades 3 were losers, 9/15 3 trades all were losers, 9/16 3 trades all were losers..??????all trades were manual live???
> 
> Ignored

yeah it's a bit curious... 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#328](/thread/post/4029579#post4029579 "Post Permalink")

  * Sep 17, 2010 8:21pm  Sep 17, 2010 8:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

i think you should have won on your EUR/USD trade !  
my charts show that it crossed your TP before the SL.  
you should have won.  
maybe your broker did not trigger your TP ?  
  
I wish i got signal for that trade.  
  
  
  

> [Quoting tahshoon](/thread/post/4029520#post4029520 "View Quoted Post")
> 
> Disliked
> 
> mr.mostashar ,do u think that trading with 4H chart to win 30 points is the goal of the system???bec. trading with large time frame is to get more points than a smaller time frame chart... just think about it plz...thnx
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#329](/thread/post/4029590#post4029590 "Post Permalink")

  * Sep 17, 2010 8:23pm  Sep 17, 2010 8:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

mind u the obvious thing is that if you are consistently getting loosers ... reverse your signals and you will be onto winners.  
  
basically system needs to be backtested. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#330](/thread/post/4029597#post4029597 "Post Permalink")

  * Sep 17, 2010 8:24pm  Sep 17, 2010 8:24pm 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

current eurgbp and usdchf is reaching stoploss 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#331](/thread/post/4029604#post4029604 "Post Permalink")

  * Sep 17, 2010 8:25pm  Sep 17, 2010 8:25pm 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

i guess this system not so good for ranging days... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#332](/thread/post/4029628#post4029628 "Post Permalink")

  * Sep 17, 2010 8:33pm  Sep 17, 2010 8:33pm 

  * [ reachjj](reachjj)

  * | Joined Dec 2009  | Status: Trader | [265 Posts](/search?do=process&provider=Member&searchuser=126406)

Can people post the their broker and the offset while posting the results. I think, then we can decide which broker with wht offset we would get the best results.   
  
Mostashar, Can this be used on lower tfs? on 1H atleast. If so, we all can test and I believe we shud have a similar results regardless of the broker. 4H tf seems to be resulting in different signals for diff brokers (mainly because of different offsets).  
  
I am running the EA on 2 brokers, Prime4x and [Liteforex](/brokers/liteforex "View LiteForex Broker Profile"). Both seem to be working fine. 4 trades on each for last 2 days (different trades on diff account) and 3 of them were in profit and one in BE.  
  
Will continue to keep it running for few more days  
  
Thanks,  
Prakash 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#333](/thread/post/4029633#post4029633 "Post Permalink")

  * Sep 17, 2010 8:35pm  Sep 17, 2010 8:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151785_7.gif) PhAnTi'](member.php?u=151785)

  * Joined Aug 2010 | Status: Tööröh | [14,292 Posts](/search?do=process&provider=Member&searchuser=151785)

hmm guys don't use it Live...  
  
i think this EA needs some configuration....  
I don't know what's the matter,   
  
mostashar seems to trading well with it...  
  
hmm 

Hero calls followed by margin calls...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#334](/thread/post/4029642#post4029642 "Post Permalink")

  * Sep 17, 2010 8:41pm  Sep 17, 2010 8:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

I 'think' problem with the usdchf trade was that previous day range was almost double to the average.   
Therefore market is correcting itself today.  
Just guessing.  
  

> [Quoting juzgood1978](/thread/post/4029597#post4029597 "View Quoted Post")
> 
> Disliked
> 
> current eurgbp and usdchf is reaching stoploss
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#335](/thread/post/4029647#post4029647 "Post Permalink")

  * Sep 17, 2010 8:43pm  Sep 17, 2010 8:43pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting intersis](/thread/post/4028654#post4028654 "View Quoted Post")
> 
> Disliked
> 
> Mostashar15... any specific answer for this question??? TQ
> 
> Ignored

Yes, it is.  
  
4Hr TF gives additional filter. I started this indicator with 1Hr TF it gave some success but I much liked 4H4 TF signals. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#336](/thread/post/4029724#post4029724 "Post Permalink")

  * Sep 17, 2010 9:13pm  Sep 17, 2010 9:13pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

EA v1.0 17, Sep. 2010 results:  
  
EURUSD = +44 (Asian Session)  
NZDUSD = -30 (Asian Session)  
AUDUSD = -30 (Asian Session)  
EURGBP = -30 (Asian Session)  
\---------------------------------  
Total = -46  
  
USDJPY is still live (-10) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#337](/thread/post/4029786#post4029786 "Post Permalink")

  * Sep 17, 2010 9:36pm  Sep 17, 2010 9:36pm 

  * [ reachjj](reachjj)

  * | Joined Dec 2009  | Status: Trader | [265 Posts](/search?do=process&provider=Member&searchuser=126406)

> [Quoting mostashar15](/thread/post/4029724#post4029724 "View Quoted Post")
> 
> Disliked
> 
> EA v1.0 17, Sep. 2010 results:  
>    
>  EURUSD = +44 (Asian Session)  
>  NZDUSD = -30 (Asian Session)  
>  AUDUSD = -30 (Asian Session)  
>  EURGBP = -30 (Asian Session)  
>  \---------------------------------  
>  Total = -46  
>    
>  USDJPY is still live (-10)
> 
> Ignored

which broker you are using? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#338](/thread/post/4029818#post4029818 "Post Permalink")

  * Sep 17, 2010 9:45pm  Sep 17, 2010 9:45pm 

  * [ vince](vince)

  * | Joined Mar 2009  | Status: Trader | [162 Posts](/search?do=process&provider=Member&searchuser=95373)

mostashar15 is there way to put an arrow on the chart whenever the signal is. That would help for backtesting. What do you think? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#339](/thread/post/4029819#post4029819 "Post Permalink")

  * Sep 17, 2010 9:46pm  Sep 17, 2010 9:46pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting juzgood1978](/thread/post/4029604#post4029604 "View Quoted Post")
> 
> Disliked
> 
> i guess this system not so good for ranging days...
> 
> Ignored

Yes, I agree. This system is good for trending markets but the strategy is supposed not to give a signal if it is not trending. We will keep watching and see how we can improve as required. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#340](/thread/post/4029854#post4029854 "Post Permalink")

  * Sep 17, 2010 9:56pm  Sep 17, 2010 9:56pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting juzgood1978](/thread/post/4028574#post4028574 "View Quoted Post")
> 
> Disliked
> 
> Yes i am running all 7 pairs with the EA for 24hrs
> 
> Ignored

Please check private messages. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#341](/thread/post/4029856#post4029856 "Post Permalink")

  * Sep 17, 2010 9:57pm  Sep 17, 2010 9:57pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting vince](/thread/post/4029818#post4029818 "View Quoted Post")
> 
> Disliked
> 
> mostashar15 is there way to put an arrow on the chart whenever the signal is. That would help for backtesting. What do you think?
> 
> Ignored

I am working on something similar but would take time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#342](/thread/post/4029857#post4029857 "Post Permalink")

  * Sep 17, 2010 9:57pm  Sep 17, 2010 9:57pm 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

> [Quoting mostashar15](/thread/post/4029724#post4029724 "View Quoted Post")
> 
> Disliked
> 
> EA v1.0 17, Sep. 2010 results:  
>    
>  EURUSD = +44 (Asian Session)  
>  NZDUSD = -30 (Asian Session)  
>  AUDUSD = -30 (Asian Session)  
>  EURGBP = -30 (Asian Session)  
>  \---------------------------------  
>  Total = -46  
>    
>  USDJPY is still live (-10)
> 
> Ignored

i don't think these losses because of Asian Session   
  
its hard to trade with 4 H and pick the Session 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#343](/thread/post/4029860#post4029860 "Post Permalink")

  * Sep 17, 2010 9:58pm  Sep 17, 2010 9:58pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting reachjj](/thread/post/4029786#post4029786 "View Quoted Post")
> 
> Disliked
> 
> which broker you are using?
> 
> Ignored

FxSol Demo 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#344](/thread/post/4029866#post4029866 "Post Permalink")

  * Sep 17, 2010 10:01pm  Sep 17, 2010 10:01pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting tarek95](/thread/post/4029857#post4029857 "View Quoted Post")
> 
> Disliked
> 
> i don't think these losses because of Asian Session   
>    
>  its hard to trade with 4 H and pick the Session
> 
> Ignored

Well, I never had this very high failure rate on the manual system. I usually trade Europe and US sessions and don't trade Asian session because it is too late. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#345](/thread/post/4030059#post4030059 "Post Permalink")

  * Sep 17, 2010 11:03pm  Sep 17, 2010 11:03pm 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

NZD/USD recvd sell signal @ 16:00 (EST) @ 0.72419, next 2 bars were bulls highs of 0.72915 and 0.73254.  
USD/JPY rcvd buy Signal @ 16:00 @85.254, sideways move bulls & bears up to 85.645 two bars later..  
suggestions/problems??? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#346](/thread/post/4030377#post4030377 "Post Permalink")

  * Sep 18, 2010 1:22am  Sep 18, 2010 1:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3317_4.gif) pipsacker](pipsacker)

  * | Joined Aug 2005  | Status: Trader | [127 Posts](/search?do=process&provider=Member&searchuser=3317)

Hi All,  
  
Asian turned against me too. NZD/USD -30.5 & EUR/USD +24.3, loss of 6.2 micro pips. Could have held EUR/USD a bit longer and ended with a few positive pips.  
  
pipsacker  
![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#347](/thread/post/4030997#post4030997 "Post Permalink")

  * Sep 18, 2010 9:00am  Sep 18, 2010 9:00am 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

> [Quoting vince](/thread/post/4029818#post4029818 "View Quoted Post")
> 
> Disliked
> 
> mostashar15 is there way to put an arrow on the chart whenever the signal is. That would help for backtesting. What do you think?
> 
> Ignored

i think the best develop for this indi is to make these arrows it will make us could easily back test to see if the indi is good or need more modification 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#348](/thread/post/4031257#post4031257 "Post Permalink")

  * Sep 18, 2010 6:09pm  Sep 18, 2010 6:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

**الاخ المستشار السلام عليكم  
كان بودي لو كان الجهد الذي يبذل منصبا على تحسين اداء المؤشر الذي قلتم انكم بذلتم فيه الكثير من الجهد والمعرفة ... وهو ما كان يستحق ان يبذل فيه المزيد ، لا ان تهدر بغيره من الطاقات والوقت في جعله يتلاءم مع المتاجرة الآلية ...  
كأن ينظر لتحسين ادائه لكسب المزيد من النقاط او ان يعمل على زيادة الفلترة لتقليص الدخول الغير صحيح ...  
شاكرا لكم حسن ادائكم و تعاونكم متمنيا منكم اخذ هذه السطور من باب الحرص على عدم اهدار المجهود الذي بذلتموه مشكورا ...  
ودمتم بود **

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#349](/thread/post/4031740#post4031740 "Post Permalink")

  * Sep 19, 2010 7:08am  Sep 19, 2010 7:08am 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

I noticed the new indicator for 5 digit the adx graph is missing, is it not needed??? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#350](/thread/post/4031769#post4031769 "Post Permalink")

  * Sep 19, 2010 8:06am  Sep 19, 2010 8:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3317_4.gif) pipsacker](pipsacker)

  * | Joined Aug 2005  | Status: Trader | [127 Posts](/search?do=process&provider=Member&searchuser=3317)

Hi sfg7th,  
  
Mostashar15 said it was already in the indicator, no need to show it.  
  
pipsacker  
![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#351](/thread/post/4031957#post4031957 "Post Permalink")

  * Sep 19, 2010 3:45pm  Sep 19, 2010 3:45pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting tahshoon](/thread/post/4031257#post4031257 "View Quoted Post")
> 
> Disliked
> 
> [font="courier new"][b][color="darkgreen"]الاخ المستشار السلام عليكم  
>  كان بودي لو كان الجهد الذي يبذل منصبا على تحسين اداء المؤشر...
> 
> Ignored

و عليكم السلام و رحمة الله و بركاته  
بالفعل انا حاليا اقوم بتحسين اداء المؤشر وقمت بعمل بعض التعديلات و اود اختبارها قبل نشرها للجميع.  

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#352](/thread/post/4032085#post4032085 "Post Permalink")

  * Sep 19, 2010 7:25pm  Sep 19, 2010 7:25pm 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

> [Quoting mostashar15](/thread/post/4031957#post4031957 "View Quoted Post")
> 
> Disliked
> 
> [right]و عليكم السلام و رحمة الله و بركاته  
>  بالفعل انا حاليا اقوم بتحسين اداء المؤشر وقمت بعمل بعض التعديلات...
> 
> Ignored

good news im waiting for the new modification to test it with you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#353](/thread/post/4032952#post4032952 "Post Permalink")

  * Sep 20, 2010 9:11am  Sep 20, 2010 9:11am 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

have the mm 2.3v 5d template chart (cad/JPY) cannot get the 2.3v EA to attach..the 1v will attach but get error msg (error opening sell order :130)..any suggestions  
also got msg that Expert advisor 5 d 2.3v is an indicator and cannot be excuted?? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#354](/thread/post/4033004#post4033004 "Post Permalink")

  * Sep 20, 2010 9:43am  Sep 20, 2010 9:43am 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

wow! are you using the EA or manual?  
  

> [Quoting DrLobo](/thread/post/4018324#post4018324 "View Quoted Post")
> 
> Disliked
> 
> I turned 100 pound account (it still a demo account) into 150 pounds today with 0.50 per PIP. Here were my trades.  
>    
>  Eur/USD = 40 pips  
>  USD/CHF = 32 pips  
>  USD/JPY = 31 pips  
>  USD/CAD = 8 pips (not sure if this trade was done on a 4h time chart looks odd to me)  
>    
>  I am still running another trade on the USD/CAD which I am shorting and I am 8 pips up.   
>    
>    
>  Anyway 111 PIPS banked today !!  
>    
>  Honestly I have never ever made 111 PIPS in my wildest dreams !   
>    
>  I am in total shock its a bit insane i expecting some turn of events to even up the scores...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#355](/thread/post/4033126#post4033126 "Post Permalink")

  * Sep 20, 2010 11:01am  Sep 20, 2010 11:01am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting sfg7th](/thread/post/4032952#post4032952 "View Quoted Post")
> 
> Disliked
> 
> have the mm 2.3v 5d template chart (cad/JPY) cannot get the 2.3v EA to attach..the 1v will attach but get error msg (error opening sell order :130)..any suggestions  
>  also got msg that Expert advisor 5 d 2.3v is an indicator and cannot be excuted??
> 
> Ignored

It looks you are trying to use EA with 5-digit broker which does not support yet. You may try to download 4-digit broker platform to try EA otherwise, you may use this indi manually. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#356](/thread/post/4033220#post4033220 "Post Permalink")

  * Sep 20, 2010 12:04pm  Sep 20, 2010 12:04pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

It looks 5-digit version still has some bugs, please only use with 4-digit brokers. I will delete from 1st post.  
  
Sorry for that 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#357](/thread/post/4033454#post4033454 "Post Permalink")

  * Sep 20, 2010 3:21pm  Sep 20, 2010 3:21pm 

  * [ plind](plind)

  * | Joined Jun 2006  | Status: Trader | [135 Posts](/search?do=process&provider=Member&searchuser=12124)

Currently have "go long' on EUR/USD on IBFX and Think Forex. Has started the up move already 3 pips in profit. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#358](/thread/post/4033586#post4033586 "Post Permalink")

  * Sep 20, 2010 4:27pm  Sep 20, 2010 4:27pm 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

strange... no trade on my side yet 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#359](/thread/post/4033701#post4033701 "Post Permalink")

  * Sep 20, 2010 6:27pm  Sep 20, 2010 6:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

Hi,  
  
This was beginning of last week and there was no EA at the time.  
  
  
  
  

> [Quoting juzgood1978](/thread/post/4033004#post4033004 "View Quoted Post")
> 
> Disliked
> 
> wow! are you using the EA or manual?
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#360](/thread/post/4033730#post4033730 "Post Permalink")

  * Sep 20, 2010 6:37pm  Sep 20, 2010 6:37pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting plind](/thread/post/4033454#post4033454 "View Quoted Post")
> 
> Disliked
> 
> Currently have "go long' on EUR/USD on IBFX and Think Forex. Has started the up move already 3 pips in profit.
> 
> Ignored

It looks you are using 5-digit broker. There is a bug in the 5-digit broker as printed in my signature. Please don't use this version until I fix it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#361](/thread/post/4033899#post4033899 "Post Permalink")

  * Sep 20, 2010 7:49pm  Sep 20, 2010 7:49pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

I see my account with FxSol is having a signal (NZDUSD:LONG) but other account with Uranus does not. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: nzdusd.gif
Size: 30 KB](/attachment/image/546306/thumbnail?d=1365650028)](/attachment/image/546306?d=1284979765)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#362](/thread/post/4033959#post4033959 "Post Permalink")

  * Sep 20, 2010 8:20pm  Sep 20, 2010 8:20pm 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

anyone have an explanation why the signals I recv are for the wrong direction..9/19 21:00 signal was to go long,GBP/AUD @ 1.66793, price dropped to 1.65220..of the Past 13 trades 11 were losers and 2 small winners? all were manual trades with MBTrading live...suggestions/comments 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#363](/thread/post/4033981#post4033981 "Post Permalink")

  * Sep 20, 2010 8:29pm  Sep 20, 2010 8:29pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting sfg7th](/thread/post/4033959#post4033959 "View Quoted Post")
> 
> Disliked
> 
> anyone have an explanation why the signals I recv are for the wrong direction..9/19 21:00 signal was to go long,GBP/AUD @ 1.66793, price dropped to 1.65220..of the Past 13 trades 11 were losers and 2 small winners? all were manual trades with MBTrading live...suggestions/comments
> 
> Ignored

Don't use with 5-digit brokers. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#364](/thread/post/4034233#post4034233 "Post Permalink")

  * Sep 20, 2010 10:23pm  Sep 20, 2010 10:23pm 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

can someone tell me how to delete indicators from the navigator screen on Meta 4..I have deleted all the murray advisors and EA's (except current one's) from the folders, but all the old deleted ones still show up when i open navigator?? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#365](/thread/post/4034265#post4034265 "Post Permalink")

  * Sep 20, 2010 10:33pm  Sep 20, 2010 10:33pm 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

i am using 4 digit but no signal at all today 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#366](/thread/post/4035124#post4035124 "Post Permalink")

  * Sep 21, 2010 4:45am  Sep 21, 2010 4:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar155481_2.gif) basalp](basalp)

  * | Joined Sep 2010  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=155481)

I've been testing this strategy for 6 days. I have been using 30 tp and 30 sl after 17 trades my balance hasn't changed (it was 50.000 now 49980). I was wondering what is the main difference between version 2.2 and 2.3 ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#367](/thread/post/4035342#post4035342 "Post Permalink")

  * Sep 21, 2010 7:13am  Sep 21, 2010 7:13am 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

im using it now on 30 min   
  
and i dont see much different 2 win tades 3 loss  
  
but in 30 min you get more signles than 4 H so you might get profits 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#368](/thread/post/4035407#post4035407 "Post Permalink")

  * Sep 21, 2010 8:08am  Sep 21, 2010 8:08am 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

> [Quoting sfg7th](/thread/post/4034233#post4034233 "View Quoted Post")
> 
> Disliked
> 
> can someone tell me how to delete indicators from the navigator screen on Meta 4..I have deleted all the murray advisors and EA's (except current one's) from the folders, but all the old deleted ones still show up when i open navigator??
> 
> Ignored

Disregard---I finally figured it out... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#369](/thread/post/4035607#post4035607 "Post Permalink")

  * Sep 21, 2010 9:59am  Sep 21, 2010 9:59am 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

has anyone recvd a signal this evening???it's 9:00pm EST and nothing so far, reloaded the 4 d ver from post 1 about 6:00pm?/ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#370](/thread/post/4036000#post4036000 "Post Permalink")

  * Sep 21, 2010 3:32pm  Sep 21, 2010 3:32pm 

  * [ plind](plind)

  * | Joined Jun 2006  | Status: Trader | [135 Posts](/search?do=process&provider=Member&searchuser=12124)

ON IBFX and Think Forex long @ 2:30 ET, short GBP/JPY 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#371](/thread/post/4036457#post4036457 "Post Permalink")

  * Sep 21, 2010 6:40pm  Sep 21, 2010 6:40pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

Hello  
  
I did some minor changes and now testing on 1 Hr Time frame. Once proven to be profitable, I will be sharing the new files.  
  
I just got in EURUSD (LONG) an closed with +52 pips.  
  
I need to continue the test till the end of this week to conclude about those changes.  
  
Let us see ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#372](/thread/post/4036483#post4036483 "Post Permalink")

  * Sep 21, 2010 6:49pm  Sep 21, 2010 6:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

good work.  
  

> [Quoting mostashar15](/thread/post/4036457#post4036457 "View Quoted Post")
> 
> Disliked
> 
> Hello  
>    
>  I did some minor changes and now testing on 1 Hr Time frame. Once proven to be profitable, I will be sharing the new files.  
>    
>  I just got in EURUSD (LONG) an closed with +52 pips.  
>    
>  I need to continue the test till the end of this week to conclude about those changes.  
>    
>  Let us see ...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#373](/thread/post/4036530#post4036530 "Post Permalink")

  * Sep 21, 2010 7:11pm  Sep 21, 2010 7:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting mostashar15](/thread/post/4036457#post4036457 "View Quoted Post")
> 
> Disliked
> 
> Hello  
>    
>  I did some minor changes and now testing on 1 Hr Time frame. Once proven to be profitable, I will be sharing the new files.  
>    
>  I just got in EURUSD (LONG) an closed with +52 pips.  
>    
>  I need to continue the test till the end of this week to conclude about those changes.  
>    
>  Let us see ...
> 
> Ignored

very good , im sure that u r doing well ... waiting for modifications 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#374](/thread/post/4036666#post4036666 "Post Permalink")

  * Sep 21, 2010 8:09pm  Sep 21, 2010 8:09pm 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

I seem to have problems with the 4 hr 4digit version..have not recvd a signal since yesterday evening @ start of trading session..did recv a signal on 2 pair @ 06:39 today that was accidently on 1 hr TF, but were wrong direction..using MBT ECN live any help/comments? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#375](/thread/post/4037601#post4037601 "Post Permalink")

  * Sep 22, 2010 1:49am  Sep 22, 2010 1:49am 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

just recvd signal (12:41 EST) for short..with 2 bull candles ???/something is not right??/ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#376](/thread/post/4037699#post4037699 "Post Permalink")

  * Sep 22, 2010 2:47am  Sep 22, 2010 2:47am 

  * [ reachjj](reachjj)

  * | Joined Dec 2009  | Status: Trader | [265 Posts](/search?do=process&provider=Member&searchuser=126406)

Was just going thru the code and can make out that, we are not using MagcNumber while checking if we have the pair is already opened or not. So If I am running 2 EAs, this EA wont open a trade if the other ea already opened a trade on that particular Pair.  
  
Can somebody fix this please. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#377](/thread/post/4038454#post4038454 "Post Permalink")

  * Sep 22, 2010 7:52am  Sep 22, 2010 7:52am 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

Finallya 18pips win from eg 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#378](/thread/post/4038896#post4038896 "Post Permalink")

  * Sep 22, 2010 11:22am  Sep 22, 2010 11:22am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting juzgood1978](/thread/post/4038454#post4038454 "View Quoted Post")
> 
> Disliked
> 
> Finallya 18pips win from eg
> 
> Ignored

Last Results Update:  
  
EURUSD +52  
USDJPY +27  
USDCAD -30  
AUDUSD +44  
EURGBP +56  
EURGBP +10 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#379](/thread/post/4038902#post4038902 "Post Permalink")

  * Sep 22, 2010 11:27am  Sep 22, 2010 11:27am 

  * [ reachjj](reachjj)

  * | Joined Dec 2009  | Status: Trader | [265 Posts](/search?do=process&provider=Member&searchuser=126406)

> [Quoting mostashar15](/thread/post/4038896#post4038896 "View Quoted Post")
> 
> Disliked
> 
> Last Results Update:  
>    
>  EURUSD +52  
>  USDJPY +27  
>  USDCAD -30  
>  AUDUSD +44  
>  EURGBP +56  
>  EURGBP +10
> 
> Ignored

this is from auto trading or manual trading.. and is it with H1 or H4 tf 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#380](/thread/post/4038913#post4038913 "Post Permalink")

  * Sep 22, 2010 11:36am  Sep 22, 2010 11:36am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting reachjj](/thread/post/4038902#post4038902 "View Quoted Post")
> 
> Disliked
> 
> this is from auto trading or manual trading.. and is it with H1 or H4 tf
> 
> Ignored

Auto - some 4hr and some 1 hr.  
  
I am running two different EAs. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#381](/thread/post/4039242#post4039242 "Post Permalink")

  * Sep 22, 2010 3:18pm  Sep 22, 2010 3:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar155481_2.gif) basalp](basalp)

  * | Joined Sep 2010  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=155481)

**Dear** M**ostashar15, could you tell me please what is the main difference between version2.2 and 2.3 ? I am still using 2.2 .I use it for 4hour and daily charts. My broker is 4 digit and signal perfectly works. Nevertheless after 23 trades it seems like a sum zero game so far.**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#382](/thread/post/4039467#post4039467 "Post Permalink")

  * Sep 22, 2010 4:38pm  Sep 22, 2010 4:38pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting basalp](/thread/post/4039242#post4039242 "View Quoted Post")
> 
> Disliked
> 
> **Dear** M**ostashar15, could you tell me please what is the main difference between version2.2 and 2.3 ? I am still using 2.2 .I use it for 4hour and daily charts. My broker is 4 digit and signal perfectly works. Nevertheless after 23 trades it seems like a sum zero game so far.**
> 
> Ignored

2.3 has a feature to filter some of the big candles after which you will see a retrace. Use 2.3 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#383](/thread/post/4039622#post4039622 "Post Permalink")

  * Sep 22, 2010 5:38pm  Sep 22, 2010 5:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102352_6.gif) Inbox](inbox)

  * | Joined May 2009  | Status: Trader | [65 Posts](/search?do=process&provider=Member&searchuser=102352)

Hey MoStAsHaR15, any advances on 5 digits advisor?  
  
Thank you! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#384](/thread/post/4039886#post4039886 "Post Permalink")

  * Sep 22, 2010 6:54pm  Sep 22, 2010 6:54pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting Inbox](/thread/post/4039622#post4039622 "View Quoted Post")
> 
> Disliked
> 
> Hey MoStAsHaR15, any advances on 5 digits advisor?  
>    
>  Thank you!
> 
> Ignored

I am now focusing only on improving indicator and EA performance. Once, we are satisfied with performance then, we will develop 5-dig versions.  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#385](/thread/post/4039936#post4039936 "Post Permalink")

  * Sep 22, 2010 7:15pm  Sep 22, 2010 7:15pm 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

MOS...your EA only has a mq4 file, all the other EA's on my system contains an exe. file???also will the 4 digit version not work on the ECN 5 d broker??Also the 4digit advisor doesn't seem to work on 5d broker?? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#386](/thread/post/4040046#post4040046 "Post Permalink")

  * Sep 22, 2010 8:03pm  Sep 22, 2010 8:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

> [Quoting sfg7th](/thread/post/4039936#post4039936 "View Quoted Post")
> 
> Disliked
> 
> MOS...your EA only has a mq4 file, all the other EA's on my system contains an exe. file???also will the 4 digit version not work on the ECN 5 d broker??Also the 4digit advisor doesn't seem to work on 5d broker??
> 
> Ignored

please read the first thread its not that long. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#387](/thread/post/4040424#post4040424 "Post Permalink")

  * Sep 22, 2010 10:11pm  Sep 22, 2010 10:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar155481_2.gif) basalp](basalp)

  * | Joined Sep 2010  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=155481)

Mostasher, I use 2 different brokers. I am running Ea and got Nzd/usd long signal (4hours) now. Order has opened. Meanwhile I got another signal from my other broker which says usd/jpy short(4hours). To sum up I haven't received same signal from different brokers. By the way both are 4 digit brokers. Have you got any idea about this issue ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#388](/thread/post/4040685#post4040685 "Post Permalink")

  * Edited 11:37pm  Sep 22, 2010 11:26pm | Edited 11:37pm 

  * [ TriMagic](trimagic)

  * | Joined Sep 2010  | Status: Trader | [77 Posts](/search?do=process&provider=Member&searchuser=154956)

> [Quoting mostashar15](/thread/post/4039886#post4039886 "View Quoted Post")
> 
> Disliked
> 
> I am now focusing only on improving indicator and EA performance. Once, we are satisfied with performance then, we will develop 5-dig versions.  
>    
>  Thanks
> 
> Ignored

To start off with, I read all 26 pages and really like what you guys are accomplishing ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) Now my question is this, I have a 5 digit broker and is it now in place to make use of Murrey Advisor 2.3 with "ma 2.3 tpl" only attached to 4H chart or the "dual .mq4" as I get two different views. I understand that the EA is not working with 5 digit brokers at the moment. Being only "ma 2.3 tpl" attached it's straight manual for now?  
  
Or is there still some tweaking to take place with the 5 digit template version? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#389](/thread/post/4040886#post4040886 "Post Permalink")

  * Sep 23, 2010 12:21am  Sep 23, 2010 12:21am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting basalp](/thread/post/4040424#post4040424 "View Quoted Post")
> 
> Disliked
> 
> Mostasher, I use 2 different brokers. I am running Ea and got Nzd/usd long signal (4hours) now. Order has opened. Meanwhile I got another signal from my other broker which says usd/jpy short(4hours). To sum up I haven't received same signal from different brokers. By the way both are 4 digit brokers. Have you got any idea about this issue ?
> 
> Ignored

This could happen as I depend on high, low and close of candles. As you know, different brokers will give different data. It is OK just follow any signal you have. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#390](/thread/post/4040902#post4040902 "Post Permalink")

  * Sep 23, 2010 12:24am  Sep 23, 2010 12:24am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting TriMagic](/thread/post/4040685#post4040685 "View Quoted Post")
> 
> Disliked
> 
> To start off with, I read all 26 pages and really like what you guys are accomplishing ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) Now my question is this, I have a 5 digit broker and is it now in place to make use of Murrey Advisor 2.3 with "ma 2.3 tpl" only attached to 4H chart or the "dual .mq4" as I get two different views. I understand that the EA is not working with 5 digit brokers at the moment. Being only "ma 2.3 tpl" attached it's straight manual for now?  
>    
>  Or is there still some tweaking to take place with the 5 digit template version?
> 
> Ignored

Thanks for reading all posts. As of now, I don't recommend using 5 digit version. What you can do is to download 4 digit platform and run the 4 digit version. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#391](/thread/post/4040928#post4040928 "Post Permalink")

  * Sep 23, 2010 12:29am  Sep 23, 2010 12:29am 

  * [ TriMagic](trimagic)

  * | Joined Sep 2010  | Status: Trader | [77 Posts](/search?do=process&provider=Member&searchuser=154956)

> [Quoting mostashar15](/thread/post/4040902#post4040902 "View Quoted Post")
> 
> Disliked
> 
> Thanks for reading all posts. As of now, I don't recommend using 5 digit version. What you can do is to download 4 digit platform and run the 4 digit version.
> 
> Ignored

Ok, to do this is to open my 4 digit demo platform and apply the signal trades onto my 5 digit manually live, would that be correct? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#392](/thread/post/4040964#post4040964 "Post Permalink")

  * Sep 23, 2010 12:38am  Sep 23, 2010 12:38am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

Just to update about progress, Below is the results so far. Actually, I am running two versions on on 4 hr and another one on 1 hr. Those versions have been modified and are different than the ones you are running. I will be sharing those files soon after further testing. We might end up by recommending running both Time frames together. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 22092010.PNG
Size: 37 KB](/attachment/image/548099/thumbnail?d=1365650507)](/attachment/image/548099?d=1285169873)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#393](/thread/post/4041013#post4041013 "Post Permalink")

  * Sep 23, 2010 12:50am  Sep 23, 2010 12:50am 

  * [ TriMagic](trimagic)

  * | Joined Sep 2010  | Status: Trader | [77 Posts](/search?do=process&provider=Member&searchuser=154956)

> [Quoting mostashar15](/thread/post/4040964#post4040964 "View Quoted Post")
> 
> Disliked
> 
> Just to update about progress, Below is the results so far. Actually, I am running two versions on on 4 hr and another one on 1 hr. Those versions have been modified and are different than the ones you are running. I will be sharing those files soon after further testing. We might end up by recommending running both Time frames together.
> 
> Ignored

Looks good, I have 4 digit broker one side with EA and 5 digit broker on the other side to see how this plays out. Would love to see the final 5 digit version but no rush.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#394](/thread/post/4041464#post4041464 "Post Permalink")

  * Sep 23, 2010 3:10am  Sep 23, 2010 3:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135120_2.gif) DrLobo](drlobo)

  * | Membership Revoked  | Joined Mar 2010 | [624 Posts](/search?do=process&provider=Member&searchuser=135120)

wow results are looking goood ! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
usd/jpy has a 100% success rate for this system that could be great pair for this system ?   
  

> [Quoting mostashar15](/thread/post/4040964#post4040964 "View Quoted Post")
> 
> Disliked
> 
> Just to update about progress, Below is the results so far. Actually, I am running two versions on on 4 hr and another one on 1 hr. Those versions have been modified and are different than the ones you are running. I will be sharing those files soon after further testing. We might end up by recommending running both Time frames together.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#395](/thread/post/4041523#post4041523 "Post Permalink")

  * Sep 23, 2010 3:40am  Sep 23, 2010 3:40am 

  * [ afolabijohns](afolabijohns)

  * | Joined Nov 2009  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=123291)

The following situation happens quite often to many traders. Look it over and see if it has been happening to you:You have been faithfully following your trading plan and the rules you've set for trading. By following them you are now in a trade that doesn't look so good. At the same time, by following your trading plan, you see that you've missed a beautiful move in a different market, one that could have made you a lot of money.You are in a bad trade and you've missed out on a great trade. You become disgruntled. You think to yourself that your trading plan must not be so great. You think there must be a better methodology that you should use that will prevent this from happening. You think to yourself,

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#396](/thread/post/4041723#post4041723 "Post Permalink")

  * Sep 23, 2010 5:26am  Sep 23, 2010 5:26am 

  * [ elvispredley](elvispredley)

  * | Joined Sep 2010  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=155497)

Hi there,  
  
I read through the majority of the posts to get caught up, seems like it's a nice indicator. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
I'm having trouble downloading the indicator though. I am able to get the Murry Adviser EA 4dig v1.0.mq4 one with no problem, click on it and it saves it okay but the second file:  
  
[Murrey Advisor v2.3 4dig.zip](http://cdn.forexfactory.com/attachment.php?attachmentid=544873&d=1284675357)   
  
When I click on it, it tries to save attachment.php and not the zip file??  
  
Anyone have any idea why this is happening or have an alternative way to get this file?  
  
Thank ya..thank ya very much ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#397](/thread/post/4042056#post4042056 "Post Permalink")

  * Sep 23, 2010 8:22am  Sep 23, 2010 8:22am 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

> [Quoting elvispredley](/thread/post/4041723#post4041723 "View Quoted Post")
> 
> Disliked
> 
> Hi there,  
>    
>  I read through the majority of the posts to get caught up, seems like it's a nice indicator. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>    
>  I'm having trouble downloading the indicator though. I am able to get the Murry Adviser EA 4dig v1.0.mq4 one with no problem, click on it and it saves it okay but the second file:  
>    
>  [Murrey Advisor v2.3 4dig.zip](http://cdn.forexfactory.com/attachment.php?attachmentid=544873&d=1284675357)   
>    
>  When I click on it, it tries to save attachment.php and not the zip file??  
>    
>  Anyone have any idea why this is happening...
> 
> Ignored

  
  
instead of the file in post 1 go to attachment file (upper right corner with paper clip) and download the file from there 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#398](/thread/post/4042190#post4042190 "Post Permalink")

  * Sep 23, 2010 9:40am  Sep 23, 2010 9:40am 

  * [ elvispredley](elvispredley)

  * | Joined Sep 2010  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=155497)

Thanks sfg7th,  
  
I used the paperclip and was able to download the file that way. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Now to find a broker that uses 4 digits now, I have the [FXCM](/brokers/fxcm "View FXCM Broker Profile"), IBFX and [FxPro](/brokers/fxpro "View FxPro Broker Profile") demos and they all have five digits, any suggestions on a broker that uses 4 digits?  
  
Thank ya, Thank ya very much.  
  
E 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#399](/thread/post/4042379#post4042379 "Post Permalink")

  * Sep 23, 2010 12:31pm  Sep 23, 2010 12:31pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting elvispredley](/thread/post/4042190#post4042190 "View Quoted Post")
> 
> Disliked
> 
> Thanks sfg7th,  
>    
>  I used the paperclip and was able to download the file that way. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>    
>  Now to find a broker that uses 4 digits now, I have the FXCM, IBFX and FxPro demos and they all have five digits, any suggestions on a broker that uses 4 digits?  
>    
>  Thank ya, Thank ya very much.  
>    
>  E
> 
> Ignored

I am using FxSol UK 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#400](/thread/post/4042528#post4042528 "Post Permalink")

  * Sep 23, 2010 2:32pm  Sep 23, 2010 2:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting elvispredley](/thread/post/4041723#post4041723 "View Quoted Post")
> 
> Disliked
> 
> Hi there,  
>    
>  I read through the majority of the posts to get caught up, seems like it's a nice indicator. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>    
>  I'm having trouble downloading the indicator though. I am able to get the Murry Adviser EA 4dig v1.0.mq4 one with no problem, click on it and it saves it okay but the second file:  
>    
>  [Murrey Advisor v2.3 4dig.zip](http://cdn.forexfactory.com/attachment.php?attachmentid=544873&d=1284675357)   
>    
>  When I click on it, it tries to save attachment.php and not the zip file??  
>    
>  Anyone have any idea why this...
> 
> Ignored

when u downloaded the attachment as it is (( attachment.php )), then re name it as zip file like this (( attachment.zip )) , try it and every thing will be ok 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#401](/thread/post/4042558#post4042558 "Post Permalink")

  * Sep 23, 2010 2:54pm  Sep 23, 2010 2:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar155481_2.gif) basalp](basalp)

  * | Joined Sep 2010  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=155481)

> [Quoting elvispredley](/thread/post/4042190#post4042190 "View Quoted Post")
> 
> Disliked
> 
> Thanks sfg7th,  
>    
>  I used the paperclip and was able to download the file that way. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>    
>  Now to find a broker that uses 4 digits now, I have the FXCM, IBFX and FxPro demos and they all have five digits, any suggestions on a broker that uses 4 digits?  
>    
>  Thank ya, Thank ya very much.  
>    
>  E
> 
> Ignored

I use hedefonline and tadawul. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#402](/thread/post/4043600#post4043600 "Post Permalink")

  * Sep 23, 2010 9:49pm  Sep 23, 2010 9:49pm 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

I check out fxsol and noticed their spread are higher than most brokers by at leSt 1pip on all majors  

> [Quoting mostashar15](/thread/post/4042379#post4042379 "View Quoted Post")
> 
> Disliked
> 
> I am using FxSol UK
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#403](/thread/post/4045267#post4045267 "Post Permalink")

  * Sep 24, 2010 10:31am  Sep 24, 2010 10:31am 

  * [ elvispredley](elvispredley)

  * | Joined Sep 2010  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=155497)

Hi guys,  
  
Thanks for the responses, I will check those out. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
E 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#404](/thread/post/4045297#post4045297 "Post Permalink")

  * Sep 24, 2010 10:51am  Sep 24, 2010 10:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar128836_2.gif) hutrader](hutrader)

  * | Joined Jan 2010  | Status: Trader | [648 Posts](/search?do=process&provider=Member&searchuser=128836)

> [Quoting mostashar15](/thread/post/4040964#post4040964 "View Quoted Post")
> 
> Disliked
> 
> Just to update about progress, Below is the results so far. Actually, I am running two versions on on 4 hr and another one on 1 hr. Those versions have been modified and are different than the ones you are running. I will be sharing those files soon after further testing. We might end up by recommending running both Time frames together.
> 
> Ignored

Nice , and mine? Look at the time :-) 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: prof.jpg
Size: 74 KB](/attachment/image/549106/thumbnail?d=1365650813)](/attachment/image/549106?d=1285293089)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#405](/thread/post/4045394#post4045394 "Post Permalink")

  * Sep 24, 2010 12:34pm  Sep 24, 2010 12:34pm 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

not sure why, mine is pretty bad. total l had 9 trades 6 losses... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#406](/thread/post/4045396#post4045396 "Post Permalink")

  * Sep 24, 2010 12:35pm  Sep 24, 2010 12:35pm 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

hi hutrader can i know which broker are you using and which version?  

> [Quoting hutrader](/thread/post/4045297#post4045297 "View Quoted Post")
> 
> Disliked
> 
> Nice , and mine? Look at the time :-)
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#407](/thread/post/4045408#post4045408 "Post Permalink")

  * Edited 2:47pm  Sep 24, 2010 12:45pm | Edited 2:47pm 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

here is the result....  
[http://www.myfxbook.com/members/luca...yadvisor/51742](http://www.myfxbook.com/members/lucasforex/murrayadvisor/51742)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#408](/thread/post/4045560#post4045560 "Post Permalink")

  * Sep 24, 2010 2:07pm  Sep 24, 2010 2:07pm 

  * [ tarek95](tarek95)

  * | Joined Sep 2010  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=154911)

> [Quoting juzgood1978](/thread/post/4045408#post4045408 "View Quoted Post")
> 
> Disliked
> 
> here is the result....  
>  <https://www.myfxbook.com/portfolio/murrayadvisor/51742>
> 
> Ignored

link dosn't work   
  
u guys have good results ...so is every one here use 2.3 auto EA   
  
or what ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#409](/thread/post/4045593#post4045593 "Post Permalink")

  * Sep 24, 2010 2:23pm  Sep 24, 2010 2:23pm 

  * [ juzgood1978](juzgood1978)

  * | Joined Aug 2010  | Status: Trader | [280 Posts](/search?do=process&provider=Member&searchuser=152227)

Sorry link here [http://www.myfxbook.com/members/luca...yadvisor/51742](http://www.myfxbook.com/members/lucasforex/murrayadvisor/51742)  

> [Quoting tarek95](/thread/post/4045560#post4045560 "View Quoted Post")
> 
> Disliked
> 
> link dosn't work   
>    
>  u guys have good results ...so is every one here use 2.3 auto EA   
>    
>  or what ?
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#410](/thread/post/4047525#post4047525 "Post Permalink")

  * Sep 25, 2010 2:29am  Sep 25, 2010 2:29am 

  * [ Eureka](eureka)

  * | Joined Aug 2006  | Status: Trader | [383 Posts](/search?do=process&provider=Member&searchuser=16246)

Is there an update on the testing, MoStAsHaR15?  
  
Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#411](/thread/post/4047813#post4047813 "Post Permalink")

  * Sep 25, 2010 5:09am  Sep 25, 2010 5:09am 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

> [Quoting Eureka](/thread/post/4047525#post4047525 "View Quoted Post")
> 
> Disliked
> 
> Is there an update on the testing, MoStAsHaR15?  
>    
>  Thanks.
> 
> Ignored

I need another week to tell ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#412](/thread/post/4047912#post4047912 "Post Permalink")

  * Sep 25, 2010 6:21am  Sep 25, 2010 6:21am 

  * [ Eureka](eureka)

  * | Joined Aug 2006  | Status: Trader | [383 Posts](/search?do=process&provider=Member&searchuser=16246)

Many thanks to you and have a great weekend.  
  
Carol 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#413](/thread/post/4049857#post4049857 "Post Permalink")

  * Sep 27, 2010 8:40am  Sep 27, 2010 8:40am 

  * [ plind](plind)

  * | Joined Jun 2006  | Status: Trader | [135 Posts](/search?do=process&provider=Member&searchuser=12124)

Does anyone have the time left indicator that displays the time in the lower left corner of the template we use to setup charts? Thanks Paul 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#414](/thread/post/4050972#post4050972 "Post Permalink")

  * Sep 27, 2010 8:40pm  Sep 27, 2010 8:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar24884_5.gif) camvcvoo](camvcvoo)

  * | Joined Nov 2006  | Status: Trader | [678 Posts](/search?do=process&provider=Member&searchuser=24884)

> [Quoting plind](/thread/post/4049857#post4049857 "View Quoted Post")
> 
> Disliked
> 
> Does anyone have the time left indicator that displays the time in the lower left corner of the template we use to setup charts? Thanks Paul
> 
> Ignored

  
Try this. It shows time and spread. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Candle Time & Spread.mq4](/attachment/file/550542?d=1285587623) 2 KB | 300 downloads 

Ã§Â¦Â Ã¥Â­Â Victor V

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#415](/thread/post/4052021#post4052021 "Post Permalink")

  * Edited 2:00am  Sep 28, 2010 1:57am | Edited 2:00am 

  * [ kapybara](kapybara)

  * | Joined Aug 2010  | Status: Trader | [167 Posts](/search?do=process&provider=Member&searchuser=151152)

> [Quoting mostashar15](/thread/post/4047813#post4047813 "View Quoted Post")
> 
> Disliked
> 
> I need another week to tell ...
> 
> Ignored

Hi mostashar,  
  
1\. Many thanks to you and all contributors here. I want to share some interesting points, while testing your system (w/ EA from Steve). Please check my chart attached. It should be described fine in chart. I would think about setting up TP 2 or 3 pips above support (while go short) or 2 or 3 pips below resistance (while go long). In may chart you can see, that my good running trademissed TP by 1 pip, then it hit my SL (-30 pips). What do you think about that?  
  
2\. While testing this EA, I would like to know, how that setting (trailing stop) works here. I didn't see, that my SL was moving, while trailing stop was set in EA settings (default = 15 pips). 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: unlucky trade.jpg
Size: 190 KB](/attachment/image/550757/thumbnail?d=1365651246)](/attachment/image/550757?d=1285606792)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#416](/thread/post/4052505#post4052505 "Post Permalink")

  * Edited 7:33am  Sep 28, 2010 5:48am | Edited 7:33am 

  * [ Mandl2007](mandl2007)

  * | Membership Revoked  | Joined Nov 2008 | [279 Posts](/search?do=process&provider=Member&searchuser=86165)

Hi mostashar15 and others .... so we are trading here on the TF H4 - but the sl is only 30 pips ? It seems to me this sl is too small for such a high FT ? Usually a sl of 3 ATRs is recommended for any TF. That means the sl for TF H4 must be approximately 100 - 200 pips ... and dependent on your trading capital we can use only 0.05 ... 0.01 lot. In any case using only sl 30 pips we will be stoped out very often. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#417](/thread/post/4058799#post4058799 "Post Permalink")

  * Sep 30, 2010 1:46am  Sep 30, 2010 1:46am 

  * [ sheenka](sheenka)

  * | Joined Oct 2008  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=83782)

Hello!  
  
  
I confirm, that trailing stop is not working. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#418](/thread/post/4070659#post4070659 "Post Permalink")

  * Oct 5, 2010 2:52am  Oct 5, 2010 2:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3317_4.gif) pipsacker](pipsacker)

  * | Joined Aug 2005  | Status: Trader | [127 Posts](/search?do=process&provider=Member&searchuser=3317)

Hi All,  
  
Is anyone trading this system manually with success?  
  
pipsacker 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#419](/thread/post/4071204#post4071204 "Post Permalink")

  * Oct 5, 2010 7:16am  Oct 5, 2010 7:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar40570_6.gif) tahshoon](tahshoon)

  * | Joined May 2007  | Status: Trader | [454 Posts](/search?do=process&provider=Member&searchuser=40570)

> [Quoting pipsacker](/thread/post/4070659#post4070659 "View Quoted Post")
> 
> Disliked
> 
> Hi All,  
>    
>  Is anyone trading this system manually with success?  
>    
>  pipsacker
> 
> Ignored

we r waiting mostashar for a new modification to test it ... i hope that it will be this weak 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#420](/thread/post/4071248#post4071248 "Post Permalink")

  * Oct 5, 2010 7:37am  Oct 5, 2010 7:37am 

  * [ sfg7th](sfg7th)

  * | Joined Apr 2007  | Status: Trader | [171 Posts](/search?do=process&provider=Member&searchuser=38118)

I think this thread has died, like others.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

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

[Murrey Math indicator is very useful in Forex](/thread/3584-murrey-math-indicator-is-very-useful-in-forex "hello viewers, 
                this is santosh from india. in forex trading murrey math indicator is very useful so i give murrey math...") 68 replies

[Murrey Math lines](/thread/78393-murrey-math-lines "Where do i go outside the company itself to determine how to place MML's into metatrader?  Has anyone used them and found and good or...") 6 replies

[Murrey Math Swing Progression](/thread/135172-murrey-math-swing-progression "I've designed this system especially for those who do not like to trade shorter time frames such as myself. With owning a business I don't...") 22 replies

[Murrey Math Line signal](/thread/107962-murrey-math-line-signal "i use murrey math in trading 
  
i think eu will go down next week 
  
what do u think. 
  
If u use murrey math, you can post in here 
 ...") 9 replies

[Murrey math trading](/thread/67173-murrey-math-trading "hi to all 
has anyone seen a murrey math indicator that resembles any of http://www.murreymath.com/these? 
mike") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)
  * Subscribe
  * [66](javascript:void\(0\);)

Attachments: Murrey Advisor by MoStAsHaR15

Tags: Murrey Advisor by MoStAsHaR15

#  [](/thread/255584-murrey-advisor-by-mostashar15)Murrey Advisor by MoStAsHaR15 

  * 

  * [#421](/thread/post/4093109#post4093109 "Post Permalink")

  * Oct 13, 2010 8:47pm  Oct 13, 2010 8:47pm 

  * [ trader07](trader07)

  * | Joined Jan 2007  | Status: Trader | [338 Posts](/search?do=process&provider=Member&searchuser=32417)

Anyone still trading this system? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#422](/thread/post/4093199#post4093199 "Post Permalink")

  * Oct 13, 2010 9:23pm  Oct 13, 2010 9:23pm 

  * [ TriMagic](trimagic)

  * | Joined Sep 2010  | Status: Trader | [77 Posts](/search?do=process&provider=Member&searchuser=154956)

To tell you the truth I am only watching the 4 digit broker for signals on my 5 digit account but nothing happening, just looking at a "hold" signal the whole time, so not sure why this thread is so quiet. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#423](/thread/post/4114981#post4114981 "Post Permalink")

  * Oct 22, 2010 11:12am  Oct 22, 2010 11:12am 

  * [ sam2vt](sam2vt)

  * | Joined Jun 2010  | Status: Trader | [211 Posts](/search?do=process&provider=Member&searchuser=144775)

Hi Mostashar15,  
  
I would like to show the Daily Range Statistic only into my chart. How could I do that? However, I do not know at all for coding or change the script for mq4 file. Would you please send me the DRS mq4 file? Thank you in advance. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#424](/thread/post/4488058#post4488058 "Post Permalink")

  * Mar 22, 2011 12:51am  Mar 22, 2011 12:51am 

  * [ akara](akara)

  * | Joined Jul 2009  | Status: Trader | [26 Posts](/search?do=process&provider=Member&searchuser=109880)

> [Quoting mostashar15](/thread/post/4047813#post4047813 "View Quoted Post")
> 
> Disliked
> 
> I need another week to tell ...
> 
> Ignored

  
HI motashar, nice work here. Any updates yet?  
  
lol ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#425](/thread/post/4500676#post4500676 "Post Permalink")

  * Mar 26, 2011 8:57pm  Mar 26, 2011 8:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar146048_3.gif) infinitus](infinitus)

  * Joined Jun 2010 | Status: s = k log W | [20,603 Posts](/search?do=process&provider=Member&searchuser=146048)

Hi Guys,  
  
just came accidentally to this "died" threat and I thought that I might say a few words regarding this system, because it seems to be interesting, but unfortunately for some/most here not really working.  
  
I came around Murrey Math 2 years ago and on the first sight it was an simple and easy to trade system by looking at the charts. But I made the experience most here made: sometimes it worked good, sometimes it worked very bad.  
  
It took me some weeks to understand why.  
  
To put it simply: Murrey Math is a fractal approach. You can not win with this system by only looking and judging from one timeframe. What does that mean?  
  
E.g.: If you try to trade this one on the 4h TF and the price is around the -1/8 line (in falling trend), you would think that chances are as high as around 95% to see price reversing here and run between 2 and 4 Murrey Math trading lines to the upper direction.  
  
But now comes the tricky part: each TF has its own Murrey Math octave. What the heck does that mean: Simply, it means:  
  
when you are in 4h TF on MMTL -1, you can be on daily TF for example just at the other end, at MMTL 8 or +2/8.  
  
And that had severe implications and might be the main reason for the failure of this system: it is not a MTF approach.  
  
The second reason for the different results here is clearly the 4h TF. 4h candles are very tricky, because most brokers have different closing times for their 4h candles. Results here would have been more equal when this system would have been run on 1h TF. Murrey Math works on all TF because it is fractal.  
  
So what can I advise to make this system working:  
  
a) do not use the 4h TF. Use the 1h TF. I do most of my Murrey Math related trading on 15min TF, and time my entries on 5 and 1min TF  
  
b) make it an MTF approach: open up a 1, 5, 15 and 60min chart and place the Murrey Math lines on it. See how this 4 TF's interact. If you place a short on 15min TF wait the price to be between 7/8 and +2/8. I prefere the +1/8 line on the first try to penetrate it (here are chances highest to get a very nice rebound). But try to time the move on 1min and 5min TF too. When you get such a move and the higher TF, e.g. the 1h TF is in accordance there is only very limited chance that you will suffer a loss. sometimes I even take a look at the 4h TF to get the idea where price is located.  
  
When I get a move where 3 or 4 TF's are in accordance regarding their MMTL I call it "the ducks are in a line".  
  
If 1,5 and 15 min TF are in accordance trade on the 5 min  
  
If 5, 15, 60 are in accordance trade on the 15 min  
  
If 15, 60, 240 are in accordance trade on 60min  
  
  
c) do not, repeat not, trade this here introduced single timeframe approach as an EA, unless the EA is changed and is able to take the, at least, upper TF into consideration.  
  
  
When you trade Murrey Math you do not need additionally support/resistance lines or pivot points, since the MMTL are just that.  
  
Better take a look at or search for the real support and resistance zones in the charts and look, if they align with Murrey Math.  
  
  
If you have questions sent me an email since I will not follow this thread.  
  
  
Best of luck to you,  
  
  
Markus 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#426](/thread/post/5781582#post5781582 "Post Permalink")

  * Jun 22, 2012 1:48am  Jun 22, 2012 1:48am 

  * [ shahir](shahir)

  * | Joined Jun 2012  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=265034)

Hye,  
  
Is there any 5 digit version which works without bugs ?  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#427](/thread/post/8499625#post8499625 "Post Permalink")

  * Last Post: Sep 21, 2015 8:29pm  Sep 21, 2015 8:29pm 

  * [ mostashar15](mostashar15)

  * | Joined Aug 2010  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=150130)

Thanks, it's been a while ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Murrey Advisor by MoStAsHaR15
  *   * [ **Reply to Thread** ](/thread/255584-murrey-advisor-by-mostashar15/reply#reply)

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)
