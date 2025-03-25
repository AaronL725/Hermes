

  * 

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#1](/thread/75394-powersm-semi-martingale-ea "Post Permalink")

  * First Post: Edited Apr 17, 2008 5:21am  Mar 14, 2008 2:49pm | Edited Apr 17, 2008 5:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I am posting my PowerSM EA and my PowerSM Calculator for those who have followed the thread by FXTradepro on the forum. For those who are a little disheartened after finding out you had to pay to use his FXTradepro EA, this is for you. Below is the link to the thread to get familiar with the concept. **Please read over first if you have not used the EA before.**  
  
[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](http://forexfactory.com/showthread.php?t=43221)  
  
Before I start, I want to say I am not disrespecting or in any way discrediting FXTradepro for his efforts because I feel he has a very profitable tool for the traders to use. In my own opinion, I feel you should never post something for free only to wet a persons appetite, then bring people to your site and start charging you to use your product, that's all I'm going to say about that.  
  
Also, I will only be posting the EX4 file since I have, out of my own pocket, personally paid to have this EA made to my specifications and plan to commercially market this outside of this forum (don't worry, the EA will be free to all forum users!). For those who want more info can pm me but I will not advertise it here on the forum. The EA itself will have an expiration date one year from today's date for those who would like to use it to trade with or to demo it with other settings to use on other pairs (This is for repaying those who have helped me on this forum and I do not expect or will accept payments, donation, or any other form of compensation for this, it is for you guys to use as you wish!). After the first year I will post a new EA with a one year expiration on it to keep some sort of control on it.  
  
For those who have not seen or used this EA, it is simple and straight forward. The EA opens a trade in three different ways  
  
1.) With the Time and Price entry set to false the EA will open a trade on the next tick.  
  
2.) With the Price entry set to true you can have the EA open trades starting at a set price point.  
  
3.) With the Time entry set to true you can have the EA open trades at a certain time (my preference).  
  
The EA will open the first trade above and either a) hit the take profit level you set or b) hit the stop. When a stop is hit a trade is immediately entered in the opposite direction with the next lot progression up to 24 progression levels. The link above will give you more details about the trading aspect of the EA.  
  
Some changes I made to fit want I wanted the EA to do is:  
  
a.) There is no longer a hibernation function.   
  
b.) The Time entry was modified to also have a stop time for those who want the EA to trade during more volatile hours, for example from London open at 08:00 GMT to London close at 17:00 GMT.  
  
c.) I have added a Breakeven function where you can move the stop after "X" number of pips. This does sometimes affect your total profit when hit as you do not lose money when you stop is hit once you stop is moved. I will explain this a little later in the thread.  
  
d.) I have also added also added extra functions like the ability to add an expiration date and to be able to code the EA to use specific account numbers (This is only activated on the commercial end for those who manage multiple accounts for their clients and for those outside the forums who only want to lease it).  
  
I will also post my demo statement daily to show the trade progress starting with yesterdays sequence on EUR/USD. I will only show the trades for that day as not to clutter up the statement. I will also be testing it out on USD/JPY and USD/CHF starting this morning using similar take profit and stop levels. 

Attached File(s)

![File Type: xls](https://assets.faireconomy.media/images/attach/xls.gif) [Original.xls](/attachment/file/95941?d=1205797592) 142 KB | 5,641 downloads | Uploaded Mar 18, 2008 8:46am 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [PowerSM V.5.ex4](/attachment/file/103551?d=1208377286) 11 KB | 6,007 downloads | Uploaded Apr 17, 2008 5:21am 

  * [#2](/thread/post/1902737#post1902737 "Post Permalink")

  * Mar 14, 2008 2:51pm  Mar 14, 2008 2:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

For those who would like to see how the EA looks on the screen here you go. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: trade lines.gif
Size: 37 KB](/attachment/image/95103/thumbnail?d=1365539749)](/attachment/image/95103?d=1205473841)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#3](/thread/post/1902761#post1902761 "Post Permalink")

  * Mar 14, 2008 3:25pm  Mar 14, 2008 3:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here is the first statement on EUR/USD from yesterday. Sorry for the zip file, I can save a statement to my desktop but don't know how to convert an .htm file. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [Statement.zip](/attachment/file/95105?d=1205475782) 2 KB | 2,814 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#4](/thread/post/1902789#post1902789 "Post Permalink")

  * Mar 14, 2008 3:56pm  Mar 14, 2008 3:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

As I mentioned earlier, I use the Breakeven function to help eliminate some losses when the EA is trading. I generally will set it to 3/4 of the takeprofit level. For example, if you set your profit level at 40 pips, your breakeven level will be 30 pips. Obviously you can set it to whatever floats your boat but I do advise not to set it too low as you will stop yourself out more often which is not what we want. 3/4 is generally past the 61.8 fib retracement ( roughly 24-25 pips) and if it is triggered, hopefully a reversal will soon show it's ugly head and the EA will be ready.   
  
A good example is on this first statement in the last post. If you look at the fourth trade, our breakeven kicked in and stopped out with **no loss** instead of normally losing $30.00 ($10 a pip @.3 lots).   
  
With out the breakeven function we would have made:   
  
-$10 \+ -$10 + -$20 \+ -$30 \+ -$40 \+ +$240 = +$130 ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
If you used the breakeven function you would've made $30.00 more:  
  
-$10 + -$10 \+ -$20 \+ $0 \+ -$40 \+ +$240 = +$160 ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#5](/thread/post/1902959#post1902959 "Post Permalink")

  * Mar 14, 2008 6:17pm  Mar 14, 2008 6:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here's the EUR/USD statement for 3/14/2008 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [statement 1.zip](/attachment/file/95124?d=1205486212) 2 KB | 1,894 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#6](/thread/post/1903053#post1903053 "Post Permalink")

  * Mar 14, 2008 7:52pm  Mar 14, 2008 7:52pm 

  * [ joselb](joselb)

  * | Joined Mar 2007  | Status: Trader | [67 Posts](/search?do=process&provider=Member&searchuser=35589)

I can not make it work..., and I tried in brokers where the stops are allowed in less than 10 pips, as IBFX. In other brokers I know that I must change the SL and TP or it doesn´t work because they limit the SL,s.  
  
Can you post more details about the EA?  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#7](/thread/post/1903058#post1903058 "Post Permalink")

  * Mar 14, 2008 7:56pm  Mar 14, 2008 7:56pm 

  * [ joselb](joselb)

  * | Joined Mar 2007  | Status: Trader | [67 Posts](/search?do=process&provider=Member&searchuser=35589)

Sorry, my bad... It works perfectly.  
  
I will check it, thanks a lot. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#8](/thread/post/1903484#post1903484 "Post Permalink")

  * Mar 14, 2008 11:19pm  Mar 14, 2008 11:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar43563_7.gif) FXTradepro](fxtradepro)

  * | Commercial User  | Joined Jul 2007 | [355 Posts](/search?do=process&provider=Member&searchuser=43563)

This is a complete and utter RIPOFF of my work and concepts. In fact the Calculator Posted is exactly mine. I would ask Scott or one of the other Moderators to please DELETE my orginal thread (the LINK is posted above) so that this thread starter cannot reference my materials. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#9](/thread/post/1903527#post1903527 "Post Permalink")

  * Edited 11:47pm  Mar 14, 2008 11:31pm | Edited 11:47pm 

  * [ raad](raad)

  * | Joined Jul 2007  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=43840)

anyone tested it on live accounts?  
how can it handle price requotes on live?  
how can it handle loss of internet connection?  
  
sorry for my english.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#10](/thread/post/1904086#post1904086 "Post Permalink")

  * Mar 15, 2008 3:07am  Mar 15, 2008 3:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

First off FXTradepro, you were unwilling to provide any source code for your EA which forced me to code one of my own. This EA is based on the**rules** of your EA and this is a **modifi ed** version fit to my trading style,**not an exact copy.  
  
**So your basically saying if a forum member posts a trading strategy for example, and I modify the settings of the strategy to my preferences, that the original poster can tell me I can no longer use his strategy because I changed it. **No, they can't!** As for the FXTradepro calculator, excel worksheets are not copyrighted material last time I checked, and you provided this free to us on the forum as well, unless you're now going to charge us for that too! If I want to change the look and color, input parameters, and name to match my EA, I have every right to and I will.   
  
And remember this, even you personally said right in your own thread I could have someone code the EA for me here in post #493.  
  
[http://forexfactory.com/showthread.php?t=43221&page=33](http://forexfactory.com/showthread.php?t=43221&page=33)  
  

> Quote
> 
> Disliked
> 
> Quote:  
>  Originally Posted by **mer071898** [](http://forexfactory.com/showthread.php?p=1609225#post1609225)<http://forexfactory.com/images/buttons/viewpost.gif>   
>  _Whew, had me a scare today on EUR/JPY!![](https://resources.faireconomy.media/images/emojis/64/1f633.png?v=15.1) I put in my normal timed entry at 6:00 GMT and let her ride and went all the way to the 24th entry! Luckily price went my way and it closed out for a nice profit of $1579.88.   
>    
>  I'm thinking because of the volatility of the pair of adjusting my settings to 15 stop and 60 TP instead of 10/40 and moving my entry time to 7 or 8 GMT. I'm pretty much stuck to a timed entry as I do work another job and need my beauty sleep. ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1) Anyone with any other ideas or options? ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)  
>    
>  My GBP/JPY closed out on the 16th progression for a profit of $1827.94. I'm also testing out NZD/USD with settings of 12 48 because of a higher spread.   
>    
>  FXTradepro, I also found a possible way to stretch out past 24 progressions but your coder will have to add a feature to the EA. On my EUR/JPY I had opened another chart and added a Breakeven EA that brings the stop to breakeven after X number of pips that you choose.   
>    
>  Here's an example, let's say you are on EUR/USD at progression level 17 (13 lots), and your target is 40 pips the Breakeven EA is set to 30 pips. When price has hit the 30 pip mark and the EA has moved your stop and then price goes against you and stops you out, what you would have is a trade with no loss instead of a -$1300.00 loss. Currently the FXTradepro Manager EA just goes to the next progression level in line. If possible, what would be cool is if the FXTradepro Manager EA could be coded to include the Breakeven EA coding and then be able open another trade at that **same progression level**. Basically what has happened is you just just received a free trade and an extra progression level!! :surprised Even if it can't be merged in with your EA this can save a lot of money for those who are using the FXTradepro Manager EA now. Any thoughts?_  
>    
>  mer....A Timed Entry alone, without some other reason to enter a Sequence can be dangerous, as you have now seen. I really do suggest that everyone pick their Initial Entry very carefully. Today was not a very active day in the Market (except for GBPUSD) as most pairs did not make their ADR (at least for the 7 pairs I track) - as a hint, I have noticed that when there are not any News Releases for a particular day (speeches don't count for me), that often these days produce very limited volatility - as such, I often stay away. This is not a rule, but something I have noticed.  
>    
>  Regarding the EA - I have no plans to alter the code of the EA, mainly because of the fact that I am a fulltime Trader and am always near my charts when I have a Sequence in progress. As a matter of fact - did you know that you can manually alter your "HARD" stop and TP on your MT4 Platform while the FXTradepro Manager is running? You may be able to figure out a way to use this information to your benefit to achieve a similar result to what you describe above. Remember that I use the FXTradepro Manager as a Trading Tool and I prefer not to complicate the code by adding features that I will not likely use.  
>    
>  **Remember, you always have the option of trying to have a similar EA coded if there are certain functions that you would like.** Personally I have no interest in spending my time on the further testing of any such Tool. For me, I prefer to explore the best way to Trade with the Tools that I have (and that I know are tested and work well).  
>    
>  Thanks for your input....  
>    
>  Dan

Unlike you,**this will be FREE to all members of this forum**! I had personally paid someone to code it for my needs so I do have the right to not post the source code as you did, but if I want to share **MY** own personally paid for EA with the other members of this forum, I will. And since the coding is completely different to yours and copyrighted in my name, you have no right to tell me what to do with it inside or outside this forum.  
  
Remember this post from the mods:  
  
SMJones  
  

> Quote
> 
> Disliked
> 
> Ok, I am going to cut to the chase here. I am a moderator as I am sure you know... This is a very nice presentation and I thank you for it... Very professional. However, Self Promotion is not allowed here at FF without prior approval from the Admin, so if this is not a promotion, that is just great and you are to be commended.. If it is a way of building a following and then charging for the services, that would be considered self promotion and would cause the thread to be deleted and the member to be banned.   
>    
>  I am just laying my cards out, so we understand each other I mean nothing other than that.   
>    
>  It would just be a shame to lead people down a path and then discontinue that.   
>    
>  So, do I have your assurance that this is not the case? If so, this could develop into a very interesting thread, if not, in all fairness, I do not want to waste your valuable time...   
>    
>  Thanks for your understanding in this,

And you replied:  
  

> Quote
> 
> Disliked
> 
> Scott,  
>    

But that's is exactly what you did. You posted the EA for free, built a following, and then charged for the services to "lease" your EA once you got them to your site, then people on the forum started catching on and then your thread was dead and was closed. So please don't waste your time here whining like you felt you were ripped off. I'm just providing my EA for free like you should have done in the first place. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#11](/thread/post/1904096#post1904096 "Post Permalink")

  * Mar 15, 2008 3:17am  Mar 15, 2008 3:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

To raad,  
  
I have not had a chance to try it live as of now. I will first be doing more testing and only then will it be tried out on a live account.   
  
As for requotes, you do have the ability to adjust the slippage and the amount of times to try and place the order if a requote occurs. like I said, I have not tried it live as of yet to test it.  
  
I have not had any issues with my internet connection as of now, but you can always test this by starting the EA and disconnecting your modem or disabling your internet connection under your "Network Connections" in the Control Panel. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#12](/thread/post/1904102#post1904102 "Post Permalink")

  * Mar 15, 2008 3:21am  Mar 15, 2008 3:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here is the statement for 3/14/2008 on USD/CHF and USD/JPY 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [statement 1.zip](/attachment/file/95245?d=1205518839) 2 KB | 1,484 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#13](/thread/post/1904118#post1904118 "Post Permalink")

  * Mar 15, 2008 3:26am  Mar 15, 2008 3:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar43563_7.gif) FXTradepro](fxtradepro)

  * | Commercial User  | Joined Jul 2007 | [355 Posts](/search?do=process&provider=Member&searchuser=43563)

Mer.....You completely misunderstand me. I could not care less that you have cloned my EA. This is well within anyones rights to do and many others have done the same. What I find offensive is the fact that you are using all the information and charts, graphs etc, that I posted about the Strategy (by sending your thread readers to that old thread) rather than explain it yourself in this thread.   
  
I have really nothing further to say and I wish you well....... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#14](/thread/post/1904181#post1904181 "Post Permalink")

  * Mar 15, 2008 3:43am  Mar 15, 2008 3:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

People put up links to previous posts all the time to refer to the original thread for information and it was done only to save time . 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#15](/thread/post/1904391#post1904391 "Post Permalink")

  * Mar 15, 2008 5:42am  Mar 15, 2008 5:42am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

This would be a great application for a virtual private server. I use one. godaddy.com, but there are others... about $250 a year. ......   
  
Look forward to seeing this develop. I LOVE the math on this. Used the Binary (modified D'Alembert progressive lot) Strategy for quite some time. Problem with that one is that it NEEDS a good system, or the lot sizes get up there pretty quick in a bad run.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#16](/thread/post/1904472#post1904472 "Post Permalink")

  * Mar 15, 2008 7:18am  Mar 15, 2008 7:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar50293_23.gif) damonl](damonl)

  * Joined Oct 2007 | Status: I'm on a 10 year plan. | [4,309 Posts](/search?do=process&provider=Member&searchuser=50293)

What TF should I put this on.  
  
I had it on the D1 EU, but no trades taken today.  
  
Nice results with UJ and UCHF  
  
Thanks for sharing ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

"Keep your eyes on the helpers" - Mr. Rogers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#17](/thread/post/1904543#post1904543 "Post Permalink")

  * Mar 15, 2008 8:54am  Mar 15, 2008 8:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

damonl,  
  
I am just using the default TP of 40 with a 10 pip stop on a 5 minute TF with timed entry to true and price entry to false so I can see the trade progress. What are your inputs set at? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#18](/thread/post/1904860#post1904860 "Post Permalink")

  * Mar 15, 2008 8:07pm  Mar 15, 2008 8:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar50293_23.gif) damonl](damonl)

  * Joined Oct 2007 | Status: I'm on a 10 year plan. | [4,309 Posts](/search?do=process&provider=Member&searchuser=50293)

> [Quoting mer071898](/thread/post/1904543#post1904543 "View Quoted Post")
> 
> Disliked
> 
> damonl,  
>    
>  I am just using the default TP of 40 with a 10 pip stop on a 5 minute TF with timed entry to true and price entry to false so I can see the trade progress. What are your inputs set at?
> 
> Ignored

I have the same settings as you. I will put the EA on the 5M TF and keep in touch. 

"Keep your eyes on the helpers" - Mr. Rogers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#19](/thread/post/1905167#post1905167 "Post Permalink")

  * Mar 16, 2008 6:21am  Mar 16, 2008 6:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

No problem, let me know how it works out. Make sure you adjust the time entry to match your GMT time. If you're GMT+1 the EA won't enter a trade til 08:00 instead of 07:00. That's why I use ODL because they're GMT+0. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#20](/thread/post/1905913#post1905913 "Post Permalink")

  * Edited 10:59am  Mar 17, 2008 4:15am | Edited 10:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Great job with this ea! I will test it out also! I do have a couple of questions for ya!  
  
1\. How should I set the time if my broker is GMT +2 (FXDD)? If I want to start at london open?  
  
2\. Since it does not have the hybernation option, does that mean that once the TP has been reached it continues to trade?  
  
3\. I use the Damiani Volatmeter v3.2 to help me determine when there is enough volatility to enter. Is there any way to set the EA to trade manually just by entering a position when I see the right conditions? (besides price or time).  
  
4\. I love the parachute stop option! I have always traded this way anyway so might as well be mechanical to move the stop to break even after a certain amount of pips!  
  
Take care! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#21](/thread/post/1906823#post1906823 "Post Permalink")

  * Mar 17, 2008 12:17pm  Mar 17, 2008 12:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

To Chartist,  
  
Thanks for the input.   
  
1.) If you are GMT+2 just add 2 to whatever start time you prefer. If London open is at 08:00 GMT, you would set the timed entry to 10:00.  
  
2.) Currently I am having some bugs in the EA where it is not entering immediately when both price and timed entries are set to false, so I can't test that out for you right now but I will e-mail my coder and ask him. With nothing there to stop the EA from starting a new sequence like a price point or a time I would assume it would start up another sequence after the TP is hit. Once I get the bug fixed I'll test it out for you to see if it keeps opening a new sequence or stops automatically.  
  
3.) Again, after I get the bug fixed, when you're indicator gives you the go ahead to enter just set the timed and price entry to false and stick it on the chart and the EA will enter the trade on the next tick.   
  
4.)The main reason I added the Breakeven function is so I don't have to sit in front of the computer all night to watch the trades and if a trade goes the wrong way after almost hitting my TP I won't lose anything. But again I warn people not to go anything less than 75% of the TP level for your breakeven point in order to minimize getting stopped out too often.  
  
Just to let you know I'm also trying to see if my coder can add another feature to the EA. Say, for example, we are in a trade and we are on the 5th sequence level and our breakeven setting was hit and our stop moved, then the trade went against us and stopped us out for 0 pips. What I'd like the EA to do is re-open the trade at the 5th level where it was stopped out instead of going to the 6th level. Basically it would be a freebie trade and we would actually end up with 25 chances instead of 24 chance to hit our TP level. What do you guys think? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#22](/thread/post/1906937#post1906937 "Post Permalink")

  * Mar 17, 2008 1:33pm  Mar 17, 2008 1:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar50293_23.gif) damonl](damonl)

  * Joined Oct 2007 | Status: I'm on a 10 year plan. | [4,309 Posts](/search?do=process&provider=Member&searchuser=50293)

> [Quoting mer071898](/thread/post/1906823#post1906823 "View Quoted Post")
> 
> Disliked
> 
> To Chartist,  
>    
>  Thanks for the input.   
>    
>  1.) If you are GMT+2 just add 2 to whatever start time you prefer. If London open is at 08:00 GMT, you would set the timed entry to 10:00.  
>    
>  2.) Currently I am having some bugs in the EA where it is not entering immediately when both price and timed entries are set to false, so I can't test that out for you right now but I will e-mail my coder and ask him. With nothing there to stop the EA from starting a new sequence like a price point or a time I would assume it would start up another sequence after the TP is hit. Once I get the bug fixed I'll test it out for you to see if it keeps opening a new sequence or stops automatically.  
>    
>  3.) Again, after I get the bug fixed, when you're indicator gives you the go ahead to enter just set the timed and price entry to false and stick it on the chart and the EA will enter the trade on the next tick.   
>    
>  4.)The main reason I added the Breakeven function is so I don't have to sit in front of the computer all night to watch the trades and if a trade goes the wrong way after almost hitting my TP I won't lose anything. But again I warn people not to go anything less than 75% of the TP level for your breakeven point in order to minimize getting stopped out too often.  
>    
>  Just to let you know I'm also trying to see if my coder can add another feature to the EA. Say, for example, we are in a trade and we are on the 5th sequence level and our breakeven setting was hit and our stop moved, then the trade went against us and stopped us out for 0 pips. What I'd like the EA to do is re-open the trade at the 5th level where it was stopped out instead of going to the 6th level. Basically it would be a freebie trade and we would actually end up with 25 chances instead of 24 chance to hit our TP level. What do you guys think?
> 
> Ignored

This makes sense to me 

"Keep your eyes on the helpers" - Mr. Rogers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#23](/thread/post/1906942#post1906942 "Post Permalink")

  * Mar 17, 2008 1:40pm  Mar 17, 2008 1:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

> [Quoting mer071898](/thread/post/1906823#post1906823 "View Quoted Post")
> 
> Disliked
> 
> To Chartist,  
>    
>  Thanks for the input.   
>    
>  1.) If you are GMT+2 just add 2 to whatever start time you prefer. If London open is at 08:00 GMT, you would set the timed entry to 10:00.  
>    
>  2.) Currently I am having some bugs in the EA where it is not entering immediately when both price and timed entries are set to false, so I can't test that out for you right now but I will e-mail my coder and ask him. With nothing there to stop the EA from starting a new sequence like a price point or a time I would assume it would start up another sequence after the TP is hit. Once I get the bug fixed I'll test it out for you to see if it keeps opening a new sequence or stops automatically.  
>    
>  3.) Again, after I get the bug fixed, when you're indicator gives you the go ahead to enter just set the timed and price entry to false and stick it on the chart and the EA will enter the trade on the next tick.   
>    
>  4.)The main reason I added the Breakeven function is so I don't have to sit in front of the computer all night to watch the trades and if a trade goes the wrong way after almost hitting my TP I won't lose anything. But again I warn people not to go anything less than 75% of the TP level for your breakeven point in order to minimize getting stopped out too often.  
>    
>  Just to let you know I'm also trying to see if my coder can add another feature to the EA. Say, for example, we are in a trade and we are on the 5th sequence level and our breakeven setting was hit and our stop moved, then the trade went against us and stopped us out for 0 pips. What I'd like the EA to do is re-open the trade at the 5th level where it was stopped out instead of going to the 6th level. Basically it would be a freebie trade and we would actually end up with 25 chances instead of 24 chance to hit our TP level. What do you guys think?
> 
> Ignored

I like it! That would bring down the risk even further.  
  
When do you think that bug will be worked out and posted the fixed version?  
  
Thank you for the advise about the stop level and also thank you for answering my questions! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#24](/thread/post/1907036#post1907036 "Post Permalink")

  * Mar 17, 2008 4:10pm  Mar 17, 2008 4:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

You're welcome Chartist, I'm hoping my coder can work on it this week and get everything worked out and fixed. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#25](/thread/post/1907093#post1907093 "Post Permalink")

  * Mar 17, 2008 5:20pm  Mar 17, 2008 5:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here's the statement for 3/17/2008 for Eur/Usd. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [statement 1.zip](/attachment/file/95752?d=1205741901) 2 KB | 764 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#26](/thread/post/1907229#post1907229 "Post Permalink")

  * Mar 17, 2008 7:06pm  Mar 17, 2008 7:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here's the statement for 3/17/2008 for Usd/Jpy and Usd/Chf. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [statement 1.zip](/attachment/file/95769?d=1205748334) 2 KB | 644 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#27](/thread/post/1907426#post1907426 "Post Permalink")

  * Mar 17, 2008 9:34pm  Mar 17, 2008 9:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Cool! Looks like after the tp is hit, the ea does not take any more trades even if the end time has not expired. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#28](/thread/post/1907682#post1907682 "Post Permalink")

  * Mar 17, 2008 11:39pm  Mar 17, 2008 11:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Yep, and as soon as I get the bug fixed I'm hoping with both entry functions set to false it'll do the same thing, go through a sequence then stop. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#29](/thread/post/1908388#post1908388 "Post Permalink")

  * Mar 18, 2008 5:30am  Mar 18, 2008 5:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

I opened a trade today by having TIME and PRICE set to false and it did take a few seconds once I dropped it in but, it didn't seem like it took waaay too long but perhaps it could be quicker. I don't know if my virtual server has anything to do with improving the ea's performance as well.  
  
Anyways, I had my first winning trades this morning during London with usd/chf reached tp on the second trade and gbp/usd reached tp during NY session on the 5th trade.  
  
I'm sleeping during London so, I set the start time to coincide with a news event and I'm awake during NY to choose when to enter. I also changed the lots sequence a little to allow for multiple currencies trading at the same time.  
  
I wonder how far fetched it would be to just have 17 levels instead of 24? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#30](/thread/post/1908513#post1908513 "Post Permalink")

  * Mar 18, 2008 6:43am  Mar 18, 2008 6:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar50293_23.gif) damonl](damonl)

  * Joined Oct 2007 | Status: I'm on a 10 year plan. | [4,309 Posts](/search?do=process&provider=Member&searchuser=50293)

> [Quoting mer071898](/thread/post/1907229#post1907229 "View Quoted Post")
> 
> Disliked
> 
> Here's the statement for 3/17/2008 for Usd/Jpy and Usd/Chf.
> 
> Ignored

I had the same results as you except my USD/JPY opened up 11 trades before hitting. Yours far less.  
  
What is your spread for UJ? At one point it looks as if it missed the P/T by 1 pip. 

"Keep your eyes on the helpers" - Mr. Rogers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#31](/thread/post/1908627#post1908627 "Post Permalink")

  * Mar 18, 2008 7:59am  Mar 18, 2008 7:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Chartist, If you want to trade 17 levels just remove the last 7 lot sequences in the inputs and there you go. That's why it is here for us to play with and test. Good job on Gbp/Usd, I never did like that pair using this EA. What are you using for TP, breakeven, and stop?  
  
damonl, my pip spread on all three pairs I trade are 2 pips but I did not open my Usd/Jpy sequence until 08:15 instead of 07:00, maybe that was the difference. Just curious, how many of those 11 trades did the breakeven setting save you from having a loss? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#32](/thread/post/1908629#post1908629 "Post Permalink")

  * Mar 18, 2008 7:59am  Mar 18, 2008 7:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar21271_4.gif) Dreamliner](dreamliner)

  * Joined Oct 2006 | Status: Trader | [2,271 Posts](/search?do=process&provider=Member&searchuser=21271)

I don't understand the Excel sheet for lot sizes. Let's say a person was trading with $1,000.00 on a mini account with IBFX at 400.1. Thank you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#33](/thread/post/1908727#post1908727 "Post Permalink")

  * Mar 18, 2008 9:24am  Mar 18, 2008 9:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Dreamliner, here is a quick video to explain a little about the spreadsheet. Before you watch it I've attached the original spreadsheet in the first post for everyone which has the info on IBFX accounts on it. It's an AVI video so let me know if you have any problems playing it.  
  
[](http://s86.photobucket.com/albums/k113/mer071898/?action=view&current=excelhelp.flv)[http://i86.photobucket.com/albums/k1..._excelhelp.jpg](http://i86.photobucket.com/albums/k113/mer071898/th_excelhelp.jpg)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#34](/thread/post/1908748#post1908748 "Post Permalink")

  * Mar 18, 2008 9:43am  Mar 18, 2008 9:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar21271_4.gif) Dreamliner](dreamliner)

  * Joined Oct 2006 | Status: Trader | [2,271 Posts](/search?do=process&provider=Member&searchuser=21271)

The video was very helpful, thank you for making it!   
  
What number is good to put in the "breakeven stop" assuming 10 sl and 40 tp? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#35](/thread/post/1908771#post1908771 "Post Permalink")

  * Mar 18, 2008 10:02am  Mar 18, 2008 10:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar21271_4.gif) Dreamliner](dreamliner)

  * Joined Oct 2006 | Status: Trader | [2,271 Posts](/search?do=process&provider=Member&searchuser=21271)

One other question: I have set both the "time entry" and "price entry" to false, I have enabled live trading, and the smiley face is on the top right, but the EA is not opening any orders. This is a demo account, is it possible that the ea needs to be worked for a demo account? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#36](/thread/post/1908833#post1908833 "Post Permalink")

  * Mar 18, 2008 10:39am  Mar 18, 2008 10:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar50293_23.gif) damonl](damonl)

  * Joined Oct 2007 | Status: I'm on a 10 year plan. | [4,309 Posts](/search?do=process&provider=Member&searchuser=50293)

> [Quoting mer071898](/thread/post/1908627#post1908627 "View Quoted Post")
> 
> Disliked
> 
> Chartist, If you want to trade 17 levels just remove the last 7 lot sequences in the inputs and there you go. That's why it is here for us to play with and test. Good job on Gbp/Usd, I never did like that pair using this EA. What are you using for TP, breakeven, and stop?  
>    
>  damonl, my pip spread on all three pairs I trade are 2 pips but I did not open my Usd/Jpy sequence until 08:15 instead of 07:00, maybe that was the difference. Just curious, how many of those 11 trades did the breakeven setting save you from having a loss?
> 
> Ignored

It would have saved me 2 trades, which with a system like this would be quite significant regarding the lots not chaning on a B/E issue.  
  
What made you wait until 8:15? That was the difference. Do you always wait until 8:15 or was that just today? 

"Keep your eyes on the helpers" - Mr. Rogers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#37](/thread/post/1908868#post1908868 "Post Permalink")

  * Mar 18, 2008 11:03am  Mar 18, 2008 11:03am 

  * [ jones247](jones247)

  * | Joined Aug 2007  | Status: Trader | [264 Posts](/search?do=process&provider=Member&searchuser=46344)

Hi Mer071898,  
  
Good job on the break-even aspect to this EA. I'm sorry that Dan (FXTradepro) was upset with your thread. Nonetheless, this is what makes forums such as this so valuable... You were able to take Dan's system and build upon it. Hopefully, someone will be able to incorporate an additional demension or technique that would even enhance this system further.   
  
As I've stated on FXTradepro's thread, the biggest challenge with this system is the fact that the drawdowns on each progession become more devastating. If one were to experience 24 failures in a row, then there you have a Blown Account. In order to minimize that situation, perhaps the best bet is to enter the trades during the opening of the London market, wherein the likihood of a break-out is greatest.  
  
Walt 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#38](/thread/post/1908912#post1908912 "Post Permalink")

  * Edited 11:36am  Mar 18, 2008 11:34am | Edited 11:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Mer, I used the regular 10 sl, 40tp, 30b/e, and one of those trades was a breakeven trade I forgot to mention and I agree with Damoni in that it would be awesome to have a second chance after the b/e without increasing the lot size. You're right about this pair though, I don't like it too much with this EA, its a little too volatile.  
  
Here's my sequence I'm going to try: .1, .1, .2, .3, .4, .6, .8, 1.1, 1.4, 1.8, 2.3, 2.9, 3.7, 4.7, 5.9, 7.4, 9.3...... the rest I've removed. So I'm going to try this 17 trade strategy which better suits my style. I'll keep you posted.  
  
Hey Mer, do you only trade usdjpy, eurusd, and usdchf with this EA? Also, do you trade the NY session at all? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#39](/thread/post/1909015#post1909015 "Post Permalink")

  * Mar 18, 2008 1:01pm  Mar 18, 2008 1:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

**Dreamliner** , your welcome, I figured a video might be easier to understand. As for my breakeven setting I try to be at least 75% of the TP because if you happen to notice that the 61.8% fib level is 24-25 pips if it retraces. Now the GBP pairs will have an uncanny knack to retrace to the 76.4% more often so maybe stick to 80% of TP on those pairs. In post #22 I mentioned there might be a bug that's not letting the EA open immediate trade sequences with both settings to false but my coder is trying to catch up and look at it.  
  
**damonl** , I didn't get in at 07:00 because my timed entry didn't open a sequence for some reason and I had to reopen my MT4 and change th entry time to get it to work correctly, another possible bug? I don't know yet.  
  
**jones247** , Thanks for the support. I have no hard feelings or hatred towards FXTradepro, I just thought he went about thing the wrong way by promising a free EA then taking it away from the rest us on the forum because he decided to charge for it. And I agree, the drawdown sucks as you go deeper in the sequence, but that's why I added the breakeven function and the ability to stop trading after the big boys shutdown for the day.  
  
**Chartist** , again I hoping my coder can put the "second chance" feature in because the more chances you have the better, especially without having to increase the total drawdown even more. Let me know how the 17 sequence thing goes. If you do change the lot sizes, go ahead and plug those into the calculator first to make sure you get some profit at each level. Right now these are the only three I'm testing right now but I do have plans to try out Gbp/Jpy because that's the pair I trade the most with my PowerSwing strategy (hopefully you'll see that here shortly). Since I do run a business with my older brother I don't get to sit at my screen and trade during London or New York opens like I would like, that's what interested me in building this EA so I can set it and forget it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#40](/thread/post/1909036#post1909036 "Post Permalink")

  * Mar 18, 2008 1:21pm  Mar 18, 2008 1:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Mer, have you thought about trying this:   
  
Instead of closing out all the lots at TP, it closes out 1/2 of the lots and moves the stoploss to 75% of the TP. From here you could call it a day OR have it open the sequence again at the TP as long as the "time end" function is willing... I think you would have to limit the amount of sequences to 2 though. This may allow you to ride out the trend longer.  
  
Look forward to your input and everybody elses'! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#41](/thread/post/1909100#post1909100 "Post Permalink")

  * Mar 18, 2008 2:28pm  Mar 18, 2008 2:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Chartist, sounds interesting, but for now I will be concentrating on some solid forward testing with just the basic settingss right now to sort out all the bugs before I start experimenting around. I really do appreciate the suggestions, maybe yourself or someone else can play around with it some more to tweak it. The only thing I would be a little concerned about is moving the stop to 75% of your TP, your setting yourself up for an easy stopout. keep the ideas coming! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#42](/thread/post/1909640#post1909640 "Post Permalink")

  * Mar 18, 2008 9:25pm  Mar 18, 2008 9:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar21271_4.gif) Dreamliner](dreamliner)

  * Joined Oct 2006 | Status: Trader | [2,271 Posts](/search?do=process&provider=Member&searchuser=21271)

Mer, so if I set "80" in the "breakevenstop" it will be correct? I see default is "30".   
  

> [Quoting mer071898](/thread/post/1909015#post1909015 "View Quoted Post")
> 
> Disliked
> 
> **Dreamliner** , your welcome, I figured a video might be easier to understand. As for my breakeven setting I try to be at least 75% of the TP because if you happen to notice that the 61.8% fib level is 24-25 pips if it retraces. Now the GBP pairs will have an uncanny knack to retrace to the 76.4% more often so maybe stick to 80% of TP on those pairs. In post #22 I mentioned there might be a bug that's not letting the EA open immediate trade sequences with both settings to false but my coder is trying to catch up and look at it.  
>    
>  **damonl** , I didn't get in at 07:00 because my timed entry didn't open a sequence for some reason and I had to reopen my MT4 and change th entry time to get it to work correctly, another possible bug? I don't know yet.  
>    
>  **jones247** , Thanks for the support. I have no hard feelings or hatred towards FXTradepro, I just thought he went about thing the wrong way by promising a free EA then taking it away from the rest us on the forum because he decided to charge for it. And I agree, the drawdown sucks as you go deeper in the sequence, but that's why I added the breakeven function and the ability to stop trading after the big boys shutdown for the day.  
>    
>  **Chartist** , again I hoping my coder can put the "second chance" feature in because the more chances you have the better, especially without having to increase the total drawdown even more. Let me know how the 17 sequence thing goes. If you do change the lot sizes, go ahead and plug those into the calculator first to make sure you get some profit at each level. Right now these are the only three I'm testing right now but I do have plans to try out Gbp/Jpy because that's the pair I trade the most with my PowerSwing strategy (hopefully you'll see that here shortly). Since I do run a business with my older brother I don't get to sit at my screen and trade during London or New York opens like I would like, that's what interested me in building this EA so I can set it and forget it.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#43](/thread/post/1909924#post1909924 "Post Permalink")

  * Mar 18, 2008 11:38pm  Mar 18, 2008 11:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Hey Dreamliner, that field in the EA refers to PIPS not a percentage so, 75% of 30 pips is 20 pips. So, what goes in the field is 20.   
  
If your take profit field is 100 pips for example and you want your breakeven field to be 80%... you would enter 80 pips. (when the price reaches 80 pips, it will move your stop to break even). Hope that helps.  
  
  
Okay... here are the results for me today:  
  
eurusd: entered on "time" @8:00 gmt: tp reached on 9th trade at 10:19 london.  
  
usdchf: entered on "time" @8:00 gmt: tp reached on 2nd trade at 10:14 london.  
  
By the way, my end time was set for 18:00 gmt. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#44](/thread/post/1910126#post1910126 "Post Permalink")

  * Mar 19, 2008 12:56am  Mar 19, 2008 12:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar21271_4.gif) Dreamliner](dreamliner)

  * Joined Oct 2006 | Status: Trader | [2,271 Posts](/search?do=process&provider=Member&searchuser=21271)

Thank you for this information Chartist. I take it that you use half of the lots in the Excel sheet if you use two currencies? Or 1/4 the lots if you use 4?  
  

> [Quoting Chartist](/thread/post/1909924#post1909924 "View Quoted Post")
> 
> Disliked
> 
> Hey Dreamliner, that field in the EA refers to PIPS not a percentage so, 75% of 30 pips is 20 pips. So, what goes in the field is 20.   
>    
>  If your take profit field is 100 pips for example and you want your breakeven field to be 80%... you would enter 80 pips. (when the price reaches 80 pips, it will move your stop to break even). Hope that helps.  
>    
>    
>  Okay... here are the results for me today:  
>    
>  eurusd: entered on "time" @8:00 gmt: tp reached on 9th trade at 10:19 london.  
>    
>  usdchf: entered on "time" @8:00 gmt: tp reached on 2nd trade at 10:14 london.  
>    
>  By the way, my end time was set for 18:00 gmt.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#45](/thread/post/1910210#post1910210 "Post Permalink")

  * Mar 19, 2008 1:40am  Mar 19, 2008 1:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

No guys, you take 75% of your __**Take Profit level**__. The default level is already at that percentage. All you do is take you TP level and multiply it by 75% to get your BE level. For example we'll use 120 pip TP:  
  
120 TP x 75% = 90 pips BE  
  
The easiest way to manage your settings for different pairs is to set up the EA with the settings you want for that particular pair the save it. If you are doing multiple pairs on the same account you'll have to use an even # of pairs because trying to divide .1 lots by 3 might be a little tough ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1):. Dreamliner for example, on his $1000 account can always trade one currency using twice the nano lots shown in the spreadsheet or use the default lots on two pairs.   
  
  
  
Also here are my statements for Eur/Usd, Usd/Jpy, and Usd/Chf for 3/18/2008 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/96133?d=1205857405) 4 KB | 683 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#46](/thread/post/1910267#post1910267 "Post Permalink")

  * Mar 19, 2008 2:09am  Mar 19, 2008 2:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar21271_4.gif) Dreamliner](dreamliner)

  * Joined Oct 2006 | Status: Trader | [2,271 Posts](/search?do=process&provider=Member&searchuser=21271)

Ah, that makes sense, thanks for the clarification.  
  

> [Quoting mer071898](/thread/post/1910210#post1910210 "View Quoted Post")
> 
> Disliked
> 
> No guys, you take 75% of your __**Take Profit level**__. The default level is already at that percentage. All you do is take you TP level and multiply it by 75% to get your BE level. For example we'll use 120 pip TP:  
>    
>  120 TP x 75% = 90 pips BE  
>    
>  The easiest way to manage your settings for different pairs is to set up the EA with the settings you want for that particular pair the save it. If you are doing multiple pairs on the same account you'll have to use an even # of pairs because trying to divide .1 lots by 3 might be a little tough ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1):. Dreamliner for example, on his $1000 account can always trade one currency using twice the nano lots shown in the spreadsheet or use the default lots on two pairs.   
>    
>    
>    
>  Also here are my statements for Eur/Usd, Usd/Jpy, and Usd/Chf for 3/18/2008
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#47](/thread/post/1910339#post1910339 "Post Permalink")

  * Mar 19, 2008 2:38am  Mar 19, 2008 2:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

No problem, the best way to understand is to ask questions. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#48](/thread/post/1910836#post1910836 "Post Permalink")

  * Mar 19, 2008 6:06am  Mar 19, 2008 6:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar50293_23.gif) damonl](damonl)

  * Joined Oct 2007 | Status: I'm on a 10 year plan. | [4,309 Posts](/search?do=process&provider=Member&searchuser=50293)

Another successful night of trading this EA.  
  
Thanks for passing this on to us![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

"Keep your eyes on the helpers" - Mr. Rogers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#49](/thread/post/1911390#post1911390 "Post Permalink")

  * Mar 19, 2008 1:26pm  Mar 19, 2008 1:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Your welcome guys. And just let you know, it was recommended by one of the admins on another forum to add a cumulative statement as some people have provided falsified daily statements on his forum in the past and I want to make sure no one thinks I'm pulling the wool over anyones eyes. So I will be posting daily statements as usual along with a cumulative statement to show the total progress. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#50](/thread/post/1911456#post1911456 "Post Permalink")

  * Mar 19, 2008 3:08pm  Mar 19, 2008 3:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

R U guys going to continue trading as we approach Easter Weekend, you know with the possible declining volumes? I'm thinking about not trading until next week. What do you guys think? Easter is big in Europe. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#51](/thread/post/1911459#post1911459 "Post Permalink")

  * Mar 19, 2008 3:13pm  Mar 19, 2008 3:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I know I will be just to see how the EA reacts. since I mostly trade daily and weekly charts with my other strategy it won't affect me that much. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#52](/thread/post/1911479#post1911479 "Post Permalink")

  * Mar 19, 2008 3:41pm  Mar 19, 2008 3:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

> [Quoting mer071898](/thread/post/1911459#post1911459 "View Quoted Post")
> 
> Disliked
> 
> I know I will be just to see how the EA reacts. since I mostly trade daily and weekly charts with my other strategy it won't affect me that much.
> 
> Ignored

Yeah, will be interesting to see if it does the full sequence of trades... in my opinion if it doesn't this week (maybe early next week); odds are really in favor of it not hitting full range during normal trading conditions ever.  
  
So are you using PA and S/R levels? I sure do and take that into consideration on all my trades on all time frames. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#53](/thread/post/1911573#post1911573 "Post Permalink")

  * Mar 19, 2008 5:13pm  Mar 19, 2008 5:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar48267_23.gif) Oksana17](oksana17)

  * | Membership Revoked  | Joined Sep 2007 | [903 Posts](/search?do=process&provider=Member&searchuser=48267)

I've tried the exact same way of trading this way about a year ago or so...I made it up myself(author has same mind as me![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)), and one day...just one day...a bad day...your burn will happen. You will be sooooooo sad that you made profits for 3 years and burnt them ALL in 1 single night! Just wait and see...and please remember to remember my words!!!  
  
Peace! 

Request custom Expert Advisor or Indicator: dostapyuk "at" gmail . com

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#54](/thread/post/1911769#post1911769 "Post Permalink")

  * Edited 6:58pm  Mar 19, 2008 6:54pm | Edited 6:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here are the daily results for all three pairs along with cumulative statements as well for 3/19/2008.   
  
Chartist, I actually rely more on fibs and murrey math levels for my personal preference.   
  
Oksana17, There is no need to throw out warnings that there's "inevitable doom" on the horizon. We've already agreed there is a possibility to blow an account going thru a full sequence, but I'm sure everybody on these forums understands the risks they take with trading forex as well as those participating in this thread. That's why you should only trade with money you can afford to lose.   
  
What we're trying to do here is develop ways to minimize the risk and the losses as much as possible. If you do not want to throw out any helpful suggestions or constructive criticism, with no disrespect, please take the negativity to a different thread so we don't waste your time or our time, thanks. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/96332?d=1205920341) 9 KB | 554 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#55](/thread/post/1911840#post1911840 "Post Permalink")

  * Mar 19, 2008 7:19pm  Mar 19, 2008 7:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar50293_23.gif) damonl](damonl)

  * Joined Oct 2007 | Status: I'm on a 10 year plan. | [4,309 Posts](/search?do=process&provider=Member&searchuser=50293)

> [Quoting mer071898](/thread/post/1911769#post1911769 "View Quoted Post")
> 
> Disliked
> 
> Here are the daily results for all three pairs along with cumulative statements as well for 3/19/2008.   
>    
>  Chartist, I actually rely more on fibs and murrey math levels for my personal preference.   
>    
>  Oksana17, There is no need to throw out warnings that there's "inevitable doom" on the horizon. We've already agreed there is a possibility to blow an account going thru a full sequence, but I'm sure everybody on these forums understands the risks they take with trading forex as well as those participating in this thread. That's why you should only trade with money you can afford to lose.   
>    
>  What we're trying to do here is develop ways to minimize the risk and the losses as much as possible. If you do not want to throw out any helpful suggestions or constructive criticism, with no disrespect, please take the negativity to a different thread so we don't waste your time or our time, thanks.
> 
> Ignored

Same results as you for today. All three pairs winners and the won early in the rotation. That is what I like ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1).  
  
I will probably not trade on Friday or Monday with this method, however I will most likely keep my daily trades open as well. 

"Keep your eyes on the helpers" - Mr. Rogers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#56](/thread/post/1912813#post1912813 "Post Permalink")

  * Mar 20, 2008 3:16am  Mar 20, 2008 3:16am 

  * [ fewhills](fewhills)

  * | Joined Apr 2006  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=8448)

Nice system Mer.  
  
First off all: I understand the risks.  
  
I've tried it on a real account (nano's) today and it looked promising.  
GBPUSD, 5 min. No time or price entry. Nano lotsize.  
Break Even feature is great.  
1% increase in equity. Started system at 11:00 GMT. Then it just stopped at about 17:12 GMT. I don't know why.  
  
Can you give a clue Mer?  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#57](/thread/post/1912963#post1912963 "Post Permalink")

  * Edited 4:50am  Mar 20, 2008 4:40am | Edited 4:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Did it hit your take profit level or did it just stop in the middle of a sequence? If you can post your log maybe we can see what happened.  
  
And remember in post #22 I mentioned a possible bug we're trying to correct where the EA will sometimes not enter a sequence when the time and price entries are set to false. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#58](/thread/post/1913058#post1913058 "Post Permalink")

  * Mar 20, 2008 5:28am  Mar 20, 2008 5:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

I didn't trade today nor will I until Tuesday of next week, when I feel more comfortable with the market.  
  
happy trading and take care guys! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#59](/thread/post/1913065#post1913065 "Post Permalink")

  * Mar 20, 2008 5:31am  Mar 20, 2008 5:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Good job Damonl! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Hey Oksana, I don't think FX is for you ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#60](/thread/post/1913429#post1913429 "Post Permalink")

  * Mar 20, 2008 10:15am  Mar 20, 2008 10:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar21271_4.gif) Dreamliner](dreamliner)

  * Joined Oct 2006 | Status: Trader | [2,271 Posts](/search?do=process&provider=Member&searchuser=21271)

> [Quoting Chartist](/thread/post/1913065#post1913065 "View Quoted Post")
> 
> Disliked
> 
> Good job Damonl! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>    
>  Hey Oksana, I don't think FX is for you ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1).
> 
> Ignored

On the other hand, I, too, have serious concerns about any martinagle system, no matter how much the risk is reduced (as is with Merc's EA). People who have much experience trading will not touch any form of Martingale at all, believing it will do exactly as Oksana has said and eventually blow out the account.  
  
I remember one time reading about a man who was a gambler, and he stated that there were times when he would watch the ball end up on "green" over 30 times in a row.   
  
I myself did the d'lambert (a semi-martingale) method of trading on a live account, and it blew up the account in 3 months. I vowed never to trade that way again.  
  
Books on trading will tell you that any Martingale system will eventually destroy your account, unless you have infinite funds to keep from a margin call.  
  
Merc I'm not wanting to be negative, but I'm curious if you have read these things also, and what your thoughts on them might be. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#61](/thread/post/1913529#post1913529 "Post Permalink")

  * Edited 1:17pm  Mar 20, 2008 11:59am | Edited 1:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Yes, I've read numerous articles, posts, and comments about it but a lot of these strategies never took into consideration proper entries times, volatility, support and resistance, fibs, and other numerous factors that can drastically improve performance and reliable. I'm sure roulette players would drool if they knew their odds of winning would increase during certain hours of the day, I know I would.   
  
And like I've said before smart traders who use any sort of martingale systems or strategies only use them with money they can afford to lose, inherently know the risk, and never leave profits in the account.   
  
If I had $100,000 account I would trade a nano account with this in a heartbeat because I would never lose on it, why? I haven't figured it up but I figure I could go 100+ progressions before I would be margin called. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#62](/thread/post/1913721#post1913721 "Post Permalink")

  * Mar 20, 2008 2:41pm  Mar 20, 2008 2:41pm 

  * [ fewhills](fewhills)

  * | Joined Apr 2006  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=8448)

> [Quoting mer071898](/thread/post/1912963#post1912963 "View Quoted Post")
> 
> Disliked
> 
> Did it hit your take profit level or did it just stop in the middle of a sequence? If you can post your log maybe we can see what happened.  
>    
>  And remember in post #22 I mentioned a possible bug we're trying to correct where the EA will sometimes not enter a sequence when the time and price entries are set to false.
> 
> Ignored

My log is attached.   
  
Even if I reload the EA, it makes no difference. It just doesn't work any more. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [20080319.zip](/attachment/file/96634?d=1205991632) 2 KB | 434 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#63](/thread/post/1913741#post1913741 "Post Permalink")

  * Mar 20, 2008 3:16pm  Mar 20, 2008 3:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

> Quote
> 
> Disliked
> 
> And remember in post #22 I mentioned a possible bug we're trying to correct where the EA will sometimes not enter a sequence when the time and price entries are set to false.

If I were you I would hold off trading live until all the kinks are worked out. I sent your log to my coder I'm hoping he can figure it out for us soon. if you want in the mean time you can try out the EA using the timed or price entries to make sure those work as well, thanks. Let me know if you have any other problems. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#64](/thread/post/1913751#post1913751 "Post Permalink")

  * Mar 20, 2008 3:21pm  Mar 20, 2008 3:21pm 

  * [ fewhills](fewhills)

  * | Joined Apr 2006  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=8448)

> [Quoting mer071898](/thread/post/1913741#post1913741 "View Quoted Post")
> 
> Disliked
> 
> If I were you I would hold off trading live until all the kinks are worked out. I sent your log to my coder I'm hoping he can figure it out for us soon. if you want in the mean time you can try out the EA using the timed or price entries to make sure those work as well, thanks. Let me know if you have any other problems.
> 
> Ignored

OK, although best forward testing is with a live account (just nano's, and I know, it's money).  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#65](/thread/post/1913783#post1913783 "Post Permalink")

  * Mar 20, 2008 3:41pm  Mar 20, 2008 3:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I agree but I just don't like to see people lose money using an EA that is still being tested but I do appreciate the input especially on a live account as long as **your** OK with it. The only other thing I can suggest in the mean time while I'm waiting to hear back is to make sure you have the current MT4 build (213) and when you remove the EA make sure to restart your MT4 platform, then add the EA back on the chart. Also maybe try increasing your "ordertries" setting to 10 instead of 5 to give the EA more chances to enter orders when it receives an error code. These may or may not work so let me know. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#66](/thread/post/1913815#post1913815 "Post Permalink")

  * Mar 20, 2008 4:09pm  Mar 20, 2008 4:09pm 

  * [ fewhills](fewhills)

  * | Joined Apr 2006  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=8448)

> [Quoting mer071898](/thread/post/1913783#post1913783 "View Quoted Post")
> 
> Disliked
> 
> I agree but I just don't like to see people lose money using an EA that is still being tested but I do appreciate the input especially on a live account as long as **your** OK with it. The only other thing I can suggest in the mean time while I'm waiting to hear back is to make sure you have the current MT4 build (213) and when you remove the EA make sure to restart your MT4 platform, then add the EA back on the chart. Also maybe try increasing your "ordertries" setting to 10 instead of 5 to give the EA more chances to enter orders when it receives an error code. These may or may not work so let me know.
> 
> Ignored

No worries Mer, I am aware of that.  
As soon as I am back from my day job I will try the other things to get the EA running and that it does something again.  
I like your strategy and want to help improve it or at least give results. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#67](/thread/post/1913834#post1913834 "Post Permalink")

  * Mar 20, 2008 4:22pm  Mar 20, 2008 4:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Thanks for all the help!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#68](/thread/post/1914891#post1914891 "Post Permalink")

  * Mar 21, 2008 2:43am  Mar 21, 2008 2:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here are the daily and cumulative statements for all three pairs. Another successful night. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/96811?d=1206034924) 9 KB | 529 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#69](/thread/post/1914965#post1914965 "Post Permalink")

  * Mar 21, 2008 3:25am  Mar 21, 2008 3:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar21271_4.gif) Dreamliner](dreamliner)

  * Joined Oct 2006 | Status: Trader | [2,271 Posts](/search?do=process&provider=Member&searchuser=21271)

> [Quoting mer071898](/thread/post/1914891#post1914891 "View Quoted Post")
> 
> Disliked
> 
> Here are the daily and cumulative statements for all three pairs. Another successful night. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

I wonder why we wouldn't use this 24/7. Are we just trying to save a couple of entries during the slow times? I've been using it 24/7 (just set the "start" and "stop" time to 0) and it has made over 20% since Monday.  
  
I started it on a $1,000.00 demo account, so I used the nano spreadsheet and doubled the lots. However, then I decided to go with 2 currencies (Eur/Usd and Usd/Chf), and didn't take the time to set the lots back to where they should be. So in essence I have doubled the risk from the spreadsheet. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#70](/thread/post/1914978#post1914978 "Post Permalink")

  * Mar 21, 2008 3:36am  Mar 21, 2008 3:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

The problem is when I tried doing it 24/7 with the original FXTradepro EA it didn't take long before I hit a ranging period where the EA would go from sequence 1 to 16-17 in a matter of an hour. I'm not saying it can't be done but you are opening yourself up to a lot more risk during the ranging part of the day. So far I haven't gone past level 10 and I would prefer to keep it that way. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#71](/thread/post/1914990#post1914990 "Post Permalink")

  * Mar 21, 2008 3:47am  Mar 21, 2008 3:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar21271_4.gif) Dreamliner](dreamliner)

  * Joined Oct 2006 | Status: Trader | [2,271 Posts](/search?do=process&provider=Member&searchuser=21271)

Yes, that makes perfect sense. What time of the day do you trade (Eastern or GMT)?  
  

> [Quoting mer071898](/thread/post/1914978#post1914978 "View Quoted Post")
> 
> Disliked
> 
> The problem is when I tried doing it 24/7 with the original FXTradepro EA it didn't take long before I hit a ranging period where the EA would go from sequence 1 to 16-17 in a matter of an hour. I'm not saying it can't be done but you are opening yourself up to a lot more risk during the ranging part of the day. So far I haven't gone past level 10 and I would prefer to keep it that way.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#72](/thread/post/1915013#post1915013 "Post Permalink")

  * Mar 21, 2008 4:00am  Mar 21, 2008 4:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I am CMT which is GMT+6. I just leave the EA with the defaults which is 07:00 GMT which was the Frankfurt opening @ 01:00 my time, but since we are now in daylight savings time here, now 07:00 GMT is now the London open @ 02:00 my time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#73](/thread/post/1915562#post1915562 "Post Permalink")

  * Mar 21, 2008 10:13am  Mar 21, 2008 10:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar46327_4.gif) toshi](toshi)

  * Joined Aug 2007 | Status: Say what ? | [1,888 Posts](/search?do=process&provider=Member&searchuser=46327)

Mer,  
  
I've read your thread thru so far and watched your video.  
Listening to you, I can tell you're an intelligent man and you're  
taking this project seriously. I say project because, I too endeavored  
to "crack the code" on such a method by integrating statistical and  
probability study into the expert and believe me, it became a PROJECT.  
  
Yours is far less complicated and straightforward and simple is better.  
I believe choosing well timed entries is still the key to mitigating risk  
and keeping it under 10 bounces in a series, no matter the approach.  
  
Besides the video, I also viewed the statements. So far, this is good too.  
You are right on track and should make 2 to 3 percent per month with  
a fair degree of consistency. Natually, the risk is what the risk is and  
the "consistency" part only comes under attack when, for all your efforts  
to minimize the risks, they still pop up and put you to the test.  
  
I think this is EXACTLY why an automated execution of such a method is  
essential, because, after several bounces in a row and some decent  
drawdown, it's way too easy to lose your faith in between bounces and  
simply abandon the chase. My opinion from personal experience is to  
let the machine do its work. Win, Lose, or Draw. Tweak and test and  
continue to make improvements, but I think one should either automate or  
go back to manual, so as not to second guess the process in motion.  
Just my opinion.  
  
Now, having said that, and testifying to the fact that the method you're  
espousing has merit and can be profitable in the right hands, I have  
a much larger question for you. As I respect the work you've put into this   
and all the help you've offered to all of us here, I don't want you to be   
at all defensive if I ask this. Purely a thinking fellow's question:  
  
**Don't you think you need a good chunk of cash to do this the RIGHT WAY ?**  
  
Using $100,000 USD returning $500 to $1000 per week and quite possibly  
2 or 3 thousand a month is definately worth investigating. It could  
potentially replace the "9 to 5" income of many a working stiff.   
THIS IS POWERFUL and COULD CHANGE SOMEONE's LIFE.  
  
Would not want to discourage anyone from trying to get ahead, but  
do you think this is the BEST way to grow a smaller account of say   
$1,000 or so at the rate of 2 or 3 dollars a day ? It will take years.  
  
Granted, if it fails you'd be out 50K or 100K instead of 1K, but I cannot  
grow old trading nanos for the next 20 years with a only thousand bucks.  
Again, not to discourage, but do you think this is a good idea for small   
accounts compared to the reality of time it will take to make the compounding kick in ?  
  
Yes I know it's 25%- 35% per year. Account could triple inside 3 years.  
In ten years, assuming 2 percent/mo. compounded (and assuming no blow-out)  
it would grow by over 1,000 percent (play with the numbers).  
If it's $10,500 after ten years I don't care because I have starved to death  
waiting for the 17th bounce !!  
  
So, asked another way, Do you think, considering the time it takes this method  
to produce meaningful results, to trade this way on a 3 or 4 figure account  
is worth adopting or worth the effort ?  
  
After all that and trying to be careful not to offend you, if you get p*ssed  
for me asking, I'm going to give you a nuggie - right here on this forum.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
And by the way, Good Work. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#74](/thread/post/1915678#post1915678 "Post Permalink")

  * Mar 21, 2008 1:20pm  Mar 21, 2008 1:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Toshi, I fully agree with you 100% that a large amount of capital is truly needed to make this EA work to it's full potential. Granted there are only a few individuals on this forum that could possibly dump this much into an account in the first place let alone have the nerve to trade any type martingale or semi-martingale system. But keep in mind there are bank traders and fund managers using automated EA's for trading millions and millions of dollars daily, so the commercial aspect is always possible.   
  
But again, I believe that someone using this EA should also trade other strategies using this EA as a supplement to increase profits to reach that level where you can trade it solely on a larger account if so desired.   
  
My goal when I go live I will be funding about 10k and dumping all profits each month into my primary trading account which as of today is around 48-49k. By using the EA as a separate secondary trading income will help me produce a larger primary trading account, on which I can increase lot sizes faster, which in turn allows me to fund a larger EA account, which in turn...well, you get the idea.   
  
As FXTradepro stated numerous times in his original thread the the EA is just a tool and is not a substitute for proper trading techniques, analysis, and money management.  
  
As for me getting pissed off because someone, like yourself, has a meaningful opinion is crazy, I value every opinion placed on this thread and don't ever feel that you would offend me. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#75](/thread/post/1915731#post1915731 "Post Permalink")

  * Mar 21, 2008 3:25pm  Mar 21, 2008 3:25pm 

  * [ fewhills](fewhills)

  * | Joined Apr 2006  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=8448)

I forgot to switch off the EA when I went to work. When I got back home I saw it still was running. It blew up my nano account. Yes, one must have a huge account...  
There was a trading range in the GBPUSD from 12:00 to 13:30 GMT (March 20th) of about 20 pips. It took up to 23 trades.  
I didn't expect it so soon, because I wanted to tweak the parameters, but unfortunately it did happen.   
Still like the system. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#76](/thread/post/1916255#post1916255 "Post Permalink")

  * Mar 22, 2008 12:35am  Mar 22, 2008 12:35am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Good intro for the 'ol Martingale discussion! Already stated earler... I too am an ex-D'Alembert trader. This approach here is more conservative, and one thing I like is that it sequences relatively quickly! But, as in all progressive lot systems, it all depends on the percentages of the system. All gaming-based discussions of PLM (progressive lot managment) have pretty much fixed percentages, by game. We don't have that luxury, which can be both good and bad. The better the edge we have, the more successful our PLM will be. But, we don't really know what the future will bring. Vegas does. The roulette wheel will cough up the same house win% today as it did yesterday, and will tomorrow, next week, and next year.   
  
So, as Mer said, previous analysis/discussion of PLM based on data from gaming is of limited use to us. Interesting, but not really applicable. We have a BIG advantage in that we can control our entry, our time-of-day (volatility) etc. This particular method is interesting because it is based on the premise that we will hit a minimum 50p run sometime in 20 or so trades. We can further increase our "odds" so to speak by selected WHEN we start this run. As above, start it at the wrong time, and you blow your account. But looking at past charting, trading the EU on the European session, on non-holidays (today would have been a bad day to trade, for example...), there has ALWAYS been at least 50p movement in the session. (I say 50p because I am assuming we are short, and the market moves long and hits our SL at -10p, then we go long, so we need another 40p to win, total 50p... plus spread...)  
  
We can further help ourselves by trying to get our first trade right! (which is what everybody does... but for us, it really doesn't matter!! )   
  
Oh... and it actually is very easy to trade the EA entry per our own indicators, without having to deal with the false-false bug. Set the EA on timed Entry, with your session time values, and set to trade long or short first depending on your analysis, but click the "OFF" button for the EA, so you have an X where the smiley face would be. EA is applied and everything,... then, watch your charts... when your indicator says go, you simply click the "ON" button for the EA,... your EA verifies that you are within your set trading session.. (kind of a nice check...) and boom, enters you long or short on the next tick, according to how you set the EA up. Actually, I like this better than trading False-False, because 1) you get a check on the session times so you don't enter a sequece outside your plan, and 2) you get the End-time limit as well.  
  
Anyway, all the above, plus good MM can make this a very viable system... (I think!!) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#77](/thread/post/1916409#post1916409 "Post Permalink")

  * Edited 8:22am  Mar 22, 2008 3:10am | Edited 8:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

fewhills, that's why I don't trade Gbp/Usd (or Gbp/Jpy or Gbp/Chf) because of their volatility. These pairs can easily range 20-30 pips before any kind of breakout can occur, using less than a 20-30 pip stop is asking for trouble. Also being Easter weekend I wouldn't have traded due to the expected low volume. Again, this is why I strongly suggest not trading live until the EA is properly tested. Just don't get discouraged over it though, maybe just stay with the pairs for live trading then test out the other pairs on a demo account. I know on the original thread they were having good success on Eur/Jpy with 100/75/25 and Gbp/Jpy with 140/105/35.  
  
Glad to have you here mrkam, the more the merrier.  
  
As expected my trades are on hold because of the ranging but since but these pairs are more stable than Gbp/Usd and my trading was stopped at 17:00 GMT, I'm not anywhere near level 23 as in the pictures. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [pics.zip](/attachment/file/97032?d=1206122928) 202 KB | 623 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#78](/thread/post/1916485#post1916485 "Post Permalink")

  * Mar 22, 2008 4:33am  Mar 22, 2008 4:33am 

  * [ Middleastern](middleastern)

  * | Joined Jan 2008  | Status: Trader | [207 Posts](/search?do=process&provider=Member&searchuser=58537)

First of all, wanted to thank everyone of you for your contributions. Just found this thread while thinking in a very similar direction.  
  
The SL and TP settings obviously must be customized to each particular pair, according to the latest volatility. In my view, a 40-pip TP is too high, and that is what leads to reaching the 10th+ level. A narrow TP I think will reduce the number of levels reached.  
  
As I see it, a good entry only saves us one level, nothing more. A wrong entry will shortly be reversed, thus getting us into the appropriate direction. Unless... we are in a range, but a system like this is based on the assumption that we cannot predict neither a trend nor a range.  
  
Where I want to get here? A 24/5 robot with tight TP's and SL's, always with one trade open. If TP is hit, then a new trade in the same direction is opened. SL hit, then SAR. Suitable pairs are those with tight [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") and high volatility, and the calculation of the SL and TP should be done in addition of the spread.  
I still didn't tried Mer's EA, but will start next Monday and post my results stating the used settings, so we can compare and optimize.   
  
One question: Once a trade is closed, either at the SL or TP, does the EA open an additional trade, or you should wait to the next day/candle/manual order?  
  
Two problems to deal with here: News times and spread widening done by the broker. Trade must be disabled during major news releases (let's say 1 hour before and 2 hours after, just to make sure not to catch a spike, or a spike to catch us, that is).   
As someone said in the other thread, brokers widen the spreads from time to time to screw people trading these kind of systems. Ideally, the EA should have a safety lock, disabling trading when the spread > X pips.  
  
Another problem I see: When in a strong trend, we would be opening and closing trades in the same direction, thus paying spreads that otherwise we would be earning ourselves. I am thinking in a way to optimize the earnings here, but any comments will be warmly welcome.  
  
Well, sorry for the long post, but my head has been bubbling these last days...  
  
Regards,  
  
Middleastern 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#79](/thread/post/1916629#post1916629 "Post Permalink")

  * Mar 22, 2008 8:06am  Mar 22, 2008 8:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

> Quote
> 
> Disliked
> 
> The SL and TP settings obviously must be customized to each particular pair, according to the latest volatility. In my view, a 40-pip TP is too high, and that is what leads to reaching the 10th+ level. A narrow TP I think will reduce the number of levels reached.

Middleastern, everyone will have different opinions on TP and stops, that's the reason I put up the EA for everyone so they can play with it as much as they want. With regards to TP and stoploss if you take the calculator on post #1 you can put in whatever TP and stoploss you want and see where your profits will end up. I, personally, have had no trouble so far reaching 40 pip TP profit levels on any pair I'm trading yet. The EA uses a 4-1 TP to stop ratio and specific lot increment sizes that has been tested to ensure you have a profit no matter what level your TP is hit at (again, play with the calculator) When you start reducing TP levels you must lower your stop to match, thus increasing your risk to being stopped out way too often especially in a sideways ranging market like today as fewhills found out. Also trading highly volatile pair like Gbp/Usd, Gbp/Jpy, or Gbp/Chf makes you more prone to stronger whipsaws and thus more stops being hit. In order to use this EA it's all about control, using controllable pairs, controlling entry points and times, and controlling your money management. as said before the EA is just a tool that you are in **control** of, not the other way around.   
  

> Quote
> 
> Disliked
> 
> One question: Once a trade is closed, either at the SL or TP, does the EA open an additional trade, or you should wait to the next day/candle/manual order?

The EA only opens a new trade in the opposite direction when the stop is triggered. When the EA hits it's TP the sequence stops and will not start until the next time or price is reached (if you use the time or price entry). The EA is suppose to enter trades immediately on the next tick when placed on the chart if both settings are set to false but currently there is a bug (which is be looked at by my coder) that's causing it not to enter trades.  
  
  

> Quote
> 
> Disliked
> 
> Two problems to deal with here: News times and spread widening done by the broker. Trade must be disabled during major news releases (let's say 1 hour before and 2 hours after, just to make sure not to catch a spike, or a spike to catch us, that is).   
>  As someone said in the other thread, brokers widen the spreads from time to time to screw people trading these kind of systems. Ideally, the EA should have a safety lock, disabling trading when the spread > X pips.

The EA does have an input for slippage built in and an "ordertries" function to help with news events and spikes. Besides you can always turn off the EA during these times by clicking on the "Expert Advisors" button.   
  

> Quote
> 
> Disliked
> 
> Another problem I see: When in a strong trend, we would be opening and closing trades in the same direction, thus paying spreads that otherwise we would be earning ourselves. I am thinking in a way to optimize the earnings here, but any comments will be warmly welcome.

Since you haven't used the EA yet you should understand the EA will open a position and if stopped out will open a new trade in the sequence in the **opposite** direction. Before you start using it I would suggest reading through the original thread on post #1 to get more info about the concept of what the EA does and how the calculator works to help you out. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#80](/thread/post/1916647#post1916647 "Post Permalink")

  * Mar 22, 2008 8:40am  Mar 22, 2008 8:40am 

  * [ Middleastern](middleastern)

  * | Joined Jan 2008  | Status: Trader | [207 Posts](/search?do=process&provider=Member&searchuser=58537)

Thanks for taking the time to answer all that ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
I'll start using the EA this week, and I'm sure things will get clearer. I was just trying to adapt the EA features to what I had in mind, which is a little different of what was proposed here. Anyway, I'm eager to see the EA in action, anyway...  
  
Thanks again, Mer  
  

> [Quoting mer071898](/thread/post/1916629#post1916629 "View Quoted Post")
> 
> Disliked
> 
> Middleastern, everyone will have different opinions on TP and stops, that's the reason I put up the EA for everyone so they can play with it as much as they want. With regards to TP and stoploss if you take the calculator on post #1 you can put in whatever TP and stoploss you want and see where your profits will end up. I, personally, have had no trouble so far reaching 40 pip TP profit levels on any pair I'm trading yet. The EA uses a 4-1 TP to stop ratio and specific lot increment sizes that has been tested to ensure you have a profit no matter what level your TP is hit at (again, play with the calculator) When you start reducing TP levels you must lower your stop to match, thus increasing your risk to being stopped out way too often especially in a sideways ranging market like today as fewhills found out. Also trading highly volatile pair like Gbp/Usd, Gbp/Jpy, or Gbp/Chf makes you more prone to stronger whipsaws and thus more stops being hit. In order to use this EA it's all about control, using controllable pairs, controlling entry points and times, and controlling your money management. as said before the EA is just a tool that you are in **control** of, not the other way around.   
>    
>  The EA only opens a new trade in the opposite direction when the stop is triggered. When the EA hits it's TP the sequence stops and will not start until the next time or price is reached (if you use the time or price entry). The EA is suppose to enter trades immediately on the next tick when placed on the chart if both settings are set to false but currently there is a bug (which is be looked at by my coder) that's causing it not to enter trades.  
>    
>    
>  The EA does have an input for slippage built in and an "ordertries" function to help with news events and spikes. Besides you can always turn off the EA during these times by clicking on the "Expert Advisors" button.   
>    
>  Since you haven't used the EA yet you should understand the EA will open a position and if stopped out will open a new trade in the sequence in the **opposite** direction. Before you start using it I would suggest reading through the original thread on post #1 to get more info about the concept of what the EA does and how the calculator works to help you out.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#81](/thread/post/1916707#post1916707 "Post Permalink")

  * Mar 22, 2008 10:59am  Mar 22, 2008 10:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Hey, no problem, feel free to throw out ideas here. I want this thread to try and be as constructive as possible. I would like to see others demo different pairs and if changes need to be made I'll look into it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#82](/thread/post/1916777#post1916777 "Post Permalink")

  * Mar 22, 2008 5:14pm  Mar 22, 2008 5:14pm 

  * [ Middleastern](middleastern)

  * | Joined Jan 2008  | Status: Trader | [207 Posts](/search?do=process&provider=Member&searchuser=58537)

Mer, any chance of putting an option to let the EA open a new trade, in the same direction, when a TP is hit? I understand you are opening just one sequence per day and per pair. Is that right? I'm thinking on several trades a day, maybe during the full London and US sessions, for instance...  
  
Could you tell me what the OrderTries and slippage options do exactly?  
  
Thanks a lot  
  

> [Quoting mer071898](/thread/post/1916707#post1916707 "View Quoted Post")
> 
> Disliked
> 
> Hey, no problem, feel free to throw out ideas here. I want this thread to try and be as constructive as possible. I would like to see others demo different pairs and if changes need to be made I'll look into it.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#83](/thread/post/1917289#post1917289 "Post Permalink")

  * Mar 23, 2008 2:45pm  Mar 23, 2008 2:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Unfortunately, I cannot make any changes unless the person wanting the changes pays me to have my coder do so, and he is not cheap. You can always change the start time or price and re-enter after each sequence.  
  
Slippage is the difference between the price you're quoted and the price you get filled at and the ordertries function allows the EA to resend orders if there are any errors. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#84](/thread/post/1917298#post1917298 "Post Permalink")

  * Mar 23, 2008 3:19pm  Mar 23, 2008 3:19pm 

  * [ Middleastern](middleastern)

  * | Joined Jan 2008  | Status: Trader | [207 Posts](/search?do=process&provider=Member&searchuser=58537)

Ok, thanks for answering.   
  
  
  

> [Quoting mer071898](/thread/post/1917289#post1917289 "View Quoted Post")
> 
> Disliked
> 
> Unfortunately, I cannot make any changes unless the person wanting the changes pays me to have my coder do so, and he is not cheap. You can always change the start time or price and re-enter after each sequence.  
>    
>  Slippage is the difference between the price you're quoted and the price you get filled at and the ordertries function allows the EA to resend orders if there are any errors.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#85](/thread/post/1917325#post1917325 "Post Permalink")

  * Mar 23, 2008 4:54pm  Mar 23, 2008 4:54pm 

  * [ Middleastern](middleastern)

  * | Joined Jan 2008  | Status: Trader | [207 Posts](/search?do=process&provider=Member&searchuser=58537)

Just one thought about the never-ending Martingale pros and cons discussion: Why not putting a "disaster stop" in the form of a limited number of re-entries? Let's say 10 (just tossing a number here). This would equal to a certain value in $. This way, in a ranging market that may be disastrous for this system, we end up with a certain, controlled loss, that should be taken as part of the business (like in any other system), but we will still have an account to trade with.  
  
Comments? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#86](/thread/post/1917473#post1917473 "Post Permalink")

  * Mar 23, 2008 11:25pm  Mar 23, 2008 11:25pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

Started forward testing on Wednesday night allowing only short trades on 5 majors pairs and profit of over 200 so far. My thinking is that ranges will kill this accout so allowing shorts only should help. Will keep you posted. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#87](/thread/post/1917714#post1917714 "Post Permalink")

  * Mar 24, 2008 5:14am  Mar 24, 2008 5:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Middleastern, the hard part is how do we know when price will break out? What happens when we put a "disaster stop" in then price breaks out immediately after? Do I really want to stomach the loss? As I said before that is basically why I trade only during those hours between 07:00 to 17:00 GMT to make sure I have the volatility I need and if I feel I'm hitting a ranging period within those hours, I'll just turn my EA off.  
  
qz10cq, I don't understand, are you starting the with the first long set to false or are you manual putting in shorts only and not letting the EA alternate trades. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#88](/thread/post/1917868#post1917868 "Post Permalink")

  * Mar 24, 2008 8:32am  Mar 24, 2008 8:32am 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting mer071898](/thread/post/1917714#post1917714 "View Quoted Post")
> 
> Disliked
> 
> qz10cq, I don't understand, are you starting the with the first long set to false or are you manual putting in shorts only and not letting the EA alternate trades.
> 
> Ignored

Expermenting with the ea, went to ea properties/common and set it to short only. The idea behind this is to trade only in the direction of a longer TF. Seems to be working with ur ea but I have only traded this for a few days and it was a sideways market. Will keep you posted. Nice ea. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#89](/thread/post/1917969#post1917969 "Post Permalink")

  * Mar 24, 2008 10:58am  Mar 24, 2008 10:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I see, interesting approach. Keep us updated on how it works out for you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#90](/thread/post/1918001#post1918001 "Post Permalink")

  * Edited Mar 25, 2008 3:05am  Mar 24, 2008 12:17pm | Edited Mar 25, 2008 3:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Happy Easter!  
  
(\ /)  
( **. .**)  
c(')(')  
  
Just wanted to update everyone, my Eur/Usd trade sequence from Friday 3/21/2008 did close when trading resumed tonight with the gap and spike down ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) and the Usd/Jpy and Usd/Chf trades that were in progress when the market closed on Friday were stopped out and we'll see how they continue tonight when the EA restarts them at 07:00 GMT. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [ODL Statements.zip](/attachment/file/97429?d=1206381888) 5 KB | 409 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#91](/thread/post/1919072#post1919072 "Post Permalink")

  * Mar 25, 2008 5:55am  Mar 25, 2008 5:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Hey guys, sorry I'm a little late today with results. Eur/Usd for 3/24/2008 finished pretty quickly (which is OK by me!) and the Usd/Jpy and Usd/Chf sequences from Friday, 3/21/2008 finished up their run this morning as well. It's good to see the timed entry is working smoothly and kept me out of trouble during the low volatility over the holiday weekend. I was expecting to go deeper in the run but a little more volume on Monday morning did kinda surprise me.  
  
Well, so far so good. Eur/Usd hasn't gone past level 10, Usd/Jpy hasn't gone past level 7, and Usd/Chf hasn't gone past level 10 as well. But there's still a long way to go before we're done testing. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [ODL Statements.zip](/attachment/file/97461?d=1206392122) 11 KB | 376 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#92](/thread/post/1919450#post1919450 "Post Permalink")

  * Mar 25, 2008 11:38am  Mar 25, 2008 11:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Just to let everyone know I reached my coder and he is going to look at the bug and get back to me shortly. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#93](/thread/post/1920127#post1920127 "Post Permalink")

  * Mar 25, 2008 9:44pm  Mar 25, 2008 9:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

NIIIICE! Whats up Mer? Are you also going to have him look at the break even/repeat last trade feature?  
  
I'm going to start my trading week this coming London session. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#94](/thread/post/1920292#post1920292 "Post Permalink")

  * Mar 25, 2008 11:28pm  Mar 25, 2008 11:28pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting Chartist](/thread/post/1920127#post1920127 "View Quoted Post")
> 
> Disliked
> 
> NIIIICE! Whats up Mer? Are you also going to have him look at the break even/repeat last trade feature?  
>    
>  I'm going to start my trading week this coming London session.
> 
> Ignored

  
I was experimenting with only short trades and it didn't work. EA only opened the one short trade and would not repeat. Agree with Chartist, this ea would be safer with those issues addressed. Still experimenting with ea, I like it, especially the progression. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#95](/thread/post/1920306#post1920306 "Post Permalink")

  * Mar 25, 2008 11:34pm  Mar 25, 2008 11:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

What do you mean with "only short trades"? That's not possible. It's a stop and reverse system...  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#96](/thread/post/1920377#post1920377 "Post Permalink")

  * Mar 26, 2008 12:07am  Mar 26, 2008 12:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar5983_4.gif) tsimic6](tsimic6)

  * | Joined Feb 2006  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=5983)

Ok Guys, a word from me. This seem to be a nice system. I will stick to it and test it for a while. I've just put an EA to my demo account, with Time and price set to false. It opened a position immediately. This function is working properly on my account. 

Gutenberg money printing machine

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#97](/thread/post/1920410#post1920410 "Post Permalink")

  * Edited 12:43am  Mar 26, 2008 12:24am | Edited 12:43am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

I think the only "bug" is if both Price and Time are set to false... Price:false and Time:true has worked great for me too....  
  
Edit: deleted discussion about trading the UJ starting at 1200 or 1300 gmt.. I had my time set wrong last night, which is why I got the 8-trade sequence... set properly, would have been less... still, 8 trades is just fine!  
  
And.... funny that the "sweet spot" in this system is right in that 7-12 trade sequence range.. If we hit every trade the first time, the gains are very small... if we hit the 18th or 20th trade, we get a MUCH larger gain, but one HECK of a drawdown... so really, we do better at 7-12 trade sequence, but we have to be able to "stomach" the drawdown...   
  
I tried to re-structure the lot sizes to ALWAYS get say, a $20 gain trading micros, and while that is quite easy to do, (thanks to the spreadsheet!!), it results in a larger drawdown progression than the "default"... but, on the other hand, every trade's gain is consistent... always about $20, regardless of the trade sequence, which has some merit,, maybe...  
  
thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#98](/thread/post/1920418#post1920418 "Post Permalink")

  * Mar 26, 2008 12:27am  Mar 26, 2008 12:27am 

  * [ saragosa](saragosa)

  * | Joined Sep 2006  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=19601)

can it start from 0,01 lot? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#99](/thread/post/1920463#post1920463 "Post Permalink")

  * Mar 26, 2008 12:48am  Mar 26, 2008 12:48am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Yes.... you just have to edit the inputs, toward the bottom, where it lists the lot sizes & progression. It is set by default to a mini lot: .1;.1;.2 etc... just change it to: .01;.01;.02 etc. In fact, you can change it to whatever size sequence you want! like .02;.02..03;.05... just for example. So, you can play with the spreadsheet to get the profit/drawdown progression you want to see, and list those lot sizes into that input, and you are off an running..  
  
VERY nice feature, good, solid EA....  
  
I second (third, fourth... ) the idea of adding a "re-trade" function that would re-enter the sequence at the SAME lot size IF the trade stops out at the breakeven point....   
  
The False:False bug is not a big deal, but should be addressed in the interest of cleaning up the code... very cool.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#100](/thread/post/1920577#post1920577 "Post Permalink")

  * Mar 26, 2008 1:47am  Mar 26, 2008 1:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

> [Quoting qz10cq](/thread/post/1920292#post1920292 "View Quoted Post")
> 
> Disliked
> 
> I was experimenting with only short trades and it didn't work. EA only opened the one short trade and would not repeat. Agree with Chartist, this ea would be safer with those issues addressed. Still experimenting with ea, I like it, especially the progression.
> 
> Ignored

  
huh? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#101](/thread/post/1920588#post1920588 "Post Permalink")

  * Mar 26, 2008 1:54am  Mar 26, 2008 1:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar49771_4.gif) fireeee](fireeee)

  * | Joined Sep 2007  | Status: No pain, no gain! | [29 Posts](/search?do=process&provider=Member&searchuser=49771)

You are so going down.Thats a test from the beginning of the year.I wish you luck.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: TesterGraph.gif
Size: 10 KB](/attachment/image/97702/thumbnail?d=1365540174)](/attachment/image/97702?d=1206464000)   

Bulls Make Money, Bears Make Money, Pigs Get Slaughtered

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#102](/thread/post/1920607#post1920607 "Post Permalink")

  * Mar 26, 2008 2:03am  Mar 26, 2008 2:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Mer knows what I'm talking about and the rest of you who have read all of the this thread but in the interest of getting some of you up to speed; what I meant:  
  
When your trade gets stopped out at break even right now what is happening is the trade progression keeps going within the EA and it will open up the next trade ratcheting up the amount of lots even though there was no loss on that break-even trade.  
  
So the feature proposed by Mer was to have his coder work on a solution where if there is a break-even trade, then the sequence is not continued on the next trade but rather repeats the last lots traded.... in a sense giving you a second opportunity at that lot level.  
  
So.... hypothetical trade sequence if and when the feature is added:  
  
1st trade: .1 lots stopped out  
2nd trade: .1 lots stopped out  
3rd trade: .2 lots (stopped out at break-even)  
4th trade: **.2 lots again instead of .3(or whatever comes next) because last trade was B/E.**  
**and the sequence continues normally unless either Break even is hit or TP!**  
  
**Good trading everyone!**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#103](/thread/post/1920780#post1920780 "Post Permalink")

  * Mar 26, 2008 3:41am  Mar 26, 2008 3:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

My coder is looking to clear up any problems with any "false-false" issues and yes Chartist, he is going to look into adding the re-enter feature to help extend the functionality of the EA.  
  
fireeee, you can't base you opinion on a backtest because there are so many variable to consider like entry points, time of day, and numerous other factors which backtesting doesn't take into consideration.  
  
What qz10cq did was change the input under the commons tab on the EA to trade only short instead of long & short. Remember it doesn't hurt to experiment ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#104](/thread/post/1920822#post1920822 "Post Permalink")

  * Mar 26, 2008 4:10am  Mar 26, 2008 4:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I don't know what happened last night but my EA didn't open up my trades on Usd/Jpy or Usd/Chf. Looks to me like a login issue. My Eur/Usd is still trading at the moment and will probably continue tomorrow morning. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [log 3252008.zip](/attachment/file/97738?d=1206472048) < 1 KB | 328 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#105](/thread/post/1921350#post1921350 "Post Permalink")

  * Mar 26, 2008 11:40am  Mar 26, 2008 11:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Just an update, my Eur/Usd finished up this morning around 15:40 GMT for a nice $460.00 dollar profit with 2 breakeven saves which would have cost me $170.00 in profit (.6 & 1.1 lot levels). I'm glad I added that in now. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/97815?d=1206499203) 5 KB | 352 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#106](/thread/post/1921405#post1921405 "Post Permalink")

  * Edited 12:58pm  Mar 26, 2008 12:44pm | Edited 12:58pm 

  * [ BGazzoni](bgazzoni)

  * | Joined Sep 2006  | Status: $/pip | [162 Posts](/search?do=process&provider=Member&searchuser=20331)

> [Quoting Chartist](/thread/post/1913065#post1913065 "View Quoted Post")
> 
> Disliked
> 
> Good job Damonl! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>    
>  Hey Oksana, I don't think FX is for you ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1).
> 
> Ignored

Chartist... I think everyone has already tried this strategy and i don't see any veteran using it, and none of them even mention this, cause they know what happens... Maybe you should try to learn more before saying thinks like that to someone who might knows more than you (and i really, really think he does).  
  
Mer congrats in putting efforts on this thread and sharing the EA for free.. But i really don't know why you put an expiration date if you don't plan to sell it.. I read the posts, but I think that in a year you won't even gonna remmember that you started this thread. It's just a thought...  
  
BTW i do martingale sometimes... But in my discretionary trades, cause i think i won't be able to be wrong more than 2 times in a row, and if i do i'll take the loss... And it's not a stop and reverse thing 

No Brain, no Gain.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#107](/thread/post/1921459#post1921459 "Post Permalink")

  * Mar 26, 2008 2:14pm  Mar 26, 2008 2:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

BGazzoni, As always your opinions are welcome here in the thread and Chartist's comments are just that, his opinion.  
  
Again, I try to stress to everyone the EA that this not designed to be an all in one solution for trading Forex but to be used in conjunction with other trading strategies and to be used as a supplemental tool to help increase ones primary trading account. As suggested before, you should always use this on a secondary account that is using "expendable money"and remove the profits you've accumulated frequently and put those profits in your primary account.  
  
As for the expiration date, it's a courtesy for those of us who **do** have an interest in this EA, but don't want to keep downloading a new one every month like in the original thread. And you're right, this thread probably won't be here in a year, but when it does expire, the EA will provide a message to the forum members so they can e-mail for a new one if they want it.   
  
As I stated in post #1, I will be marketing the EA commercially **outside of this site** after proper testing, which is the main goal of posting this EA on the forum. I will still be providing this EA for free to all registered members of this forum. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#108](/thread/post/1921463#post1921463 "Post Permalink")

  * Mar 26, 2008 2:18pm  Mar 26, 2008 2:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar48267_23.gif) Oksana17](oksana17)

  * | Membership Revoked  | Joined Sep 2007 | [903 Posts](/search?do=process&provider=Member&searchuser=48267)

> [Quoting Chartist](/thread/post/1913065#post1913065 "View Quoted Post")
> 
> Disliked
> 
> Good job Damonl! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>    
>  Hey Oksana, I don't think FX is for you ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1).
> 
> Ignored

wow...i' m not even gonna say anything. ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)  
  
just asking, how long have YOU been trading forex? Just curious...![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Request custom Expert Advisor or Indicator: dostapyuk "at" gmail . com

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#109](/thread/post/1921465#post1921465 "Post Permalink")

  * Edited 2:25pm  Mar 26, 2008 2:23pm | Edited 2:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Unlike other threads, I don't want the negativity here guys. If you want to bad mouth each other do it with pm's.  
  
Oksana, I do appreciate your concerns, we are all aware of the risk involved. That's why we trying to make improvements to eliminate as much risk as possible 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#110](/thread/post/1921928#post1921928 "Post Permalink")

  * Mar 26, 2008 8:44pm  Mar 26, 2008 8:44pm 

  * [ saragosa](saragosa)

  * | Joined Sep 2006  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=19601)

Hello  
i change lots from 0,01, i have been wait for more 4 hours, but there is no open position, what happen? is there something wrong? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#111](/thread/post/1922207#post1922207 "Post Permalink")

  * Mar 26, 2008 11:22pm  Mar 26, 2008 11:22pm 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

ummm... I noticed you use european form, 0,01. The EA is written in formal decimal, 0.01.... so if you input 0,01 in the EA lots input, it probably won't recognize it as a number, and hence, won't trade?? just a thought...  
  
Ditto on the bashing, Mer. Many of us have traded FX for a whiles, and some even make their living on it. You have provided enough caveats, no more really needed. There is always risk. Even with the "pros". This just provides a different version of that risk, and as with ALL systems, it is all a game of probabilities and percentages... all we want is an edge... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#112](/thread/post/1922292#post1922292 "Post Permalink")

  * Mar 27, 2008 12:01am  Mar 27, 2008 12:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

> [Quoting BGazzoni](/thread/post/1921405#post1921405 "View Quoted Post")
> 
> Disliked
> 
> Chartist... I think everyone has already tried this strategy and i don't see any veteran using it, and none of them even mention this, cause they know what happens... Maybe you should try to learn more before saying thinks like that to someone who might knows more than you (and i really, really think he does).  
>    
>  Mer congrats in putting efforts on this thread and sharing the EA for free.. But i really don't know why you put an expiration date if you don't plan to sell it.. I read the posts, but I think that in a year you won't even gonna remmember that you started this thread. It's just a thought...  
>    
>  BTW i do martingale sometimes... But in my discretionary trades, cause i think i won't be able to be wrong more than 2 times in a row, and if i do i'll take the loss... And it's not a stop and reverse thing
> 
> Ignored

Your opinions are appreciated! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#113](/thread/post/1922293#post1922293 "Post Permalink")

  * Mar 27, 2008 12:02am  Mar 27, 2008 12:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

> [Quoting Oksana17](/thread/post/1921463#post1921463 "View Quoted Post")
> 
> Disliked
> 
> wow...i' m not even gonna say anything. ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)  
>    
>  just asking, how long have YOU been trading forex? Just curious...![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

  
Your opinions are appreciated! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#114](/thread/post/1922323#post1922323 "Post Permalink")

  * Mar 27, 2008 12:22am  Mar 27, 2008 12:22am 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

Mer, put in stop and break even at 60, profit 350 with progression of .1, .2 thru 1.0. Positive around 600 pips so far this week. With the 60 break even the trades close when the price retracts 60 and then opens another trade at .1 as long as it is positive . Trading pairs are eur/usd. gbp/usd, usd/chf, usd/jpy and gbp/jpy. I also attached a close all orders ea when price hits 400, which it has twice this week. This is more of a weekly type system, with the 60 sl it takes away most of the trending market problems. If u look at weekly charts there is a lot of pips to be gotten from the opens to the close/high/low, just how to get them is the question. Love the idea of opening a channel at the beginning of the week and just keep refilling the orders until there is a major move of some sort for ur profit. With the close all orders ea at 400 it resets all trading pairs back to .1. Still experimenting with this ea and I like it, will keep u informed. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#115](/thread/post/1922324#post1922324 "Post Permalink")

  * Mar 27, 2008 12:24am  Mar 27, 2008 12:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Okay another profitable London session with your EA Mer.  
  
My usd/chf trade closed out on the first trade with +44 pips. I'm trading this pair with 44tp, 10sl, 25be.   
  
Good trading to all of you! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#116](/thread/post/1922735#post1922735 "Post Permalink")

  * Edited 5:24am  Mar 27, 2008 4:22am | Edited 5:24am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

QZ: Interesting! are you using this EA to do that? If so, can you elaborate on your settings.... sounds like your "close all" is another EA?  
  
To all: Looks to me like that all of our sequence-ending trades at 40p profit ALL go onto much more, but AT LEAST 60-70p.... Wouldn't it significantly help us to set our TP at 60, 10p SL still, and 30p breakeven still...  
  
If we do that, and leave the default progression the same thru the first 12 trades... (the majority of sequences will end before 12 trades), we make more money, by a bit... (10th original micro trade is $29 profit, at 60TP, it is $69)  
  
But the real benefit is from trades 13-24... the potentially disabling trades. If we adjust the lots from trades 13 to 24 to approximate the profit of the original series, ending at 24th trade profit at $160 or so... our drawdown at that point is REDUCED to -$1,227 instead of -$-3,115. Our 24th trade is 1.98 lots instead of 6.55 lots, and our margin required to trade the full 24 trades is only $2,217 instead of $6,390....  
  
Of course, only IF all trades that hit our 40p TP also go on to hit our 60p TP. To me, it seems like they all do. This sytem seems to "tread water" until it a move, and then goes beyond, (often FAR beyond) our 40p. So maybe 60p is a reasonable extension.... netting us GREAT rewards for virtually no additional risk.   
  
Comments??? Maybe Mer, with more past forward testing history can speak to the assumption that if the market hits our 40p TP, it always continues to hit 60p...  
  
thanks.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#117](/thread/post/1922753#post1922753 "Post Permalink")

  * Mar 27, 2008 4:35am  Mar 27, 2008 4:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

That's the beauty of the spreadsheet!![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Feel free to adjust and play with the settings as much as you want to get the desired setting that fits your style.   
  
qz10cq, another interesting twist, keep us informed! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#118](/thread/post/1922797#post1922797 "Post Permalink")

  * Mar 27, 2008 5:07am  Mar 27, 2008 5:07am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

QZ: can you post a link to the "Close all Orders" EA?  
  
And... do you just set this to run at the beginning of each week and let it go? Do you reset at the end of friday or just let whatever orders are open carry on to the next week. (I suspect the latter ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) ...)  
  
thanks.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#119](/thread/post/1922820#post1922820 "Post Permalink")

  * Mar 27, 2008 5:31am  Mar 27, 2008 5:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Well guys, I've got good news and bad news.  
  
First the good news. PowerSM V.2 is here!!! ![](https://resources.faireconomy.media/images/emojis/64/1f911.png?v=15.1)  
  
1) This is for Chartist. My coder was able to make the "Re-Enter" function possible! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) I've attached a pic of the trades to show everyone how it shows it re-entering a trade at the same level where it was stopped out at. It will only perform this function when your breakeven input is triggered. I purposely set my BE to 20 pips to risk being stopped out more often for testing purposes and I will change it back to 30 for tomorrow's trades.  
  
2) A small bug in the PriceEntry logic was fixed.  
  
3) The "False-False" bug I believe has been fixed. I entered trades last night around 03:00 GMT (way early for me) because I was itching to see if it worked and it did.  
  
Now the bad news.![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
For those of you using the EA with the time and price entries set to "False", **the** **EA will enter a new sequence immediately after a sequence is closed**. The only way to combat this is to manually turn off the EA to stop trading or, once the EA is placed on the chart, change either the time or price entry to "True" to override.  
  
My Eur/Usd did finish out three sequences this morning and would have keep going if I didn't change it to a Timed Entry. Same with Usd/Chf. My Usd/Jpy is still going and since it closed out at 16.50 lots with $0 profit (probably due to the time entered and the BE input is too low), it should start up tomorrow at the same 16.50 lot level if all is well. I'm going to start the EA back up at 00:00 GMT because Usd/Jpy is around the 38.2 retracement and I don't want to go longer than 7 levels if possible. Also this shows why it is important to be in at the right time of day for the correct volatility and you should keep your BE input to no less than 75%. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: usdjpy_usdchf_current.gif
Size: 100 KB](/attachment/image/98068/thumbnail?d=1365540220)](/attachment/image/98068?d=1206561511)   

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/98069?d=1206561525) 15 KB | 387 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [PowerSM V.2.ex4](/attachment/file/98070?d=1206561791) 11 KB | 661 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#120](/thread/post/1922849#post1922849 "Post Permalink")

  * Mar 27, 2008 5:54am  Mar 27, 2008 5:54am 

  * [ fewhills](fewhills)

  * | Joined Apr 2006  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=8448)

> [Quoting mer071898](/thread/post/1922820#post1922820 "View Quoted Post")
> 
> Disliked
> 
> Well guys, I've got good news and bad news.  
>    
>  First the good news. PowerSM V.2 is here!!! ![](https://resources.faireconomy.media/images/emojis/64/1f911.png?v=15.1)  
>    
>  1) This is for Chartist. My coder was able to make the "Re-Enter" function possible! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) I've attached a pic of the trades to show everyone how it shows it re-entering a trade at the same level where it was stopped out at. It will only perform this function when your breakeven input is triggered. I purposely set my BE to 20 pips to risk being stopped out more often for testing purposes and I will change it back to 30 for tomorrow's trades.  
>    
>  2) A small bug in the PriceEntry logic was fixed.  
>    
>  3) The "False-False" bug I believe has been fixed. I entered trades last night around 03:00 GMT (way early for me) because I was itching to see if it worked and it did.  
>    
>  Now the bad news.![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
>    
>  For those of you using the EA with the time and price entries set to "False", **the** **EA will enter a new sequence immediately after a sequence is closed**. The only way to combat this is to manually turn off the EA to stop trading or, once the EA is placed on the chart, change either the time or price entry to "True" to override.  
>    
>  My Eur/Usd did finish out three sequences this morning and would have keep going if I didn't change it to a Timed Entry. Same with Usd/Chf. My Usd/Jpy is still going and since it closed out at 16.50 lots with $0 profit (probably due to the time entered and the BE input is too low), it should start up tomorrow at the same 16.50 lot level if all is well. I'm going to start the EA back up at 00:00 GMT because Usd/Jpy is around the 38.2 retracement and I don't want to go longer than 7 levels if possible. Also this shows why it is important to be in at the right time of day for the correct volatility and you should keep your BE input to no less than 75%.
> 
> Ignored

Very nice Mer,  
  
Maybe an idea when Timed entry and Price entry are set to false:  
  
Why not write a file every per TF bar and check if this file exists. In that case it will not open a trade until the next bar of the specific TF during the EA session.  
So if you only want to open a bar, let's say, every hour, you just put your EA TF on 60 min charts. If you want to do it every 1 minute you just set your chart on 1 minute.  
In this way you can determine the frequency of opening a trade.   
I would add one more bool and ask for something like: TradePerTFBar. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#121](/thread/post/1922864#post1922864 "Post Permalink")

  * Mar 27, 2008 6:06am  Mar 27, 2008 6:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

good idea, I'll see what my coder can do. I'm pushing the freebies he gives me to the limit as it is but we'll see. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#122](/thread/post/1923283#post1923283 "Post Permalink")

  * Mar 27, 2008 11:36am  Mar 27, 2008 11:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

> [Quoting mer071898](/thread/post/1922820#post1922820 "View Quoted Post")
> 
> Disliked
> 
> Well guys, I've got good news and bad news.  
>    
>  First the good news. PowerSM V.2 is here!!! ![](https://resources.faireconomy.media/images/emojis/64/1f911.png?v=15.1)  
>    
>  1) This is for Chartist. My coder was able to make the "Re-Enter" function possible! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) I've attached a pic of the trades to show everyone how it shows it re-entering a trade at the same level where it was stopped out at. It will only perform this function when your breakeven input is triggered. I purposely set my BE to 20 pips to risk being stopped out more often for testing purposes and I will change it back to 30 for tomorrow's trades.  
>    
>  2) A small bug in the PriceEntry logic was fixed.  
>    
>  3) The "False-False" bug I believe has been fixed. I entered trades last night around 03:00 GMT (way early for me) because I was itching to see if it worked and it did.  
>    
>  Now the bad news.![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
>    
>  For those of you using the EA with the time and price entries set to "False", **the** **EA will enter a new sequence immediately after a sequence is closed**. The only way to combat this is to manually turn off the EA to stop trading or, once the EA is placed on the chart, change either the time or price entry to "True" to override.  
>    
>  My Eur/Usd did finish out three sequences this morning and would have keep going if I didn't change it to a Timed Entry. Same with Usd/Chf. My Usd/Jpy is still going and since it closed out at 16.50 lots with $0 profit (probably due to the time entered and the BE input is too low), it should start up tomorrow at the same 16.50 lot level if all is well. I'm going to start the EA back up at 00:00 GMT because Usd/Jpy is around the 38.2 retracement and I don't want to go longer than 7 levels if possible. Also this shows why it is important to be in at the right time of day for the correct volatility and you should keep your BE input to no less than 75%.
> 
> Ignored

Way to go Mer! ![](https://resources.faireconomy.media/images/emojis/64/1f973.png?v=15.1)  
  
This 2nd version sounds awesome! Will start using it during London! Thank you for all your effort!   
  
I like fewhills' suggestion and who knows, some people might even like the idea of it opening a new cycle! That could be a feature all by itself.   
  
Profitable trading to everyone! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#123](/thread/post/1923332#post1923332 "Post Permalink")

  * Mar 27, 2008 12:12pm  Mar 27, 2008 12:12pm 

  * [ steve50](steve50)

  * | Membership Revoked  | Joined Apr 2007 | [32 Posts](/search?do=process&provider=Member&searchuser=36530)

I tested it many different ways and always get a margin call. I fail to see why anyone would be interested in this. All martingale style ea's are absolutely worthless without exeption. Work on something else in your free time as this is a loser. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#124](/thread/post/1923372#post1923372 "Post Permalink")

  * Mar 27, 2008 12:50pm  Mar 27, 2008 12:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45302_5.gif) azjeff](azjeff)

  * | Joined Aug 2007  | Status: Trader | [661 Posts](/search?do=process&provider=Member&searchuser=45302)

Steve,  
  
Backtesting is worthless. The forex is a changing market and this ea is not a stand alone ea where people do not leave it unattended 24 hours a day. If you have read all the posts in the thread you would know this. With human intervention this ea has been very profitable for myself and other people so far.   
  
Jeff  
  

> [Quoting steve50](/thread/post/1923332#post1923332 "View Quoted Post")
> 
> Disliked
> 
> I tested it many different ways and always get a margin call. I fail to see why anyone would be interested in this. All martingale style ea's are absolutely worthless without exeption. Work on something else in your free time as this is a loser.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#125](/thread/post/1923487#post1923487 "Post Permalink")

  * Mar 27, 2008 3:16pm  Mar 27, 2008 3:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Steve, I agree with Jeff in that backtesting is worthless because there are a lot of variables to consider when using this EA. Also you may not have enough equity needed in the account to match whatever leverage you are using. You must have had _some_ interest to go through all that so called testing _._  
  
Feel free to post your test results like I do and I'm sure we'll be able to see what you doing wrong because myself, Chartist, and several others have had no problems in our testing. Hell, I even entered 4 hours before my normal time yesterday, suffered through a ranging period, and still closed before the 24th level. So I know the EA works, especially if you follow the rules!  
  
I guess if you don't like the EA feel free to just post elsewhere and let us "losers" do our own constructive evaluations. ![](https://resources.faireconomy.media/images/emojis/64/1f644.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#126](/thread/post/1924039#post1924039 "Post Permalink")

  * Mar 27, 2008 10:07pm  Mar 27, 2008 10:07pm 

  * [ tvanny](tvanny)

  * | Joined Sep 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=48715)

Hi Mer, et al...  
thanks for your (and your programmers) hard work on this EA. I used the new version 2 last night on the GBP/JPY, with a Break Even set at 90. I use a 120 TP and 30 SL. The stop loss didn't adjust itself to break even after the GBP/JPY went up by more then 90. I was wondering if this was a problem with V2 and if anyone else had experienced it. BTW, it closed out on the 2nd entry for +120.  
  
I have been working with Dan's EA ever since he first put it up. I like both versions, yours and his. I have been very profitable (so far demo only). It is so customizable that it can fit almost anyones trading style. BUT...like has been said many times, it is not a set it and forget it system. The only times I got in trouble were when I made stupid entries and didn't follow my rules. Just like any trading system. Discipline! I'll put up some of the things I learned later.  
  
Thanks again,  
Tvanny 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#127](/thread/post/1924149#post1924149 "Post Permalink")

  * Mar 27, 2008 11:16pm  Mar 27, 2008 11:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

> [Quoting tvanny](/thread/post/1924039#post1924039 "View Quoted Post")
> 
> Disliked
> 
> Hi Mer, et al...  
>  thanks for your (and your programmers) hard work on this EA. I used the new version 2 last night on the GBP/JPY, with a Break Even set at 90. I use a 120 TP and 30 SL. The stop loss didn't adjust itself to break even after the GBP/JPY went up by more then 90. I was wondering if this was a problem with V2 and if anyone else had experienced it. BTW, it closed out on the 2nd entry for +120.  
>    
>  I have been working with Dan's EA ever since he first put it up. I like both versions, yours and his. I have been very profitable (so far demo only). It is so customizable that it can fit almost anyones trading style. BUT...like has been said many times, it is not a set it and forget it system. The only times I got in trouble were when I made stupid entries and didn't follow my rules. Just like any trading system. Discipline! I'll put up some of the things I learned later.  
>    
>  Thanks again,  
>  Tvanny
> 
> Ignored

Well I haven't reached any break evens yet with testing the v2 but I will surely watch and report any bugs! Please do share with us any experiences and knowledge you may have with this!   
  
I do agree with you; this is not a (randomly) set and forget system. Working it that way could potentially kill your account if you make stupid entries and thus robotic back testing does not work as Mer has already stated. Anyways, could you tell us more about when you enter your gbp/jpy trades and have you found 120TP, 90BE, 30SL to be the best setting for this pair?   
  
My first V2 trade:  
usd/chf: set to open on "time" function @ 10:30AM GMT.  
Closed on first trade of cycle @ 12:10PM GMT +44pips TP.  
  
Last two days have not cycled past the 1st trade. Not bad for a "loser"! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#128](/thread/post/1924246#post1924246 "Post Permalink")

  * Mar 28, 2008 12:06am  Mar 28, 2008 12:06am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Both my EU and UJ trades had a breakeven move, which functioned perfectly. I have not yet had a breakeven stopout to test the re-entry function.....  
  
This system simply can not be backtested with MT4... due to the time component. I have worked with a programmer on several other time-dependent systems, and they won't backtest either. So all these "testing" reports are simply not valid. Not to say the comments aren't true!!  
  
Every system has a risk. The risk here is of course, getting a run of 25 trades. (or more). That is the system risk. The trader risk is trading at lot sizes that will margin call you before the 24 trades, which is every traders' perogative. You can trade at higher lots, thereby reducing the max run to say, 16 trades. You run a greater risk of loss, but also reap a greater return.  
  
If one is fearful of hitting that 25th trade, then don't trade this system! I you can't handle the risk aspect, find another system. This type of trading is unique, and carries a unique risk "psychcology". One's risk psyche must be compatible with the system risk.... one of the hardest fits to find in trading.  
  
So for those of us that "fit" with PowerSM, let's continue to work this, slowly, and smartly! This whole thing is based on hitting a 50p (pretty much direct) run sometime within the European trading session, or Asian, or whichever time frame you pick for greatest movement... What are the percentages? Select pairs that ALWAYS move at least 50p one way or another in a session and you WILL hit your takeprofit 100%. That is simple math and market movement.   
  
The BIG question is IF you can hit the move within 24 trades, (or whatever number you pick according to your risk psyche....). What are the percentages in that?? From what I see, pretty dang high... nothing is 100%, but hitting a 50p run in the EU or UJ during market opening?? Slam dunk...  
  
Let's trade smart, with good success!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#129](/thread/post/1924327#post1924327 "Post Permalink")

  * Mar 28, 2008 12:59am  Mar 28, 2008 12:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

tvanny, you have to remember your inputs don't factor in the spread. I had a couple of trades that looked like they should have closed out, but after taking off the spread I was actually 1 pip short. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#130](/thread/post/1924357#post1924357 "Post Permalink")

  * Mar 28, 2008 1:09am  Mar 28, 2008 1:09am 

  * [ tvanny](tvanny)

  * | Joined Sep 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=48715)

> [Quoting Chartist](/thread/post/1924149#post1924149 "View Quoted Post")
> 
> Disliked
> 
> Well I haven't reached any break evens yet with testing the v2 but I will surely watch and report any bugs! Please do share with us any experiences and knowledge you may have with this!   
>    
>  I do agree with you; this is not a (randomly) set and forget system. Working it that way could potentially kill your account if you make stupid entries and thus robotic back testing does not work as Mer has already stated. Anyways, could you tell us more about when you enter your gbp/jpy trades and have you found 120TP, 90BE, 30SL to be the best setting for this pair?   
>    
>  My first V2 trade:  
>  usd/chf: set to open on "time" function @ 10:30AM GMT.  
>  Closed on first trade of cycle @ 12:10PM GMT +44pips TP.  
>    
>  Last two days have not cycled past the 1st trade. Not bad for a "loser"! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

I guess I’ll have to look at my settings for Break Even again.  
  
I’ve been using a TP/SL of 120/30 for GBP/GPY for quite awhile. Just look at its average daily range! Holy crap! Sometimes I wish I would put in a higher TP. The larger TP/SL gives me a much more relaxed trading posture. There’s a little more room for slop. I use a Bollinger band with settings of 10/2 and I also use a Bollinger Band width indicator with a 10/2 setting (just helps me visualize). I also put fractals and a support/resistance indicator on the chart. I’ll put up a copy of my chart when I get home. What I’ll do is open a 15 minute chart and look at the last couple weeks of data. When I see where the Bollinger Bands have contracted, I put a reference line on the Bollinger Band width indicator in the lower window. I look at a 15 minute chart and see where the Bollinger Band width indicator breaks through my reference line. It just indicates increasing volatility. The perfect trade setup (ok, nothings perfect) is when the Bollinger Band width indicator starts to break out right before the Europe open. There is a lot more to it. It’s hard to explain a discretionary trading style. Is there a lot of news scheduled? Was there a huge run yesterday? Has there already been too much movement before the Europe open? Etc, etc…  
  
I’ve also gone back and manually forward tested my 30/120 settings for GBP/JPY, from about the first of October thru the beginning of March. Just use the F12 button and advance one bar or candle at a time. I skipped holidays. I just open a trade at 7 GMT and see how it goes. Here’s the fun part, I was experimenting with only going to 11 levels, not 24. I don’t have my statistics in hand, but if I remember, out of about 100 trades I hit the 12th level (bust) 4 times. But because the other trades were winners, I more then doubled my account in less the six months (remember, very UNscientific study). Look at the Excel spread sheet for the profit at different levels. I also saw that I would have hit 25 levels at least once thereby taking a huge hit on my account.  
  
Bla bla bla, I’ve rambled enough.  
  
Tvanny

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#131](/thread/post/1924364#post1924364 "Post Permalink")

  * Mar 28, 2008 1:15am  Mar 28, 2008 1:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Results are in! Eur/Usd for 3/27/2008 was normal closing out around level 7. My Usd/Jpy and Usd/Chf daily statement is for 3/26-3/27/2008 due to early testing of version V.2. As you can see it can be very dangerous and unpredictable to leave this running on "false-false" outside of the big boys trading hours without being there to watch it or to change one of the inputs to true after the sequence has started. Even after all that mess we still closed out at level 20. And keep in mind without the new re-enter function this would have went to level 24 so it definitely does help!!!! 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/98313?d=1206634440) 16 KB | 361 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#132](/thread/post/1924377#post1924377 "Post Permalink")

  * Mar 28, 2008 1:22am  Mar 28, 2008 1:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

That's why low spread pairs are preferred, not that you can't trade larger spread pairs, the problem is as you increase your TP the stop doesn't move up the ladder as fast. For Gbp/Jpy you could run through 4-5 levels in one bar with only a 30 pip stop because of the pairs erratic behavior, same with Gbp/Usd and Gbp/Chf. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#133](/thread/post/1924402#post1924402 "Post Permalink")

  * Mar 28, 2008 1:38am  Mar 28, 2008 1:38am 

  * [ tvanny](tvanny)

  * | Joined Sep 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=48715)

> [Quoting mer071898](/thread/post/1924377#post1924377 "View Quoted Post")
> 
> Disliked
> 
> That's why low spread pairs are preferred, not that you can't trade larger spread pairs, the problem is as you increase your TP the stop doesn't move up the ladder as fast. For Gbp/Jpy you could run through 4-5 levels in one bar with only a 30 pip stop because of the pairs erratic behavior, same with Gbp/Usd and Gbp/Chf.
> 
> Ignored

Like I said, those settings have worked very well for me in both live demo trading and looking back. I'm not comfortable with a 10 pip stop. I've seen all the Majors churn away thru 10 pips back and forth plenty of times when I was using the original 40/10 setup. Any pair can be erratic. We all have to find what we're comfortable with and contribute what we can. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#134](/thread/post/1924603#post1924603 "Post Permalink")

  * Mar 28, 2008 3:26am  Mar 28, 2008 3:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Don't worry, I'm not saying the way you're doing it is wrong by any means ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1), everybody has there own preference. I prefer to use the more stable pairs and others, like yourself, use what's comfortable for them. there is no wrong way as long as the basics are followed. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#135](/thread/post/1925561#post1925561 "Post Permalink")

  * Mar 28, 2008 5:07pm  Mar 28, 2008 5:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Alright, it's not even been an hour after the London open and my trades for 3/28/2008 are already done and I can go to bed, gotta love it!![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) One thing I did do was start my timed entry at the Frankfurt open if we could see if there are any improvements on how much faster the sequences closed and was pleasantly surprised. It may be different next week so we won't get our hopes up.  
  
Obviously, we've still got a long way to go but it's been 13 days and still going strong except for the scare on the 26th which was my fault for breaking my rules and getting ahead of myself with testing V.2. Hope everyone else is doing well.![](https://resources.faireconomy.media/images/emojis/64/1f911.png?v=15.1)

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/98478?d=1206691255) 14 KB | 380 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#136](/thread/post/1926686#post1926686 "Post Permalink")

  * Mar 29, 2008 6:20am  Mar 29, 2008 6:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Just thought I'd drop in before the weekend to see if anyone is having any issues with V.2. If not we'll see you bright and early Monday morning. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#137](/thread/post/1927164#post1927164 "Post Permalink")

  * Mar 29, 2008 11:12pm  Mar 29, 2008 11:12pm 

  * [ arui](arui)

  * | Joined Jul 2006  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=13730)

Your EA works perfect for me on Friday, Thanks for sharing 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#138](/thread/post/1927287#post1927287 "Post Permalink")

  * Mar 30, 2008 2:44am  Mar 30, 2008 2:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

You are welcome, glad to have you aboard. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#139](/thread/post/1928631#post1928631 "Post Permalink")

  * Mar 31, 2008 1:39pm  Mar 31, 2008 1:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Hi all!  
  
+50TP on the eur/usd on Friday. I don't know how either because I made a mistake on the entry time and actually entered -2.5 GMT and it went into a range but I managed to close out on the 8th trade.  
  
Granite, breakeven was activated once and V(1).2 worked exactly like it was supposed to! Have a great trading week Mer and everyone! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#140](/thread/post/1928723#post1928723 "Post Permalink")

  * Mar 31, 2008 3:21pm  Mar 31, 2008 3:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Yeah, V.2 is working smoothly so far. I'm glad the re-enter function is working because my coder said sometimes that particular type of coding can be misinterpreted by an EA a lot unless it's done correctly. Even if you BE 2 or 3 times the EA will do nothing but help you.   
  

> Quote
> 
> Disliked
> 
> Even after all that mess we still closed out at level 20. And keep in mind without the new re-enter function this would have went to level 24 so it definitely does help!!!!

Those times the EA hit BE saved me when I decided to be an idiot and do some early testing with a different BE stop. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#141](/thread/post/1928736#post1928736 "Post Permalink")

  * Mar 31, 2008 3:36pm  Mar 31, 2008 3:36pm 

  * [ saragosa](saragosa)

  * | Joined Sep 2006  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=19601)

this EA has expired date? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#142](/thread/post/1928768#post1928768 "Post Permalink")

  * Mar 31, 2008 4:06pm  Mar 31, 2008 4:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Yes, since this will be eventually marketed **outside** of this forum after proper testing, account and expiration coding has been put into it in for those wanting to lease the EA commercially. **It will be free to all registered members of this forum** and doesn't expire until 3/13/2009. If at that time you need a new version, the EA will provide you a message regarding how to contact me on getting a fresh one. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#143](/thread/post/1929496#post1929496 "Post Permalink")

  * Mar 31, 2008 11:00pm  Mar 31, 2008 11:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

That B/E function TRULY takes advantage of the previous "free trade". ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#144](/thread/post/1929623#post1929623 "Post Permalink")

  * Apr 1, 2008 12:00am  Apr 1, 2008 12:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here's the results for Monday 3/31/2008. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/99156?d=1206975611) 14 KB | 341 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#145](/thread/post/1930710#post1930710 "Post Permalink")

  * Apr 1, 2008 3:40pm  Apr 1, 2008 3:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Nailed my Eur/Usd on the first trade this morning. We'll wait to see how the other two pan out. Talk to everyone in a while. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#146](/thread/post/1930983#post1930983 "Post Permalink")

  * Apr 1, 2008 6:44pm  Apr 1, 2008 6:44pm 

  * [ saragosa](saragosa)

  * | Joined Sep 2006  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=19601)

> [Quoting mer071898](/thread/post/1929623#post1929623 "View Quoted Post")
> 
> Disliked
> 
> Here's the results for Monday 3/31/2008.
> 
> Ignored

execuse me sir, this is u real account or not? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#147](/thread/post/1931717#post1931717 "Post Permalink")

  * Apr 2, 2008 12:16am  Apr 2, 2008 12:16am 

  * [ mastergunner](mastergunner)

  * | Commercial User  | Joined Mar 2008 | [52 Posts](/search?do=process&provider=Member&searchuser=65001)

My time charts are you using this on?  
  
I'm backtesting EUR/USD and it only seems to work dandy on the daily chart. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#148](/thread/post/1931737#post1931737 "Post Permalink")

  * Apr 2, 2008 12:30am  Apr 2, 2008 12:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

saragosa, these are on a demo account as we will be extensively testing this before any live trading will be done.  
  
mastergunner, backtesting this EA is completely worthless as you need to use this with a little discretion regarding your entries. I only trade this during the hours of 07:00 to 17:00 which is the Frankfurt open to the London close and you can't specify that in a backtest. That is why this has to be forward tested only. With regards to what timeframe, the EA will work on any timeframe. I use 5 or 15 minute so I can view how the sequences progresses.  
  
Here are the trades for 4/1/2008. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/99580?d=1207063687) 15 KB | 291 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#149](/thread/post/1931788#post1931788 "Post Permalink")

  * Apr 2, 2008 12:57am  Apr 2, 2008 12:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar21847_4.gif) jlpi](jlpi)

  * | Joined Oct 2006  | Status: Trader and EA programmer | [158 Posts](/search?do=process&provider=Member&searchuser=21847)

> [Quoting mer071898](/thread/post/1931737#post1931737 "View Quoted Post")
> 
> Disliked
> 
> mastergunner, backtesting this EA is completely worthless as you need to use this with a little discretion regarding your entries. I only trade this during the hours of 07:00 to 17:00 which is the Frankfurt open to the London close and you can't specify that in a backtest. That is why this has to be forward tested only.
> 
> Ignored

To add a filter on the hours in an EA is very easy to do. We could put that in parameters in order for everybody to adjust according to the broker server's time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#150](/thread/post/1931807#post1931807 "Post Permalink")

  * Apr 2, 2008 1:08am  Apr 2, 2008 1:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

> [Quoting mer071898](/thread/post/1930710#post1930710 "View Quoted Post")
> 
> Disliked
> 
> Nailed my Eur/Usd on the first trade this morning. We'll wait to see how the other two pan out. Talk to everyone in a while.
> 
> Ignored

Me too!   
  
1st trade TP hit +50 on the eur/usd. Entered @ gmt -1! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#151](/thread/post/1931810#post1931810 "Post Permalink")

  * Apr 2, 2008 1:10am  Apr 2, 2008 1:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

> Quote
> 
> Disliked
> 
> To add a filter on the hours in an EA is very easy to do. We could put that in parameters in order for everybody to adjust according to the broker server's time.

  
That's great if it can be done, but as we all know backtesting can be very unreliable. That's why I will be sticking to forward testing only. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#152](/thread/post/1931815#post1931815 "Post Permalink")

  * Apr 2, 2008 1:11am  Apr 2, 2008 1:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Great job Chartist, no issues with the larger TP I see. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#153](/thread/post/1931905#post1931905 "Post Permalink")

  * Apr 2, 2008 2:08am  Apr 2, 2008 2:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar21847_4.gif) jlpi](jlpi)

  * | Joined Oct 2006  | Status: Trader and EA programmer | [158 Posts](/search?do=process&provider=Member&searchuser=21847)

> [Quoting mer071898](/thread/post/1931810#post1931810 "View Quoted Post")
> 
> Disliked
> 
> That's great if it can be done, but as we all know backtesting can be very unreliable. That's why I will be sticking to forward testing only.
> 
> Ignored

Yes that can be done but requires to modify the source code....  
Backtesting quality depends on the data quality you have and also on how the EA is coded (working on close prices only, no scalping...) .   
But I think it is anyway useful because if your system crashes once every 6 months that means a lot of waiting time in forward testing. And anyway you will forward test it fine during several months and as soon as you will put it live it will crash (Murphy laws still apply) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#154](/thread/post/1932054#post1932054 "Post Permalink")

  * Apr 2, 2008 3:34am  Apr 2, 2008 3:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Well I won't be modifying the source code just to improve backtesting results, and your opinion is noted, I don't agree, but again that's just the way I see it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#155](/thread/post/1932076#post1932076 "Post Permalink")

  * Apr 2, 2008 3:50am  Apr 2, 2008 3:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45302_5.gif) azjeff](azjeff)

  * | Joined Aug 2007  | Status: Trader | [661 Posts](/search?do=process&provider=Member&searchuser=45302)

Hi Merol,  
  
What settings would you recommend for a $10,000 account and trading what pairs?  
  
Thank You,  
Jeff  
  
quote=mer071898;1932054]Well I won't be modifying the source code just to improve backtesting results, and your opinion is noted, I don't agree, but again that's just the way I see it.[/quote] 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#156](/thread/post/1932154#post1932154 "Post Permalink")

  * Apr 2, 2008 4:53am  Apr 2, 2008 4:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Well, Eur/Usd is probably the most stable pair, but I'm kinda starting to like Usd/Chf. I try to stick with the lower spread pairs with the default settings because once you use pairs that go past 5-6+ pip [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") you have to increase your TP and stop, which in turn you'll have to increase your bankroll to not get margin called. Some guys have used Eur/Jpy because of the low spread (3 pips on ODL) and higher daily range (roughly 150-200 pips). But in turn you get more erratic behavior. Sort of a catch 22 if you know what I mean.  
  
If your using standard mini account you'd start out with .01 lots ($.10 a pip). At 100:1 leverage you'd be able to trade 1 pair or at 400:1 you could actually trade two pairs. Just make sure the broker can trade odd lot sizes like .11, .36, and so on. On a nano account you could actually trade up to 10 pairs at 100:1 leverage or 20 pairs at 400:1. But that's figuring you'll use default TP, BE, and stop levels. Use the calculator in post #1 and play around with the numbers to see what you'd need to trade with beforehand, it'll help.  
  
I, personally, like the idea of the nano account better because you can spread out the risk to up to 20 different pairs so if one pair backfires, 19 others will lessen the sting. The other option I'm looking into is to possibly add a few more levels to also decrease the risk but that is on the back burner for now.  
  
Also, as others have mention before there won't be a substantial account growth (2-4% a month) with this EA but as I said before, take those profits out frequently and put them in your primary trading account and use money that you can afford to lose because, as I will admit, this is a riskier than average EA to trade with. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#157](/thread/post/1932263#post1932263 "Post Permalink")

  * Apr 2, 2008 6:21am  Apr 2, 2008 6:21am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Question on times.... couple of you said you hit the EU first time today, took me 9 trades, with one breakeven in there....  
  
You also mentioned you started at GMT-1... what time is that? Up to now, we have been starting at 7gmt (I think?), so did you start an hour earlier, 6gmt? (not broker times, but actually GMT times....)  
  
Have you found a better start time for the EU?  
  
thanks for the clarification..... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#158](/thread/post/1932669#post1932669 "Post Permalink")

  * Apr 2, 2008 1:29pm  Apr 2, 2008 1:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I start the EA at the Frankfurt open which is normally 07:00 GMT. With daylight savings here in the states it will show 06:00 in the EA's input and on the statements. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#159](/thread/post/1932765#post1932765 "Post Permalink")

  * Apr 2, 2008 3:11pm  Apr 2, 2008 3:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar57172_6.gif) forexmoments](forexmoments)

  * | Commercial User  | Joined Dec 2007 | [1,927 Posts](/search?do=process&provider=Member&searchuser=57172)

> [Quoting mer071898](/thread/post/1932154#post1932154 "View Quoted Post")
> 
> Disliked
> 
> Well, Eur/Usd is probably the most stable pair, but I'm kinda starting to like Usd/Chf. I try to stick with the lower spread pairs with the default settings because once you use pairs that go past 5-6+ pip spreads you have to increase your TP and stop, which in turn you'll have to increase your bankroll to not get margin called. Some guys have used Eur/Jpy because of the low spread (3 pips on ODL) and higher daily range (roughly 150-200 pips). But in turn you get more erratic behavior. Sort of a catch 22 if you know what I mean.  
> 
> 
> Ignored

I agree, stick with the 4 majors for this particular EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#160](/thread/post/1933568#post1933568 "Post Permalink")

  * Apr 2, 2008 11:40pm  Apr 2, 2008 11:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

> [Quoting mer071898](/thread/post/1931815#post1931815 "View Quoted Post")
> 
> Disliked
> 
> Great job Chartist, no issues with the larger TP I see.
> 
> Ignored

Nope! So far its been well within the eur/usd range. Granite, I vary the entry times but always enter during the European trading session.   
  
Last session was no different:  
  
EUR/USD OPENED AT 08:00 GMT and was out with the 4th trade at 08:23GMT (wow! it whipped around good!) with 50 TP. No Break evens to report for this one.  
  
My 2cents on backtesting this EA: It doesn't work for me even if I had perfect data and coding because I vary the entry times to better take advantage of volatile sessions. There are some days I don't even trade! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#161](/thread/post/1933583#post1933583 "Post Permalink")

  * Apr 2, 2008 11:48pm  Apr 2, 2008 11:48pm 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Ah ha!! Now we get to the crux of success for this system:  
  
Determining the start of a volatile range! Maybe further discussion is in order... do you all just watch the charts, (how fast the ticks are coming in, and an increasing range of a bar...etc...) and just jump in when it "feels" right?  
  
Or... is there any volatility indicator that would be helpful... as we know, there is no real "volume" for FX, which is too bad, we could use an increase in that number to indicate more volatility... Tried the Daimiani Volatmeter, but it doesn't really help... Thought of overlaying a ATR1 over an ATR13 say, to indicate an increase in range... maybe indicating more activity/volatility...  
  
Any other ideas or approaches??  
  
Then, there is the good ol' clock "indicator". 7gmt, 8gmt.. somewhere around there for the start of the European session, while everybody is waking up and starting to trade for the day.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#162](/thread/post/1933848#post1933848 "Post Permalink")

  * Apr 3, 2008 2:05am  Apr 3, 2008 2:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar21847_4.gif) jlpi](jlpi)

  * | Joined Oct 2006  | Status: Trader and EA programmer | [158 Posts](/search?do=process&provider=Member&searchuser=21847)

> [Quoting mer071898](/thread/post/1932054#post1932054 "View Quoted Post")
> 
> Disliked
> 
> Well I won't be modifying the source code just to improve backtesting results, and your opinion is noted, I don't agree, but again that's just the way I see it.
> 
> Ignored

of course everybody can have different opinions on backtesting. The idea was not to improve the backtest with optimisation but just to run a backtest.  
But anyway it is your EA, and it is 100% your decision to let other people backtest your strategy or not.  
  
I only wanted to mention 2 points that I think may be important for the users of the EA and for martingale EAs in general:  
\- usually people complain about backtest and give as example scalping strategies that have excellent results in backtest and are catastrophic in forward test. I have not seen yet the opposite: a strategy failing in backtest and very succesful in live and I have coded myself more than 100 EAs either for me or for clients.  
\- forward test are clearly a better test than backtest for "standard" strategies but for martingale ones you have to take into account one other parameter. Martingale strategies will either wipped out the account or have large losses at some point in time. The question is not "if" the losses will occur but only "when" or even more accurately "how often". Because if it is rare enough you may be able to withdraw your benefits often enough to still go out positive (even if in my opinion it is unlikely). Then how can you get this information, or a least kind of estimate. If the system is good enough and doesn't get wipped out every 2 weeks but lasts many months, forward test is a long way to get the info. Backtest is then the way to go (in my opinion of course) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#163](/thread/post/1933892#post1933892 "Post Permalink")

  * Apr 3, 2008 2:33am  Apr 3, 2008 2:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Wow, a little reversal this morning with my Usd/Jpy and Usd/Chf closing out on the first sequence before my Eur/Usd!![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) Here's the statements for 4/2/2008. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/99928?d=1207157553) 15 KB | 369 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#164](/thread/post/1934345#post1934345 "Post Permalink")

  * Apr 3, 2008 10:46am  Apr 3, 2008 10:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar15241_4.gif) juxta14](juxta14)

  * | Joined Aug 2006  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=15241)

Since this strategy depends more on volatility when entering a trade, how about entering at daily high or low + 5pips, this is mostly a breakout position.  
  
Price entry option is available on EA which is really good.  
  
Just my 2pips.  
  
  
  
  
.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#165](/thread/post/1934507#post1934507 "Post Permalink")

  * Apr 3, 2008 2:19pm  Apr 3, 2008 2:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

This is just my opinion... Fundamentals drive the FX market first and foremost (technicals take over after this).   
  
Taking this into consideration, I try to enter when I think a certain fundamental (news) time will tend to move my position from my starting point.   
  
I really think that the European session (as long as there is good fundamentals coming out) has great trends, volumes, and great possibilities to make a winning trade.  
  
I personally don't use any other indicators at the moment. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#166](/thread/post/1934531#post1934531 "Post Permalink")

  * Apr 3, 2008 3:00pm  Apr 3, 2008 3:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I tell you a great way to use this EA if with fibs. If you haven't gone through Bobokus' thread on Fibonacci trading, you should even if you never use this EA ever again. I use fibs to analyze the predictive nature of the market in my everyday trading and you could use this in your EA placement as well. If you look at the pic, and I know it's a little cluttered, there were several fib swings present yesterday and this morning that with proper placement would have easily made money with my EA.   
  
Currently, I'm just experimenting with the timed entry for now to be as consistent as possible for testing purposes. I guess what I'm trying to say is use what is in your comfort zone to make proper judgments on your entries and stick with the plan. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: usdjpy_usdchf_current.gif
Size: 50 KB](/attachment/image/100047/thumbnail?d=1365540563)](/attachment/image/100047?d=1207202374)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#167](/thread/post/1934661#post1934661 "Post Permalink")

  * Apr 3, 2008 5:20pm  Apr 3, 2008 5:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45302_5.gif) azjeff](azjeff)

  * | Joined Aug 2007  | Status: Trader | [661 Posts](/search?do=process&provider=Member&searchuser=45302)

Hi Mer071898,  
  
What a terrific idea. Anyway your coder can tie the together and have a fully automatic ea do both?  
  
Jeff  
  

> [Quoting mer071898](/thread/post/1934531#post1934531 "View Quoted Post")
> 
> Disliked
> 
> I tell you a great way to use this EA if with fibs. If you haven't gone through Bobokus' thread on Fibonacci trading, you should even if you never use this EA ever again. I use fibs to analyze the predictive nature of the market in my everyday trading and you could use this in your EA placement as well. If you look at the pic, and I know it's a little cluttered, there were several fib swings present yesterday and this morning that with proper placement would have easily made money with my EA.   
>    
>  Currently, I'm just experimenting with the timed entry for now to be as consistent as possible for testing purposes. I guess what I'm trying to say is use what is in your comfort zone to make proper judgments on your entries and stick with the plan.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#168](/thread/post/1935110#post1935110 "Post Permalink")

  * Apr 3, 2008 11:04pm  Apr 3, 2008 11:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Entered at 10:00AM GMT +50 TP at 12:35 on first trade eur/usd.   
  
Thanks Mer will check that out! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#169](/thread/post/1935178#post1935178 "Post Permalink")

  * Apr 3, 2008 11:40pm  Apr 3, 2008 11:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here's the results for 4/3/2008 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/100187?d=1207233643) 16 KB | 380 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#170](/thread/post/1936218#post1936218 "Post Permalink")

  * Apr 4, 2008 5:36pm  Apr 4, 2008 5:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Hope everyone's doing well. My Eur/Usd is already closed and waiting for the others to close shortly. Talk to everyone a little later with results. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#171](/thread/post/1936330#post1936330 "Post Permalink")

  * Apr 4, 2008 7:25pm  Apr 4, 2008 7:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar50781_4.gif) Kfx](kfx)

  * | Joined Oct 2007  | Status: Trader | [339 Posts](/search?do=process&provider=Member&searchuser=50781)

Hey mer071898 thanks for the sistem and EA. I will post my results too. I only changed the settings of start time (9:00) and end time (18.00). I´m using MIG broker. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PSM_04-04-08.zip](/attachment/file/100456?d=1207304669) 1 KB | 433 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#172](/thread/post/1936350#post1936350 "Post Permalink")

  * Apr 4, 2008 7:41pm  Apr 4, 2008 7:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar50781_4.gif) Kfx](kfx)

  * | Joined Oct 2007  | Status: Trader | [339 Posts](/search?do=process&provider=Member&searchuser=50781)

Only one question. The EA works in live account? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#173](/thread/post/1936354#post1936354 "Post Permalink")

  * Apr 4, 2008 7:43pm  Apr 4, 2008 7:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

> [Quoting Kfx](/thread/post/1936350#post1936350 "View Quoted Post")
> 
> Disliked
> 
> Only one question. The EA works in live account?
> 
> Ignored

Yes. But please be aware that this EA might blow your account away. The timer start isn't the safest thing. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Someday it will happen, noone knows when, but it will happen. The only question is: Will your balance minus a 24 sequence loss be higher than your initial deposit? ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#174](/thread/post/1936371#post1936371 "Post Permalink")

  * Apr 4, 2008 8:01pm  Apr 4, 2008 8:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar50781_4.gif) Kfx](kfx)

  * | Joined Oct 2007  | Status: Trader | [339 Posts](/search?do=process&provider=Member&searchuser=50781)

> [Quoting Xaron](/thread/post/1936354#post1936354 "View Quoted Post")
> 
> Disliked
> 
> Yes. But please be aware that this EA might blow your account away. The timer start isn't the safest thing. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Someday it will happen, noone knows when, but it will happen. The only question is: Will your balance minus a 24 sequence loss be higher than your initial deposit? ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
>    
>  Regards - Xaron
> 
> Ignored

Yes, I know. If someday happen that the system reaches the 24 level, we should have a great deposit of money, to withstand the drawdown. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#175](/thread/post/1936753#post1936753 "Post Permalink")

  * Apr 5, 2008 12:15am  Apr 5, 2008 12:15am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Well, the only thing certain about FX is that you can't be certain.  
  
Hit the 24 losses a certainty? Maybe. Maybe not. We don't know! But we all CAN agree that we don't want to be the one that hits it!! So.... this is why MER is continually reminding us that this is not a blind system. The ONLY thing we have complete control over is when we take our first trade... (and the SL/TP, but that is different issue...). Agreed with above that WHEN we take our first trade can make us or break us...   
  
So far, the timed entry, coupled with a bit of fundaments analysis (we are looking for movement, volatility....) seems to be the best approach, and has proven to be quite successful so far.  
  
Regarding "blowing" the account... that is why we have the spreadsheet. To ask the question "will the 24th loss blow our account", means that you have not used the spreadsheet. If we do, we will KNOW absolutely where our account will be at each step in the sequence. The spreadsheet Money Management analysis is CRITICAL to the success of this system, and can not be ignored! It is as much if not MORE important than the logic, the EA, the actual trading...   
  
So... play with the spreadsheet... the default will give you around a 50% DD at the 24th loss. Try to reduce it, or make every trade net you $10, see what it does to your DD... pretty fun really!! Currently, I have set the lot sizes to always give me 20p per trade. If I win on the first trade, I make 20p. If I win on the 9th trade, I get 20p. That way, I can calc my returns more accurately. In order to reduce the ultimate DD at the 24th loss (again IF it happens, not WHEN....), I have chosen to accept a breakeven trade, or even small losses for trades 16 and above. In other words, if the sequence goes to 16 or more trades, I am fine with bailing at no gain, or a small loss, in order to reduce my losses at the 24th level. But you can do all this with the spreadsheet, it is GREAT!!  
  
This really is a good discussion, and a good group of traders to work with. Trading is all about probabilities AND risk-acceptance. A friend of mine trades an EA that has performed well over the past few years, but you take a 6 month drawdown period every year!! Too long for me, but he is fine with it. I like this system. I can live with the risk of 24 losing trades, but he can't! He can't stand progressive lot systems, which I have traded for years. So, success for each of us lies in finding the psychological "fit" between system and trader...   
  
Good success to all!! Let's keep working this one here.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#176](/thread/post/1936802#post1936802 "Post Permalink")

  * Apr 5, 2008 12:52am  Apr 5, 2008 12:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

> Quote
> 
> Disliked
> 
> Well, the only thing certain about FX is that you can't be certain.

Very well said mrkam, I totally agree maybe someday it will happen. It may not happen in 10 yrs, it may happen next month. The last time we talked to FXTradepro he was using this live for over 3 years with no loss past the 24**with proper entries and fundamentals**.   
  
As you can see, the spreadsheet can be your savior as I've heard about guys in the other thread trying to run this live with half of what they needed in their account, getting blown out and margin called, and then wondering why the hell it happened. Common sense is key, you have to have the equity to cover the possibility of a 24th sequence. And back to the point again, don't sit there and leave all your profits in the account. Take them out every month, three months, a year, I don't care but take them out and don't risk losing it all.  
  
I do appreciate everyones input (including Xaron's) and keeping a positive light with this. Any martingale systems or EA's get bashed pretty hard on forums no matter how safe they look, good job guys.![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
Oh, and here are the results for 4/4/2008 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/100533?d=1207324259) 16 KB | 358 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#177](/thread/post/1936807#post1936807 "Post Permalink")

  * Apr 5, 2008 12:54am  Apr 5, 2008 12:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Don't get me wrong. I LOVE this kind of trading as it's based on volatility! I just want to warn to use this completely automatically.  
  
E.g. don't use it on bank holidays! I already use the martingale EA from Rama, and I know the risks... ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#178](/thread/post/1937020#post1937020 "Post Permalink")

  * Apr 5, 2008 3:12am  Apr 5, 2008 3:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Don't worry Xaron, we understand want you mean. It's great to have someone on the thread that's used a martingale system to give us some insights based on experience. This EA was actually ran during Easter weekend, (Friday and Monday) and made it through without a hitch which is a great sign. Actually, I don't think the EA went past the 9th or 10th level! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#179](/thread/post/1937378#post1937378 "Post Permalink")

  * Apr 5, 2008 1:24pm  Apr 5, 2008 1:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

> [Quoting mrkam](/thread/post/1936753#post1936753 "View Quoted Post")
> 
> Disliked
> 
> Well, the only thing certain about FX is that you can't be certain.  
>    
>  Hit the 24 losses a certainty? Maybe. Maybe not. We don't know! But we all CAN agree that we don't want to be the one that hits it!! So.... this is why MER is continually reminding us that this is not a blind system. The ONLY thing we have complete control over is when we take our first trade... (and the SL/TP, but that is different issue...). Agreed with above that WHEN we take our first trade can make us or break us...   
>    
>  So far, the timed entry, coupled with a bit of fundaments analysis (we are looking for movement, volatility....) seems to be the best approach, and has proven to be quite successful so far.  
>    
>  Regarding "blowing" the account... that is why we have the spreadsheet. To ask the question "will the 24th loss blow our account", means that you have not used the spreadsheet. If we do, we will KNOW absolutely where our account will be at each step in the sequence. The spreadsheet Money Management analysis is CRITICAL to the success of this system, and can not be ignored! It is as much if not MORE important than the logic, the EA, the actual trading...   
>    
>  So... play with the spreadsheet... the default will give you around a 50% DD at the 24th loss. Try to reduce it, or make every trade net you $10, see what it does to your DD... pretty fun really!! Currently, I have set the lot sizes to always give me 20p per trade. If I win on the first trade, I make 20p. If I win on the 9th trade, I get 20p. That way, I can calc my returns more accurately. In order to reduce the ultimate DD at the 24th loss (again IF it happens, not WHEN....), I have chosen to accept a breakeven trade, or even small losses for trades 16 and above. In other words, if the sequence goes to 16 or more trades, I am fine with bailing at no gain, or a small loss, in order to reduce my losses at the 24th level. But you can do all this with the spreadsheet, it is GREAT!!  
>    
>  This really is a good discussion, and a good group of traders to work with. Trading is all about probabilities AND risk-acceptance. A friend of mine trades an EA that has performed well over the past few years, but you take a 6 month drawdown period every year!! Too long for me, but he is fine with it. I like this system. I can live with the risk of 24 losing trades, but he can't! He can't stand progressive lot systems, which I have traded for years. So, success for each of us lies in finding the psychological "fit" between system and trader...   
>    
>  Good success to all!! Let's keep working this one here....
> 
> Ignored

Very nicely stated indeed! I did not trade this Friday for example... thats just my style however, Mer traded and did well. Thats the beauty of this EA. There is a fit for every type of trader within it. Welcome Xaron and have a good weekend everyone!  
  
I know I will since I found out the gender of my unborn child today... its a girl! Its my first. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#180](/thread/post/1937430#post1937430 "Post Permalink")

  * Apr 5, 2008 3:29pm  Apr 5, 2008 3:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Well, congratulations! I see you've made time for other things ![](https://resources.faireconomy.media/images/emojis/64/1f917.png?v=15.1) besides trading ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#181](/thread/post/1937434#post1937434 "Post Permalink")

  * Apr 5, 2008 3:34pm  Apr 5, 2008 3:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar57172_6.gif) forexmoments](forexmoments)

  * | Commercial User  | Joined Dec 2007 | [1,927 Posts](/search?do=process&provider=Member&searchuser=57172)

> [Quoting Chartist](/thread/post/1937378#post1937378 "View Quoted Post")
> 
> Disliked
> 
> I know I will since I found out the gender of my unborn child today... its a girl! Its my first. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)
> 
> Ignored

Aww bless! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#182](/thread/post/1937460#post1937460 "Post Permalink")

  * Apr 5, 2008 5:15pm  Apr 5, 2008 5:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Well actually I've used the EA from FXTradePro last year and had once a trade which went past progression level 21 in the EUR/JPY. So yes, it's not for the faint hearted. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#183](/thread/post/1937532#post1937532 "Post Permalink")

  * Apr 5, 2008 8:25pm  Apr 5, 2008 8:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

BTW: I think FXTradePro's "Lucky 7" setup is really great. The progression ends at level 7 but you use a SL of 30 and a TP of 120. The loss after 7 levels is only 2.5 times higher than the win you can create (you get $1,000 on level 7 and can lose $2,500). That's great for such a semi-martingale approach - at least compared to the 24 level progression thing. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#184](/thread/post/1937659#post1937659 "Post Permalink")

  * Apr 6, 2008 12:27am  Apr 6, 2008 12:27am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

I have heard of that progression... but haven't seen it... can you post the lots sizes? an the 30/120 is just for the EJ correct?  
  
Thanks!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#185](/thread/post/1937671#post1937671 "Post Permalink")

  * Apr 6, 2008 12:37am  Apr 6, 2008 12:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Progression: 0.19; 0.24; 1.05; 1.31; 1.64; 2.05; 2.56  
  
This should work with the cable and GBP/JPY as well. The SL/TP ratio has to be 1:4 as usual, so 20/80 or 30/120 or 40/160...  
  
10/40 is too tight to use it with 4 levels only.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#186](/thread/post/1937675#post1937675 "Post Permalink")

  * Apr 6, 2008 12:41am  Apr 6, 2008 12:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar43563_7.gif) FXTradepro](fxtradepro)

  * | Commercial User  | Joined Jul 2007 | [355 Posts](/search?do=process&provider=Member&searchuser=43563)

If anyone is interested in my "Lucky 7" Set-Up. Please contact me privately and I will direct you to some FREE information on the subject.  
  
Dan 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#187](/thread/post/1937684#post1937684 "Post Permalink")

  * Apr 6, 2008 12:53am  Apr 6, 2008 12:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Dan, it's very nice to see you here again! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) I have to thank you for all your effort you've done and I hope you're doing well! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
OT: Is there a reason why your forum is read only now? There were some really nice threads last year...  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#188](/thread/post/1937695#post1937695 "Post Permalink")

  * Apr 6, 2008 1:07am  Apr 6, 2008 1:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar43563_7.gif) FXTradepro](fxtradepro)

  * | Commercial User  | Joined Jul 2007 | [355 Posts](/search?do=process&provider=Member&searchuser=43563)

Hi Xaron...........All is quite well with me. Thanks for asking. The Forum has become "read-only' primarily because interest in the ideas presented was not as strong as I had hoped. It seemed to me that MOST people wanted all the answers handed to them and did not really want to learn to trade the method without me telling them EXACTLY what to do. At one point I actually closed the Forum, however, there were and still are several Members that are actively Trading the method. These people asked me to keep things running so that they could reference the materials whenever they wanted to. I agreed and still offer support via email for the SERIOUS Trader.  
  
Please feel free to keep in touch.  
  
Regards, 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#189](/thread/post/1937705#post1937705 "Post Permalink")

  * Apr 6, 2008 1:31am  Apr 6, 2008 1:31am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Thanks Xaron & FXTP.... Xaron, are you trading on a time start? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#190](/thread/post/1938202#post1938202 "Post Permalink")

  * Apr 7, 2008 12:12am  Apr 7, 2008 12:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

It depends. You just need volatility. Due to the higher stop (30 pips) you don't switch the position so often.  
  
I think the best would be to use a high volatile session like London combined with a support/resistance.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#191](/thread/post/1938973#post1938973 "Post Permalink")

  * Apr 7, 2008 2:11pm  Apr 7, 2008 2:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Hey everyone, I know it's a little off topic but I've posted my PowerSwing strategy in the Trading Systems forum if anyone has an interest. This is my primary system I trade and will be trading the EA along side this strategy as a supplemental trading account. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#192](/thread/post/1939237#post1939237 "Post Permalink")

  * Apr 7, 2008 6:30pm  Apr 7, 2008 6:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Thanks for sharing the other strategy! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) It's too complicated for me. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) That doesn't mean that it don't work, but it's not for me. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
BTW: I've started to code my own progression EA. I'd like to add something like a breakout OCO (once cancels the other) order. So you can set 2 price levels above and below the current price where the progression shall start. If one of the orders got filled the other will be removed.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#193](/thread/post/1939775#post1939775 "Post Permalink")

  * Apr 8, 2008 12:50am  Apr 8, 2008 12:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Great idea Xaron, let us know how it works out.   
  
My Eur/Usd closed out around 3:30 a.m. est. but the other two are still going probably due to the big early run up around 00:00 GMT which exhausted itself at our time of entry. I will update you later. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/101137?d=1207583385) 7 KB | 308 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#194](/thread/post/1940063#post1940063 "Post Permalink")

  * Apr 8, 2008 3:56am  Apr 8, 2008 3:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

My Usd/Jpy and Usd/Chf have went past there end times and will restart tomorrow morning. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#195](/thread/post/1940148#post1940148 "Post Permalink")

  * Apr 8, 2008 4:51am  Apr 8, 2008 4:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Yep, I'll post the EA here if it's ready. This will take some time. I'm a professional programmer but have only limited time... ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
If you have any ideas you want to have build in, please let me know.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#196](/thread/post/1940328#post1940328 "Post Permalink")

  * Apr 8, 2008 7:19am  Apr 8, 2008 7:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Hey Mer, yep gotta make time for love and peace! ![](https://resources.faireconomy.media/images/emojis/64/270c-fe0f.png?v=15.1) lol!  
thanks for that forexmoments, we do feel really blessed!  
  
Okay, back to this exciting strategy...  
  
I did not take any trades this morning London, so will see if I can justify entry tomorow! Happy trading everyone! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#197](/thread/post/1940377#post1940377 "Post Permalink")

  * Apr 8, 2008 8:15am  Apr 8, 2008 8:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Amen brother, that's why after trading intraday for 8-10 months straight with 3-4 hours sleep I had to change to something different to get the time to do things with the family. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#198](/thread/post/1940642#post1940642 "Post Permalink")

  * Apr 8, 2008 1:52pm  Apr 8, 2008 1:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

I just skimmed through your swing system right now for the 1st time and trying to wrap my grey matter around it! Sounds really interesting though!  
  
I will give it a more in-depth look and possibly demo try tomorow! Thanks for posting it! I may post over there as well!  
  
P.S. You're not the only one! Its a wonder I haven't burned my retinas out gazing at charts the last 3 years I've been trading! ![](https://resources.faireconomy.media/images/emojis/64/1f633.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#199](/thread/post/1940646#post1940646 "Post Permalink")

  * Apr 8, 2008 1:57pm  Apr 8, 2008 1:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

feel free to try it out because it works out great for me because I run a business during the day and this systems makes it so much easier for me to free up time. Any questions about it just let me know ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#200](/thread/post/1941396#post1941396 "Post Permalink")

  * Apr 8, 2008 9:32pm  Apr 8, 2008 9:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Good morning everyone, here are the results for 4/8/2008. Eur/Usd closed out like normal but then I encountered another glitch with Usd/Jpy and Usd/Chf. When the EA hit the end time and finished up trading on both pairs, I turned off my computer to do some maintenance on it and then I restarted it before the EA was to re-enter trading at the start time. It did not start where it left off but started a fresh sequence from .1 lots instead ![](https://resources.faireconomy.media/images/emojis/64/1f615.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/2753.png?v=15.1). I've e-mailed my coder to see if there are any resetting issues to be dealt with and will let you all know. I guess that's why they call it testing, right ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1). 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/101376?d=1207657747) 18 KB | 288 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#201](/thread/post/1941761#post1941761 "Post Permalink")

  * Apr 9, 2008 12:26am  Apr 9, 2008 12:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Sounds like you have it tweaked to fit your lifestyle! Thats what I like about fx, there is a fit for everyone. Problem is figuring it out. Once you go through the learning curve, its really nice.  
  
I haven't noticed that glitch because I use a remote trading desktop on a 24/7 supervised server, so I know I will always be up and running. I got that service because I've had problems with my ISP and connection with it falling off at times in the past! That was last year though.  
  
Anyway here are my results for last session:   
  
Opened eur/usd @ 10:00 GMT; 40Pip TP hit at 4th trade in sequence at 13:54 GMT. Third trade was a breakeven trade.  
  
Happy trading everyone! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#202](/thread/post/1942391#post1942391 "Post Permalink")

  * Apr 9, 2008 6:03am  Apr 9, 2008 6:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

PowerSM V.3 is now in post #1. The expert will now check the last order from history once it is restarted to get the last sequence step if the platform is closed or if there are any issues with a power outage. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#203](/thread/post/1944044#post1944044 "Post Permalink")

  * Apr 10, 2008 2:38am  Apr 10, 2008 2:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Good afternoon guys, my Eur/Usd for 4/9/2008 closed out again like normal (ho-hum![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)). I'm going to test the new version tonight on my Usd/Jpy & Usd/Chf pairs as I started my EA and once the trades were placed I shut down the platform. I will restart it tomorrow morning to see if it picks up where it left off this morning. If all is well, I will update the progress tomorrow. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/101784?d=1207762672) 7 KB | 311 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#204](/thread/post/1944179#post1944179 "Post Permalink")

  * Apr 10, 2008 4:31am  Apr 10, 2008 4:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar7751_16.gif) Cobra](cobra)

  * Joined Mar 2006 | Status: Trader | [786 Posts](/search?do=process&provider=Member&searchuser=7751)

> [Quoting mer071898](/thread/post/1944044#post1944044 "View Quoted Post")
> 
> Disliked
> 
> Good afternoon guys, my Eur/Usd for 4/9/2008 closed out again like normal (ho-hum![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)). I'm going to test the new version tonight on my Usd/Jpy & Usd/Chf pairs as I started my EA and once the trades were placed I shut down the platform. I will restart it tomorrow morning to see if it picks up where it left off this morning. If all is well, I will update the progress tomorrow.
> 
> Ignored

Hi  
Could you please tell me or refer me to a thread where it is explained how to upload an ea to my mt4 platform and how to activate it. Many thanks.  
  
Cobra 

Never Ever Give Up!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#205](/thread/post/1944283#post1944283 "Post Permalink")

  * Apr 10, 2008 6:10am  Apr 10, 2008 6:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

all you have to do is download the EA from post #1, then watch this:  
  

Inserted Video

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#206](/thread/post/1945808#post1945808 "Post Permalink")

  * Apr 11, 2008 1:00am  Apr 11, 2008 1:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Ok, now that all the bugs are out I'm going to start a fresh test on these 5 pairs:  
  
Eur/Usd  
Usd/Jpy  
Usd/Chf  
Eur/Chf  
Gbp/Usd  
  
The pairs will use a 40 pip TP, 30 pip BE, and 10 pip stop except Gbp/Usd will use 60/45/15 with 100k devoted to each pair at 200:1 leverage. I will also adjust the start time to 05:00 which currently is 12:00 Est. or 06:00 GMT with a stop time of 16:00 which is 11:00 Est. or 17:00 GMT. You will have to adjust your inputs to match your broker's time. Here are the first nights results for 4/10/2008. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/102045?d=1207842917) 3 KB | 314 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#207](/thread/post/1945897#post1945897 "Post Permalink")

  * Apr 11, 2008 1:48am  Apr 11, 2008 1:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

eur/usd: opened at 12:30 GMT and closed out tp40 at 13:40 GMT on the 10th trade in the sequence. I could have let it run another sequence and would have gotten another 40pips but discipline won't let me! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#208](/thread/post/1946600#post1946600 "Post Permalink")

  * Apr 11, 2008 11:03am  Apr 11, 2008 11:03am 

  * [ jones247](jones247)

  * | Joined Aug 2007  | Status: Trader | [264 Posts](/search?do=process&provider=Member&searchuser=46344)

Mer,  
  
Your efforts and the EA provided are well appreciated. Keep up the good work...  
  
Walt 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#209](/thread/post/1946629#post1946629 "Post Permalink")

  * Apr 11, 2008 11:35am  Apr 11, 2008 11:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Keep up the good work chartist, I think Eur/Usd is the perfect pair for this baby, never had a problem finishing yet!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
Hey Walt, thanks for the comments, had you tried the EA out? I also stuck my PowerSwing day trading strategy up also. If you get bored, I'd wouldn't mind hearing what you think about it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#210](/thread/post/1947335#post1947335 "Post Permalink")

  * Apr 11, 2008 9:04pm  Apr 11, 2008 9:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Used your EA today in my live account. Did work very well on the EUR/USD. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Just a question. Do I have to disable the EA over the weekend, as it might try to open a position tomorrow which will lead to errors?  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#211](/thread/post/1947366#post1947366 "Post Permalink")

  * Apr 11, 2008 9:19pm  Apr 11, 2008 9:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

If it's on a timed entry it won't open a position until the market opens back up at whatever times you have it set for. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#212](/thread/post/1947368#post1947368 "Post Permalink")

  * Apr 11, 2008 9:21pm  Apr 11, 2008 9:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Ah I see. Yes I use a time entry.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#213](/thread/post/1947390#post1947390 "Post Permalink")

  * Apr 11, 2008 9:35pm  Apr 11, 2008 9:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Not a problem, you know, just to feel safe you can always turn the EA off on the platform if it'll make you feel better ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1). I don't know if you'd mind but maybe you can help post your trade statement (blocking out the info of course) so other can see how it's doing on a live account.   
  
What size, leverage, pair or pairs, and broker are you using? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#214](/thread/post/1947406#post1947406 "Post Permalink")

  * Apr 11, 2008 9:46pm  Apr 11, 2008 9:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Sure. I use Alpari UK. Currently I trade only the EUR/USD but think about to use the Lucky-7-Setup on the EUR/JPY as well...  
  
I use my own progression system. So I'll end up always with about $40.  
  
Regards - Xaron 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 110408.png
Size: 11 KB](/attachment/image/102290/thumbnail?d=1365541065)](/attachment/image/102290?d=1207917958)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#215](/thread/post/1947630#post1947630 "Post Permalink")

  * Apr 11, 2008 11:35pm  Apr 11, 2008 11:35pm 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Sort of the same for me... timed entry... 7gmt... I use a 16 trade progression that yields 20p per day on the EU, for every $5000 in account. Then for the remaining 8 trades, it yields breakeven. This reduces the ultimate risked amount, figuring that we will rarely get beyond 16 trades. If we do, I am content to breakeven vs. have a higher risked amount...  
  
I use FXDD. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#216](/thread/post/1947760#post1947760 "Post Permalink")

  * Edited 12:52am  Apr 12, 2008 12:38am | Edited 12:52am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

WOW!!! My EU just ran it's 24 trade sequence this morning for a complete losing sequence?? 7gmt timed entry, 24 losses... go figure??  
  
6gmt entry would have won on the first or second entry, depending on buy/sell ..... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#217](/thread/post/1947908#post1947908 "Post Permalink")

  * Apr 12, 2008 1:59am  Apr 12, 2008 1:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Thanks Xaron, that's what it's all about, the ability to adapt this to your own trading style.  
  
mrkam, sorry to here you hit 24. Strange, I've never gone past 9-10 levels on my Eur/Usd. I don't know what your settings are but to go that far on this pair something might need to be adjusted a touch. I know I've adjusted my entry time to start an hour before the Frankfurt open and seems to work out great.  
  
Results for Friday 4/11/2008 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/102345?d=1207933150) 6 KB | 303 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#218](/thread/post/1947947#post1947947 "Post Permalink")

  * Apr 12, 2008 2:18am  Apr 12, 2008 2:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar65141_7.gif) Postrock](postrock)

  * | Joined Mar 2008  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=65141)

> [Quoting Xaron](/thread/post/1947406#post1947406 "View Quoted Post")
> 
> Disliked
> 
> Sure. I use Alpari UK. Currently I trade only the EUR/USD but think about to use the Lucky-7-Setup on the EUR/JPY as well...  
>    
>  I use my own progression system. So I'll end up always with about $40.  
>    
>  Regards - Xaron
> 
> Ignored

nice one..did this kind of setup ever fail a progression yet on eurusd? If yes how many times does it succeed against the times it doesnt? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#219](/thread/post/1948003#post1948003 "Post Permalink")

  * Apr 12, 2008 2:58am  Apr 12, 2008 2:58am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Yea, Mer, kind of a bummer! Settings are default, 10SL, 40TP, using your 30 breakeven etc... starting at 7gmt... (I thought 7gmt was an hour before Frankfurt??? if not, my miscalc....) What is your gmt start time, and do you change for Standard/DST??  
  
I could post the screenshot, but it might be too painful!!  
  
But to answer somebodies question, YES IT CAN HAPPEN!!! It did, last night... but maybe the time was wrong, even at that, I would say it STILL can happen... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#220](/thread/post/1948038#post1948038 "Post Permalink")

  * Apr 12, 2008 3:36am  Apr 12, 2008 3:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar15241_4.gif) juxta14](juxta14)

  * | Joined Aug 2006  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=15241)

> [Quoting mrkam](/thread/post/1948003#post1948003 "View Quoted Post")
> 
> Disliked
> 
> Yea, Mer, kind of a bummer! Settings are default, 10SL, 40TP, using your 30 breakeven etc... starting at 7gmt... (I thought 7gmt was an hour before Frankfurt??? if not, my miscalc....) What is your gmt start time, and do you change for Standard/DST??  
>    
>  I could post the screenshot, but it might be too painful!!  
>    
>  But to answer somebodies question, YES IT CAN HAPPEN!!! It did, last night... but maybe the time was wrong, even at that, I would say it STILL can happen...
> 
> Ignored

  
YES IT HAPPENED last night on my demo also IBFX default EA setting.   
It will surely happen sometime someday, please take caution.  
  
  
>>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#221](/thread/post/1948050#post1948050 "Post Permalink")

  * Apr 12, 2008 3:42am  Apr 12, 2008 3:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

My EA is set to start at 12:00 EST which, if you figure in DST, is 06:00 GMT or the hour before the Frankfurt open. My Eur/Usd closed out 9 minutes before the London open at level 4. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#222](/thread/post/1948067#post1948067 "Post Permalink")

  * Apr 12, 2008 3:58am  Apr 12, 2008 3:58am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

OK, there is the answer!! You closed at level 4. I started one hour later and ran all 24 losses... that is both good and bad!  
  
Good because 6gmt has been consistently winning, but so has 7gmt until today...  
  
Bad, because it proves that even one hour difference can make or break you!! I am (reasonably) sure that perhaps one day it just might be the inverse... 7gmt would be OK, but 6gmt might bust....  
  
Food for though, I guess!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#223](/thread/post/1948136#post1948136 "Post Permalink")

  * Apr 12, 2008 5:03am  Apr 12, 2008 5:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

If it helps, I see Eur/Usd falling soon because of resistance from the 61.8 fib. Of course you never know what the market will throw at you. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eususd current.gif
Size: 52 KB](/attachment/image/102376/thumbnail?d=1365541065)](/attachment/image/102376?d=1207944112)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#224](/thread/post/1948649#post1948649 "Post Permalink")

  * Apr 12, 2008 11:12pm  Apr 12, 2008 11:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

I use 6:00 GMT as well. At the moment this is 08:00 local german time so one hour before Frankfurt open. In winter you have to set it to 7:00 GMT due to daylight saving...  
  
7:00 GMT should work, too. But there is no guarantee of course. Someday it will happen... That's why the best entry might be not a timed one but an important(!) support/resistance level where bulls fight against bears and a breakout in one of the directions will happen...  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#225](/thread/post/1948841#post1948841 "Post Permalink")

  * Apr 13, 2008 4:10am  Apr 13, 2008 4:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

PowerSM V.4 is now posted in first post. When my sequenced stop at my end time (if using timed entry function), a small bug caused the EA to pick up where it left off if outside of the timed entry parameters once I restarted my platform. The CheckForSignals() function has been optimized and is now fixed. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#226](/thread/post/1948846#post1948846 "Post Permalink")

  * Apr 13, 2008 4:18am  Apr 13, 2008 4:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Thanks for posting. Is there a way to use the time entry start without a stop time? If I want to use higher stop and tp settings a trade can last several days... I don't want to stop then, I just want to use the time entry start.  
  
Thanks and best regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#227](/thread/post/1948881#post1948881 "Post Permalink")

  * Apr 13, 2008 5:21am  Apr 13, 2008 5:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Unfortunately I don't think so unless you try setting the end time about a minute before your start time. At least that way when the sequence ends the EA won't immediately enter new sequences like it would if the timed entry and price entry were false. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#228](/thread/post/1948890#post1948890 "Post Permalink")

  * Apr 13, 2008 5:28am  Apr 13, 2008 5:28am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Xaron.... YES it WILL HAPPEN... (7gmt bust...) .and did.... Friday, with a 7gmt start time, ran all 24 losses, and actually a few more just tracking it!! Default settings 10/40, 30pBE etc... all 24 losses...  
  
So we now have it documented!! It will happen at any time really, 6gmt is no guarantee that it will or won't in and of itself...   
  
We need a good entry strategy IN ADDITION to time....  
  
But, that's what we are all here for!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#229](/thread/post/1948908#post1948908 "Post Permalink")

  * Apr 13, 2008 5:57am  Apr 13, 2008 5:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Well said mrkam, In my opinion I believe the hour before the Frankfurt allows the EA to get "setup" sooner because we do have some movement after the Frankfurt open and then if that doesn't hit during that hour hopefully the EA will be aimed in the right direction. I do strongly think using fibs and Murrey levels might help for predicting general direction but the entry can still be fickle. I also thought about lowering my BE way down, say to 15-20, now that the EA will re-enter at the same level if stopped out to see what that might do. Any thoughts? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#230](/thread/post/1948941#post1948941 "Post Permalink")

  * Apr 13, 2008 7:07am  Apr 13, 2008 7:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

I did not trade on Friday because of the lack of fundamentals during London... I'm not a fan of entering during NY with this EA either.  
  
Good rule of thumb is.... if there is no critical news coming out and especially on Fridays... don't use this EA that day. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#231](/thread/post/1949271#post1949271 "Post Permalink")

  * Apr 13, 2008 6:29pm  Apr 13, 2008 6:29pm 

  * [ etypejag](etypejag)

  * | Joined Jan 2007  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=29922)

Hi mer...  
Could I ask a question, and I apologise in advance if this has been covered elsewhere.  
Can I change the lot sizes to start at 0.01 instead of 0.1?  
If so, do I alter all in the 'Lots Progression' sector of Inputs.  
  
Also I was running the demo V.2 on Alpari last week (using default settings) and Friday was a winner only going to 0.6 lots so nowhere near 24th level.  
  
Cheers  
Marek 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#232](/thread/post/1949377#post1949377 "Post Permalink")

  * Edited 11:29pm  Apr 13, 2008 10:59pm | Edited 11:29pm 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Hi Marek! I think we have a mutual friend!!   
  
Yea, very easy. It will trade .01 just fine... if your account does, of course. And you can change both the progression lot sizes and number of trades just by editing that input. Just type in new numbers, seperated by a ";". So,, .01;.01;.03 would be just a three trade sequence, then stop, with the lot sizes shown....  
  
If Alpari did not bust, then we have another "issue". I trade FXDD. Could this be "broker dependent??. Probably not, I bet your start time was 6gmt, not 7gmt like mine.... It busted. No doubt about it, see the screenshot below... We HAVE to be aware that it can (and DID!) happen.... Screen shots below... (I stopped it after 20 losses, but tracked a bunch more, over 24!) 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: powersm_24_losses.gif
Size: 35 KB](/attachment/image/102591/thumbnail?d=1365541092)](/attachment/image/102591?d=1208096916)   
[![Click to Enlarge

Name: powersm_24_losses2.gif
Size: 55 KB](/attachment/image/102592/thumbnail?d=1365541092)](/attachment/image/102592?d=1208096916)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#233](/thread/post/1949394#post1949394 "Post Permalink")

  * Apr 13, 2008 11:27pm  Apr 13, 2008 11:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar43563_7.gif) FXTradepro](fxtradepro)

  * | Commercial User  | Joined Jul 2007 | [355 Posts](/search?do=process&provider=Member&searchuser=43563)

> [Quoting mrkam](/thread/post/1949377#post1949377 "View Quoted Post")
> 
> Disliked
> 
> .......... It busted. No doubt about it, see the screenshot below... We HAVE to be aware that it can (and DID!) happen.... Screen shots below... (I stopped it after 20 losses, but tracked a bunch more, over 24!)
> 
> Ignored

Hello Mark and everyone else.......As the creator of this Stratgey, I have likely been trading this concept longer than anyone else so please understand that the use of a TIMED ENTRY without any other consideration will eventually lose. Price Action is the key to finding a good entry in ADDITION to time and other factors such as, do we expect volatility due to upcoming news, etc. Traders cannot just enter ramdomly during a particular session. This is a recipe for disaster.  
  
GOOD TRDAING !  
  
Dan 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#234](/thread/post/1949447#post1949447 "Post Permalink")

  * Edited 1:04am  Apr 14, 2008 1:01am | Edited 1:04am 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting Chartist](/thread/post/1948941#post1948941 "View Quoted Post")
> 
> Disliked
> 
> I did not trade on Friday because of the lack of fundamentals during London... I'm not a fan of entering during NY with this EA either.  
>    
>  Good rule of thumb is.... if there is no critical news coming out and especially on Fridays... don't use this EA that day.
> 
> Ignored

  
I agree with you and Dan (FXTradepro), if there is no critical news coming out turn off this EA. I have let this EA run all the time and have not lost yet but can't stomach the huge dd, I don't like this EA during the NY session either.....Dan 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#235](/thread/post/1949462#post1949462 "Post Permalink")

  * Apr 14, 2008 1:44am  Apr 14, 2008 1:44am 

  * [ etypejag](etypejag)

  * | Joined Jan 2007  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=29922)

Hi MrKam,  
Yes we do have a mutual friend!!  
He has just gone to France and has phoned me for your email and to help set up his trading PC.  
Regarding the trades on Friday; You seem to have started a lot later than me. My winning trade took place at 08:08 on Alpari's time (buy@1.5776 closing at 08:55 @1.5816). So I was all done and dusted before you!  
  
Cheers  
Marek 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#236](/thread/post/1950217#post1950217 "Post Permalink")

  * Apr 14, 2008 1:49pm  Apr 14, 2008 1:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

> [Quoting qz10cq](/thread/post/1949447#post1949447 "View Quoted Post")
> 
> Disliked
> 
> I agree with you and Dan (FXTradepro), if there is no critical news coming out turn off this EA. I have let this EA run all the time and have not lost yet but can't stomach the huge dd, I don't like this EA during the NY session either.....Dan
> 
> Ignored

Yeah, I won't be trading this London session either! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#237](/thread/post/1950603#post1950603 "Post Permalink")

  * Apr 14, 2008 7:18pm  Apr 14, 2008 7:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Hi,  
  
today I've tried the Lucky 7 setup with a SL of 20 and a TP of 80 in the EUR/JPY. TP was reached in the 4th progression level. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
I used a price entry - short below a support level in the hourly chart. I've attached the statement.  
  
Regards - Xaron 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 140408.png
Size: 5 KB](/attachment/image/102793/thumbnail?d=1365541149)](/attachment/image/102793?d=1208168326)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#238](/thread/post/1950897#post1950897 "Post Permalink")

  * Apr 14, 2008 10:44pm  Apr 14, 2008 10:44pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Xaron](/thread/post/1950603#post1950603 "View Quoted Post")
> 
> Disliked
> 
> Hi,  
>    
>  today I've tried the Lucky 7 setup with a SL of 20 and a TP of 80 in the EUR/JPY. TP was reached in the 4th progression level. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>    
>  I used a price entry - short below a support level in the hourly chart. I've attached the statement.  
>    
>  Regards - Xaron
> 
> Ignored

Hi Xaron  
What power SM version did you use ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#239](/thread/post/1950937#post1950937 "Post Permalink")

  * Apr 14, 2008 11:25pm  Apr 14, 2008 11:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

I used V.3  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#240](/thread/post/1950957#post1950957 "Post Permalink")

  * Apr 14, 2008 11:37pm  Apr 14, 2008 11:37pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Xaron](/thread/post/1950937#post1950937 "View Quoted Post")
> 
> Disliked
> 
> I used V.3  
>    
>  Regards - Xaron
> 
> Ignored

Woow, you have changed avatar ! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#241](/thread/post/1951158#post1951158 "Post Permalink")

  * Apr 15, 2008 2:14am  Apr 15, 2008 2:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here's are the results for Monday 4/14/2008 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/102887?d=1208193225) 8 KB | 300 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#242](/thread/post/1951175#post1951175 "Post Permalink")

  * Apr 15, 2008 2:30am  Apr 15, 2008 2:30am 

  * [ tvanny](tvanny)

  * | Joined Sep 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=48715)

Hi Mer,  
I was using V4 today on my GBP/JPY trade. It closed out on the 4th entry but then reopened a new series instantly. I was using a timed entry of 0700. I was wondering if anyone else xperienced this with V4?  
  
Thanks,  
Tom 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#243](/thread/post/1951235#post1951235 "Post Permalink")

  * Apr 15, 2008 3:48am  Apr 15, 2008 3:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I'll have to talk to my coder, this was supposed to be fixed in V.3 but he must have changed something in V.4, sorry. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#244](/thread/post/1951681#post1951681 "Post Permalink")

  * Apr 15, 2008 12:04pm  Apr 15, 2008 12:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

The only thing my coder said he fixed in V.4 was the CheckForSignals() function of the EA. I had V.4 on my platform last night and it did not re-enter any new sequences for me. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#245](/thread/post/1952072#post1952072 "Post Permalink")

  * Apr 15, 2008 5:31pm  Apr 15, 2008 5:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Today was easy. My first entry in the EUR/USD reached its goal. I've used a price entry: support in the hourly chart.  
  
Regards - Xaron 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 150408.png
Size: 3 KB](/attachment/image/103096/thumbnail?d=1365541214)](/attachment/image/103096?d=1208248301)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#246](/thread/post/1952209#post1952209 "Post Permalink")

  * Apr 15, 2008 6:55pm  Apr 15, 2008 6:55pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Xaron](/thread/post/1952072#post1952072 "View Quoted Post")
> 
> Disliked
> 
> Today was easy. My first entry in the EUR/USD reached its goal. I've used a price entry: support in the hourly chart.  
>    
>  Regards - Xaron
> 
> Ignored

Very nice, Xaron.  
Finally , you use a TP of 40 or 60 ?  
Regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#247](/thread/post/1952229#post1952229 "Post Permalink")

  * Apr 15, 2008 7:16pm  Apr 15, 2008 7:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

For the EUR/USD I use 10/40, for the EUR/JPY I use 20/80.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#248](/thread/post/1952258#post1952258 "Post Permalink")

  * Apr 15, 2008 7:42pm  Apr 15, 2008 7:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Do you use support resistance but enter at any time, or do you mind your time of day also? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#249](/thread/post/1952263#post1952263 "Post Permalink")

  * Apr 15, 2008 7:48pm  Apr 15, 2008 7:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

I enter at s/r during the London session. If it doesn't happen there I remove the order.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#250](/thread/post/1952413#post1952413 "Post Permalink")

  * Apr 15, 2008 9:55pm  Apr 15, 2008 9:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Hey Mer! The EA V4 was done with its sequence at take profit and then all of a sudden, it opened up another sequence. Here are the details:  
  
Opened at 8:00 GMT eur/usd and closed with TP at 12:00 GMT on 8th trade. Then at 12:40 GMT EA took off by itself and I manually shutdown EA and closed 1st trade in sequence for small TP at 12:44 GMT.  
  
Looks like a bug on this one. Take care! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#251](/thread/post/1952417#post1952417 "Post Permalink")

  * Apr 15, 2008 9:58pm  Apr 15, 2008 9:58pm 

  * [ tvanny](tvanny)

  * | Joined Sep 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=48715)

> [Quoting mer071898](/thread/post/1951681#post1951681 "View Quoted Post")
> 
> Disliked
> 
> The only thing my coder said he fixed in V.4 was the CheckForSignals() function of the EA. I had V.4 on my platform last night and it did not re-enter any new sequences for me.
> 
> Ignored

Thanks. I'll have to check my settings again. The only thing that I did was set the slippage setting to zero to see what happens. That's the only thing I can think of. My GBP/JPY trade did it again today. Closed on the 2nd entry, and then opened another series right away (and chewed up 11 levels). I guess I'll redownload it again and start over. What does the slippage setting do again? I know what slippage is, I'm just not sure what the slippage setting does. If the spread is 5 and I put the slippage setting on 3, does that mean if the spread widens larger then 8 during a news event, or something, the EA won't enter any orders until the spread falls below 8?  
thanks,  
Tom 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#252](/thread/post/1952422#post1952422 "Post Permalink")

  * Apr 15, 2008 10:00pm  Apr 15, 2008 10:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

> [Quoting Xaron](/thread/post/1952263#post1952263 "View Quoted Post")
> 
> Disliked
> 
> I enter at s/r during the London session. If it doesn't happen there I remove the order.  
>    
>  Regards - Xaron
> 
> Ignored

Ok. Do you use natural s/r or do you use the calculated pivots or both? Also, what time frame do you use?   
  
I personally like the 4h time frame for s/r and I look for price action at those natural and calculated pivots in my regular trading.  
  
Cheers![](https://resources.faireconomy.media/images/emojis/64/270c-fe0f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#253](/thread/post/1952426#post1952426 "Post Permalink")

  * Apr 15, 2008 10:03pm  Apr 15, 2008 10:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Yes, 4h s/r looks good. Usually I use the hourly timeframe and just simple 1-2-3 patterns to enter (higher highs, higher lows and vice versa).  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#254](/thread/post/1952535#post1952535 "Post Permalink")

  * Apr 15, 2008 11:01pm  Apr 15, 2008 11:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I have him look at it again, in the mean time just use V.3 on post #1. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#255](/thread/post/1952762#post1952762 "Post Permalink")

  * Apr 16, 2008 1:09am  Apr 16, 2008 1:09am 

  * [ indianguyinny24](indianguyinny24)

  * | Joined Jul 2007  | Status: Trader | [2,994 Posts](/search?do=process&provider=Member&searchuser=43649)

I followed this Semi martingale approach but at some time i remember it happened twice on EUR JPY it tooked me down like 25 trades   
and i got A MARGIN CALL THANK GOD it was demo.  
  
But i think this is a great EA .... if there is one change a person can code...i.e. rather then buying and selling...   
Let the EA also add only do one way trading i.e to Buy or Sell ...  
  
so if a person wants he can only trade for Buy side with the lot size as this approach...   
  
I have still to find one instance on EUR JPY with this that it would go beyoind 10 th loss..  
  
  
just my thoughts  
  
  
  
V 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#256](/thread/post/1952933#post1952933 "Post Permalink")

  * Apr 16, 2008 3:07am  Apr 16, 2008 3:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

@indianguy: Check out this thread (the postings and EA from Rama!): <http://www.forexfactory.com/showthread.php?t=65869>  
  
I use this method in a second account with great success. Make about 10-30% per month so far. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#257](/thread/post/1953034#post1953034 "Post Permalink")

  * Apr 16, 2008 4:06am  Apr 16, 2008 4:06am 

  * [ indianguyinny24](indianguyinny24)

  * | Joined Jul 2007  | Status: Trader | [2,994 Posts](/search?do=process&provider=Member&searchuser=43649)

Xaron,   
  
I just want to say only go long with this system . Can i do it with any EA .... i saw those and it seems to be going long and short ...whereas i just want to go long...  
  
  
Thanks  
  
V 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#258](/thread/post/1953572#post1953572 "Post Permalink")

  * Edited Apr 17, 2008 5:23am  Apr 16, 2008 12:22pm | Edited Apr 17, 2008 5:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I had the same issue last night with the EA entering a new sequence after the first one finished. My coder has now added a function called "RestartNewCycle" to the EA. If you want the EA to start a new sequence immediately after the original sequence closes, enter True, otherwise leave it on the default setting of False. I hope this fixes the problem, if not guys let me know.  
  
I had closed the current sequences on all the pairs that it had re-opened on and removed V.4 from the charts, still made a profit though. V.5 is added to post #1. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/103350?d=1208318416) 11 KB | 287 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#259](/thread/post/1953937#post1953937 "Post Permalink")

  * Apr 16, 2008 5:56pm  Apr 16, 2008 5:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Thanks, that's very helpful. It's like the hibernation mode?  
  
From now on I'll use simple price entries. I already use a 5m scalping entry technique which should be a very good entry for this approach here as well. It should reach its target in the first levels most of the time:  
  
<http://www.forexfactory.com/showthread.php?t=11854>  
  
The good thing is that you don't need a very good timing...  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#260](/thread/post/1954037#post1954037 "Post Permalink")

  * Apr 16, 2008 7:00pm  Apr 16, 2008 7:00pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Xaron](/thread/post/1953937#post1953937 "View Quoted Post")
> 
> Disliked
> 
> Thanks, that's very helpful. It's like the hibernation mode?  
>    
>  From now on I'll use simple price entries. I already use a 5m scalping entry technique which should be a very good entry for this approach here as well. It should reach its target in the first levels most of the time:  
>    
>  <http://www.forexfactory.com/showthread.php?t=11854>  
>    
>  The good thing is that you don't need a very good timing...  
>    
>  Regards - Xaron
> 
> Ignored

Hi Xaron  
Excellent idea.  
You could post a template with your settings and V5 ?  
Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#261](/thread/post/1954074#post1954074 "Post Permalink")

  * Apr 16, 2008 7:23pm  Apr 16, 2008 7:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Hmm... I think there is no need for a template. I just use the 3 moving averages, nothing more...  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#262](/thread/post/1954397#post1954397 "Post Permalink")

  * Apr 16, 2008 11:04pm  Apr 16, 2008 11:04pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Congratulations mer071898 for your EA.  
Maybe could you include in the left corner of the screen some informations about the number of trades in the sequence and the balance of the sequence.  
Regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#263](/thread/post/1954942#post1954942 "Post Permalink")

  * Apr 17, 2008 5:26am  Apr 17, 2008 5:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here are the statements for 4/16/2008 I got a little late of a start as I didn't get back home from a personal function til early this morning, sorry. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/103554?d=1208377571) 10 KB | 302 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#264](/thread/post/1956110#post1956110 "Post Permalink")

  * Apr 17, 2008 8:26pm  Apr 17, 2008 8:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Another successful day with the entry technique I've described. I think I'll switch to the Lucky-7-setup in the EUR/USD using 10/40 settings. Should work most of the time.  
  
Regards - Xaron 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eurusd_170408.png
Size: 10 KB](/attachment/image/103760/thumbnail?d=1365541360)](/attachment/image/103760?d=1208431569)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#265](/thread/post/1956123#post1956123 "Post Permalink")

  * Apr 17, 2008 8:34pm  Apr 17, 2008 8:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

I'll use this sequence using my entry technique from now on. I'll use it on the EUR/USD primary. The risk/reward is great for such a strategy. Even if I lose a sequence I only need two winners to recover. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Regards - Xaron 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: lucky7_10_40.png
Size: 31 KB](/attachment/image/103761/thumbnail?d=1365541360)](/attachment/image/103761?d=1208432020)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#266](/thread/post/1956156#post1956156 "Post Permalink")

  * Apr 17, 2008 8:52pm  Apr 17, 2008 8:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

New entry, reached its target in the first progression. I love it. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
Regards - Xaron 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eurusd_170408_2.png
Size: 10 KB](/attachment/image/103770/thumbnail?d=1365541360)](/attachment/image/103770?d=1208433175)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#267](/thread/post/1956344#post1956344 "Post Permalink")

  * Apr 17, 2008 10:19pm  Apr 17, 2008 10:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

BTW: There is a mistake in my lucky-7-sequence. You must divide the lot size by 10 as the pip value is $10 and not $1...  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#268](/thread/post/1956380#post1956380 "Post Permalink")

  * Apr 17, 2008 10:36pm  Apr 17, 2008 10:36pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Xaron](/thread/post/1956344#post1956344 "View Quoted Post")
> 
> Disliked
> 
> BTW: There is a mistake in my lucky-7-sequence. You must divide the lot size by 10 as the pip value is $10 and not $1...  
>    
>  Regards - Xaron
> 
> Ignored

Hi Xaron  
Logically, what could be the continuation of the sequence after the 7th entry ?  
Regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#269](/thread/post/1956383#post1956383 "Post Permalink")

  * Apr 17, 2008 10:38pm  Apr 17, 2008 10:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

I don't know. But the risk/rewards becomes worse then...  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#270](/thread/post/1956644#post1956644 "Post Permalink")

  * Apr 18, 2008 12:41am  Apr 18, 2008 12:41am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Hi Xaron.... can you clarify your 5m entry concept? I checked the thread you referenced earlier, which is pretty dang complicated... looks like you just use the 3 ma, but do you use a simple cross? or all the variaus slope criterea in the thread...  
  
thanks for the idea! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#271](/thread/post/1956959#post1956959 "Post Permalink")

  * Apr 18, 2008 3:58am  Apr 18, 2008 3:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar43563_7.gif) FXTradepro](fxtradepro)

  * | Commercial User  | Joined Jul 2007 | [355 Posts](/search?do=process&provider=Member&searchuser=43563)

> [Quoting Xaron](/thread/post/1956123#post1956123 "View Quoted Post")
> 
> Disliked
> 
> I'll use this sequence using my entry technique from now on. I'll use it on the EUR/USD primary. The risk/reward is great for such a strategy. Even if I lose a sequence I only need two winners to recover. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>    
>  Regards - Xaron
> 
> Ignored

  
Hey Xaron......If you modify the TP to 50 Pips your risk/reward will improve even more. That assumes that you feel your entry technique can get you 50 pips instead of 40.  
  
Good Trading !  
  
Dan 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#272](/thread/post/1957273#post1957273 "Post Permalink")

  * Apr 18, 2008 7:06am  Apr 18, 2008 7:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here are the result for 4/17/2008. I don't know why it happened but my Usd/Jpy & Usd/Chf reloaded itself around 4:39-4:50 this morning but did not continue with the sequence and the logs kept saying "invalid stops" after the reload. The other three pairs worked just fine so I'll have to look into it. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/103984?d=1208469965) 114 KB | 352 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#273](/thread/post/1957411#post1957411 "Post Permalink")

  * Apr 18, 2008 8:56am  Apr 18, 2008 8:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Hi Mer! Thank you for posting V.5. So far, I haven't encountered any bugs with it however, I have only traded the eur/usd with it and it did not re-enter upon TP reached. Granite, I had the continue option set to false, maybe I'll try setting it to true to check it out!  
  
Xaron, good job man! I entered eur/usd off the pin bar at 7:45am GMT and hit my TP at 40 on the second trade!  
  
Hypothetically somebody could have played the (riskier) pin bar as I did then, played your trades. That would have been 3 trades totaling 120 pips. Not bad huh? Good job though! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#274](/thread/post/1958314#post1958314 "Post Permalink")

  * Apr 18, 2008 8:53pm  Apr 18, 2008 8:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Closed my lucky 7 setup in the 2nd progression level. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Regards - Xaron 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eurusd_180408.png
Size: 9 KB](/attachment/image/104161/thumbnail?d=1365541465)](/attachment/image/104161?d=1208519632)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#275](/thread/post/1958317#post1958317 "Post Permalink")

  * Apr 18, 2008 8:54pm  Apr 18, 2008 8:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

> [Quoting mrkam](/thread/post/1956644#post1956644 "View Quoted Post")
> 
> Disliked
> 
> Hi Xaron.... can you clarify your 5m entry concept? I checked the thread you referenced earlier, which is pretty dang complicated... looks like you just use the 3 ma, but do you use a simple cross? or all the variaus slope criterea in the thread...  
>    
>  thanks for the idea!
> 
> Ignored

It's simple. Wait for the 3 MA's to spread out and enter exactly in the middle of the EMA 10 and EMA 21 during a pullback.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#276](/thread/post/1958320#post1958320 "Post Permalink")

  * Apr 18, 2008 8:55pm  Apr 18, 2008 8:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

> [Quoting FXTradepro](/thread/post/1956959#post1956959 "View Quoted Post")
> 
> Disliked
> 
> Hey Xaron......If you modify the TP to 50 Pips your risk/reward will improve even more. That assumes that you feel your entry technique can get you 50 pips instead of 40.  
>    
>  Good Trading !  
>    
>  Dan
> 
> Ignored

Thanks Dan, this should work as well. Thanks so much for your effort! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#277](/thread/post/1958823#post1958823 "Post Permalink")

  * Apr 19, 2008 12:41am  Apr 19, 2008 12:41am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Thanks Xaron!! do you also have a time frame you enter within? Start looking at 6gmt?? try to catch the new day's movement? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#278](/thread/post/1959010#post1959010 "Post Permalink")

  * Apr 19, 2008 2:33am  Apr 19, 2008 2:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Had to adjust my TP and stop to remove the invalid stop errors. I'm trying out a lower Breakeven level to see if we get more re-enters in the sequence. Here is what they are now:  
  
**_Pair_ _Take Profit_ _Stoploss_ _Breakeven  
  
_**Eur/Usd 48 12 24  
Usd/Jpy 48 12 24  
Usd/Chf 52 13 26  
Eur/Chf 56 14 28  
Gbp/Usd 60 15 30  
  
Results for 4/18/2008. Usd/Chf and Usd/Jpy picked up where they left off 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/104283?d=1208539974) 11 KB | 323 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#279](/thread/post/1959518#post1959518 "Post Permalink")

  * Apr 19, 2008 5:35pm  Apr 19, 2008 5:35pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting mer071898](/thread/post/1959010#post1959010 "View Quoted Post")
> 
> Disliked
> 
> Had to adjust my TP and stop to remove the invalid stop errors. I'm trying out a lower Breakeven level to see if we get more re-enters in the sequence. Here is what they are now:  
>    
>  **_Pair_ _Take Profit_ _Stoploss_ _Breakeven_**  
>    
>  Eur/Usd 48 12 24  
>  Usd/Jpy 48 12 24  
>  Usd/Chf 52 13 26  
>  Eur/Chf 56 14 28  
>  Gbp/Usd 60 15 30  
>    
>  Results for 4/18/2008. Usd/Chf and Usd/Jpy picked up where they left off
> 
> Ignored

Thanks  
And do you keep the same numbers for the sequence ?  
Regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#280](/thread/post/1959738#post1959738 "Post Permalink")

  * Apr 20, 2008 2:30am  Apr 20, 2008 2:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

yes, same lot sequence, just different TP, stop, and breakeven levels. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#281](/thread/post/1959781#post1959781 "Post Permalink")

  * Apr 20, 2008 3:27am  Apr 20, 2008 3:27am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting mer071898](/thread/post/1959738#post1959738 "View Quoted Post")
> 
> Disliked
> 
> yes, same lot sequence, just different TP, stop, and breakeven levels.
> 
> Ignored

OK  
So your favorite sequence is 0.1;0.1;0.2;0.3;0.4;0.6;0.8;1.1;1.5;2.0;2.7;3.6;4.7;etc....  
In your opinion,why is it better than Xaron's ?  
Best regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#282](/thread/post/1959879#post1959879 "Post Permalink")

  * Apr 20, 2008 7:32am  Apr 20, 2008 7:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I never said it was better, Xaron just uses a different setup. This is the original lot sequence from the original EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#283](/thread/post/1960109#post1960109 "Post Permalink")

  * Apr 20, 2008 4:06pm  Apr 20, 2008 4:06pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting mer071898](/thread/post/1959879#post1959879 "View Quoted Post")
> 
> Disliked
> 
> I never said it was better, Xaron just uses a different setup. This is the original lot sequence from the original EA.
> 
> Ignored

Thanks for your explanation.  
Regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#284](/thread/post/1960115#post1960115 "Post Permalink")

  * Apr 20, 2008 4:34pm  Apr 20, 2008 4:34pm 

  * [ sentaco](sentaco)

  * | Membership Revoked  | Joined Jul 2006 | [86 Posts](/search?do=process&provider=Member&searchuser=13725)

Hi all  
Thanks for the EA but did it only Trade for one day? Because i tried Backtest and it opens only trades for the first day.  
  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#285](/thread/post/1960120#post1960120 "Post Permalink")

  * Apr 20, 2008 4:46pm  Apr 20, 2008 4:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

> [Quoting sentaco](/thread/post/1960115#post1960115 "View Quoted Post")
> 
> Disliked
> 
> Hi all  
>  Thanks for the EA but did it only Trade for one day? Because i tried Backtest and it opens only trades for the first day.  
>    
>  Regards
> 
> Ignored

There is a variable called "RestartNewCycle" which prevents a restart.  
  
Please note that backtests are worthless with this EA. It's not an automated system, just a tool. There is a good reason why the EA stops after a sequence. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#286](/thread/post/1961181#post1961181 "Post Permalink")

  * Apr 21, 2008 4:50pm  Apr 21, 2008 4:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Trade #1 successfully done. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Target reached in the first progression...  
  
Regards - Xaron 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: gbpusd_210408.png
Size: 10 KB](/attachment/image/104798/thumbnail?d=1365541572)](/attachment/image/104798?d=1208764219)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#287](/thread/post/1961216#post1961216 "Post Permalink")

  * Apr 21, 2008 5:03pm  Apr 21, 2008 5:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Wohoo... EUR/USD hit its target in the first progression as well.  
  
These were fast 2% today. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Regards - Xaron 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eurusd_210408.png
Size: 10 KB](/attachment/image/104803/thumbnail?d=1365541572)](/attachment/image/104803?d=1208765028)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#288](/thread/post/1961231#post1961231 "Post Permalink")

  * Apr 21, 2008 5:12pm  Apr 21, 2008 5:12pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Yes... nice volatility this morning 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#289](/thread/post/1962518#post1962518 "Post Permalink")

  * Apr 22, 2008 6:22am  Apr 22, 2008 6:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here are my results for 4/21/2008. Very quick night for all pairs. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/105038?d=1208812948) 11 KB | 366 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#290](/thread/post/1963353#post1963353 "Post Permalink")

  * Apr 22, 2008 6:00pm  Apr 22, 2008 6:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

2 Lucky 7 setup finished successfully. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Regards - Xaron 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: eurusd_220408.png
Size: 10 KB](/attachment/image/105216/thumbnail?d=1365541639)](/attachment/image/105216?d=1208854821)   
[![Click to Enlarge

Name: gbpusd_220408.png
Size: 10 KB](/attachment/image/105217/thumbnail?d=1365541639)](/attachment/image/105217?d=1208854821)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#291](/thread/post/1964735#post1964735 "Post Permalink")

  * Apr 23, 2008 7:23am  Apr 23, 2008 7:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Real good job Xaron! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#292](/thread/post/1965005#post1965005 "Post Permalink")

  * Apr 23, 2008 11:31am  Apr 23, 2008 11:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Results for 4/22/2008 all pairs finished except for Usd/Jpy is currently still in a trade. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [PowerSM Statements.zip](/attachment/file/105548?d=1208917871) 14 KB | 424 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#293](/thread/post/1965715#post1965715 "Post Permalink")

  * Apr 23, 2008 8:22pm  Apr 23, 2008 8:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Hi all,  
  
I've done with my first version of the EA.  
  
**ATTENTION: It isn't fully tested yet! Try it on Demo only!**  
  
I've only tested the direct entry, price entry, time entry and OCO entry should work, too.  
  
Could you please test it on a demo account and report any problems? I'll post the source as well when it's production ready. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Regards - Xaron 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Sequencer_v1_0.ex4](/attachment/file/105668?d=1208949676) 26 KB | 458 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#294](/thread/post/1966044#post1966044 "Post Permalink")

  * Apr 23, 2008 10:53pm  Apr 23, 2008 10:53pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Xaron](/thread/post/1965715#post1965715 "View Quoted Post")
> 
> Disliked
> 
> Hi all,  
>    
>  I've done with my first version of the EA.  
>    
>  **ATTENTION: It isn't fully tested yet! Try it on Demo only!**  
>    
>  I've only tested the direct entry, price entry, time entry and OCO entry should work, too.  
>    
>  Could you please test it on a demo account and report any problems? I'll post the source as well when it's production ready. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
>    
>  Regards - Xaron
> 
> Ignored

Thanks Xaron.  
What pair do you advise for try ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#295](/thread/post/1966051#post1966051 "Post Permalink")

  * Apr 23, 2008 10:56pm  Apr 23, 2008 10:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Hmm... It's the same thing. I use it for EUR/USD, EUR/JPY, GBP/USD and USD/JPY.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#296](/thread/post/1966062#post1966062 "Post Permalink")

  * Apr 23, 2008 11:05pm  Apr 23, 2008 11:05pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Xaron](/thread/post/1966051#post1966051 "View Quoted Post")
> 
> Disliked
> 
> Hmm... It's the same thing. I use it for EUR/USD, EUR/JPY, GBP/USD and USD/JPY.  
>    
>  Regards - Xaron
> 
> Ignored

OK, I'm trying actually EURUSD.  
I appreciate the indications (lots,level,...) in the left corner <http://www.forexfactory.com/images/icons/icon12.gif>  
Do you explain the fonction "UseBreakoutEntryOCO" ?  
Good job, Xaron. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#297](/thread/post/1966088#post1966088 "Post Permalink")

  * Apr 23, 2008 11:18pm  Apr 23, 2008 11:18pm 

  * [ Autumm](autumm)

  * | Joined Sep 2006  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=18393)

Hi xaron  
realise that the EA would start a new sequence even if all entry methods are put to false. any way to remedy this? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#298](/thread/post/1966097#post1966097 "Post Permalink")

  * Apr 23, 2008 11:21pm  Apr 23, 2008 11:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Ah Autumm, you're right. That's the direct manual entry. It's the same with mer's EA I think.  
  
@madscalp: Using this option you can enter 2 price levels, upper and lower bounds. That way you can handle breakouts out of a channel. If one is filled the other is removed. Use the reverse flag if you want to sell at the upper side and buy at the lower one...  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#299](/thread/post/1966118#post1966118 "Post Permalink")

  * Apr 23, 2008 11:30pm  Apr 23, 2008 11:30pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Xaron](/thread/post/1966097#post1966097 "View Quoted Post")
> 
> Disliked
> 
> Ah Autumm, you're right. That's the direct manual entry. It's the same with mer's EA I think.  
>    
>  @madscalp: Using this option you can enter 2 price levels, upper and lower bounds. That way you can handle breakouts out of a channel. If one is filled the other is removed. Use the reverse flag if you want to sell at the upper side and buy at the lower one...  
>    
>  Regards - Xaron
> 
> Ignored

OK thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#300](/thread/post/1966292#post1966292 "Post Permalink")

  * Apr 24, 2008 12:44am  Apr 24, 2008 12:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Hi Xaron, okay will try it out and report any bugs if any and results! thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#301](/thread/post/1966329#post1966329 "Post Permalink")

  * Apr 24, 2008 1:05am  Apr 24, 2008 1:05am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

An important bug: the arrows always are green <http://www.forexfactory.com/images/icons/icon10.gif>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#302](/thread/post/1966457#post1966457 "Post Permalink")

  * Apr 24, 2008 2:26am  Apr 24, 2008 2:26am 

  * [ tvanny](tvanny)

  * | Joined Sep 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=48715)

> [Quoting Xaron](/thread/post/1965715#post1965715 "View Quoted Post")
> 
> Disliked
> 
> Hi all,  
>    
>  I've done with my first version of the EA.  
>    
>  **ATTENTION: It isn't fully tested yet! Try it on Demo only!**  
>    
>  I've only tested the direct entry, price entry, time entry and OCO entry should work, too.  
>    
>  Could you please test it on a demo account and report any problems? I'll post the source as well when it's production ready. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
>    
>  Regards - Xaron
> 
> Ignored

Many, many thanks Xaron!  
I use support and resistance levels for my triggers. This will help me immeasurably! I'll let you know how it goes. I wish I had the programming skills to contribute more.   
  
The willingness to give is what I enjoy about these forums.<http://www.forexfactory.com/images/icons/icon7.gif>  
  
Tom 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#303](/thread/post/1966983#post1966983 "Post Permalink")

  * Apr 24, 2008 10:35am  Apr 24, 2008 10:35am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Yes, THANKS Xaron.... Tom, always interested in entries... What time to you look to enter, and are your S/R levels by "eye" or do you use an indicator? If so, which one!! Thanks..... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#304](/thread/post/1967118#post1967118 "Post Permalink")

  * Apr 24, 2008 12:25pm  Apr 24, 2008 12:25pm 

  * [ tvanny](tvanny)

  * | Joined Sep 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=48715)

> [Quoting mrkam](/thread/post/1966983#post1966983 "View Quoted Post")
> 
> Disliked
> 
> Yes, THANKS Xaron.... Tom, always interested in entries... What time to you look to enter, and are your S/R levels by "eye" or do you use an indicator? If so, which one!! Thanks.....
> 
> Ignored

Hi mrKam,  
I wrote up what I usually look for before I trade on one of the earlier pages. I've attatched a chart to show what I look for. I look for periods of low volatility before the Europe open and the put in an order above or below the areas of support/resistance. I've mostly been using timed entries but with the OCO orders I can put on trades above or below resistance.  
  
Tom 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: GPB_USD.JPG
Size: 186 KB](/attachment/image/105925/thumbnail?d=1365541748)](/attachment/image/105925?d=1209007425)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#305](/thread/post/1967372#post1967372 "Post Permalink")

  * Apr 24, 2008 4:07pm  Apr 24, 2008 4:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Thanks! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) Wrong arrow color? Fixed. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
I've attached a new version + the source code. Should be stable.  
  
Regards - Xaron 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Sequencer_v1_1.ex4](/attachment/file/105976?d=1209020843) 26 KB | 487 downloads 

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [sequencer_v1_1.zip](/attachment/file/105977?d=1209020843) 7 KB | 506 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#306](/thread/post/1967663#post1967663 "Post Permalink")

  * Apr 24, 2008 6:35pm  Apr 24, 2008 6:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

You're the man Xaron! thanks so much for that! By the way, here goes the first trade just about an hour ago with your ea: Actually coming up on another possible entry, check it out! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eurlive7.gif
Size: 16 KB](/attachment/image/106004/thumbnail?d=1365541769)](/attachment/image/106004?d=1209029653)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#307](/thread/post/1967727#post1967727 "Post Permalink")

  * Apr 24, 2008 7:13pm  Apr 24, 2008 7:13pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Hi Xaron  
It seems be a problem with several pairs trading.  
If a pair is working, it's impossible to open another trade with another pair.  
I have to close MT4 and open it again : at this moment, the orders are opened ????  
Best regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#308](/thread/post/1967744#post1967744 "Post Permalink")

  * Apr 24, 2008 7:18pm  Apr 24, 2008 7:18pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

I'm thinking about a thing.  
Is it necessary to put the file "info" in the folder "include" ?  
Maybe is it the trouble ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#309](/thread/post/1967746#post1967746 "Post Permalink")

  * Apr 24, 2008 7:18pm  Apr 24, 2008 7:18pm 

  * [ Autumm](autumm)

  * | Joined Sep 2006  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=18393)

there is also a problem with stoptradingaftersqeuence part.  
even if put to false, it will not restart sequence after a successful sequence. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#310](/thread/post/1967747#post1967747 "Post Permalink")

  * Apr 24, 2008 7:20pm  Apr 24, 2008 7:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

@madscalp: I guess it's because of the MagicNumber. Have you changed it for the other pair? Every pair needs its own unique MagicNumber.  
The include files are only needed if you want to compile the EA by yourself.  
  
@Autumm: Thanks, I'll take a look at this.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#311](/thread/post/1967855#post1967855 "Post Permalink")

  * Apr 24, 2008 8:29pm  Apr 24, 2008 8:29pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Xaron](/thread/post/1967747#post1967747 "View Quoted Post")
> 
> Disliked
> 
> @madscalp: I guess it's because of the MagicNumber. Have you changed it for the other pair? Every pair needs its own unique MagicNumber.  
>  The include files are only needed if you want to compile the EA by yourself.  
>    
>  @Autumm: Thanks, I'll take a look at this.  
>    
>  Regards - Xaron
> 
> Ignored

OK, I'm going to change magic number.  
I like a lot that kind of EA.  
All the martingales (Rama, 10p3, etc..) need a retracement against the trend to win.  
And the retracement can occur...... or no.  
I blew up many demo accounts with these martingales.  
This one allows to go with the trend and it's important especially during the news time.  
The only necessary thing is the volatility.  
With good entries and a good management, I believe it can become a great EA.  
Thanks mer071898 and Xaron. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#312](/thread/post/1967995#post1967995 "Post Permalink")

  * Apr 24, 2008 9:52pm  Apr 24, 2008 9:52pm 

  * [ cashearner](cashearner)

  * | Joined Aug 2007  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=46480)

Hi,  
  
I'm trying this EA on MT4 but the following error is coming:  
  
2008.04.24 18:20:31 Sequencer_v1_1 EURUSD,M5: Error: 130 invalid stops SL: 1.57190000 TP: 1.57240000 Retry: 10/10  
  
Can anyone suggest what parameters to change? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#313](/thread/post/1968004#post1968004 "Post Permalink")

  * Apr 24, 2008 9:58pm  Apr 24, 2008 9:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

cashearner, looks like your stop is just too close to the market price. It depends on your broker... What was the entry price?  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#314](/thread/post/1968010#post1968010 "Post Permalink")

  * Apr 24, 2008 10:01pm  Apr 24, 2008 10:01pm 

  * [ cashearner](cashearner)

  * | Joined Aug 2007  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=46480)

Xaron,  
  
Do I have to trade manually or will the EA take the trade Automatically? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#315](/thread/post/1968016#post1968016 "Post Permalink")

  * Apr 24, 2008 10:02pm  Apr 24, 2008 10:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Whatever you want. Use the TimeEntry, PriceEntry or OCO entry. If all 3 are set to false, the EA starts immediately with the next tick.  
  
Please not, it's not intended to use this EA as a completely automated system. It will fail that way. It's only a tool to manage the trades.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#316](/thread/post/1968183#post1968183 "Post Permalink")

  * Edited 11:41pm  Apr 24, 2008 11:14pm | Edited 11:41pm 

  * [ Autumm](autumm)

  * | Joined Sep 2006  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=18393)

1 more problem i am having with the EA is that the time entry function doesnt seem to work right..  
  
when i set entryhour to 5, it will still start off the progression straight.  
is there a format for the timing ?? i tried double digits hours works fine. only single digits hour gives the problem.  
  
i think i found out whats wrong. For example its 14:00 now. time entry only works when u input timing above 14:00. anything below and it will start off the sequence straight away. anyway to go fix this? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#317](/thread/post/1968375#post1968375 "Post Permalink")

  * Apr 25, 2008 12:50am  Apr 25, 2008 12:50am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

I confirm the problem about StopTradingAfterSequence.  
If it's false , the EA don't open a new order.  
If MT4 is closed and opened again, a new order is launched.  
(I have different magic numbers now)  
Regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#318](/thread/post/1968654#post1968654 "Post Permalink")

  * Apr 25, 2008 4:05am  Apr 25, 2008 4:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Thanks guys, I'll look at these issues tomorrow.  
  
Regarding the time entry: I check just if the current time is greater than the TimeEntry value. This might not the right way as it will immediately open a new position, e.g. if the current time is 09:00 but the TimeEntry is set to 08:00... I'll fix that tomorrow.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#319](/thread/post/1968734#post1968734 "Post Permalink")

  * Apr 25, 2008 4:40am  Apr 25, 2008 4:40am 

  * [ fry2010](fry2010)

  * | Joined Mar 2008  | Status: Trader | [785 Posts](/search?do=process&provider=Member&searchuser=63379)

Hi, looks like a v good ea. I am having a problem tho, it is always adjusting the orders. All I would like to do is buy, then sell, then buy untill profit is reached with now adjustment to tp or sl. I wud like to try without break even function. What would I need to adjust to correct this? Also I have set it to do order entry tries to 10. does this mean it will only try a trade in opposite direction 10 times before stopping? Currently it seems to stop after about 8 tries, and seems to just stay on fixed lot amount on a lot of trades i.e. i put lot of 0.01 it hits stop loss, enters with 0.01 again and again and again untill it decides by itself it wants to change to 0.02, what am I doing wrong here? I want it to change from 0.01 to 0.02 to 0.04 etc with each opposite order. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#320](/thread/post/1969508#post1969508 "Post Permalink")

  * Apr 25, 2008 3:27pm  Apr 25, 2008 3:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Good morning,  
  
here comes a new version. You don't need the magic number any more, it seems to be too confusing. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) The time entry issue is fixed as well as the stoptradingaftersequence thing.  
  
Regards - Xaron 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Sequencer_v1_2.ex4](/attachment/file/106328?d=1209104818) 28 KB | 781 downloads 

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [sequencer_v1_2.zip](/attachment/file/106329?d=1209104818) 32 KB | 844 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#321](/thread/post/1969515#post1969515 "Post Permalink")

  * Apr 25, 2008 3:30pm  Apr 25, 2008 3:30pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Xaron](/thread/post/1969508#post1969508 "View Quoted Post")
> 
> Disliked
> 
> Good morning,  
>    
>  here comes a new version. You don't need the magic number any more, it seems to be too confusing. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) The time entry issue is fixed as well as the stoptradingaftersequence thing.  
>    
>  Regards - Xaron
> 
> Ignored

Thanks Xaron  
Excellent tool for try immediately  
Have a good day in Germany <http://www.forexfactory.com/images/icons/icon7.gif>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#322](/thread/post/1969904#post1969904 "Post Permalink")

  * Apr 25, 2008 6:19pm  Apr 25, 2008 6:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Thanks for all your help Xaron! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#323](/thread/post/1969955#post1969955 "Post Permalink")

  * Apr 25, 2008 6:48pm  Apr 25, 2008 6:48pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

It seems be good.  
With false in StopTradingAfterSequence, a new order is opened immediately.  
I like a lot this EA: it's a "kalashnikov" <http://www.forexfactory.com/images/icons/icon10.gif>  
Thanks for sharing , Xaron. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#324](/thread/post/1970030#post1970030 "Post Permalink")

  * Apr 25, 2008 7:21pm  Apr 25, 2008 7:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Thanks guys. BTW: I found a bug, but it's only a display bug, will fix that asap.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#325](/thread/post/1970425#post1970425 "Post Permalink")

  * Apr 25, 2008 10:58pm  Apr 25, 2008 10:58pm 

  * [ tvanny](tvanny)

  * | Joined Sep 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=48715)

Hey Mer,  
just curious how the USD/JPY trade ended. Looking at the charts during that time frame it didn't look good. The trade was already in it's 20th entry and it didn't look like it took out the 102.66 TP (real close depending on broker). Let us know. That's what we're all here for, to evaluate and tweek.  
  
Tom 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#326](/thread/post/1970998#post1970998 "Post Permalink")

  * Apr 26, 2008 6:53am  Apr 26, 2008 6:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

It did go to 24 which is why we test ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1). I'll probably end up sticking with just Eur/Usd with this EA as I've never had a problem with it yet as it is the most consistent pair out there IMO. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#327](/thread/post/1971121#post1971121 "Post Permalink")

  * Apr 26, 2008 11:06am  Apr 26, 2008 11:06am 

  * [ jones247](jones247)

  * | Joined Aug 2007  | Status: Trader | [264 Posts](/search?do=process&provider=Member&searchuser=46344)

Would you guys be interested in checking-out Dan Davidson's new journal. He originated the concept behind this thread. However, his system has since evolved into a more powerful one, with less risk. His journal is called FXTradepro "Lucky 7" Journal. With capital of only about $5k, you could enter a r:r ratio of 1:1, having the chance of winning $1k while risking only $1k. He's been logging his daily results. Perhaps members of this thread would be interested in such a modification, as it would prevent the account "blow-up" if you lose...  
  
  
Walt 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#328](/thread/post/1971184#post1971184 "Post Permalink")

  * Apr 26, 2008 1:53pm  Apr 26, 2008 1:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I don't think I should have to pay a "monthly fee" just to see info we can get from others unless you're going to provide it to us for free here on the thread. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#329](/thread/post/1971375#post1971375 "Post Permalink")

  * Apr 26, 2008 10:41pm  Apr 26, 2008 10:41pm 

  * [ jones247](jones247)

  * | Joined Aug 2007  | Status: Trader | [264 Posts](/search?do=process&provider=Member&searchuser=46344)

I'm sorry, but I'm referencing the free journal here on ForexFactory. It's located in the Journals forum...  
  
I agree that it should be "Free Share". I am not advocating paying at all. My point was that the 7 series strategy may be worthwhile exploring and discussing on this thread because it's safer and more powerful than the 24 series strategy...  
  
Walt 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#330](/thread/post/1973752#post1973752 "Post Permalink")

  * Apr 29, 2008 1:04am  Apr 29, 2008 1:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

Hey Xaron, I've been using your entries and I have had 3 trading days in a row so far where I have not gone above 3 sequences with your EA! I think one of the keys to the success of this EA is to really FINE-TUNE your entries guys!  
  
Just my thoughts! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#331](/thread/post/1973873#post1973873 "Post Permalink")

  * Apr 29, 2008 2:40am  Apr 29, 2008 2:40am 

  * [ jones247](jones247)

  * | Joined Aug 2007  | Status: Trader | [264 Posts](/search?do=process&provider=Member&searchuser=46344)

> [Quoting Chartist](/thread/post/1973752#post1973752 "View Quoted Post")
> 
> Disliked
> 
> Hey Xaron, I've been using your entries and I have had 3 trading days in a row so far where I have not gone above 3 sequences with your EA! I think one of the keys to the success of this EA is to really FINE-TUNE your entries guys!  
>    
>  Just my thoughts!
> 
> Ignored

Hi Chartist,  
  
What have been your entry times (GMT or EST) over those 3 trading days?  
  
Walt 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#332](/thread/post/1974502#post1974502 "Post Permalink")

  * Apr 29, 2008 1:41pm  Apr 29, 2008 1:41pm 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Hi all.... My Sequencer EA v1.2 doesn't seem to be taking trades... smiley face OK, set to both long and short, live trading etc... all the basics are OK.. Time entry false, price entry false, breakout entry true... but no trades?  
  
any ideas? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#333](/thread/post/1974567#post1974567 "Post Permalink")

  * Apr 29, 2008 3:20pm  Apr 29, 2008 3:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

I'll take a look at it.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#334](/thread/post/1974625#post1974625 "Post Permalink")

  * Apr 29, 2008 4:03pm  Apr 29, 2008 4:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

> [Quoting jones247](/thread/post/1973873#post1973873 "View Quoted Post")
> 
> Disliked
> 
> Hi Chartist,  
>    
>  What have been your entry times (GMT or EST) over those 3 trading days?  
>    
>  Walt
> 
> Ignored

I usually enter between 7am - 9am gmt but I use an entry system that uses sma lines, s/r, and price movements. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#335](/thread/post/1975094#post1975094 "Post Permalink")

  * Apr 29, 2008 8:18pm  Apr 29, 2008 8:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Just for info: I found a minor bug: If the EA is in it's last progression level the BreakEven function won't work. I'll fix that asap.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#336](/thread/post/1976537#post1976537 "Post Permalink")

  * Apr 30, 2008 1:02pm  Apr 30, 2008 1:02pm 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Xaron... THANKS for all your work on this... I am getting a "trading has been stopped" error when I activate my EA with new OCO entries... Can you tell me why? (The EA was applied, but I had unchecked allow live trading after the trade last night, then re-checked it with new OCO entry levels...)  
  
I removed the EA, then re-applied it with the same settings and all was well, if that helps....  
  
mk 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#337](/thread/post/1976898#post1976898 "Post Permalink")

  * Apr 30, 2008 5:13pm  Apr 30, 2008 5:13pm 

  * [ alexwaller](alexwaller)

  * | Joined Feb 2008  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=60712)

Hi xaron,  
  
Yeah thanks for making this E.A., I really like the oco function, however it works fine on my demo but as soon as I use it on a real acc it 'plays up' Yesterday it opened the first order but then no more even though the S.L. was hit and today it did open the 2nd progression but twice! So i ended up with double the lots open that I wanted to. Any ideas!  
  
I use Alpari by the way,  
  
Kind regards  
  
Alex 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#338](/thread/post/1976938#post1976938 "Post Permalink")

  * Apr 30, 2008 5:26pm  Apr 30, 2008 5:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Strange, will have a look at this. Currently I have limited time so please stay tuned. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#339](/thread/post/1977467#post1977467 "Post Permalink")

  * Apr 30, 2008 10:22pm  Apr 30, 2008 10:22pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Xaron,  
Have you corrected the minor bug about the StopTradingAfterSequence ?  
If we put "true", the EA effectively stops trading but if we want to launch again an order later, the EA don't start with "false".  
We must stop MT4 and open it again to begin the sequence.  
Maybe have you another solution ?  
Regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#340](/thread/post/1977514#post1977514 "Post Permalink")

  * Apr 30, 2008 10:44pm  Apr 30, 2008 10:44pm 

  * [ alexwaller](alexwaller)

  * | Joined Feb 2008  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=60712)

Hi xaron,  
  
No worries. Just an idea, would it be possible for the E.A. to set a pending order for the next progression rather than opening it itself? The reason I say is because live trading the E.A. reacts a little slower to open the next progression however if it was set as a pending order it would not be a problem (unless caused by the broker)   
  
So basically there would always be an open trade + a pending trade.  
  
Its just an idea and i do appreciate all your work with this E.A.,  
  
Thanks again  
  
Alex 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#341](/thread/post/1980470#post1980470 "Post Permalink")

  * May 2, 2008 7:09am  May 2, 2008 7:09am 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

Xaron,  
  
Been sucessful playing your channel with the 4 majors + gbp/jpy in the 1hr TF starting at the London open. The size of the channel is my sl, tp is 4x's the sl and I've been closing when I have a 100 pip equity profit. This way I don't seem to go very deep into the progression and after closing all I start new progressions the next night at the beginning. It would be nice if you could add an **__equity close__** all feature at a certain price. I like Mer's PowerSM but love ur channel's. Playing several curriencies for a equity profit makes more sence to me than a possible bust of an account with a 24 loss sequence which does happen. Adding an emergency equity stop would probably help also. Thanks Mer for starting this thread it's sparked my interest. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#342](/thread/post/1980556#post1980556 "Post Permalink")

  * Edited 11:59am  May 2, 2008 8:42am | Edited 11:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar63756_4.gif) BillyZ](billyz)

  * | Joined Mar 2008  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=63756)

Mer & Xaron  
Thanks for all the hard work. I have read through the forum and am quite impressed with the results from both of your EA's. I have attempted to get both the PowerSM V5 and Sequencer v1.2 functioning to no avail. I have attached them to a chart, set both time entry and price entry to false and waited for over an hour. No trades have been initiated.   
  
Any thoughts?  
  
Thanks Again!  
  
_**Figured it out.**_ Enabled Expert Advisors in the options menu. DOH ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#343](/thread/post/1980557#post1980557 "Post Permalink")

  * May 2, 2008 8:43am  May 2, 2008 8:43am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Well, until then...... here you go! Just put this EA on a seperate chart, one that does not already have your PowerSM/Sequencer EA on it, (doesn't matter which currency....) and plug in your equity target.. and it will close ALL orders...  
  
Don't know how the EA will act, though... maybe it will continue the sequence, or possibly start over?  
  
test test test, I guess.... 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [CloseAllAtEquityLevel.mq4](/attachment/file/108303?d=1209685266) 5 KB | 486 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#344](/thread/post/1980760#post1980760 "Post Permalink")

  * Edited 12:04pm  May 2, 2008 11:47am | Edited 12:04pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

Thanks Mrkam I'm testing that one tonight, I will also be testing one that has a % of equity. Will keep u guys informed. I've had some strange things happening to these ea's because I've been attaching the scripts so what I've been doing is removing the ea's after the equity profit has hit and re-setting up the following night. The re-setting starts the sequence at the beginning. test, test, test. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [AutoEquityManager 1.0.mq4](/attachment/file/108340?d=1209696786) 3 KB | 528 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#345](/thread/post/1980918#post1980918 "Post Permalink")

  * May 2, 2008 3:23pm  May 2, 2008 3:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Thanks for all the good ideas and bug reports. I'll work on it. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#346](/thread/post/1980952#post1980952 "Post Permalink")

  * May 2, 2008 3:53pm  May 2, 2008 3:53pm 

  * [ malarraz](malarraz)

  * | Joined Mar 2008  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=63101)

Hi Xaron:  
What are the differences in function between the two EA´s?  
Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#347](/thread/post/1980976#post1980976 "Post Permalink")

  * May 2, 2008 4:16pm  May 2, 2008 4:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

There is no real difference. The only difference is that I've included the source code. The other thing is the breakout channel I've added.  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#348](/thread/post/1981894#post1981894 "Post Permalink")

  * May 3, 2008 12:30am  May 3, 2008 12:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar13787_4.gif) Chartist](chartist)

  * | Joined Jul 2006  | Status: Trend Surfer | [79 Posts](/search?do=process&provider=Member&searchuser=13787)

> [Quoting qz10cq](/thread/post/1980470#post1980470 "View Quoted Post")
> 
> Disliked
> 
> Xaron,  
>    
>  Been sucessful playing your channel with the 4 majors + gbp/jpy in the 1hr TF starting at the London open. The size of the channel is my sl, tp is 4x's the sl and I've been closing when I have a 100 pip equity profit. This way I don't seem to go very deep into the progression and after closing all I start new progressions the next night at the beginning. It would be nice if you could add an **__equity close__** all feature at a certain price. I like Mer's PowerSM but love ur channel's. Playing several curriencies for a equity profit makes more sence to me than a possible bust of an account with a 24 loss sequence which does happen. Adding an emergency equity stop would probably help also. Thanks Mer for starting this thread it's sparked my interest.
> 
> Ignored

Are you dividing your lot size by 4 to be able to stretch your margin to trade the 4 pairs and have you ever gone from one london session to the next without the equity EA closing you out? It seems really cool what you are doing but the only concern that comes to mind is the increased margin consumption with trading several pairs at the same time and I just wanted to know how you handle that. thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#349](/thread/post/1982401#post1982401 "Post Permalink")

  * May 3, 2008 12:31pm  May 3, 2008 12:31pm 

  * [ learn2gain](learn2gain)

  * | Joined May 2008  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=68204)

Hi Xaron and members, Just want to share one of martingle concept which I got. Your EA look like this one but only different at lot during entry buy/sell position and rule. Please look at the concept attached. I try to create this EA but not familiar with meta4. Hopefully someone can help me to create it and share here. Target is to get 40pips daily after one cycle complete. May be the best setting is 40 profit, step 40 and SL 60 for any pair. Also if using this concept, I think we can gain constant and profitable pip with small margin. 

Attached File(s)

![File Type: doc](https://assets.faireconomy.media/images/attach/doc.gif) [Hedging Lot Strategy.doc](/attachment/file/108665?d=1209785479) 172 KB | 971 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#350](/thread/post/1982405#post1982405 "Post Permalink")

  * Edited 1:36pm  May 3, 2008 12:53pm | Edited 1:36pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting Chartist](/thread/post/1981894#post1981894 "View Quoted Post")
> 
> Disliked
> 
> Are you dividing your lot size by 4 to be able to stretch your margin to trade the 4 pairs and have you ever gone from one london session to the next without the equity EA closing you out? It seems really cool what you are doing but the only concern that comes to mind is the increased margin consumption with trading several pairs at the same time and I just wanted to know how you handle that. thanks!
> 
> Ignored

Alex, created my own lucky 7 consisting of .1, .125, .156, .195, .244, .305, .381 total of -1.506 if losing the progression. Margin hasn't been a concern so far on a 3000 demo, TP hasn't been reached on any of the 4 majors + gbp/jpy, DD has been less than 10%. This is the first time (in 2 weeks of playing this twisted combo of the 2 systems) that equity profit has not been reached. As market closed today gbp/jpy is the only one in trouble of losing and I'm in the 5th trade with it, the rest are at 1 and 2 with my equity target -130, I knew I should not have trade today (first Friday) but I'm testing. My break even setting which is half of my SL killed me today, it kept moving the channels on me. Just reviewed my charts and found out the thing that did not work was my script to close when equity was hit. Equity was hit just after the big news. Sunday will be playing 0 break even and adding a different script for equity take profit. This is the first time that I went past the London session, usually I wake up and close manually with my 100+ equity target reached, maybe I will have to get serious and spend the time watching the screen to close all at the correct time.  
  
Trying this one on Sunday. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [CloseAtEquityAmount v1.0.mq4](/attachment/file/108667?d=1209789285) 3 KB | 521 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#351](/thread/post/1982560#post1982560 "Post Permalink")

  * May 3, 2008 10:06pm  May 3, 2008 10:06pm 

  * [ alexwaller](alexwaller)

  * | Joined Feb 2008  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=60712)

Guys,  
  
has anyone tried the E.A. on a live account? For me it works fine on demo but on my real micro account is where it starts to play up, I think its the slippage thats causing the problems and the E.A. cant open the orders fast enough. Would be interested to know if anyone else has tried on live acc,  
  
Cheers  
  
Alex 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#352](/thread/post/1982606#post1982606 "Post Permalink")

  * May 4, 2008 12:00am  May 4, 2008 12:00am 

  * [ mrkam](mrkam)

  * | Joined Aug 2006  | Status: Trader | [169 Posts](/search?do=process&provider=Member&searchuser=17053)

Hi Alex,  
  
I have been using it for a week or so on a live micro account... has worked just fine, with a few "hiccups"....  
  
1\. Sometimes, it just does not "energize" after being turned off. So, I have remove the EA and re-apply it, then it goes to "waiting for OCO trade"...  
  
2\. Friday, it took the first trade on my OCO breakout, hit a loss, then had a error 136 on the second trade, followed by (10) error 129's, so it never took the 2nd trade, then shut down.... (using a 7 trade progression, limited loss...). Was a good thing because it looked as if it would have run the whole progression!! Usually, I don't trade this on friday, because often the EU is quiet... but anyway, that was sort of an odd string of errors, but I think probably it was on the broker side (FXDD).. I will call them on Monday to see what they say...  
  
Other than that, it has worked just fine!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#353](/thread/post/1982622#post1982622 "Post Permalink")

  * May 4, 2008 12:46am  May 4, 2008 12:46am 

  * [ alexwaller](alexwaller)

  * | Joined Feb 2008  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=60712)

Thanks mrkam,  
  
maybe ill take a look over the settings again. But the last couple of times I was about halfway through a progression of 7 when it has suddenly stopped taking the trades, on both times they went on to bo the winner! Luckily it is only a micro account.   
  
But this is the reason that I thought having the next progression level already set as a pending order would mean as soon as the current one is exited the pending one would open unless there was slippage at the brokers end.   
  
This does seem like a good system, just hope I can get it sorted!  
  
Cheers mate  
  
Alex 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#354](/thread/post/1982735#post1982735 "Post Permalink")

  * May 4, 2008 5:45am  May 4, 2008 5:45am 

  * [ Schminner](schminner)

  * | Joined Jun 2007  | Status: Trader | [939 Posts](/search?do=process&provider=Member&searchuser=41559)

> [Quoting learn2gain](/thread/post/1982401#post1982401 "View Quoted Post")
> 
> Disliked
> 
> Hi Xaron and members, Just want to share one of martingle concept which I got. Your EA look like this one but only different at lot during entry buy/sell position and rule. Please look at the concept attached. I try to create this EA but not familiar with meta4. Hopefully someone can help me to create it and share here. Target is to get 40pips daily after one cycle complete. May be the best setting is 40 profit, step 40 and SL 60 for any pair. Also if using this concept, I think we can gain constant and profitable pip with small margin.
> 
> Ignored

I already have the EA, it works alright, but needs some tweaking because it only trade once per day .... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#355](/thread/post/1983097#post1983097 "Post Permalink")

  * May 4, 2008 9:25pm  May 4, 2008 9:25pm 

  * [ learn2gain](learn2gain)

  * | Joined May 2008  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=68204)

> [Quoting Schminner](/thread/post/1982735#post1982735 "View Quoted Post")
> 
> Disliked
> 
> I already have the EA, it works alright, but needs some tweaking because it only trade once per day ....
> 
> Ignored

Hi, Schminner. If u don't mind can you share the EA here or please email to me at [jzrResources@gmail.com](mailto:jzrResources@gmail.com). Really appreciate your support. Tq Later I will tweak it and if you have the best experience using this EA, please inform us the any tips.  
  
regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#356](/thread/post/1983925#post1983925 "Post Permalink")

  * May 5, 2008 5:46pm  May 5, 2008 5:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Hi,  
  
it would be nice if you could attach your log files from the EA to your posts if there were any errors.  
  
You find these logs in the folder /experts/logs/  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#357](/thread/post/1983928#post1983928 "Post Permalink")

  * May 5, 2008 5:50pm  May 5, 2008 5:50pm 

  * [ alexwaller](alexwaller)

  * | Joined Feb 2008  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=60712)

Hi xaron,  
  
Im just wondering whether my problems were because im running the E.A. via a VPS. Im gonna try it direct from my computer and see what happens.  
  
Cheers  
  
Alex 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#358](/thread/post/1983935#post1983935 "Post Permalink")

  * May 5, 2008 5:55pm  May 5, 2008 5:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Hi Alex,  
  
I run my EA on a VPS as well...  
  
I'll write down all problem which have been occured here and will work on a solution this week. But log files would make it easier for me. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#359](/thread/post/1983962#post1983962 "Post Permalink")

  * May 5, 2008 6:17pm  May 5, 2008 6:17pm 

  * [ alexwaller](alexwaller)

  * | Joined Feb 2008  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=60712)

Xaron,  
  
I think this is it, I can see from them that its trying to open the trade but cant for some reason. (i had to copy it into word as it wouldnt let me upload it in the original form) Hope this helps,  
  
Thanks Again for this  
  
Alex 

Attached File(s)

![File Type: doc](https://assets.faireconomy.media/images/attach/doc.gif) [log 1.doc](/attachment/file/108981?d=1209978956) 59 KB | 728 downloads 

![File Type: doc](https://assets.faireconomy.media/images/attach/doc.gif) [log 2.doc](/attachment/file/108982?d=1209978956) 38 KB | 587 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#360](/thread/post/1984694#post1984694 "Post Permalink")

  * May 6, 2008 1:05am  May 6, 2008 1:05am 

  * [ morander](morander)

  * | Joined Apr 2008  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=65555)

Hello,  
  
first I want to thank mer and xaron for there good work  
and for the helpful statements.  
  
Xaron: I miss your daily statements about your results  
with the combination of phil nell's 5min-system and the  
lucky seven. Does it still producing such good results like  
in the beginning of your tests?  
  
(Please excuse my bad english)  
  
Regards, Erik 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#361](/thread/post/1985926#post1985926 "Post Permalink")

  * May 6, 2008 6:52pm  May 6, 2008 6:52pm 

  * [ alexwaller](alexwaller)

  * | Joined Feb 2008  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=60712)

xaron,  
  
I have just had the problem again of it opening 2 trades at about level 4 of the progression, not sure why its doing this. Ill post the log a bit later on today  
  
Alex 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#362](/thread/post/1986757#post1986757 "Post Permalink")

  * May 7, 2008 2:10am  May 7, 2008 2:10am 

  * [ learn2gain](learn2gain)

  * | Joined May 2008  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=68204)

> [Quoting Schminner](/thread/post/1982735#post1982735 "View Quoted Post")
> 
> Disliked
> 
> I already have the EA, it works alright, but needs some tweaking because it only trade once per day ....
> 
> Ignored

Hi Schminner, How I can contact you. Really hope you can share the EA with me and the others . You can contact me or send the EA to [jzrResources@gmail.com](mailto:jzrResources@gmail.com).  
  
Tq and regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#363](/thread/post/1991263#post1991263 "Post Permalink")

  * May 9, 2008 2:04am  May 9, 2008 2:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar63756_4.gif) BillyZ](billyz)

  * | Joined Mar 2008  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=63756)

xaron  
Thanks for the great ea. I have been trying it out all week on several pairs. One thing I noticed today is that the gbpusd stalled out after 4 trades in a 7 trade sequence and the usdchf stalled out at 6 trades in a 7 trade sequence. I have attached the log.  
  
Thanks Again  
  
BTW does anyone know why mer's powerswing forum was closed?  
  
Much Thanks  
  
Bill 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#364](/thread/post/1995996#post1995996 "Post Permalink")

  * May 12, 2008 11:12pm  May 12, 2008 11:12pm 

  * [ giraia_br](giraia_br)

  * | Joined Jun 2007  | Status: Trader | [1,021 Posts](/search?do=process&provider=Member&searchuser=41373)

the video on post #33 was deleted. Someone have it? I don't understand how to use the spreadsheet. I want to use it to calculate a sequence like the Lucky 7. Someone can help me with examples? My math is very very bad.  
  
thanks in advance. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#365](/thread/post/1996148#post1996148 "Post Permalink")

  * May 13, 2008 12:29am  May 13, 2008 12:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar63756_4.gif) BillyZ](billyz)

  * | Joined Mar 2008  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=63756)

> [Quoting giraia_br](/thread/post/1995996#post1995996 "View Quoted Post")
> 
> Disliked
> 
> the video on post #33 was deleted. Someone have it? I don't understand how to use the spreadsheet. I want to use it to calculate a sequence like the Lucky 7. Someone can help me with examples? My math is very very bad.  
>    
>  thanks in advance.
> 
> Ignored

  
giraia  
The spreadsheet was originally posted by FXTradePro. He has a really good explanation on this thread [http://www.forexfactory.com/showthre...t=43221&page=2](http://www.forexfactory.com/showthread.php?t=43221&page=2). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#366](/thread/post/2007226#post2007226 "Post Permalink")

  * May 19, 2008 11:38am  May 19, 2008 11:38am 

  * [ giraia_br](giraia_br)

  * | Joined Jun 2007  | Status: Trader | [1,021 Posts](/search?do=process&provider=Member&searchuser=41373)

> [Quoting BillyZ](/thread/post/1996148#post1996148 "View Quoted Post")
> 
> Disliked
> 
> giraia  
>  The spreadsheet was originally posted by FXTradePro. He has a really good explanation on this thread [http://www.forexfactory.com/showthre...t=43221&page=2](http://www.forexfactory.com/showthread.php?t=43221&page=2).
> 
> Ignored

thanks  
  
what i understand is that AFTERA i have the calcs about lots i use the spreadsheet to calculate R:R of the entire sequence. Correct? I asked him in this new thread and still with problems to understand if there is a method choose the lots of each sequence. What i came with is: multiply the second by 1.2, third by 3.75 and 1.2 again in the next lots.   
  
or i am wrong?  
  
sorry, is that my maths is bad as my english.  
  
thanks again.  
  
best regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#367](/thread/post/2013043#post2013043 "Post Permalink")

  * May 22, 2008 2:26am  May 22, 2008 2:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar63756_4.gif) BillyZ](billyz)

  * | Joined Mar 2008  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=63756)

> [Quoting giraia_br](/thread/post/2007226#post2007226 "View Quoted Post")
> 
> Disliked
> 
> thanks  
>    
>  what i understand is that AFTERA i have the calcs about lots i use the spreadsheet to calculate R:R of the entire sequence. Correct? I asked him in this new thread and still with problems to understand if there is a method choose the lots of each sequence. What i came with is: multiply the second by 1.2, third by 3.75 and 1.2 again in the next lots.   
>    
>  or i am wrong?  
>    
>  sorry, is that my maths is bad as my english.  
>    
>  thanks again.  
>    
>  best regards.
> 
> Ignored

I am not sure I understand your question. What I do is enter my order size into the orange order column, I use a sequence of 11 on a micro account with a max profit of $28.60 and max draw down $26.40. The sequence is .01, .01, .02, .03, .05, .08, .13, .22, .37, .62, 1.1. As I enter the order sizes I look for something close to 1:1 in the profit and draw down columns.  
  
Hope this helps. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#368](/thread/post/2014889#post2014889 "Post Permalink")

  * May 22, 2008 10:09pm  May 22, 2008 10:09pm 

  * [ giraia_br](giraia_br)

  * | Joined Jun 2007  | Status: Trader | [1,021 Posts](/search?do=process&provider=Member&searchuser=41373)

many thanks BillyZ.   
  
i am testing the FxtraderPRO and now yours pregression too. Only losses even entering in the correct sessions and where i thing there is a good signal.  
  
how are you doing with it? how many progressions have you took?  
  
thanks again and sorry for my bad english.  
  
and thanks Xaron, i am testing using your EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#369](/thread/post/2015347#post2015347 "Post Permalink")

  * May 23, 2008 1:23am  May 23, 2008 1:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar31400_6.gif) lcfxtrader](lcfxtrader)

  * | Commercial User  | Joined Jan 2007 | [460 Posts](/search?do=process&provider=Member&searchuser=31400)

Mer,  
  
Could you please post the EA that will not expire? I plan on using this long term. I am having good success with a 20p S/L and 80p T/P and just letting the EA run 24/5 on the EUR/USD.  
  
Thanks, Lcfx 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#370](/thread/post/2019428#post2019428 "Post Permalink")

  * May 26, 2008 12:31pm  May 26, 2008 12:31pm 

  * [ Mantorp](mantorp)

  * | Joined Feb 2008  | Status: Trader | [44 Posts](/search?do=process&provider=Member&searchuser=61965)

> [Quoting BillyZ](/thread/post/2013043#post2013043 "View Quoted Post")
> 
> Disliked
> 
> I am not sure I understand your question. What I do is enter my order size into the orange order column, I use a sequence of 11 on a micro account with a max profit of $28.60 and max draw down $26.40. The sequence is .01, .01, .02, .03, .05, .08, .13, .22, .37, .62, 1.1. As I enter the order sizes I look for something close to 1:1 in the profit and draw down columns.  
>    
>  Hope this helps.
> 
> Ignored

When you modify the EA do you stop the last number in your series with a ; or just end it? I just added this but as soon as I started the EA it opened a deal with 0.16  
0.1;0.13;0.16;0.2;0.25;0.31;0.4  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#371](/thread/post/2022395#post2022395 "Post Permalink")

  * May 28, 2008 6:36am  May 28, 2008 6:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar63756_4.gif) BillyZ](billyz)

  * | Joined Mar 2008  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=63756)

I have been running Xaron's sequencer EA (thanks Xaron) for 3 weeks now. EURUSD is 12 for 13 with a total profit of $29.40, not a lot but with a account of $200 I will take it. On my demo account I have tested quite a few pairs, the best performing were the eurchf (8 for 9), gbpusd (10 for 12), eurjpy (7 for 10), the remaining pairs did not fair so well. I am running the ea Mon - Thur from 5:00 until 16:00 gmt.  
  
  
  

> [Quoting giraia_br](/thread/post/2014889#post2014889 "View Quoted Post")
> 
> Disliked
> 
> many thanks BillyZ.   
>    
>  i am testing the FxtraderPRO and now yours pregression too. Only losses even entering in the correct sessions and where i thing there is a good signal.  
>    
>  how are you doing with it? how many progressions have you took?  
>    
>  thanks again and sorry for my bad english.  
>    
>  and thanks Xaron, i am testing using your EA.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#372](/thread/post/2022400#post2022400 "Post Permalink")

  * May 28, 2008 6:38am  May 28, 2008 6:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar63756_4.gif) BillyZ](billyz)

  * | Joined Mar 2008  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=63756)

Mantorp  
Personally I use Xaron's Sequencer EA. I have found that I have fewer problems with it. With it you enter the sequence on seperate lines.  
  

> [Quoting Mantorp](/thread/post/2019428#post2019428 "View Quoted Post")
> 
> Disliked
> 
> When you modify the EA do you stop the last number in your series with a ; or just end it? I just added this but as soon as I started the EA it opened a deal with 0.16  
>  0.1;0.13;0.16;0.2;0.25;0.31;0.4  
>    
>  Thanks
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#373](/thread/post/2023943#post2023943 "Post Permalink")

  * May 28, 2008 11:17pm  May 28, 2008 11:17pm 

  * [ Mantorp](mantorp)

  * | Joined Feb 2008  | Status: Trader | [44 Posts](/search?do=process&provider=Member&searchuser=61965)

> [Quoting BillyZ](/thread/post/2022400#post2022400 "View Quoted Post")
> 
> Disliked
> 
> Mantorp  
>  Personally I use Xaron's Sequencer EA. I have found that I have fewer problems with it. With it you enter the sequence on seperate lines.
> 
> Ignored

Thanks, I started using that as well. In your testing are you using the same S/L - T/P for all pairs? Also do you know where I can find a good explanation of how the breakeven thing works? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#374](/thread/post/2026547#post2026547 "Post Permalink")

  * May 30, 2008 1:05am  May 30, 2008 1:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar63756_4.gif) BillyZ](billyz)

  * | Joined Mar 2008  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=63756)

I am using the 10/40 sl/tp. I looked briefly for the explanation to the ea but could not find it. It is buried in this thread somewhere.  
  
  
  

> [Quoting Mantorp](/thread/post/2023943#post2023943 "View Quoted Post")
> 
> Disliked
> 
> Thanks, I started using that as well. In your testing are you using the same S/L - T/P for all pairs? Also do you know where I can find a good explanation of how the breakeven thing works?
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#375](/thread/post/2026849#post2026849 "Post Permalink")

  * May 30, 2008 3:14am  May 30, 2008 3:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar68510_7.gif) okehiedon](okehiedon)

  * | Joined May 2008  | Status: EMPEROR | [437 Posts](/search?do=process&provider=Member&searchuser=68510)

Hi Mer071898 am new to your thread and find it interesting. I seem to like the concept. What settings(tp,be and sl) would you recommend for trading GU and GJ.  
Okehiedon 

LISTEN TO MR FUNDAMENTAL AND MR TECHNICAL

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#376](/thread/post/2026932#post2026932 "Post Permalink")

  * May 30, 2008 3:49am  May 30, 2008 3:49am 

  * [ Mantorp](mantorp)

  * | Joined Feb 2008  | Status: Trader | [44 Posts](/search?do=process&provider=Member&searchuser=61965)

> [Quoting BillyZ](/thread/post/2026547#post2026547 "View Quoted Post")
> 
> Disliked
> 
> I am using the 10/40 sl/tp. I looked briefly for the explanation to the ea but could not find it. It is buried in this thread somewhere.
> 
> Ignored

Break Even stop. If the price reached this level the stop loss will be set to the open price. That way the EA will use the same progression level again. If you don't want to use it, set it to 0.  
  
Testing 0.01, 0.01, 0.02, 0.03, 0.04, 0.06, 0.08 on USD-JPY with SL15 TP60 and BE45 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#377](/thread/post/2047678#post2047678 "Post Permalink")

  * Jun 11, 2008 3:06am  Jun 11, 2008 3:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar31400_6.gif) lcfxtrader](lcfxtrader)

  * | Commercial User  | Joined Jan 2007 | [460 Posts](/search?do=process&provider=Member&searchuser=31400)

Mer,  
  
Are you still here? Can you please post the EA that will not expire? I am currently using 30s/l & 120t/p on EUR/USD with good success.  
  
Thanks, Lcfx 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#378](/thread/post/2048775#post2048775 "Post Permalink")

  * Jun 11, 2008 4:03pm  Jun 11, 2008 4:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar37532_9.gif) Xaron](xaron)

  * Joined Apr 2007 | Status: Evil Kraut | [2,559 Posts](/search?do=process&provider=Member&searchuser=37532)

Lcfx, you might want to use mine. There are still some (minor) bugs I'll have to fix...  
  
Regards - Xaron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#379](/thread/post/2056088#post2056088 "Post Permalink")

  * Jun 15, 2008 4:31pm  Jun 15, 2008 4:31pm 

  * [ lovesub69](lovesub69)

  * | Joined Jun 2007  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=41161)

Hi, I really appreciate your work and thanks to TXTradePro, mer071898, Xaron.  
I think these EAs are great tools in trader’s hands.  
May be you could put in it one more option - for ranging markets. Example – if price ranges between 1.0500 and 1.0550 you can set EA to sell at 1.0545 and bay at 1.0505 with S/L, T/P and in this case you should turn off leveling.   
  
Great Job … Thanks.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#380](/thread/post/2060685#post2060685 "Post Permalink")

  * Jun 18, 2008 5:05am  Jun 18, 2008 5:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar52245_6.gif) Evaluator](evaluator)

  * Joined Oct 2007 | Status: Trader | [2,972 Posts](/search?do=process&provider=Member&searchuser=52245)

Hi!  
  
I downloaded your EA and opened in my Metatrader using the default setting I am backtesting. However, I keep getting the following error message.  
  
"PowerSM V.5 EURUSD, M15: OrderSend error 130"  
  
What does that mean?  
  
I want to test with an account balance of $500 and am using the EveryTick mode for my backtesting.  
  
Can you give me assistance as to the proper settings?  
  
Thanks.  
  
evaluator 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#381](/thread/post/2444464#post2444464 "Post Permalink")

  * Jan 1, 2009 2:05am  Jan 1, 2009 2:05am 

  * [ daceterito](daceterito)

  * | Joined Jan 2009  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=89994)

Do you rent it?  
Can I test it by one year?  
  
  

> [Quoting mer071898](/thread/post/1902736#post1902736 "View Quoted Post")
> 
> Disliked
> 
> I am posting my PowerSM EA and my PowerSM Calculator for those who have followed the thread by FXTradepro on the forum. For those who are a little disheartened after finding out you had to pay to use his FXTradepro EA, this is for you. Below is the link to the thread to get familiar with the concept. **Please read over first if you have not used the EA before.**  
>    
>  [FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](http://forexfactory.com/showthread.php?t=43221)  
>    
>  Before I start, I want to say I am not disrespecting or...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#382](/thread/post/2445258#post2445258 "Post Permalink")

  * Jan 2, 2009 2:01am  Jan 2, 2009 2:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here is an updated version that has an expiration date of 1/1/2010 for you to use for whatever you would like. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [PowerSM.ex4](/attachment/file/187265?d=1230829272) 11 KB | 809 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#383](/thread/post/2514081#post2514081 "Post Permalink")

  * Feb 4, 2009 3:34pm  Feb 4, 2009 3:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar91845_4.gif) Toxic](toxic)

  * | Joined Jan 2009  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=91845)

> [Quoting mer071898](/thread/post/2445258#post2445258 "View Quoted Post")
> 
> Disliked
> 
> Here is an updated version that has an expiration date of 1/1/2010 for you to use for whatever you would like.
> 
> Ignored

Mer,  
Thank you very much...working fine....it would be nice if we can see the number of sequence and Lot in the next version of your PowerSM....i mean some info like Xaron Sequencer.....  
Regards.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#384](/thread/post/2518644#post2518644 "Post Permalink")

  * Feb 6, 2009 1:35am  Feb 6, 2009 1:35am 

  * [ criss73](criss73)

  * | Joined Aug 2006  | Status: Trader | [194 Posts](/search?do=process&provider=Member&searchuser=16150)

hey mer, I've tried your EA and it's not working properly. I changed the TP and SL to 20 and the ea won't let me. It comes up as an error. also, when the EA was up and running the SL would disappear and the position would prematurely close.  
  
  
  
  

> [Quoting mer071898](/thread/post/2445258#post2445258 "View Quoted Post")
> 
> Disliked
> 
> Here is an updated version that has an expiration date of 1/1/2010 for you to use for whatever you would like.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#385](/thread/post/2523014#post2523014 "Post Permalink")

  * Feb 8, 2009 2:07am  Feb 8, 2009 2:07am 

  * [ forfac](forfac)

  * | Joined May 2008  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=68720)

Hi Mer ,  
  
I just downloaded your updated version of your EA , as per the one you posted a day or so ago .  
  
Ive just gone through nearly every post ..... pheew ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
I was wondering is everything working out ok with the EA  
  
at present and are you still ongoing with its developement .  
  
All the reading seems to suggest many are having   
  
good fun using the system . I will try it out on Monday   
  
Ive attached it to my Meta trader ODL and Alpari Demo platforms   
  
just as it is set ( default) Im hoping it should work ok as it is .  
  
Should it be ok as it is Mer ?.  
  
  
Thanks ,  
  
Forfac. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#386](/thread/post/2529517#post2529517 "Post Permalink")

  * Feb 11, 2009 5:29am  Feb 11, 2009 5:29am 

  * [ forfac](forfac)

  * | Joined May 2008  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=68720)

I placed it on my alpari chart and the smiley shows ..... I ticked allow live trades ........ but it doesnt seem to trade .  
  
  
What am I not doing right ?   
  
  
  
  
Forfac 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#387](/thread/post/2529599#post2529599 "Post Permalink")

  * Feb 11, 2009 6:10am  Feb 11, 2009 6:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar31400_6.gif) lcfxtrader](lcfxtrader)

  * | Commercial User  | Joined Jan 2007 | [460 Posts](/search?do=process&provider=Member&searchuser=31400)

Thanks Mer for the updated version. It made some good pips this week using 25sl/50be/100tp on the EUR/USD & EUR/JPY. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#388](/thread/post/2542099#post2542099 "Post Permalink")

  * Feb 16, 2009 9:34pm  Feb 16, 2009 9:34pm 

  * [ forfac](forfac)

  * | Joined May 2008  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=68720)

can anyone tell me why the new version.ex4 as per mers post Jan 01 2009   
  
was working ok last week and now it will not trade .  
  
  
  
All ive done is change TimeEntry from true to false and vice versa  
  
Just does not place trades .  
  
  
  
Any help would be useful.  
  
  
Thanks,  
Forfac. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#389](/thread/post/2545652#post2545652 "Post Permalink")

  * Feb 18, 2009 5:10am  Feb 18, 2009 5:10am 

  * [ daceterito](daceterito)

  * | Joined Jan 2009  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=89994)

Can Anybory help me to create a expert martingale this way?  
Open 1 2 4 8 16(10 pips each order distance) after 20 pips up start again 1 2 4 8 16 (30 pips distance) after 30 pips 1 2 4 8 16 (50 pips distance) after 30 pips 1 2 4 8 16 ( 100 pips distance)  
I think is a good Idea  
Example  
Buy 0.01 lot 1.0020  
10 pips distance  
Buy 0.02 lot 1.0030  
10 pips distance  
Buy 0.04 lot 1.0040  
10 pips distance  
Buy 0.08 lot 1.0050  
10 pips distance  
Buy 0.16 lot 1.0060  
After 20 pips to open new order (or the pips number that I want )  
  
Buy 0.01 lot 1.0080  
30 pips distance  
Buy 0.02 lot 1.0110  
30 pips distance  
Buy 0.04 lot 1.0140  
30 pips distance  
Buy 0.08 lot 1.0170  
30 pips distance  
Buy 0.16 lot 1.0200  
After 30 pips start again with 50 pips distance martinagale  
Buy 0.01 lot 1.0230  
50 pips distance  
Buy 0.02 lot 1.0280  
50 pips distance  
Buy 0.04 lot 1.0330  
50 pips distance  
Buy 0.08 lot 1.0380  
50 pips distance  
Buy 0.16 lot 1.0430  
After 70 pips Start again with 100 pips distance martingale  
Always start again until 2000 pips 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#390](/thread/post/2545702#post2545702 "Post Permalink")

  * Feb 18, 2009 5:37am  Feb 18, 2009 5:37am 

  * [ Cosmo](cosmo)

  * | Joined Sep 2008  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=80412)

Can Anybory help me to create a expert martingale this way?  
Open 1 2 4 8 16(10 pips each order distance) after 20 pips up start again 1 2 4 8 16 (30 pips distance) after 30 pips 1 2 4 8 16 (50 pips distance) after 30 pips 1 2 4 8 16 ( 100 pips distance)  
I think is a good Idea  
  
  
What is the SL and TP for this proposed EA 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#391](/thread/post/2545797#post2545797 "Post Permalink")

  * Feb 18, 2009 6:14am  Feb 18, 2009 6:14am 

  * [ daceterito](daceterito)

  * | Joined Jan 2009  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=89994)

> [Quoting Cosmo](/thread/post/2545702#post2545702 "View Quoted Post")
> 
> Disliked
> 
> Can Anybory help me to create a expert martingale this way?  
>  Open 1 2 4 8 16(10 pips each order distance) after 20 pips up start again 1 2 4 8 16 (30 pips distance) after 30 pips 1 2 4 8 16 (50 pips distance) after 30 pips 1 2 4 8 16 ( 100 pips distance)  
>  I think is a good Idea  
>    
>    
>  What is the SL and TP for this proposed EA
> 
> Ignored

TP that you want( pips)  
Without stop loss 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#392](/thread/post/2545805#post2545805 "Post Permalink")

  * Feb 18, 2009 6:16am  Feb 18, 2009 6:16am 

  * [ daceterito](daceterito)

  * | Joined Jan 2009  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=89994)

Can Anybory help me to create a expert martingale this way?  
Open 1 2 4 8 16(10 pips each order distance) after 20 pips up start again 1 2 4 8 16 (30 pips distance) after 30 pips 1 2 4 8 16 (50 pips distance) after 30 pips 1 2 4 8 16 ( 100 pips distance)  
I think is a good Idea  
Example  
Buy 0.01 lot 1.0020  
10 pips distance  
Buy 0.02 lot 1.0030  
10 pips distance  
Buy 0.04 lot 1.0040  
10 pips distance  
Buy 0.08 lot 1.0050  
10 pips distance  
Buy 0.16 lot 1.0060  
  
After 20 pips to open new order (or the pips number that I want )  
  
  
Buy 0.01 lot 1.0080  
30 pips distance  
Buy 0.02 lot 1.0110  
30 pips distance  
Buy 0.04 lot 1.0140  
30 pips distance  
Buy 0.08 lot 1.0170  
30 pips distance  
Buy 0.16 lot 1.0200  
  
After 30 pips start again with 50 pips distance martinagale  
  
Buy 0.01 lot 1.0230  
50 pips distance  
Buy 0.02 lot 1.0280  
50 pips distance  
Buy 0.04 lot 1.0330  
50 pips distance  
Buy 0.08 lot 1.0380  
50 pips distance  
Buy 0.16 lot 1.0430  
  
After 70 pips Start again with 100 pips distance martingale  
  
Buy 0.01 lot 1.0500  
100 pips distance  
Buy 0.02 lot 1.0600  
100 pips distance  
Buy 0.04 lot 1.0700  
100 pips distance  
Buy 0.08 lot 1.0800  
100 pips distance  
Buy 0.16 lot 1.0900  
  
After 100 pips with 200 pips martingale distance  
  
Buy 0.01 lot 1.0100  
200 pips distance  
Buy 0.02 lot 1.0300  
200 pips distance  
Buy 0.04 lot 1.0500  
200 pips distance  
But 0.08 lot 1.0700  
200 pips distance  
But 0.16 lot 1.0900  
Always start again until 2000 pips or more 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#393](/thread/post/2552046#post2552046 "Post Permalink")

  * Feb 20, 2009 7:02am  Feb 20, 2009 7:02am 

  * [ daceterito](daceterito)

  * | Joined Jan 2009  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=89994)

> [Quoting mer071898](/thread/post/2445258#post2445258 "View Quoted Post")
> 
> Disliked
> 
> Here is an updated version that has an expiration date of 1/1/2010 for you to use for whatever you would like.
> 
> Ignored

  
Ok thanks a lot 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#394](/thread/post/2552194#post2552194 "Post Permalink")

  * Feb 20, 2009 8:19am  Feb 20, 2009 8:19am 

  * [ daceterito](daceterito)

  * | Joined Jan 2009  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=89994)

> [Quoting mer071898](/thread/post/2445258#post2445258 "View Quoted Post")
> 
> Disliked
> 
> Here is an updated version that has an expiration date of 1/1/2010 for you to use for whatever you would like.
> 
> Ignored

I would like that each order to buy or sell have 30 pips grid  
The firt order 0.01 lot open   
The second order (0.02 lot)and the others open after how much grids?  
10;20;30;40... pips??? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#395](/thread/post/2555516#post2555516 "Post Permalink")

  * Feb 21, 2009 10:46pm  Feb 21, 2009 10:46pm 

  * [ daceterito](daceterito)

  * | Joined Jan 2009  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=89994)

> [Quoting mer071898](/thread/post/2445258#post2445258 "View Quoted Post")
> 
> Disliked
> 
> Here is an updated version that has an expiration date of 1/1/2010 for you to use for whatever you would like.
> 
> Ignored

Is there a especif Time frime? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#396](/thread/post/2555869#post2555869 "Post Permalink")

  * Feb 22, 2009 6:42am  Feb 22, 2009 6:42am 

  * [ daceterito](daceterito)

  * | Joined Jan 2009  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=89994)

> [Quoting daceterito](/thread/post/2555516#post2555516 "View Quoted Post")
> 
> Disliked
> 
> Is there a especif Time frime?
> 
> Ignored

Can I start with 0.01 lot?  
0.01;0.01;0.02;0.03;0.04...??? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#397](/thread/post/2555872#post2555872 "Post Permalink")

  * Feb 22, 2009 7:02am  Feb 22, 2009 7:02am 

  * [ daceterito](daceterito)

  * | Joined Jan 2009  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=89994)

> [Quoting Xaron](/thread/post/1969508#post1969508 "View Quoted Post")
> 
> Disliked
> 
> Good morning,  
>    
>  here comes a new version. You don't need the magic number any more, it seems to be too confusing. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) The time entry issue is fixed as well as the stoptradingaftersequence thing.  
>    
>  Regards - Xaron
> 
> Ignored

I have a suggestion  
Can you put x pips to open a new order?  
For example I Want that open after 30 pips   
0.01 lot after 30 pips 0.02 lot after 30 pips 0.03 lot  
I think is a good idea 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#398](/thread/post/2623265#post2623265 "Post Permalink")

  * Mar 24, 2009 4:29am  Mar 24, 2009 4:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I've been p'md numerous times about posting up trades using the EA. So if anyone is still interested, there is a new trading journal entry being posted today and will start trading this evening. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#399](/thread/post/2623309#post2623309 "Post Permalink")

  * Mar 24, 2009 4:51am  Mar 24, 2009 4:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Here is a link to the journal for those who would like to follow it.  
  
<http://www.forexfactory.com/showthread.php?t=159789>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#400](/thread/post/2625927#post2625927 "Post Permalink")

  * Mar 25, 2009 6:35am  Mar 25, 2009 6:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

First trading statement is posted in the journal.![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#401](/thread/post/2647266#post2647266 "Post Permalink")

  * Apr 2, 2009 11:06pm  Apr 2, 2009 11:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar93155_5.gif) BullsAndBear](bullsandbear)

  * | Joined Feb 2009  | Status: Trader | [266 Posts](/search?do=process&provider=Member&searchuser=93155)

> [Quoting mer071898](/thread/post/1908727#post1908727 "View Quoted Post")
> 
> Disliked
> 
> Dreamliner, here is a quick video to explain a little about the spreadsheet. Before you watch it I've attached the original spreadsheet in the first post for everyone which has the info on IBFX accounts on it. It's an AVI video so let me know if you have any problems playing it.  
>    
>  [](http://s86.photobucket.com/albums/k113/mer071898/?action=view&current=excelhelp.flv)[http://i86.photobucket.com/albums/k1..._excelhelp.jpg](http://i86.photobucket.com/albums/k113/mer071898/th_excelhelp.jpg)
> 
> Ignored

Hi mer,  
  
The video was taken down. Do you have it anywhere else? I am studying this EA like a banshee. The firebird ea is also successful if you need another feather in ur hat. Cant wait to get this one down and much thanks for your generosity to post it.  
  
bulls 

Whats happening in EUR/USD should be happening to you! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#402](/thread/post/2665014#post2665014 "Post Permalink")

  * Apr 13, 2009 2:08pm  Apr 13, 2009 2:08pm 

  * [ rbrtsha](rbrtsha)

  * | Joined Apr 2008  | Status: Trader | [77 Posts](/search?do=process&provider=Member&searchuser=65487)

i have restart cycle checked but stategy retester just stops after 24th time on a loss...any suggestions? i also rechecked my lots and all semicolons and it looks coreect and my acct still had 5k in it and my max lot was 5 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#403](/thread/post/2671105#post2671105 "Post Permalink")

  * Apr 16, 2009 12:58am  Apr 16, 2009 12:58am 

  * [ jones247](jones247)

  * | Joined Aug 2007  | Status: Trader | [264 Posts](/search?do=process&provider=Member&searchuser=46344)

Hi Mer,  
  
I'm very familiar with this strategy, as I've been closely following the FXTradepro Semi-Martingale thread until Dan closed it. As you know, the BIG problem with this strategy is the potential for the BIG BLOW-UP! I think that there's a modification that can be implemented, which creates only a "manageable" loss when or if a loss occurs. In essence, this strategy changes from a "stop & reverse" method to a "keep & reverse" method.  
  
Would you be interested in creating an EA on such a modification? Or would you want to start a different thread/journal on the modified methodology?  
  
I assure you that it all but completely removes the BIG BLOW-UP risk that's associated with the original method.  
  
thanks,  
  
Walt 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#404](/thread/post/2671516#post2671516 "Post Permalink")

  * Apr 16, 2009 4:06am  Apr 16, 2009 4:06am 

  * [ tokyomaster](tokyomaster)

  * | Additional Username  | Joined Feb 2009 | [256 Posts](/search?do=process&provider=Member&searchuser=94662)

The source code to PowerSM is freely available on the net. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [PowerSM.mq4](/attachment/file/233431?d=1239822378) 9 KB | 871 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#405](/thread/post/2671558#post2671558 "Post Permalink")

  * Apr 16, 2009 4:29am  Apr 16, 2009 4:29am 

  * [ jones247](jones247)

  * | Joined Aug 2007  | Status: Trader | [264 Posts](/search?do=process&provider=Member&searchuser=46344)

thanks... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#406](/thread/post/2671643#post2671643 "Post Permalink")

  * Apr 16, 2009 5:10am  Apr 16, 2009 5:10am 

  * [ jones247](jones247)

  * | Joined Aug 2007  | Status: Trader | [264 Posts](/search?do=process&provider=Member&searchuser=46344)

The main crux of my earlier inquiry was to find out if Mer was o.k. with discussing a modification to this strategy. Instead of a "stop & reverse" approach, it's a "keep & reverse" approach.  
  
The bad news with the "keep & reverse" is that it requires a greate movement in price to be profitable; however, the good news is that the chances of a Blow-up are virtually eliminated. For example, a 24 progression failure in the "stop & reverse" method will cause a loss of about $31k; however, a 24 progression failure in the "keep & reverse" method will cause a loss of less than $4k... BIG DIFFERENCE!!!  
  
thanks,  
  
Walt 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#407](/thread/post/2671677#post2671677 "Post Permalink")

  * Apr 16, 2009 5:23am  Apr 16, 2009 5:23am 

  * [ tokyomaster](tokyomaster)

  * | Additional Username  | Joined Feb 2009 | [256 Posts](/search?do=process&provider=Member&searchuser=94662)

Isnt that just the same as the old buy/sell grid ?? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#408](/thread/post/2671862#post2671862 "Post Permalink")

  * Apr 16, 2009 6:52am  Apr 16, 2009 6:52am 

  * [ jones247](jones247)

  * | Joined Aug 2007  | Status: Trader | [264 Posts](/search?do=process&provider=Member&searchuser=46344)

> [Quoting tokyomaster](/thread/post/2671677#post2671677 "View Quoted Post")
> 
> Disliked
> 
> Isnt that just the same as the old buy/sell grid ??
> 
> Ignored

I'm sorry, but I'm not familar with the buy/sell grid. Nonetheless, it's really not so much a grid system, as it's a hedge system.  
  
Walt 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#409](/thread/post/2671925#post2671925 "Post Permalink")

  * Apr 16, 2009 7:22am  Apr 16, 2009 7:22am 

  * [ tokyomaster](tokyomaster)

  * | Additional Username  | Joined Feb 2009 | [256 Posts](/search?do=process&provider=Member&searchuser=94662)

Yes, grid, hedge are basically the same. Some brokers do not allow hedging of same symbols. i.e. you cant long and short the same pair otherwise they will close one of them automatically.  
  
Besides allot of EA's have been built around grid or hedge and they all fail at some point with huge DD.  
  
The only EA's that i have seen work consistently are ones which place buy or sell orders at the previous days highs and lows.  
  
News statements will always be a major problem to any EA, this is why that a fully automated 24/5 EA (left alone) cannot work. Having said that Neural type EA's (that learn for themselves) do show some promise. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#410](/thread/post/2710656#post2710656 "Post Permalink")

  * May 4, 2009 1:01pm  May 4, 2009 1:01pm 

  * [ Explorer3333](explorer3333)

  * | Joined Jan 2009  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=90168)

> [Quoting jones247](/thread/post/2671643#post2671643 "View Quoted Post")
> 
> Disliked
> 
> The main crux of my earlier inquiry was to find out if Mer was o.k. with discussing a modification to this strategy....
> 
> Ignored

Walt,  
  
What is the difference between the "stop & reverse" and the "keep & reverse"? I fully understand the 24 progression system, I just don't understand this proposed modification. Could you elaborate a little please?  
  
thanks, explorer 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#411](/thread/post/2710659#post2710659 "Post Permalink")

  * May 4, 2009 1:06pm  May 4, 2009 1:06pm 

  * [ Explorer3333](explorer3333)

  * | Joined Jan 2009  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=90168)

> [Quoting tokyomaster](/thread/post/2671925#post2671925 "View Quoted Post")
> 
> Disliked
> 
> News statements will always be a major problem to any EA, this is why that a fully automated 24/5 EA (left alone) cannot work.
> 
> Ignored

tokyomaster,  
  
I am sorry to disappoint you, but I do trade live successfully a fully automated 24/5 EA. It can be done if you are carefully set the margins to include "black swan" events, like unfavorable news releases. In other word, never say never.  
  
explorer 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#412](/thread/post/2734961#post2734961 "Post Permalink")

  * May 15, 2009 3:00am  May 15, 2009 3:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar100202_10.gif) erfan_hi](erfan_hi)

  * | Joined Apr 2009  | Status: Trader | [50 Posts](/search?do=process&provider=Member&searchuser=100202)

> [Quoting tokyomaster](/thread/post/2671516#post2671516 "View Quoted Post")
> 
> Disliked
> 
> The source code to PowerSM is freely available on the net.
> 
> Ignored

hi every body  
i don't know how i can write expert.i bought this martingale expert many time.and it will be expired in 2 week also.i ask some body correct it and put it here or send to my email: [davood_forex@yahoo.com](mailto:davood_forex@yahoo.com)  
thank you 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Forex.Soldier.VD959.ex4](/attachment/file/246965?d=1242324010) 15 KB | 629 downloads 

thanks erfan

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#413](/thread/post/2962446#post2962446 "Post Permalink")

  * Aug 18, 2009 11:17am  Aug 18, 2009 11:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar63756_4.gif) BillyZ](billyz)

  * | Joined Mar 2008  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=63756)

Is anyone using the Sequencer on a Interbank FX account? I canot get it to work on a practice account with them but it works fine on a FX Solutions account. Curious what might be happening here.  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#414](/thread/post/3152260#post3152260 "Post Permalink")

  * Oct 16, 2009 2:04pm  Oct 16, 2009 2:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar107368_2.gif) Universal](universal)

  * | Joined Jun 2009  | Status: Trader | [26 Posts](/search?do=process&provider=Member&searchuser=107368)

Can anyone help me for free. Juz wan to modify a little bit.  
Thanx 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#415](/thread/post/3152288#post3152288 "Post Permalink")

  * Oct 16, 2009 2:22pm  Oct 16, 2009 2:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

I am no longer involved in this project so please do not pm me to make changes in the code. You will need to have someone else make the changes for you. Since this EA has been unlawfully cracked and is available on the web, I will post it here for whoever wants to use it for whatever purpose, good luck. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [PowerSM.mq4](/attachment/file/338108?d=1255670449) 8 KB | 1,154 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#416](/thread/post/3153432#post3153432 "Post Permalink")

  * Oct 16, 2009 10:19pm  Oct 16, 2009 10:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83928_5.gif) magicchance](magicchance)

  * | Additional Username  | Joined Oct 2008 | [280 Posts](/search?do=process&provider=Member&searchuser=83928)

Mer, is this EA locked or disabled somehow? Or do the new NFA rules prevent it from working on an American broker? Nothing I do will get it to work. Any help would be appreciated,  
  
Chance 

" Average traders look to the left, great traders look to the right."

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#417](/thread/post/3153758#post3153758 "Post Permalink")

  * Oct 17, 2009 12:12am  Oct 17, 2009 12:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

The EA is not locked in any way. It has account and expiration date coding but that can be altered or removed if you desire to do so. NFA rules don't effect the EA as it only puts in one trade at a time and does not hedge. Like I said, I am no longer involved in this project. You'll have to have a coder take care of any changes or issues. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#418](/thread/post/3212196#post3212196 "Post Permalink")

  * Nov 6, 2009 7:45am  Nov 6, 2009 7:45am 

  * [ acereto](acereto)

  * | Joined Sep 2009  | Status: Trader | [29 Posts](/search?do=process&provider=Member&searchuser=117072)

is there anyway to make this EA work on a 4 digit broker ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#419](/thread/post/3595920#post3595920 "Post Permalink")

  * Mar 30, 2010 8:43pm  Mar 30, 2010 8:43pm 

  * [ Brb-Fraudin](brb-fraudin)

  * | Joined Jan 2009  | Status: 10K a day. | [502 Posts](/search?do=process&provider=Member&searchuser=90724)

> [Quoting mer071898](/thread/post/3152288#post3152288 "View Quoted Post")
> 
> Disliked
> 
> I am no longer involved in this project so please do not pm me to make changes in the code. You will need to have someone else make the changes for you. Since this EA has been unlawfully cracked and is available on the web, I will post it here for whoever wants to use it for whatever purpose, good luck.
> 
> Ignored

Its expired , anyone has unexpired version?? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#420](/thread/post/3597292#post3597292 "Post Permalink")

  * Mar 31, 2010 4:19am  Mar 31, 2010 4:19am 

  * [ Brb-Fraudin](brb-fraudin)

  * | Joined Jan 2009  | Status: 10K a day. | [502 Posts](/search?do=process&provider=Member&searchuser=90724)

Hello , anyone has unexpired EA? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#421](/thread/post/3598034#post3598034 "Post Permalink")

  * Mar 31, 2010 11:21am  Mar 31, 2010 11:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30318_5.gif) mer071898](mer071898)

  * Joined Jan 2007 | Status: Trader | [1,621 Posts](/search?do=process&provider=Member&searchuser=30318)

Open the .mq4 file in post #415 with MetaEditor and just change the date (see pic). 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Power SM.jpg
Size: 157 KB](/attachment/image/449167/thumbnail?d=1365620015)](/attachment/image/449167?d=1270002068)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#422](/thread/post/3646797#post3646797 "Post Permalink")

  * Apr 17, 2010 11:32am  Apr 17, 2010 11:32am 

  * [ tjsun80](tjsun80)

  * | Joined Oct 2007  | Status: Trader | [324 Posts](/search?do=process&provider=Member&searchuser=49947)

Hi,  
  
I saw your post.  
Do you have an EA for your hedging lot strategy?  
I find it interesting using this EA and i would like to have one.  
  

> [Quoting learn2gain](/thread/post/1982401#post1982401 "View Quoted Post")
> 
> Disliked
> 
> Hi Xaron and members, Just want to share one of martingle concept which I got. Your EA look like this one but only different at lot during entry buy/sell position and rule. Please look at the concept attached. I try to create this EA but not familiar with meta4. Hopefully someone can help me to create it and share here. Target is to get 40pips daily after one cycle complete. May be the best setting is 40 profit, step 40 and SL 60 for any pair. Also if using this concept, I think we can gain constant and profitable pip with small margin.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#423](/thread/post/3751026#post3751026 "Post Permalink")

  * May 25, 2010 4:05pm  May 25, 2010 4:05pm 

  * [ HealWhat](healwhat)

  * | Joined Oct 2009  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=121361)

Hi,  
  
May i know what is the NewCycle function for? 1 more thing, the ea sometimes did not start a new opposite trade when the current trade hit the stop loss. Did i miss out something?  
  
thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#424](/thread/post/3761845#post3761845 "Post Permalink")

  * May 29, 2010 1:19am  May 29, 2010 1:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar127274_1.gif) noogolf](noogolf)

  * | Joined Dec 2009  | Status: Trader | [29 Posts](/search?do=process&provider=Member&searchuser=127274)

I can open the EA only 1 round   
for next round can't open trade  
  
How to setting the EA? ( now i set RestarNewcycle = true ) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#425](/thread/post/3799165#post3799165 "Post Permalink")

  * Jun 14, 2010 5:54pm  Jun 14, 2010 5:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar91290_3.gif) andreasp70](andreasp70)

  * | Joined Jan 2009  | Status: Trader | [50 Posts](/search?do=process&provider=Member&searchuser=91290)

hello, just started reading. backtested original ea from post 1  
from 010108 to today using usdcad, using the same tp and sl of 50 pips for a 4 digit broker, its maximum winning streak was 12  
  
i think thats amazing. can we change the code to double up lot size after every winning trade? up to x level as per each traders liking? and restart sequence of original lot size when x level has been reached or if x level hasnt been reached. what i mean is if we have x = 10 and its reached level 8 and the 9thlevel isnt reached, next trade goes back to origianl lot size.  
  
seems like it will do the exact opposite of the original ea.  
  
if we have enough capital, or even using micro lots, hitting 12 straight wins equals a lot of profit for our account.  
  
thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#426](/thread/post/3799203#post3799203 "Post Permalink")

  * Jun 14, 2010 6:07pm  Jun 14, 2010 6:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar91290_3.gif) andreasp70](andreasp70)

  * | Joined Jan 2009  | Status: Trader | [50 Posts](/search?do=process&provider=Member&searchuser=91290)

gpbypn same setting. 13 wins in a row. amazing.  
  
i d be willing to bet to win 13 wins in a row.  
  
10 wins in a row with inital bet at $10 equals $10240 profit  
  
13 wins in a row = $82000  
  
simply wow.  
  
lets do it . i m willing to trade live right now. yes, im serious. this is what i ve searching for a couple of months. i know, its casino trading. but i do beleive that luck has something to do with trading as well. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#427](/thread/post/3807623#post3807623 "Post Permalink")

  * Jun 17, 2010 7:33am  Jun 17, 2010 7:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar86323_17.gif) Jigsaw](jigsaw)

  * | Joined Nov 2008  | Status: One Man Hedge Fund | [797 Posts](/search?do=process&provider=Member&searchuser=86323)

> [Quoting andreasp70](/thread/post/3799203#post3799203 "View Quoted Post")
> 
> Disliked
> 
> gpbypn same setting. 13 wins in a row. amazing.  
>    
>  i d be willing to bet to win 13 wins in a row.  
>    
>  10 wins in a row with inital bet at $10 equals $10240 profit  
>    
>  13 wins in a row = $82000  
>    
>  simply wow.  
>    
>  lets do it . i m willing to trade live right now. yes, im serious. this is what i ve searching for a couple of months. i know, its casino trading. but i do beleive that luck has something to do with trading as well. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

I actually don't think this semi-martingale stuff is casino trading at all.   
  
If you have high RR (one:five or better) and stop after eight or nine trades then you can improve the expectancy of any high RR system if you already have positive expectancy on the market.   
  
Still can't get this automated one to run for me in metatrader, however i havent a clue about EA's.   
  
Anybody know what I am doing wrong here ? As I sure as hell don't. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: prosm.jpg
Size: 444 KB](/attachment/image/492280/thumbnail?d=1365635389)](/attachment/image/492280?d=1276727453)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#428](/thread/post/3807902#post3807902 "Post Permalink")

  * Jun 17, 2010 10:40am  Jun 17, 2010 10:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar70177_3.gif) kijkij](kijkij)

  * | Commercial User  | Joined May 2008 | [211 Posts](/search?do=process&provider=Member&searchuser=70177)

> [Quoting Jigsaw](/thread/post/3807623#post3807623 "View Quoted Post")
> 
> Disliked
> 
> I actually don't think this semi-martingale stuff is casino trading at all.   
>    
>  If you have high RR (one:five or better) and stop after eight or nine trades then you can improve the expectancy of any high RR system if you already have positive expectancy on the market.   
>    
>  Still can't get this automated one to run for me in metatrader, however i havent a clue about EA's.   
>    
>  Anybody know what I am doing wrong here ? As I sure as hell don't.
> 
> Ignored

  
Try this one sir, I hope it will work for you also with 3 and 5 digit brokers. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [PowerSM.mq4](/attachment/file/492360?d=1276738806) 8 KB | 1,441 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#429](/thread/post/3838344#post3838344 "Post Permalink")

  * Jun 30, 2010 1:17am  Jun 30, 2010 1:17am 

  * [ rockon](rockon)

  * | Joined Jun 2010  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=146862)

it's great to have this EA..  
does anyone know how to add options to this EA to place their first trade on exact timing  
  
Eg.   
first trade will be place at 8.00 sharp  
instead of placing the first trade on x_price target   
  
let's rock! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#430](/thread/post/3840722#post3840722 "Post Permalink")

  * Jun 30, 2010 10:33pm  Jun 30, 2010 10:33pm 

  * [ rockon](rockon)

  * | Joined Jun 2010  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=146862)

> [Quoting rockon](/thread/post/3838344#post3838344 "View Quoted Post")
> 
> Disliked
> 
> it's great to have this EA..  
>  does anyone know how to add options to this EA to place their first trade on exact timing  
>    
>  Eg.   
>  first trade will be place at 8.00 sharp  
>  instead of placing the first trade on x_price target   
>    
>  let's rock!
> 
> Ignored

hi,  
i tried to add in some of the code..   
i manage to get the robot to place the first trade on exact time..  
but after they hit sl the cycle doesn't continue.. can anyone help fix this?  
  
\----new input----  
extern bool PreciseTimeEntry=false;  
extern string EntryTime="8:00";  
  
\----condition----  
  
if (PreciseTimeEntry)  
{  
datetime tm0 = TimeCurrent();  
datetime tm1 = StrToTime(TimeToStr(tm0, TIME_DATE) + " " + EntryTime);  
  
cond = (tm0 == tm1);  
if (!cond) return;  
  
} 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#431](/thread/post/4019648#post4019648 "Post Permalink")

  * Sep 14, 2010 4:16pm  Sep 14, 2010 4:16pm 

  * [ pearlo](pearlo)

  * | Joined Sep 2010  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=154805)

i believe its a good EA with the right settings, i'm running it with FXDD and it ok.  
  
now i tried i with IBFX and MBTrading but it only gives me errors.  
  
14:54:33 PowerSM EURUSDm,H1: buy open 0.01 0  
14:54:33 PowerSM EURUSDm,H1: market order:: EURUSDm 0 0.01 1.2862 1.2858 1.2866 0_eurusd_591801  
14:54:33 PowerSM EURUSDm,H1: error opening order : invalid stops  
  
can someone help me pls. TIA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#432](/thread/post/4070621#post4070621 "Post Permalink")

  * Oct 5, 2010 2:28am  Oct 5, 2010 2:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar151775_1.gif) farsisub](farsisub)

  * | Joined Aug 2010  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=151775)

> [Quoting mer071898](/thread/post/3598034#post3598034 "View Quoted Post")
> 
> Disliked
> 
> Open the .mq4 file in post #415 with MetaEditor and just change the date (see pic).
> 
> Ignored

hey my dear friend  
i have a question about PowerSm EA i want to know that how can i edit this ea that when i run this on any chart and open in specific time or price after that ea put 4,5,.... pending orders and when price touch these price and orders opened after that ea just set new T/p and s/L i mean that EA shall not be trade automatically when price touch 20pip away from first position just set t/p and s/l in new orders just like that we trade this strategy manually   
can u help me? i have no knowledge about mT4 coding 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#433](/thread/post/4838676#post4838676 "Post Permalink")

  * Edited 11:19pm  Aug 4, 2011 11:19pm | Edited 11:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar152124_1.gif) xxl205](xxl205)

  * | Joined Aug 2010  | Status: Trader | [151 Posts](/search?do=process&provider=Member&searchuser=152124)

Hey guys,  
  
just did some fun to watch demo and wanted to share it ... I have done some experimenting with the settings and tuned it to SL5 / TP12 / BE5 ... if anyone is interested, I could upload my version used and the setfiles also ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
<http://www.myfxbook.com/members/smee205/powersm/144576>  
  
Cheers, George 

"We are all just prisoners ... of our own device ..." (Hotel California)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#434](/thread/post/4838892#post4838892 "Post Permalink")

  * Aug 5, 2011 12:08am  Aug 5, 2011 12:08am 

  * [ saragosa](saragosa)

  * | Joined Sep 2006  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=19601)

> [Quoting xxl205](/thread/post/4838676#post4838676 "View Quoted Post")
> 
> Disliked
> 
> Hey guys,  
>    
>  just did some fun to watch demo and wanted to share it ... I have done some experimenting with the settings and tuned it to SL5 / TP12 / BE5 ... if anyone is interested, I could upload my version used and the setfiles also ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>    
>  <http://www.myfxbook.com/members/smee205/powersm/144576>  
>    
>  Cheers, George
> 
> Ignored

i cant wait for u share sir,,,  
thank you before 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#435](/thread/post/4839103#post4839103 "Post Permalink")

  * Aug 5, 2011 1:13am  Aug 5, 2011 1:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar152124_1.gif) xxl205](xxl205)

  * | Joined Aug 2010  | Status: Trader | [151 Posts](/search?do=process&provider=Member&searchuser=152124)

> [Quoting xxl205](/thread/post/4838676#post4838676 "View Quoted Post")
> 
> Disliked
> 
> Hey guys,  
>    
>  just did some fun to watch demo and wanted to share it ... I have done some experimenting with the settings and tuned it to SL5 / TP12 / BE5 ... if anyone is interested, I could upload my version used and the setfiles also ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>    
>  <http://www.myfxbook.com/members/smee205/powersm/144576>  
>    
>  Cheers, George
> 
> Ignored

Ok, here we go. The set-file must be renamed from powersm.txt into powersm.set accordingly.  
  
Changes were : TP 13 instead of 40, SL 5 instead of 10 and BE 5 instead of 10. Also I have set the TradingTimes to false because I watch it very closely and am prepared to shut it down immediatly if there occurs a lack of volatility.  
  
It has been fun to watch in NY session this afternoon. But it may get killed easily. You also need a broker with very small [spreads](/brokers/spreads "View Live Spreads on the Broker Guide"). On my Alpari UK demo this was not the problem, but running it live that might be a neckbreaker.  
  
I started it 1 hour before london opening and let it run until 3rd hour of NY session for today. I will NOT let this one run on its own by any means. Takes a lot of screen time, but hey ... the reward would be too cool ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
PLEASE BE AWARE : HIGH RISK MARTINGALE STRATEGY, USE AT OWN RISK ONLY ! I AM IN NO WAY RESPONSIBLE FOR ANY REAL LOSSES ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Bye, George 

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [powersm.txt](/attachment/file/756406?d=1312474227) < 1 KB | 779 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [PowerSM.mq4](/attachment/file/756407?d=1312474227) 8 KB | 963 downloads 

"We are all just prisoners ... of our own device ..." (Hotel California)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#436](/thread/post/4841963#post4841963 "Post Permalink")

  * Aug 5, 2011 6:48pm  Aug 5, 2011 6:48pm 

  * [ forfac](forfac)

  * | Joined May 2008  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=68720)

Hi xxl205  
  
What time frame are you using your EA on ?  
  
  
Thx  
Forfac 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#437](/thread/post/4842101#post4842101 "Post Permalink")

  * Aug 5, 2011 7:47pm  Aug 5, 2011 7:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar152124_1.gif) xxl205](xxl205)

  * | Joined Aug 2010  | Status: Trader | [151 Posts](/search?do=process&provider=Member&searchuser=152124)

> [Quoting forfac](/thread/post/4841963#post4841963 "View Quoted Post")
> 
> Disliked
> 
> Hi xxl205  
>    
>  What time frame are you using your EA on ?  
>    
>    
>  Thx  
>  Forfac
> 
> Ignored

Err, at this martingale EA the timeframe is not essential at all because it goes after price only. As soon as you start the EA, it will open an order and see where the journey goes. To watch it though I have it open the M1 timeframe.  
  
Observing it I have discovered a way to strech out the martingale effect a little more. Set the BreakEven setting to 2 or 3 ... that means if a BE is set and then hit, the EA takes this as a free trade and goes on with the SAME LOTSIZE in the other direction, because it actually didn't loose anything. That prevents it a little more from blowing the acount ^^  
  
Had fun again today, but it is scary NFP friday and the damn thing stalled very much unexpectedly, boosting lot sizes up to 16 ... but the account survived. This was before I set the BE from 5 to 2.  
  
I have switched it off for now, NY open I will be back again to see how this one handles the NFP anomalies.  
  
Cheers, George 

"We are all just prisoners ... of our own device ..." (Hotel California)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#438](/thread/post/4843333#post4843333 "Post Permalink")

  * Aug 6, 2011 1:04am  Aug 6, 2011 1:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar93533_3.gif) starlimit03](starlimit03)

  * | Joined Feb 2009  | Status: Trader | [45 Posts](/search?do=process&provider=Member&searchuser=93533)

Just attached the EA to my Major 10 pairs a demo account of $300 using starting lot of 0.01. the current closing balance is $342.... more testing next week. 

It takes the Mind to Make Money.............

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#439](/thread/post/4844629#post4844629 "Post Permalink")

  * Aug 6, 2011 5:18pm  Aug 6, 2011 5:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar152124_1.gif) xxl205](xxl205)

  * | Joined Aug 2010  | Status: Trader | [151 Posts](/search?do=process&provider=Member&searchuser=152124)

> [Quoting starlimit03](/thread/post/4843333#post4843333 "View Quoted Post")
> 
> Disliked
> 
> Just attached the EA to my Major 10 pairs a demo account of $300 using starting lot of 0.01. the current closing balance is $342.... more testing next week.
> 
> Ignored

ok, but be very careful not to overtrade with multiple pairs. Check your lotsize limits and the progressions therefor. At Alpari UK for instance I can only trade from 0.01 to 2 lots on a micro account. On the classic accounts it is from 0.1 to open end / account balance.  
  
I won't ever let this one trade on its own. I am using it more like a trade helping EA. Currently I am looking for a good volatility indicator that could tell us if we could dare to trade or better not.  
  
Now as USA has finally gotten rated down, I expect enough volatility next week an on ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Cheers, George 

"We are all just prisoners ... of our own device ..." (Hotel California)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#440](/thread/post/4844632#post4844632 "Post Permalink")

  * Aug 6, 2011 5:23pm  Aug 6, 2011 5:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar152124_1.gif) xxl205](xxl205)

  * | Joined Aug 2010  | Status: Trader | [151 Posts](/search?do=process&provider=Member&searchuser=152124)

Hey guys,  
  
as I was experimenting with different lot sizes on the martingale progression, I made a little mistake in separating them with a semicolon.  
  
E.g. if you look at the lotsizes input it says 0.1;0.1;0.2;0.3;0.4 and so on.  
Now if you put in a blank between them like 0.8;;1.1;1.65 or so, the EA pauses between 0.8 and 1.1 lots ... this could be used as a safety feature to stop it and prevent further damage for the moment chosen.  
  
After removing the blank from 0.8;;1.1 to 0.8;1.1 the EA continues to trade with the right progression and you could do so if volatility has come back ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

"We are all just prisoners ... of our own device ..." (Hotel California)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

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

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[PowerSM Semi-Martingale EA Trades](/thread/159789-powersm-semi-martingale-ea-trades "***Everybody, as a courtesy, please refrain from coming in this journal and warning everyone how bad martingale methods are! I have...") 54 replies

[Safe (PowerSM Modified) EA](/thread/234976-safe-powersm-modified-ea "Hello. I'm not a big EA fan, but I do find some to be useful or worth trying. I found this one some time ago on the internet somewhere...") 72 replies

[FXTradepro: Strategy using a “Semi-Martingale” Position Sizing](/thread/43221-fxtradepro-strategy-using-a-semi-martingale-position-sizing "Hello Traders: 
  
 

[Simple MACD w/ Semi-Martingale MM](/thread/20001-simple-macd-w-semi-martingale-mm "System is as follows: 
 
Eur/Usd Gbp/Usd 4h charts. 
 
Enter at the candle after the cross, cross down=short and vise versa. 
 
Stop loss...") 8 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)
  * Subscribe
  * [80](javascript:void\(0\);)

Attachments: PowerSM Semi-Martingale EA

Tags: PowerSM Semi-Martingale EA

#  [](/thread/75394-powersm-semi-martingale-ea)PowerSM Semi-Martingale EA 

  * 

  * [#441](/thread/post/4844832#post4844832 "Post Permalink")

  * Aug 6, 2011 9:06pm  Aug 6, 2011 9:06pm 

  * [ forfac](forfac)

  * | Joined May 2008  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=68720)

Thanks for your further insights in tweeking the BE xxI205  
  
I'll give them settings a run and see how we go.  
  
  
Thanks,  
forfac 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#442](/thread/post/4850259#post4850259 "Post Permalink")

  * Aug 9, 2011 12:36am  Aug 9, 2011 12:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar152124_1.gif) xxl205](xxl205)

  * | Joined Aug 2010  | Status: Trader | [151 Posts](/search?do=process&provider=Member&searchuser=152124)

Ok, demo blown away. Closed thread thus for me ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) moving on. 

"We are all just prisoners ... of our own device ..." (Hotel California)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#443](/thread/post/4852845#post4852845 "Post Permalink")

  * Aug 9, 2011 4:19pm  Aug 9, 2011 4:19pm 

  * [ forfac](forfac)

  * | Joined May 2008  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=68720)

Same here ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#444](/thread/post/4956437#post4956437 "Post Permalink")

  * Sep 15, 2011 3:14pm  Sep 15, 2011 3:14pm 

  * [ fx_daimon](fx_daimon)

  * | Joined Sep 2011  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=194737)

> [Quoting xxl205](/thread/post/4850259#post4850259 "View Quoted Post")
> 
> Disliked
> 
> Ok, demo blown away. Closed thread thus for me ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) moving on.
> 
> Ignored

Dear xxl205,  
  
I want to ask a question about blown away demo account.   
What was the ae setting. what were the currencies you tried.  
  
Thx a lot. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#445](/thread/post/6022002#post6022002 "Post Permalink")

  * Sep 19, 2012 12:24am  Sep 19, 2012 12:24am 

  * [ elconde1969](elconde1969)

  * | Joined Apr 2012  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=250086)

hello .. while I am testing this with another ea ea managed sl closure and movement, trailinea.  
  
interesting that someone would be able to encode with a trailing powersm several positions, with this we get that positive transactions coming in say 20 or 30 pits, pits secure 10 or 20 so if the market changes and no loss no is passed to the next batch, as does the current breakeven ...  
  
One option could be to put points level 3 or 4 and its own fixed sl and last level with trailstoploss to close the order can take maximum benefits.  
  
only if the last act resetearia cycle level, the other levels are positive if repeated lot and if negative happens next lot ..  
  
I've been doing this manually and works well with smaller lots as not all close to the total initial soptloss and positive benefit to the total added to increase without lots ...  
  
  
  
Please excuse my English is google  
  
  
  
Thanks in advance and congratulations for the work done  
  
  
  
salu2 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#446](/thread/post/6055058#post6055058 "Post Permalink")

  * Last Post: Sep 30, 2012 11:27pm  Sep 30, 2012 11:27pm 

  * [ elconde1969](elconde1969)

  * | Joined Apr 2012  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=250086)

this is two ea i am used... but i nedd the orders closed in positive.. no count for slot ... than the breakevent close no count .. i need the order in +o and -250 no count for the slot +1 ok ...sorry for my englis...  
  
salu2 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [TrailingEA mod elconde.mq4](/attachment/file/1048766?d=1349014966) 29 KB | 563 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [PowerSM -250+250 prueba.mq4](/attachment/file/1048769?d=1349015064) 8 KB | 790 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * PowerSM Semi-Martingale EA
  *   * [ **Reply to Thread** ](/thread/75394-powersm-semi-martingale-ea/reply#reply)

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)
