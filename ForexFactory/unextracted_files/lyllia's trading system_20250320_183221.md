

  * 

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#1](/thread/160639-lyllias-trading-system "Post Permalink")

  * First Post: Edited Apr 10, 2009 11:15pm  Mar 29, 2009 4:32pm | Edited Apr 10, 2009 11:15pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I start this trading thread to share with fellow traders my trading system.See template_fx attached.Apply it to your chart, any time frame .I prefer one hour ++. Hope you enjoy and try it on Monday.  
  
All the indicators included from the internet published resources.The most reliable indicator is IINWMARROWS.mq4.It is the core of this system. It has 95% + successful rate.In another word, if you only trade this arrow. you could be able to make pips.....;  
  
Other indicators are used as reference.They are together make a complet system.After you used this system,hope you could share your experience here. And you could make suggestion of any adjustments to make this system promising and more perfect.Thanks! Looking forward to your opinions.  
Please download all the indicators in post 18 & 19.  
  
lyllia 

Attached File(s)

![File Type: tpl](https://assets.faireconomy.media/images/attach/tpl.gif) [template_fx.tpl](/attachment/file/225260?d=1238311935) 15 KB | 4,269 downloads 

  * [#2](/thread/post/2635314#post2635314 "Post Permalink")

  * Mar 29, 2009 4:35pm  Mar 29, 2009 4:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar48267_23.gif) Oksana17](oksana17)

  * | Membership Revoked  | Joined Sep 2007 | [903 Posts](/search?do=process&provider=Member&searchuser=48267)

> [Quoting lyllia](/thread/post/2635312#post2635312 "View Quoted Post")
> 
> Disliked
> 
> I start this trading thread to share with fellow traders my trading system.See template_fx attached.Apply it to your chart, any time frame .I prefer one hour ++. Hope you enjoy and try it on Monday.  
>    
>  All the indicators included from the internet published resources.The most reliable indicator is IINWMARROWS.mq4.It is the core of this system. It has 95% + successful rate.In another word, if you only trade this arrow. you could be able to make pips.....;  
>    
>  Other indicators are used as reference.They are together make a complet system.After you...
> 
> Ignored

Hi. Interesting. Would you mind sharing all of the indicators that produce this templete, i.e., IINWMARROWS.mq4 would be one.  
Thanks. 

Request custom Expert Advisor or Indicator: dostapyuk "at" gmail . com

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#3](/thread/post/2635315#post2635315 "Post Permalink")

  * Mar 29, 2009 4:37pm  Mar 29, 2009 4:37pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I find this system is very good.And I perfer somebody could help make a EA from the indicator:IINWMARROWS.mq4,which I have used for a long time.Very reliable,95% successful rate.If somebody could make an EA for it then everybody will be benifit from it.  
  
The rules of the Ea are very simple:  
  
1\. As soon as the selling arrow appeared the sell position will be open,same for the buy position;  
2.sell and buy position close each other.  
3.If in one time frame there are several sell arrows(eg.several selling position opned),then the first buy arrow will close all the positions opened.Same for the buy position.  
4.no stop loss.  
5.no trailling stop.(leave all the positions to the arrow,or you could manually close the postion as you wish).  
6.set time frame preference adjustable by the user.eg,user could decide which time frame chart to be used. For example I use daily and 4 hours time frame only.  
7.original code of the indicator attached as following:  
  
//+------------------------------------------------------------------+  
//| IINWMARROWS.mq4 |  
//| Based on EMA_CROSS.mq4 |  
//| Copyright ?2006, MetaQuotes Software Corp. |  
//| [http://www.metaquotes.net](http://www.metaquotes.net/) |  
//| Last little modified by Iin Zulkarnain |  
//+------------------------------------------------------------------+  
#property copyright "Copyright ?2006, MetaQuotes Software Corp."  
#property link "[http://www.metaquotes.net](http://www.metaquotes.net/)"  
//----  
#property indicator_chart_window  
#property indicator_buffers 2  
#property indicator_color1 White  
#property indicator_color2 Red  
#property indicator_width1 2  
#property indicator_width2 2  
//----  
double CrossUp[];  
double CrossDown[];  
extern int FasterMode=3; //0=sma, 1=ema, 2=smma, 3=lwma  
extern int FasterMA= 3;  
extern int SlowerMode=3; //0=sma, 1=ema, 2=smma, 3=lwma  
extern int SlowerMA= 3;  
//+------------------------------------------------------------------+  
//| Custom indicator initialization function |  
//+------------------------------------------------------------------+  
int init()  
{  
//---- indicators  
SetIndexStyle(0, DRAW_ARROW, EMPTY);  
SetIndexArrow(0, 233);  
SetIndexBuffer(0, CrossUp);  
SetIndexStyle(1, DRAW_ARROW, EMPTY);  
SetIndexArrow(1, 234);  
SetIndexBuffer(1, CrossDown);  
//----  
return(0);  
}  
//+------------------------------------------------------------------+  
//| Custom indicator deinitialization function |  
//+------------------------------------------------------------------+  
int deinit()  
{  
//----   
//----  
return(0);  
}  
//+------------------------------------------------------------------+  
//| Custom indicator iteration function |  
//+------------------------------------------------------------------+  
int start()   
{  
int limit, i, counter;  
double fasterMAnow, slowerMAnow, fasterMAprevious, slowerMAprevious, fasterMAafter, slowerMAafter;  
double Range, AvgRange;  
int counted_bars=IndicatorCounted();  
//---- check for possible errors  
if(counted_bars<0) return(-1);  
//---- last counted bar will be recounted  
if(counted_bars>0) counted_bars--;  
//----  
limit=Bars-counted_bars;  
for(i=0; i<=limit; i++)   
{  
counter=i;  
Range=0;  
AvgRange=0;  
for(counter=i ;counter<=i+9;counter++)  
{  
AvgRange=AvgRange+MathAbs(High[counter]-Low[counter]);  
}  
Range=AvgRange/10;  
fasterMAnow=iMA(NULL, 0, FasterMA, 0, FasterMode, PRICE_CLOSE, i);  
fasterMAprevious=iMA(NULL, 0, FasterMA, 0, FasterMode, PRICE_CLOSE, i+1);  
fasterMAafter=iMA(NULL, 0, FasterMA, 0, FasterMode, PRICE_CLOSE, i-1);  
//----  
slowerMAnow=iMA(NULL, 0, SlowerMA, 0, SlowerMode, PRICE_OPEN, i);  
slowerMAprevious=iMA(NULL, 0, SlowerMA, 0, SlowerMode, PRICE_OPEN, i+1);  
slowerMAafter=iMA(NULL, 0, SlowerMA, 0, SlowerMode, PRICE_OPEN, i-1);  
if ((fasterMAnow > slowerMAnow) && (fasterMAprevious < slowerMAprevious) && (fasterMAafter > slowerMAafter))   
{  
CrossUp[i]=Low[i] - Range*0.5;  
}  
else if ((fasterMAnow < slowerMAnow) && (fasterMAprevious > slowerMAprevious) && (fasterMAafter < slowerMAafter))   
{  
CrossDown[i]=High[i] + Range*0.5;  
}  
}  
return(0);  
}  
//+------------------------------------------------------------------+  
  
Hope somebody here could help!After it has been compiled into Ea,pleae give me a notice:lyllia45@yhoo.com.au Tia.  
  
lyllia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#4](/thread/post/2635316#post2635316 "Post Permalink")

  * Mar 29, 2009 4:38pm  Mar 29, 2009 4:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar54316_6.gif) magnumfreak](magnumfreak)

  * Joined Nov 2007 | Status: Trying manual mode again | [2,210 Posts](/search?do=process&provider=Member&searchuser=54316)

> [Quoting Oksana17](/thread/post/2635314#post2635314 "View Quoted Post")
> 
> Disliked
> 
> Hi. Interesting. Would you mind sharing all of the indicators that produce this templete, i.e., IINWMARROWS.mq4 would be one.  
>  Thanks.
> 
> Ignored

Don't bother, when you see the code you will see that it repaints. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#5](/thread/post/2635317#post2635317 "Post Permalink")

  * Mar 29, 2009 4:39pm  Mar 29, 2009 4:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar48267_23.gif) Oksana17](oksana17)

  * | Membership Revoked  | Joined Sep 2007 | [903 Posts](/search?do=process&provider=Member&searchuser=48267)

Hi lyllia,  
I'll take a look into the indicator.  
If I see it worked well in history, I'll code it for you; no sweat. 

Request custom Expert Advisor or Indicator: dostapyuk "at" gmail . com

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#6](/thread/post/2635321#post2635321 "Post Permalink")

  * Mar 29, 2009 4:42pm  Mar 29, 2009 4:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar48267_23.gif) Oksana17](oksana17)

  * | Membership Revoked  | Joined Sep 2007 | [903 Posts](/search?do=process&provider=Member&searchuser=48267)

> [Quoting magnumfreak](/thread/post/2635316#post2635316 "View Quoted Post")
> 
> Disliked
> 
> Don't bother, when you see the code you will see that it repaints.
> 
> Ignored

LOL, you're right. When you hear someone say 95%, you think of the word repaint.   
  
Look at attached. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.JPG
Size: 70 KB](/attachment/image/225263/thumbnail?d=1365566474)](/attachment/image/225263?d=1238312513)   

Request custom Expert Advisor or Indicator: dostapyuk "at" gmail . com

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#7](/thread/post/2635322#post2635322 "Post Permalink")

  * Mar 29, 2009 4:43pm  Mar 29, 2009 4:43pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Hi nice to meet you here.Are you a programmer?Can you help?Just make an EA for IINWMARROWS.mq4.That will be enough.Do not make it too complicated.The simple, the effective ,the better.  
  
If you apply the template to the chart then you will know all the indicators. I try to find them in my system and attached here later on. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#8](/thread/post/2635323#post2635323 "Post Permalink")

  * Mar 29, 2009 4:44pm  Mar 29, 2009 4:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar48267_23.gif) Oksana17](oksana17)

  * | Membership Revoked  | Joined Sep 2007 | [903 Posts](/search?do=process&provider=Member&searchuser=48267)

> [Quoting lyllia](/thread/post/2635322#post2635322 "View Quoted Post")
> 
> Disliked
> 
> Hi nice to meet you here.Are you a programmer?Can you help?Just make an EA for IINWMARROWS.mq4.That will be enough.Do not make it too complicated.The simple, the effective ,the better.  
>    
>  If you apply the template to the chart then you will know all the indicators. I try to find them in my system and attached here later on.
> 
> Ignored

Yes, I'm a programmer. Are you aware that this indicator has a 95% chance that it repaints? 

Request custom Expert Advisor or Indicator: dostapyuk "at" gmail . com

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#9](/thread/post/2635330#post2635330 "Post Permalink")

  * Mar 29, 2009 5:00pm  Mar 29, 2009 5:00pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Like I said the arrow will repraint several times in one time frame such as four hours.Which means if four buy arrows appear then four positions will be opened, and the first sell arrow would close them all.It is like a self- position menagement manager.  
  
I basically use it in 4hrs time frame.it is quite reliable.In shorter time frame.There are more failed rate when there is congestion area.Because sell and buy arrow close each other all the time.Make little pips or no pips (like stop/loss, not a big deal) but risk reward ratio is still very good once a good potion is opened .All the pips earned back.I prefer using this indicator to make an EA for One hr + .The most important thindg is it is very simple. I like to discuss any issues regarding this system.Thanks for your observation.  
  
lyllia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#10](/thread/post/2635334#post2635334 "Post Permalink")

  * Mar 29, 2009 5:03pm  Mar 29, 2009 5:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar48267_23.gif) Oksana17](oksana17)

  * | Membership Revoked  | Joined Sep 2007 | [903 Posts](/search?do=process&provider=Member&searchuser=48267)

> [Quoting lyllia](/thread/post/2635330#post2635330 "View Quoted Post")
> 
> Disliked
> 
> Like I said the arrow will repraint several times in one time frame such as...
> 
> Ignored

Lyllia,  
I understand. I'll take a shot of coding on the EA. But it's pretty late here; I'm going to code it tomorrow if no one will while I'm sleeping.   
Post trades you made on demo or live account. That would be interesting as well! 

Request custom Expert Advisor or Indicator: dostapyuk "at" gmail . com

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#11](/thread/post/2635345#post2635345 "Post Permalink")

  * Mar 29, 2009 5:17pm  Mar 29, 2009 5:17pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I also think the repaint is a good advantage of this indicator.  
  
Take 4 hrs's Euro as an example: from 1.2445 area you star to get 7 buy arrows and 6 sell arrows; The positions are all closed. No stop/loss. no failed position. The buy and sell arrows are not even because between 1.2758 and 1.3032 there are two buy arrow and one sell arrow.The sell arrow closed the two buy arrows.  
  
And then from 1.3757 to 1.3290 area, There are 6 sell arrows and only 4 buy arrows.which means the first buy arrow has to close the firt two sell arrows and the last sell arrow has not been closed due to no buy arrow appears.Which also mean the down trend maybe continue and we have to wait for it to come out on Monday.  
  
lyllia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#12](/thread/post/2635349#post2635349 "Post Permalink")

  * Mar 29, 2009 5:25pm  Mar 29, 2009 5:25pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Take your time.If you could do it it will be very much appreciated. I will test it and post result here for further improvment.   
  
I also would like everybody share the fruit of the sytem.Because it is hard to get good sytem to trade.Many traders lost their money deserve to get them back if they got a good sytem. Have a good weekend!Looking forward to your EA.  
  
lyllia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#13](/thread/post/2635352#post2635352 "Post Permalink")

  * Mar 29, 2009 5:28pm  Mar 29, 2009 5:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar96656_4.gif) $aly]($aly)

  * | Commercial User  | Joined Mar 2009 | [183 Posts](/search?do=process&provider=Member&searchuser=96656)

hi iyllia  
thanks for sharing your system which pairs do you use???? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#14](/thread/post/2635357#post2635357 "Post Permalink")

  * Mar 29, 2009 5:37pm  Mar 29, 2009 5:37pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

please have a look at the chart Euro daily. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: euro daily.gif
Size: 25 KB](/attachment/image/225268/thumbnail?d=1365566474)](/attachment/image/225268?d=1238315804)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#15](/thread/post/2635358#post2635358 "Post Permalink")

  * Mar 29, 2009 5:40pm  Mar 29, 2009 5:40pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Chart euro 4hrs 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: euro 4hrs.gif
Size: 21 KB](/attachment/image/225273/thumbnail?d=1365566474)](/attachment/image/225273?d=1238315986)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#16](/thread/post/2635361#post2635361 "Post Permalink")

  * Mar 29, 2009 5:43pm  Mar 29, 2009 5:43pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

euro 1 hr 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: euro 1hrs.gif
Size: 22 KB](/attachment/image/225275/thumbnail?d=1365566474)](/attachment/image/225275?d=1238316186)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#17](/thread/post/2635364#post2635364 "Post Permalink")

  * Mar 29, 2009 5:45pm  Mar 29, 2009 5:45pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

euro weekly 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: euro weekly.gif
Size: 24 KB](/attachment/image/225276/thumbnail?d=1365566474)](/attachment/image/225276?d=1238316285)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#18](/thread/post/2635367#post2635367 "Post Permalink")

  * Mar 29, 2009 5:51pm  Mar 29, 2009 5:51pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

All the indicators attached 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [IINWMARROWS.mq4](/attachment/file/225277?d=1238316479) 4 KB | 4,164 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Heiken Ashi.mq4](/attachment/file/225278?d=1238316532) 4 KB | 1,864 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [BeginnerAlert.mq4](/attachment/file/225279?d=1238316563) 4 KB | 2,663 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Auto Pivot 4.04.mq4](/attachment/file/225282?d=1238316589) 17 KB | 2,242 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [SilverTrend Signal w[1].Alert.mq4](/attachment/file/225283?d=1238316616) 3 KB | 2,369 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [SHI_Channel_true.mq4](/attachment/file/225284?d=1238316641) 7 KB | 2,275 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Rads MACD.mq4](/attachment/file/225285?d=1238316690) 3 KB | 2,445 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#19](/thread/post/2635368#post2635368 "Post Permalink")

  * Mar 29, 2009 5:54pm  Mar 29, 2009 5:54pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

all the indicators continue 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Fisher_Yur4ik_2.mq4](/attachment/file/225286?d=1238316794) 2 KB | 2,442 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [_____ABHA CENTER TIMING SIGNAL AVG.ex4](/attachment/file/225287?d=1238316809) 10 KB | 3,245 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Gann Hi-lo Activator SSL.mq4](/attachment/file/225288?d=1238316855) 2 KB | 2,267 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Signal Line.mq4](/attachment/file/225289?d=1238316884) 4 KB | 2,301 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#20](/thread/post/2635373#post2635373 "Post Permalink")

  * Mar 29, 2009 6:24pm  Mar 29, 2009 6:24pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Anybody who use this system pay attention to IINWMARROWS.mq4 indicator. I do not know the the author but I think we owe to him or her. it is the best reliable indicator I have come cross.Try it for yourself .  
  
And if you have a good system or indicator,please introduce them here.  
  
If you are a programmer,please help to make it an EA.  
  
Please make improvment of this system for non -commercial purpose.Because if a trader get a good system which could make money you do not have to sell the system for commercial purpose.Just help both losing trader and new trader to have a good start.We all know trading is not that easy and simple like those broker said. But if we could have a good & simple trading system,that will make things a lot easier.  
  
lyllia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#21](/thread/post/2635378#post2635378 "Post Permalink")

  * Mar 29, 2009 6:37pm  Mar 29, 2009 6:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83209_5.gif) pitpiter](pitpiter)

  * | Joined Oct 2008  | Status: Trader | [300 Posts](/search?do=process&provider=Member&searchuser=83209)

Hi there.  
Please introduse all rules for trade this system , it will help make EA. On your chart You have more indi and I hope You use all of them for generate or confirm signal.  
Regards  
Peter 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#22](/thread/post/2635398#post2635398 "Post Permalink")

  * Mar 29, 2009 7:10pm  Mar 29, 2009 7:10pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Other indicators for visual reference only.Because they are not reliable.Once IINWMARROWS.mq4 come out it confirms all. Use them as reference only for manual trading purpose.Because they are very instructive.  
  
For an example,3 level zz moves with th price action until IINWMARROWS.mq4 come out to confirm the major top is in place.  
  
Fish yur4ik and IINWMARROWS.mq4 could confirm with each other.But that only for manual trading purpose.If you could work out the way to make both of them confirm each other in one EA it would be better. If it is too complicated just make it for IINWMARROWS.mq4.That will be enough.same apply to Heiken Ashi.A very good indicator.  
  
Gann hi-lo and silver trend signal can be used to confirm as well but only for visual manual trading purpose .Because they move with the PA which could make trader confusing.  
  
Also for day trader,pay attention to daily R2 and S2.That will be enough for trading.  
  
The reason I only suggest IINWMARROWS.mq4 because it is stable and reliable .Thanks for your help!  
  
lyllia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#23](/thread/post/2635401#post2635401 "Post Permalink")

  * Mar 29, 2009 7:15pm  Mar 29, 2009 7:15pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

aud weekly,daily,4hrs 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: aud weekly.gif
Size: 24 KB](/attachment/image/225308/thumbnail?d=1365566474)](/attachment/image/225308?d=1238321613)   
[![Click to Enlarge

Name: aud daily.gif
Size: 26 KB](/attachment/image/225309/thumbnail?d=1365566474)](/attachment/image/225309?d=1238321629)   
[![Click to Enlarge

Name: aud 4hr.gif
Size: 22 KB](/attachment/image/225310/thumbnail?d=1365566474)](/attachment/image/225310?d=1238321645)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#24](/thread/post/2635403#post2635403 "Post Permalink")

  * Mar 29, 2009 7:16pm  Mar 29, 2009 7:16pm 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

I run the indicator IINWMARROWS via the strategy tester [once the arrow is drawn it will stick there and will not be erase even if it redraw]. IMO, the 4H will work a whole lot better than 1H becoz I saw many arrows in 1H chart when in consolidation and too many arrows means kills a lot of profit [which is why u said lower TF doesnt work]. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#25](/thread/post/2635406#post2635406 "Post Permalink")

  * Mar 29, 2009 7:23pm  Mar 29, 2009 7:23pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

3 level zz is in place but it might move with PA because IINWMARROWS.mq4 did not come out.Which might be indicate a new high next week. Then the 3 level zz will adjust itself to the new high. or we wait Monday the IINWMARROWS.mq4 come out to confirm it.  
  
4hr is OK.4hr need a big Green 3 level zz with the confirmation of IINWMARROWS.mq4 to make a new low then goes higher.  
which principle apply all the time frame. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#26](/thread/post/2635413#post2635413 "Post Permalink")

  * Mar 29, 2009 7:34pm  Mar 29, 2009 7:34pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

You are right.Please refer to my previous post. As a trader we prefer larger time frame.  
  
GBP 4hr there is big green dot but IINWMARROWS.mq4 did not come out .so we have to wait it come out on Monday. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: gbp weekly.gif
Size: 21 KB](/attachment/image/225312/thumbnail?d=1365566474)](/attachment/image/225312?d=1238322741)   
[![Click to Enlarge

Name: gbp daily.gif
Size: 27 KB](/attachment/image/225313/thumbnail?d=1365566474)](/attachment/image/225313?d=1238322751)   
[![Click to Enlarge

Name: gbp 4hr.gif
Size: 23 KB](/attachment/image/225314/thumbnail?d=1365566474)](/attachment/image/225314?d=1238322763)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#27](/thread/post/2635418#post2635418 "Post Permalink")

  * Mar 29, 2009 7:41pm  Mar 29, 2009 7:41pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

4hr's new low is in place ,need new top being confirmed next week. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: chf weekly.gif
Size: 27 KB](/attachment/image/225315/thumbnail?d=1365566474)](/attachment/image/225315?d=1238323277)   
[![Click to Enlarge

Name: chf daily.gif
Size: 26 KB](/attachment/image/225316/thumbnail?d=1365566474)](/attachment/image/225316?d=1238323289)   
[![Click to Enlarge

Name: chf 4hr.gif
Size: 23 KB](/attachment/image/225317/thumbnail?d=1365566474)](/attachment/image/225317?d=1238323301)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#28](/thread/post/2635420#post2635420 "Post Permalink")

  * Edited 7:50pm  Mar 29, 2009 7:43pm | Edited 7:50pm 

  * [ victusa](victusa)

  * | Joined Mar 2008  | Status: Mr | [12 Posts](/search?do=process&provider=Member&searchuser=65342)

[lyllia](http://www.forexfactory.com/member.php?u=67706),  
  
The indicators as shown on the attached graph could not be shown on my chart, So what do I do? Especially the buy/sell arrows. You can see the attached. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: what i see.gif
Size: 50 KB](/attachment/image/225318/thumbnail?d=1365566474)](/attachment/image/225318?d=1238323775)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#29](/thread/post/2635425#post2635425 "Post Permalink")

  * Mar 29, 2009 7:51pm  Mar 29, 2009 7:51pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

4hr new low is in place, Daily new low is not in place. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: cad weekly.gif
Size: 18 KB](/attachment/image/225319/thumbnail?d=1365566474)](/attachment/image/225319?d=1238323847)   
[![Click to Enlarge

Name: cad daily.gif
Size: 21 KB](/attachment/image/225320/thumbnail?d=1365566474)](/attachment/image/225320?d=1238323857)   
[![Click to Enlarge

Name: cad 4hr.gif
Size: 18 KB](/attachment/image/225321/thumbnail?d=1365566474)](/attachment/image/225321?d=1238323868)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#30](/thread/post/2635428#post2635428 "Post Permalink")

  * Mar 29, 2009 7:58pm  Mar 29, 2009 7:58pm 

  * [ Mandl2007](mandl2007)

  * | Membership Revoked  | Joined Nov 2008 | [279 Posts](/search?do=process&provider=Member&searchuser=86165)

Opening the template from your first post, I got another picture - without all the indi's ! I can see only the pivots, HA's and the channel ?  
  
Is there any alert for the sell/buy arrows ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#31](/thread/post/2635430#post2635430 "Post Permalink")

  * Mar 29, 2009 8:03pm  Mar 29, 2009 8:03pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

weekly new high ahead.daily and 4hrs new low need to be confirmed 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: gjpy weekly.gif
Size: 21 KB](/attachment/image/225324/thumbnail?d=1365566474)](/attachment/image/225324?d=1238324559)   
[![Click to Enlarge

Name: gjpy daily.gif
Size: 23 KB](/attachment/image/225325/thumbnail?d=1365566474)](/attachment/image/225325?d=1238324569)   
[![Click to Enlarge

Name: gjpy 4hrs.gif
Size: 23 KB](/attachment/image/225326/thumbnail?d=1365566474)](/attachment/image/225326?d=1238324580)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#32](/thread/post/2635432#post2635432 "Post Permalink")

  * Mar 29, 2009 8:06pm  Mar 29, 2009 8:06pm 

  * [ Mandl2007](mandl2007)

  * | Membership Revoked  | Joined Nov 2008 | [279 Posts](/search?do=process&provider=Member&searchuser=86165)

wow ... lyllia you are posting like a machine !!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#33](/thread/post/2635435#post2635435 "Post Permalink")

  * Mar 29, 2009 8:09pm  Mar 29, 2009 8:09pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Weekly and daily new high need to be confirmed.4hr new low need to be confirmed. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: ejpy weekly.gif
Size: 22 KB](/attachment/image/225327/thumbnail?d=1365566474)](/attachment/image/225327?d=1238324952)   
[![Click to Enlarge

Name: ejpy daily.gif
Size: 27 KB](/attachment/image/225328/thumbnail?d=1365566474)](/attachment/image/225328?d=1238324963)   
[![Click to Enlarge

Name: ejpy 4hr.gif
Size: 23 KB](/attachment/image/225329/thumbnail?d=1365566474)](/attachment/image/225329?d=1238324975)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#34](/thread/post/2635439#post2635439 "Post Permalink")

  * Edited 10:33pm  Mar 29, 2009 8:13pm | Edited 10:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83209_5.gif) pitpiter](pitpiter)

  * | Joined Oct 2008  | Status: Trader | [300 Posts](/search?do=process&provider=Member&searchuser=83209)

Try this one. It open trade after bar on which indi generate signal close.  
Good luck  
Peter  
edit look post 62 for correct version 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [lyliaEA.mq4](/attachment/file/225330?d=1238325124) 3 KB | 966 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#35](/thread/post/2635442#post2635442 "Post Permalink")

  * Mar 29, 2009 8:16pm  Mar 29, 2009 8:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83209_5.gif) pitpiter](pitpiter)

  * | Joined Oct 2008  | Status: Trader | [300 Posts](/search?do=process&provider=Member&searchuser=83209)

> [Quoting Mandl2007](/thread/post/2635428#post2635428 "View Quoted Post")
> 
> Disliked
> 
> Opening the template from your first post, I got another picture - without all the indi's ! I can see only the pivots, HA's and the channel ?  
>    
>  Is there any alert for the sell/buy arrows ?
> 
> Ignored

You need download all indi for getting the same pic , because now it show only indi which You have in your mt4 folder  
Hope it help  
Peter 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#36](/thread/post/2635445#post2635445 "Post Permalink")

  * Mar 29, 2009 8:17pm  Mar 29, 2009 8:17pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

with 4h ejpy chart from 1.22 area to 134.89 area we have 7 buy arrows and only two sell arrows.which means the first buy arrow has been closed by first sell arrow.And left 6 buy arrows have been closed by sell second arrow. Make your own observation.   
  
There are so many opportunities in fx trading .So only depends on manual trading is not enough.So an Ea is needed. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#37](/thread/post/2635446#post2635446 "Post Permalink")

  * Mar 29, 2009 8:20pm  Mar 29, 2009 8:20pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Thanks for your help! I will try it and post result. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#38](/thread/post/2635447#post2635447 "Post Permalink")

  * Mar 29, 2009 8:30pm  Mar 29, 2009 8:30pm 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

i think what kills the arrow is strong reverse like EURUSD recent last 2 arrow.  
  
\- 250 pips drop. 

Attached Image

![](/attachment/image/225332?d=1238326202)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#39](/thread/post/2635448#post2635448 "Post Permalink")

  * Mar 29, 2009 8:31pm  Mar 29, 2009 8:31pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I am not a programmer.Does this EA will close all the postions opened in one time frame? like the one in Ejpy 4 hr chart as per my last post befor this one. For an example I only want to use 4hr time frame . How could I adjust it in your EA.Tia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#40](/thread/post/2635456#post2635456 "Post Permalink")

  * Mar 29, 2009 8:40pm  Mar 29, 2009 8:40pm 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

> [Quoting pitpiter](/thread/post/2635439#post2635439 "View Quoted Post")
> 
> Disliked
> 
> Try this one. It open trade after bar on which indi generate signal close.  
>  Good luck  
>  Peter
> 
> Ignored

I got this error trying to back test the EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#41](/thread/post/2635458#post2635458 "Post Permalink")

  * Mar 29, 2009 8:41pm  Mar 29, 2009 8:41pm 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

> [Quoting lyllia](/thread/post/2635448#post2635448 "View Quoted Post")
> 
> Disliked
> 
> I am not a programmer.Does this EA will close all the postions opened in one time frame? like the one in Ejpy 4 hr chart as per my last post befor this one. For an example I only want to use 4hr time frame . How could I adjust it in your EA.Tia
> 
> Ignored

just attach the EA the the TF u want. If u need to trade on 4H TF, just attached the EA to the 4H TF. The EA will follow the TF on your chart. The EA also identify the trade using magic number. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#42](/thread/post/2635459#post2635459 "Post Permalink")

  * Edited 10:34pm  Mar 29, 2009 8:43pm | Edited 10:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83209_5.gif) pitpiter](pitpiter)

  * | Joined Oct 2008  | Status: Trader | [300 Posts](/search?do=process&provider=Member&searchuser=83209)

> [Quoting forexisfx](/thread/post/2635456#post2635456 "View Quoted Post")
> 
> Disliked
> 
> I got this error trying to back test the EA.
> 
> Ignored

sorry , I make mistake in name indi , here is good  
look post 62 for correct version 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [lyliaEA.mq4](/attachment/file/225338?d=1238327008) 3 KB | 788 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#43](/thread/post/2635465#post2635465 "Post Permalink")

  * Mar 29, 2009 8:47pm  Mar 29, 2009 8:47pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

It is 4 hr euro chart.there are 6 sell arrows and 4 buy arrows.  
  
the first two sell arrows have been closed by first buy arrow;  
  
the first buy arrow has been closed by the third sell arrow;  
  
the third sell arrow has been closed by second buy arrow;  
  
the second buy arrow has been closed by fourth sell arrow;  
  
the fourth sell arrow has been closed by third buy arrow;  
  
the third buy arrow has been closed by fifth sell arrow;   
  
the fifth sell arrow has been closed by the fourth buy arrow;  
  
the fourth buy arrow has been closed bu the sixth sell arrow;  
  
the sixth sell arrow has not been closed yet;  
  
no failed trade. Have a good look yourself. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#44](/thread/post/2635467#post2635467 "Post Permalink")

  * Mar 29, 2009 8:48pm  Mar 29, 2009 8:48pm 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

> [Quoting pitpiter](/thread/post/2635459#post2635459 "View Quoted Post")
> 
> Disliked
> 
> sorry , I make mistake in name indi , here is good
> 
> Ignored

got this error now  
  
"TestGenerator: unmatched data error (low value 1.2793 at 2009.03.11 20:00 is not reached from the least timeframe, low price 1.2803 mismatches)  
"  
  
"TestGenerator: unmatched data error (volume limit 3860 at 2009.03.12 04:00 exceeded)" 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#45](/thread/post/2635470#post2635470 "Post Permalink")

  * Mar 29, 2009 8:53pm  Mar 29, 2009 8:53pm 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

> [Quoting lyllia](/thread/post/2635465#post2635465 "View Quoted Post")
> 
> Disliked
> 
> It is 4 hr euro chart.there are 6 sell arrows and 4 buy arrows.  
>    
>  the first two sell arrows have been closed by first buy arrow;  
>    
>  the first buy arrow has been closed by the third sell arrow;  
>    
>  the third sell arrow has been closed by second buy arrow;  
>    
>  the second buy arrow has been closed by fourth sell arrow;  
>    
>  the fourth sell arrow has been closed by third buy arrow;  
>    
>  the third buy arrow has been closed by fifth sell arrow;   
>    
>  the fifth sell arrow has been closed by the fourth buy arrow;  
>    
>  the fourth buy arrow has been closed bu the sixth sell...
> 
> Ignored

each broker has different 4H candle so their value is different. Yours might have arrow but mine doesnt.  
  
Can u post a screen shot of the trades u saw ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#46](/thread/post/2635471#post2635471 "Post Permalink")

  * Mar 29, 2009 8:53pm  Mar 29, 2009 8:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83209_5.gif) pitpiter](pitpiter)

  * | Joined Oct 2008  | Status: Trader | [300 Posts](/search?do=process&provider=Member&searchuser=83209)

> [Quoting forexisfx](/thread/post/2635467#post2635467 "View Quoted Post")
> 
> Disliked
> 
> got this error now  
>    
>  "TestGenerator: unmatched data error (low value 1.2793 at 2009.03.11 20:00 is not reached from the least timeframe, low price 1.2803 mismatches)  
>  "  
>    
>  "TestGenerator: unmatched data error (volume limit 3860 at 2009.03.12 04:00 exceeded)"
> 
> Ignored

I think it generate from indi , 12 of march is a day when was big move on all pair USD 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#47](/thread/post/2635473#post2635473 "Post Permalink")

  * Mar 29, 2009 8:57pm  Mar 29, 2009 8:57pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

The worst trade in this group I think is the fifth sell arrow closed by fourth buy arrow.Maybe you could get 50 pips. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#48](/thread/post/2635474#post2635474 "Post Permalink")

  * Mar 29, 2009 8:57pm  Mar 29, 2009 8:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83209_5.gif) pitpiter](pitpiter)

  * | Joined Oct 2008  | Status: Trader | [300 Posts](/search?do=process&provider=Member&searchuser=83209)

2009.03.29 13:48:35 2009.02.04 16:30 lyliaEA: the comment parameter for OrderSend function must be a string  
Is sombody have this comment?  
Because I can't udersand it I make sendfunc like:  
nt=OrderSend(Symbol(),OP_SELL,lots,Bid,slip,0,0,mn,0,Red);  
where Symbol() return string value 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#49](/thread/post/2635478#post2635478 "Post Permalink")

  * Mar 29, 2009 9:03pm  Mar 29, 2009 9:03pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

here it is 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: euro 4hr.gif
Size: 23 KB](/attachment/image/225346/thumbnail?d=1365566474)](/attachment/image/225346?d=1238328227)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#50](/thread/post/2635480#post2635480 "Post Permalink")

  * Mar 29, 2009 9:06pm  Mar 29, 2009 9:06pm 

  * [ Trader7](trader7)

  * | Joined Jul 2006  | Status: Trader | [223 Posts](/search?do=process&provider=Member&searchuser=14097)

> [Quoting lyllia](/thread/post/2635446#post2635446 "View Quoted Post")
> 
> Disliked
> 
> Thanks for your help! I will try it and post result.
> 
> Ignored

Hi there lyllia,  
  
G'day mate!  
  
Wow.........At the rate at which you are posting charts......it is truly amazing. I have been following all that you have been posting and it is leaving me breathless. Keep up the good work. It is truly impressive.![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
If the indicators do not repaint you have in your possession a great pip making machine. An Ace! What we need now is a good dependable EA.  
  
May the PIPS be with you.  
  
Trader7 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#51](/thread/post/2635482#post2635482 "Post Permalink")

  * Mar 29, 2009 9:12pm  Mar 29, 2009 9:12pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

you have to make this EA workable.I will test it starting tommorrow.Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#52](/thread/post/2635484#post2635484 "Post Permalink")

  * Mar 29, 2009 9:17pm  Mar 29, 2009 9:17pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

May pips with all traders.Hope traders get good luck starting from today.Hope everybody contribute to a good reliable free EA.May God bless trader. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#53](/thread/post/2635498#post2635498 "Post Permalink")

  * Mar 29, 2009 9:37pm  Mar 29, 2009 9:37pm 

  * [ rob24hrs](rob24hrs)

  * | Joined Feb 2009  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=94928)

BeginnerAlert.ex4  
  
What does this actually do?  
  
On lower timeframe ie m1 m5 it gives a more consistant indication it would appear than arrows.........  
  
rgds  
  
Rob 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#54](/thread/post/2635501#post2635501 "Post Permalink")

  * Mar 29, 2009 9:39pm  Mar 29, 2009 9:39pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

you have to download all the indicators I posted to your metetrader.then apply the template_fx. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#55](/thread/post/2635503#post2635503 "Post Permalink")

  * Mar 29, 2009 9:39pm  Mar 29, 2009 9:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar28647_2.gif) availdollars](availdollars)

  * | Joined Dec 2006  | Status: Trader | [190 Posts](/search?do=process&provider=Member&searchuser=28647)

> [Quoting lyllia](/thread/post/2635484#post2635484 "View Quoted Post")
> 
> Disliked
> 
> May pips with all traders.Hope traders get good luck starting from today.Hope everybody contribute to a good reliable free EA.May God bless trader.
> 
> Ignored

good go 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#56](/thread/post/2635505#post2635505 "Post Permalink")

  * Mar 29, 2009 9:44pm  Mar 29, 2009 9:44pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

beginner alert is a kind of indicator like fractal.It is very helpful to predict the the potential R & S. If you go through all the time frame of the chart and see the indicator there ,which means the trend might change and IINWMARROWS.mq4 often comes out where the begining alert is. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#57](/thread/post/2635506#post2635506 "Post Permalink")

  * Mar 29, 2009 9:46pm  Mar 29, 2009 9:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar91811_2.gif) tafadzwa02](tafadzwa02)

  * | Commercial User  | Joined Jan 2009 | [1,490 Posts](/search?do=process&provider=Member&searchuser=91811)

Am a fan of bill williams theory but havge just come across your system and it loks like it works on a ranging market , or does it? i jus wanna know something about these arrows .At what stage do they appear beggining of a candlestick or at the close of it , coz in a live trading situation , that means a lot.Do they disappear once they appear or once they are there they will remain? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#58](/thread/post/2635510#post2635510 "Post Permalink")

  * Mar 29, 2009 9:49pm  Mar 29, 2009 9:49pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Download all the indicators I posted to your platform 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#59](/thread/post/2635511#post2635511 "Post Permalink")

  * Mar 29, 2009 9:53pm  Mar 29, 2009 9:53pm 

  * [ Mandl2007](mandl2007)

  * | Membership Revoked  | Joined Nov 2008 | [279 Posts](/search?do=process&provider=Member&searchuser=86165)

I did it ! No more problems here - it works good now ! Thanks for sharing your system !!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#60](/thread/post/2635514#post2635514 "Post Permalink")

  * Mar 29, 2009 9:58pm  Mar 29, 2009 9:58pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

No it works in all markets. you could apply the arrow to your chart and have a study on it. It is a very reliable and stable indicator.Once come out it will stay there .Seldom change the the place.So that's the main reason I recoomend it here. I have observed many arrow indicators.This one is the best like I said. I could not say it is a 100 % stable.But so far I only come cross once it moved the place, only a few pips away from where it originally appeared on 4hr's chart.Not a big deal.Like I said if there are two or more sell or buy arrows appeared the opsite arrow will close them all. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#61](/thread/post/2635525#post2635525 "Post Permalink")

  * Mar 29, 2009 10:08pm  Mar 29, 2009 10:08pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

on your chart, there is 5 sell arrows and three buy arrows.  
  
The first sell closed by first buy;  
  
The first buy closed by second sell;  
  
the second sell closed by second buy;  
  
the second buy closed by third sell;  
  
the third and fourth sell cloosed by third buy;  
  
the third buy closed by fifth sell;  
  
the fifth sell has not been closed, waiting to be closed on monday. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#62](/thread/post/2635535#post2635535 "Post Permalink")

  * Mar 29, 2009 10:18pm  Mar 29, 2009 10:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83209_5.gif) pitpiter](pitpiter)

  * | Joined Oct 2008  | Status: Trader | [300 Posts](/search?do=process&provider=Member&searchuser=83209)

I find bug , here is workable version 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [lyliaEA.mq4](/attachment/file/225363?d=1238332687) 3 KB | 1,749 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#63](/thread/post/2635545#post2635545 "Post Permalink")

  * Mar 29, 2009 10:41pm  Mar 29, 2009 10:41pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Thanks again. post result tomorrow. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#64](/thread/post/2635587#post2635587 "Post Permalink")

  * Mar 29, 2009 11:47pm  Mar 29, 2009 11:47pm 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

> [Quoting lyllia](/thread/post/2635514#post2635514 "View Quoted Post")
> 
> Disliked
> 
> No it works in all markets. you could apply the arrow to your chart and have a study on it. It is a very reliable and stable indicator.Once come out it will stay there .Seldom change the the place.So that's the main reason I recoomend it here. I have observed many arrow indicators.This one is the best like I said. I could not say it is a 100 % stable.But so far I...
> 
> Ignored

How long u have been watching the arrow ? 1 month ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#65](/thread/post/2635591#post2635591 "Post Permalink")

  * Mar 29, 2009 11:51pm  Mar 29, 2009 11:51pm 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

> [Quoting lyllia](/thread/post/2635514#post2635514 "View Quoted Post")
> 
> Disliked
> 
> Like I said if there are two or more sell or buy arrows appeared the opsite arrow will close them all.
> 
> Ignored

I don't understand this point. Can u give an example with opening and closing of positions. Thnx. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#66](/thread/post/2635596#post2635596 "Post Permalink")

  * Mar 29, 2009 11:58pm  Mar 29, 2009 11:58pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

have a look at the chart you posted in this thread.Then follow my account of your chart, you will see the point. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#67](/thread/post/2635599#post2635599 "Post Permalink")

  * Mar 30, 2009 12:01am  Mar 30, 2009 12:01am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

first sell means first sell arrow.first buy means first buy arrow. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#68](/thread/post/2635603#post2635603 "Post Permalink")

  * Mar 30, 2009 12:03am  Mar 30, 2009 12:03am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

as soon as an arrow appears the position is opened. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#69](/thread/post/2635604#post2635604 "Post Permalink")

  * Mar 30, 2009 12:04am  Mar 30, 2009 12:04am 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

> [Quoting lyllia](/thread/post/2635599#post2635599 "View Quoted Post")
> 
> Disliked
> 
> first sell means first sell arrow.first buy means first buy arrow.
> 
> Ignored

Can u give example ? I am trying to understand how trade is open and close. Please give example, its hard to imagine when I dont understand. Thnx 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#70](/thread/post/2635614#post2635614 "Post Permalink")

  * Mar 30, 2009 12:12am  Mar 30, 2009 12:12am 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

the arrow repaints so if anyone wanna show any chart should run it in strategy tester first so that the arrow will stay there. If u show a normal chart, it will only show after repaint. I can see a different of 2 or more addition of arrow compare to a normal 4H chart. I guess what lyllia shown us is not very accurate. After running the tester, I manual trade 2 weeks data and the result is very bad. Base on my understanding, current position will be close once there is opposite signal and I manual trade that way. The 2 weeks i choose is ranging market. The reason i dont choose trending market to manual back test is becoz anything goes when it's trending and right now market tend to range more than trend. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#71](/thread/post/2635618#post2635618 "Post Permalink")

  * Mar 30, 2009 12:17am  Mar 30, 2009 12:17am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

take your chart as ab example: as soon as the first sell arrow appears the sell position is opened.When the first buy arrow appears the sell position has been closed, at the same time a buy position is opened. Do I make myself clear? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#72](/thread/post/2635623#post2635623 "Post Permalink")

  * Mar 30, 2009 12:21am  Mar 30, 2009 12:21am 

  * [ Mandl2007](mandl2007)

  * | Membership Revoked  | Joined Nov 2008 | [279 Posts](/search?do=process&provider=Member&searchuser=86165)

ok let's wait the monday - since monday we can try this system in forward test ! This will be the only proof !![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#73](/thread/post/2635627#post2635627 "Post Permalink")

  * Mar 30, 2009 12:24am  Mar 30, 2009 12:24am 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

> [Quoting Mandl2007](/thread/post/2635623#post2635623 "View Quoted Post")
> 
> Disliked
> 
> ok let's wait the monday - since monday we can try this system in forward test ! This will be the only proof !![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

U cannot test only 1 day unless u trade 1H TF which gives even worst results. If u gonna trade 4H TF, u need at least a month to tell. On 4H TF, 1 day only have 6 candle. U cannot tell anything with 6 candle. The arrow doesn't repaint 100%, so u have to wait for at least a month to tell how much it will repaint. I hope I'm wrong and the strategy tester is wrong becoz I wanna make money too. Let's see how it goes for the coming weeks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#74](/thread/post/2635628#post2635628 "Post Permalink")

  * Mar 30, 2009 12:25am  Mar 30, 2009 12:25am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I hope tommorrow you test real 4hr chart and then you will see the result.What do you mean repaint? you mean sell arrow paint one after another? I do not think there will be problem with that.that only means more potions would be opened.Then they will be all closed by the oppsite signal . 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#75](/thread/post/2635632#post2635632 "Post Permalink")

  * Mar 30, 2009 12:27am  Mar 30, 2009 12:27am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Two weekly arrow data all appear on real time chart.you can see it yourself. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#76](/thread/post/2635641#post2635641 "Post Permalink")

  * Mar 30, 2009 12:37am  Mar 30, 2009 12:37am 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

This is a normal chart u see [repainted] 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: repaint.jpg
Size: 63 KB](/attachment/image/225397/thumbnail?d=1365566474)](/attachment/image/225397?d=1238341040)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#77](/thread/post/2635644#post2635644 "Post Permalink")

  * Mar 30, 2009 12:38am  Mar 30, 2009 12:38am 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

This is the chart after running the strategy tester [no repaint]  
  
Everything shown is 4H chart. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: no_repaint.jpg
Size: 61 KB](/attachment/image/225398/thumbnail?d=1365566474)](/attachment/image/225398?d=1238341094)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#78](/thread/post/2635645#post2635645 "Post Permalink")

  * Mar 30, 2009 12:41am  Mar 30, 2009 12:41am 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

> [Quoting lyllia](/thread/post/2635632#post2635632 "View Quoted Post")
> 
> Disliked
> 
> Two weekly arrow data all appear on real time chart.you can see it yourself.
> 
> Ignored

Like i said before, the arrow doesnt repaint 100%, if u wanna show weekly chart, u got to see for at least a year of data. 1 month only have 4 candles... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#79](/thread/post/2635648#post2635648 "Post Permalink")

  * Mar 30, 2009 12:42am  Mar 30, 2009 12:42am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

what chart you applied to ? euro? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#80](/thread/post/2635650#post2635650 "Post Permalink")

  * Mar 30, 2009 12:43am  Mar 30, 2009 12:43am 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

> [Quoting lyllia](/thread/post/2635648#post2635648 "View Quoted Post")
> 
> Disliked
> 
> what chart you applied to ? euro?
> 
> Ignored

sorry i didnt mention. yeah u are right. EURUSD. The 1H chart it's even worst. The lower the TF, the more repaint occur becoz there is more candles. For those who doesnt believe it, Monday, use the indicator on 1 min chart and see for yourself how it repaint and how stable it is.  
  
I don't understand how u got 95% + successful rate. How long u have been trading this system and how many trades u have trigger so far ? Can u show us some trade statement ?   
  
Thnx 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#81](/thread/post/2635664#post2635664 "Post Permalink")

  * Mar 30, 2009 12:53am  Mar 30, 2009 12:53am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

did yiu see on your chart all the arrows closed each other? They do repaint but they could manage to close all the positions 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: gjpy 4hr.gif
Size: 13 KB](/attachment/image/225400/thumbnail?d=1365566474)](/attachment/image/225400?d=1238342018)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#82](/thread/post/2635667#post2635667 "Post Permalink")

  * Mar 30, 2009 12:58am  Mar 30, 2009 12:58am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I did mentioned in my previous post I apply it to larger time frame : prefer one hr ++.You wil get good result on 4 hr ,daily chart. Why we have to bother small time frame if we could make money on big time frame and more safer? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#83](/thread/post/2635670#post2635670 "Post Permalink")

  * Mar 30, 2009 12:59am  Mar 30, 2009 12:59am 

  * [ artov](artov)

  * | Joined Sep 2008  | Status: Trader | [567 Posts](/search?do=process&provider=Member&searchuser=79619)

To say it has a 95% success rate is in my opinion very vague.  
  
What do you define as success?   
  
Does it hit target profit 95% of the times you have a SL 10 and TP 10 setting?  
  
Does it hit target profit 95% of the times you have SL 80 and TP 10 setting?  
  
And in addition to the money management, when (open bar, close bar, appearing of arrow) do you enter the trade to achieve this 95% success rate.  
  
Please clarify, thanks in advance. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#84](/thread/post/2635676#post2635676 "Post Permalink")

  * Mar 30, 2009 1:03am  Mar 30, 2009 1:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar84807_4.gif) todd960960](todd960960)

  * | Joined Nov 2008  | Status: Trader | [470 Posts](/search?do=process&provider=Member&searchuser=84807)

lyllia when it 'repaints', your arrows are changing positions and disappearing in live time. Do you understand this?  
  
thx,  
todd 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#85](/thread/post/2635687#post2635687 "Post Permalink")

  * Mar 30, 2009 1:12am  Mar 30, 2009 1:12am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I observed this indicator for almost 5 months. It seldom repaint. I do not know why your guys test it, it repaint with such a high frequency? I hope you observ the indicator in real trading session ,then you test it in real time and get real test result.  
  
95 % success rate refer to one hr ++ TF. I hope you could get result afteryou test it for one week. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#86](/thread/post/2635690#post2635690 "Post Permalink")

  * Mar 30, 2009 1:16am  Mar 30, 2009 1:16am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

on larger time frame this method could close up to 95 % of the postions opened. For this method no stop/loss no trailing stop. Do I make myself clear? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#87](/thread/post/2635692#post2635692 "Post Permalink")

  * Mar 30, 2009 1:20am  Mar 30, 2009 1:20am 

  * [ artov](artov)

  * | Joined Sep 2008  | Status: Trader | [567 Posts](/search?do=process&provider=Member&searchuser=79619)

> [Quoting lyllia](/thread/post/2635690#post2635690 "View Quoted Post")
> 
> Disliked
> 
> on larger time frame this method could close up to 95 % of the postions opened. For this method no stop/loss no trailing stop. Do I make myself clear?
> 
> Ignored

If I understand you correctly, the EA can close 95% of the trades on a larger time frame. I know that 99,9% of the EA's are capable of closing 100% of the trades no matter what timeframe it's being run on.  
  
Yes it sounds crazy but that's what I understand from your explaination. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#88](/thread/post/2635694#post2635694 "Post Permalink")

  * Mar 30, 2009 1:24am  Mar 30, 2009 1:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar91811_2.gif) tafadzwa02](tafadzwa02)

  * | Commercial User  | Joined Jan 2009 | [1,490 Posts](/search?do=process&provider=Member&searchuser=91811)

Guys , i will be testing this system tmorow first thing and see what happens , if it works it should at least work on an hr time frame , saying it only works on 4hr or daily or weekly is a bit dodgy for me , i wil se, i am lookin for a system that works when the market is ranging and this one works , i will use it , if it doesnt , i wil continue using bill williams chaos theory which has made me money so far.I~ guess its worth a try and if it doesnt , we shouldnt stop looking for systems that work in choppy markets like whats hapening these days .I will definitely give it a go , on an HR tiem farme though , Sorry lly but if it doesnt work on HR i dont see it working on 4hr . 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#89](/thread/post/2635721#post2635721 "Post Permalink")

  * Mar 30, 2009 1:47am  Mar 30, 2009 1:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar96656_4.gif) $aly]($aly)

  * | Commercial User  | Joined Mar 2009 | [183 Posts](/search?do=process&provider=Member&searchuser=96656)

the only way to find out whereas indicator repaint or not is testing in 1min chart...i think this is a repaint indicator and dosen't make money..**i yllia repaint means changing position no repeat arrows.........**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#90](/thread/post/2635759#post2635759 "Post Permalink")

  * Mar 30, 2009 2:35am  Mar 30, 2009 2:35am 

  * [ preawansyah](preawansyah)

  * | Additional Username  | Joined Jan 2009 | [17 Posts](/search?do=process&provider=Member&searchuser=90826)

I think if this system can work as prescribed throughout the threads, all of us will be rich.:-), yet, let's see what happens next week. Thanks for your hard work creating this system. I will have a try. Cheers 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#91](/thread/post/2635801#post2635801 "Post Permalink")

  * Mar 30, 2009 3:25am  Mar 30, 2009 3:25am 

  * [ preawansyah](preawansyah)

  * | Additional Username  | Joined Jan 2009 | [17 Posts](/search?do=process&provider=Member&searchuser=90826)

Hi Lillya,  
  
I am a newbie. I just would like to clarify. Is this system an autoamtically-generated buy/sell order? Or Do we have to do it manually? I am not so clear when U said for example that once the first Buy arrow appears and the next sell arrow comes up will close the previous (first) buy order and so on. Please clarify it...!  
  
Of course, I will test it in a demo account first before going live.  
  
Thanks for your great work.  
  
Prea 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#92](/thread/post/2635927#post2635927 "Post Permalink")

  * Mar 30, 2009 5:46am  Mar 30, 2009 5:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar48267_23.gif) Oksana17](oksana17)

  * | Membership Revoked  | Joined Sep 2007 | [903 Posts](/search?do=process&provider=Member&searchuser=48267)

I see that someone made an EA while I was sleeping! No worries. 

Request custom Expert Advisor or Indicator: dostapyuk "at" gmail . com

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#93](/thread/post/2635956#post2635956 "Post Permalink")

  * Mar 30, 2009 6:10am  Mar 30, 2009 6:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar96656_4.gif) $aly]($aly)

  * | Commercial User  | Joined Mar 2009 | [183 Posts](/search?do=process&provider=Member&searchuser=96656)

> [Quoting Oksana17](/thread/post/2635927#post2635927 "View Quoted Post")
> 
> Disliked
> 
> I see that someone made an EA while I was sleeping! No worries.
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1) U R a big programmer 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#94](/thread/post/2636210#post2636210 "Post Permalink")

  * Mar 30, 2009 8:55am  Mar 30, 2009 8:55am 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

> [Quoting lyllia](/thread/post/2635687#post2635687 "View Quoted Post")
> 
> Disliked
> 
> I observed this indicator for almost 5 months. It seldom repaint. I do not know why your guys test it, it repaint with such a high frequency? I hope you observ the indicator in real trading session ,then you test it in real time and get real test result.  
>    
>  95 % success rate refer to one hr ++ TF. I hope you could get result afteryou test it for one week.
> 
> Ignored

i really hope what u claim is true. If u have been trading for 5 months, i am u have some trade statement to proof u have 95% success rate ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#95](/thread/post/2636340#post2636340 "Post Permalink")

  * Mar 30, 2009 10:22am  Mar 30, 2009 10:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar48267_23.gif) Oksana17](oksana17)

  * | Membership Revoked  | Joined Sep 2007 | [903 Posts](/search?do=process&provider=Member&searchuser=48267)

> [Quoting $aly](/thread/post/2635956#post2635956 "View Quoted Post")
> 
> Disliked
> 
> ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1) U R a big programmer
> 
> Ignored

not sure i'm getting the sense of laughter. 

Request custom Expert Advisor or Indicator: dostapyuk "at" gmail . com

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#96](/thread/post/2636420#post2636420 "Post Permalink")

  * Mar 30, 2009 11:22am  Mar 30, 2009 11:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar48267_23.gif) Oksana17](oksana17)

  * | Membership Revoked  | Joined Sep 2007 | [903 Posts](/search?do=process&provider=Member&searchuser=48267)

Did anyone get luck in backtesting? 

Request custom Expert Advisor or Indicator: dostapyuk "at" gmail . com

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#97](/thread/post/2636461#post2636461 "Post Permalink")

  * Mar 30, 2009 11:49am  Mar 30, 2009 11:49am 

  * [ Trader7](trader7)

  * | Joined Jul 2006  | Status: Trader | [223 Posts](/search?do=process&provider=Member&searchuser=14097)

> [Quoting lyllia](/thread/post/2635687#post2635687 "View Quoted Post")
> 
> Disliked
> 
> I observed this indicator for almost 5 months. It seldom repaint. I do not know why your guys test it, it repaint with such a high frequency? I hope you observ the indicator in real trading session ,then you test it in real time and get real test result.  
>    
>  95 % success rate refer to one hr ++ TF. I hope you could get result afteryou test it for one week.
> 
> Ignored

Hi there lyllia,  
  
I have been keeping a detailed record of the indicators used by you in your charts for the last 1 hour on the GBPJPY M1 chart where price moves like a wild horse.  
  
I have good news and some bad news. Let us first get the bad news out of the way.  
  
The ABHA Center Timing Signal repaints big time. A Green bar appeared at 00:45 (GMT) and then disappeared at 00:47. Another appeared at 00:47 and then disappeared at 00:52. The same thing happened to the Red bar at 01:07 when it disappeared at 01:10.  
  
This repainting makes the indicator unreliable for trading purposes in real time. Imagine trying to score a goal with moving goalposts! Even if you bend it like Beckham!![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
The Shi Channel repaints as it keeps adjusting to the price range. To be dynamic this is part of its feature.   
  
Now for the good news lyllia. I have kept a detailed record of the arrows as soon as they appeared. I am happy to report that once the Big Blue and White arrows appeared they did not disappear. So there is no problem of repainting when trading in real time.  
  
The Big Blue and White arrows appear at the close of the bar.  
  
The Small Blue and Red arrows appear after the open of the bar. So during the course of the bar the arrows can disappear as price changes. But once the bar closes the arrows do not disappear.   
  
For trading purposes the arrows are reliable. Keep up the good work and success will be yours.![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
Trader7 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#98](/thread/post/2636707#post2636707 "Post Permalink")

  * Mar 30, 2009 2:18pm  Mar 30, 2009 2:18pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Thanks!This is what I said in my previous begining post the arrow are more reliable than other indicators which are included into this system for instructive purpose. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#99](/thread/post/2636763#post2636763 "Post Permalink")

  * Mar 30, 2009 2:49pm  Mar 30, 2009 2:49pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Hi Peter,How are you   
  
I report bad news first about EA Trading:  
  
4hr ACHF sell arrow appeared at 0.789 but sell position opened at 0.7829;  
  
4hr EJPY sell arrow appeared at 129.94 but position opened at 128.5;  
  
4hr CHFJPY there is no sell or buy singal (arrow) with my normal trading account in asian session.But there are buy and sell signals with demo trading account. buy position opened but sell position not opened. so the buy position could not be closed. so far 100 pips down.  
  
4hr NJPY there is no buy signal in asian time but a buy position has been opened.There is a sell signal in asian time but no sell position opened. so far  
so far 110 pips down.  
  
  
There are buy signals on 4hr AUD,Euro ,GBP Chart buy position opened but sell position did not close them .no sell positions opened.  
  
Good news:  
  
1hr GJPY 200 pips so far, ECAD 50pips, nzd55pips, CADCHF50 pips. EjPY25pips  
ACHF6 pips.ANZD-6 pips;ACAD-50 pips  
  
portfolio balance:$ 34.61 so far 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#100](/thread/post/2636768#post2636768 "Post Permalink")

  * Mar 30, 2009 2:51pm  Mar 30, 2009 2:51pm 

  * [ Mandl2007](mandl2007)

  * | Membership Revoked  | Joined Nov 2008 | [279 Posts](/search?do=process&provider=Member&searchuser=86165)

@trader7: quite interesting to read that ! So does that even mean - the arrows can be used for smaller TF's ? May be not for 1M - but 5M or 15M ? Or what can you say about the results of your attempts ?  
  
The EA isn't optimal so far ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#101](/thread/post/2636782#post2636782 "Post Permalink")

  * Mar 30, 2009 3:00pm  Mar 30, 2009 3:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar87885_5.gif) hemantaims](hemantaims)

  * | Joined Dec 2008  | Status: Trader | [35 Posts](/search?do=process&provider=Member&searchuser=87885)

Hey guys i have just backtested lyliaEA Posted on post no 62. Results are no so promising. date of backtesting is from 1-1-2007 to 30-3-1009.just have a look.   
  
May be some modification is required in EA.![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: StrategyTester h1 report.gif
Size: 10 KB](/attachment/image/225638/thumbnail?d=1365566525)](/attachment/image/225638?d=1238392688)   
[![Click to Enlarge

Name: StrategyTester h4.gif
Size: 10 KB](/attachment/image/225639/thumbnail?d=1365566525)](/attachment/image/225639?d=1238392688)   
[![Click to Enlarge

Name: StrategyTester d1.gif
Size: 9 KB](/attachment/image/225640/thumbnail?d=1365566525)](/attachment/image/225640?d=1238392736)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#102](/thread/post/2636791#post2636791 "Post Permalink")

  * Mar 30, 2009 3:05pm  Mar 30, 2009 3:05pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

could you find reason why position opened so far from the time an arrow appears? could you make it open the position as soon as possible?It is critical.  
  
I leave all the positions to be closed by themselves.Then we can get real result.Because this method based on selfullfilled theory. If they could not make money then we have to throw it away.  
  
I am considering to put stop/loss rules into the EA:  
1)as soon as the position enter into the positive area the stop/loss will be  
equal to entry  
2)trailing stop will be 10 step forward.   
  
Could you do it? Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#103](/thread/post/2636800#post2636800 "Post Permalink")

  * Mar 30, 2009 3:12pm  Mar 30, 2009 3:12pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Anybody made pips using the arrow? please tell us here:  
  
What time frame do you think trading it the best?  
  
how do you manage the stop/loss and increase risk/ reward rotios? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#104](/thread/post/2636815#post2636815 "Post Permalink")

  * Mar 30, 2009 3:20pm  Mar 30, 2009 3:20pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Today the Potential S & R for the pairs:  
  
AUSD 0.7134-0.6778  
NZD 0.5856-0.5578  
EURO 1.3687-1.2992  
GBP 1.4676-1.4018  
JPY 100.35-95.9  
CHF 1.1565-1.1247  
CAD 1.2589-1.2187 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#105](/thread/post/2636854#post2636854 "Post Permalink")

  * Mar 30, 2009 3:47pm  Mar 30, 2009 3:47pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Hi Mate,  
  
why you laugh? Could you help to what happened to the EA trading since you are a programmer as well? Please read what I post about EA trading.You peomised to help yesterday.tia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#106](/thread/post/2636865#post2636865 "Post Permalink")

  * Mar 30, 2009 3:52pm  Mar 30, 2009 3:52pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

hi you have a strange name.  
  
I am not a programmar. I just have an idea about a system EA and let people help to make it. People really help here and hope we could further improve it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#107](/thread/post/2636880#post2636880 "Post Permalink")

  * Edited 4:14pm  Mar 30, 2009 4:01pm | Edited 4:14pm 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

> [Quoting lyllia](/thread/post/2636800#post2636800 "View Quoted Post")
> 
> Disliked
> 
> Anybody made pips using the arrow? please tell us here:  
>    
>  What time frame do you think trading it the best?  
>    
>  how do you manage the stop/loss and increase risk/ reward rotios?
> 
> Ignored

i think u ask the question too early. IMO, 4H would work better.  
  
SL is a must. Like i said before, strong reverse kills you. If any sudden news came out and went 400 pips reverse [quite possible nowadays], it's gonna get ugly.  
  
I think a reasonable SL for EURUSD could be 100 pips SL. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#108](/thread/post/2636891#post2636891 "Post Permalink")

  * Mar 30, 2009 4:12pm  Mar 30, 2009 4:12pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Since we just start to make it work.I hope people who using the arrow for trading please give us your insight about how to improve it. Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#109](/thread/post/2637073#post2637073 "Post Permalink")

  * Mar 30, 2009 5:29pm  Mar 30, 2009 5:29pm 

  * [ victusa](victusa)

  * | Joined Mar 2008  | Status: Mr | [12 Posts](/search?do=process&provider=Member&searchuser=65342)

To Lyllia,  
Your system looks okay but the issue of working with 4H TF is not encouraging at all. I have been using the EA all night and discovered that the EA is actually working according to your description. But my experience in FX taught me that any system that descriminates against TFs is not a good system. A good system should work with any time frame. I started using Peter Crowns DIBS awhile ago and I found out that the Daily Inside Bar is 90% accurate.  
  
Please can you modify this system more so that it can trade on all TFs  
  
Victus 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#110](/thread/post/2637115#post2637115 "Post Permalink")

  * Mar 30, 2009 5:48pm  Mar 30, 2009 5:48pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Thanks! I will have a look at it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#111](/thread/post/2637268#post2637268 "Post Permalink")

  * Edited 9:21pm  Mar 30, 2009 7:11pm | Edited 9:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83209_5.gif) pitpiter](pitpiter)

  * | Joined Oct 2008  | Status: Trader | [300 Posts](/search?do=process&provider=Member&searchuser=83209)

> [Quoting lyllia](/thread/post/2636791#post2636791 "View Quoted Post")
> 
> Disliked
> 
> could you find reason why position opened so far from the time an arrow appears? could you make it open the position as soon as possible?It is critical.  
>    
>  I leave all the positions to be closed by themselves.Then we can get real result.Because this method based on selfullfilled theory. If they could not make money then we have to throw it away.  
>    
>  I am considering to put stop/loss rules into the EA:  
>  1)as soon as the position enter into the positive area the stop/loss will...
> 
> Ignored

Hi there.  
I can't ansver your question , because I do not know which broker You use . Give me information about your broker and correctly pair and time (brokers time) when indi give signal and EA did not open trade or opened with another price , in this case I can make some analize .  
I do not know , I will have time to make some change in EA before weekend . But You can wright clear rule which You want have in EA and somebody add it to EA , or I will do it if find time. My sugestion - think about filtering bad signal , IINWMARROWS based on crossing two LWMA and I think it not enaph for clear signal. And second thing - 10 pips trailing on 1H or 4H is too tight as for me , especialy with current market.  
Regards  
Peter 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#112](/thread/post/2639008#post2639008 "Post Permalink")

  * Mar 31, 2009 8:20am  Mar 31, 2009 8:20am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Hi Peter,  
  
EA works well on Most positions:  
  
ECAD 180 pips so far. The position opened as soon as the arrow appeared;  
  
Acad 10 pips.It did not get good luck.The arrow seems positioned itself at 12.30pm but it might appear 2 hrs later because the arrow signal requires the breakout of the previous bar to appear ,plus the spread too wide, the position opened at 16.00pm.so it opened the position 100 pip above.I manually closed it for risk/reward reason.This also might be the reason why some positions are opened too late.  
  
CADCHF good 100 pips ; GCHF 20 pips;GBP 40 pips so far.  
  
. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#113](/thread/post/2639027#post2639027 "Post Permalink")

  * Mar 31, 2009 8:29am  Mar 31, 2009 8:29am 

  * [ Mandl2007](mandl2007)

  * | Membership Revoked  | Joined Nov 2008 | [279 Posts](/search?do=process&provider=Member&searchuser=86165)

Anyway - it seems the EA is so far suboptimal ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#114](/thread/post/2639104#post2639104 "Post Permalink")

  * Mar 31, 2009 9:07am  Mar 31, 2009 9:07am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I feel you just standing there watching cool.Why do not make some positive suggestion or do something?Are you trading for a long time?Share your good skills with us,please.tia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#115](/thread/post/2639320#post2639320 "Post Permalink")

  * Mar 31, 2009 10:36am  Mar 31, 2009 10:36am 

  * [ Snowdogg](snowdogg)

  * | Joined Mar 2005  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=1871)

What time frame are you using? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#116](/thread/post/2639335#post2639335 "Post Permalink")

  * Mar 31, 2009 10:49am  Mar 31, 2009 10:49am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I prefer 4 hr TF it gives good pips and less stress once the PA in good direction.  
  
But for the arrow sometime if PA move too quick,it will be a long candle then it takes time to have next candle to breakout the previous one.When you get signal the price already go up or down a lot.because it is a trending still could manage to make pips, but makes you nervous.  
  
If PA basing steady then you will get good entry point.that's a perfect situation to open a position. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#117](/thread/post/2639488#post2639488 "Post Permalink")

  * Mar 31, 2009 12:20pm  Mar 31, 2009 12:20pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Hi Peter,  
  
I find reason why some position could not be opened or closed:because when I open the metatrder I forget to enable the EA .So some positions opened could not be closed and new position could not be opened.It is my mistake. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#118](/thread/post/2639501#post2639501 "Post Permalink")

  * Mar 31, 2009 12:24pm  Mar 31, 2009 12:24pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

and for testing purpose I shouldn't close down the the platform. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#119](/thread/post/2639663#post2639663 "Post Permalink")

  * Mar 31, 2009 2:19pm  Mar 31, 2009 2:19pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting pitpiter](/thread/post/2637268#post2637268 "View Quoted Post")
> 
> Disliked
> 
> Hi there.  
>  I can't ansver your question , because I do not know which broker You use . Give me information about your broker and correctly pair and time (brokers time) when indi give signal and EA did not open trade or opened with another price , in this case I can make some analize .  
>  I do not know , I will have time to make some change in EA before weekend . But You can wright clear rule which You want have in EA and somebody add it to EA , or I will do it if find time. My sugestion - think about filtering bad signal , IINWMARROWS based on crossing...
> 
> Ignored

  
Hi Peter,  
  
Are you sure is LWMA? I think is FastEMA. I do notice that sometimes if PA moves quickly that will generate a big candle and an arrow always appears when next candle breakout the previous one.That will give a high level entry signal and make me nervous. about filter I have thought about it before but give it up. I think if the arrow is reliable it is better focus on arrow trading with a good risk management .That will be enough.Since the arrow is reliable, do you think it is necessary to put s/l at entry? You are very helpful.Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#120](/thread/post/2639672#post2639672 "Post Permalink")

  * Mar 31, 2009 2:26pm  Mar 31, 2009 2:26pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lyllia](/thread/post/2639663#post2639663 "View Quoted Post")
> 
> Disliked
> 
> Hi Peter,  
>    
>  Are you sure is LWMA? I think is FastEMA. I do notice that sometimes if PA moves quickly that will generate a big candle and an arrow always appears when next candle breakout the previous one.That will give a high level entry signal and make me nervous. about filter I have thought about it before but give it up. I think if the arrow is reliable it is better focus on arrow trading with a good risk management .That will be enough.Since the arrow is reliable, do you think it is necessary to put s/l at entry? You are very helpful.Thanks!...
> 
> Ignored

What I mean is if closed the position at entry,should trend continue,then we just lost the opportunuty.Because the arrow only open the position once. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#121](/thread/post/2639908#post2639908 "Post Permalink")

  * Mar 31, 2009 4:28pm  Mar 31, 2009 4:28pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Peter,  
  
Remember if there is a news and there is big Price movement.The arrow will quickly cancel each other's position and open a new position.Am I right? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#122](/thread/post/2639938#post2639938 "Post Permalink")

  * Mar 31, 2009 4:42pm  Mar 31, 2009 4:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar96656_4.gif) $aly]($aly)

  * | Commercial User  | Joined Mar 2009 | [183 Posts](/search?do=process&provider=Member&searchuser=96656)

i test this method on 16 pairs,,,, NEVER USE THIS METHOD FOR LOWER 4H WHILE THIS IS VERY PROFITABLE FOR H4 AND HIGHER......

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#123](/thread/post/2639980#post2639980 "Post Permalink")

  * Mar 31, 2009 5:01pm  Mar 31, 2009 5:01pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting $aly](/thread/post/2639938#post2639938 "View Quoted Post")
> 
> Disliked
> 
> i test this method on 16 pairs,,,, NEVER USE THIS METHOD FOR LOWER 4H WHILE THIS IS VERY PROFITABLE FOR H4 AND HIGHER......
> 
> Ignored

Thanks $Aly, how many pips have you made so far? Could you share?  
This is a no brain trade isn't it? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#124](/thread/post/2639991#post2639991 "Post Permalink")

  * Mar 31, 2009 5:06pm  Mar 31, 2009 5:06pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Aud 0.7064-0.6592  
Nzd 0.5812-0.5450  
Cad 1.2784-1.2344  
Jpy 99.77-94.96  
Euro 1.3581-1.2842  
Gbp 1.4671-1.3841  
Chf 1.1618-1.1354 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#125](/thread/post/2640017#post2640017 "Post Permalink")

  * Mar 31, 2009 5:16pm  Mar 31, 2009 5:16pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Anybody who test this method please share your opinions here and make some recommendation to improve it.  
  
For an example, for some congestion area there is high frequency of arrows come out .On higher TF 4hr + .They could manage themselves to close each other and make profit.But for lower TF >1hr,there will be a lot of wishawp signals.that will ruin the profit.  
  
Especially those people who have good trading & EA experience please give your advice and help to improve this profitable method. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#126](/thread/post/2640039#post2640039 "Post Permalink")

  * Mar 31, 2009 5:24pm  Mar 31, 2009 5:24pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I thank the author of the IINWMARROWS on behalf of all the users who are using this method ;  
  
Also thank Pitpiter for his selfless and timely help to make EA for this indicator. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#127](/thread/post/2640049#post2640049 "Post Permalink")

  * Mar 31, 2009 5:28pm  Mar 31, 2009 5:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar7927_5.gif) BillGates](billgates)

  * | Joined Mar 2006  | Status: Rempung - Lombok Island | [135 Posts](/search?do=process&provider=Member&searchuser=7927)

> [Quoting lyllia](/thread/post/2635445#post2635445 "View Quoted Post")
> 
> Disliked
> 
> There are so many opportunities in fx trading .So only depends on manual trading is not enough.So an Ea is needed.
> 
> Ignored

To be profitable, good EA is not enough, good (manual) trading skill is required to run that good EA. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#128](/thread/post/2640054#post2640054 "Post Permalink")

  * Mar 31, 2009 5:29pm  Mar 31, 2009 5:29pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lyllia](/thread/post/2640039#post2640039 "View Quoted Post")
> 
> Disliked
> 
> I thank the author of the IINWMARROWS on behalf of all the users who are using this method ;  
>    
>  Also thank Pitpiter for his selfless and timely help to make EA for this indicator.
> 
> Ignored

Sorry spelling mistake:selfishless and timiningly help? My English is still not very good. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#129](/thread/post/2640057#post2640057 "Post Permalink")

  * Mar 31, 2009 5:29pm  Mar 31, 2009 5:29pm 

  * [ jgadefelth](jgadefelth)

  * | Joined Jan 2008  | Status: Trillion Dollar Man | [1,495 Posts](/search?do=process&provider=Member&searchuser=58861)

Saly why can i use it on 4h but not on 1h is there a speciel sort of arrows i shall follow ??   
  
what did you have as a stopploss and target ?  
  
best regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#130](/thread/post/2640067#post2640067 "Post Permalink")

  * Mar 31, 2009 5:33pm  Mar 31, 2009 5:33pm 

  * [ preawansyah](preawansyah)

  * | Additional Username  | Joined Jan 2009 | [17 Posts](/search?do=process&provider=Member&searchuser=90826)

> [Quoting lyllia](/thread/post/2640039#post2640039 "View Quoted Post")
> 
> Disliked
> 
> I thank the author of the IINWMARROWS on behalf of all the users who are using this method ;  
>    
>  Also thank Pitpiter for his selfless and timely help to make EA for this indicator.
> 
> Ignored

Lyllia..!! I put all the indicators and EA and Template that you posted in this thread into my Trading Platform but it did not execute the trades automatically. What is the problem. What trading platform (broker) is yours?   
  
Could you please show and post the result of your trading here so that we may see visually how the sytem work?  
  
Thanks much.  
Prea 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#131](/thread/post/2640080#post2640080 "Post Permalink")

  * Mar 31, 2009 5:37pm  Mar 31, 2009 5:37pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Yes,you are right. But it is not easy to master the good maual trading skills. No matter for experienced trader or beginners. If we could find a short cut to make money and at the same time to learn the skill isn't it a good way to have a better life? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#132](/thread/post/2640087#post2640087 "Post Permalink")

  * Mar 31, 2009 5:41pm  Mar 31, 2009 5:41pm 

  * [ preawansyah](preawansyah)

  * | Additional Username  | Joined Jan 2009 | [17 Posts](/search?do=process&provider=Member&searchuser=90826)

> [Quoting lyllia](/thread/post/2640080#post2640080 "View Quoted Post")
> 
> Disliked
> 
> Yes,you are right. But it is not easy to master the good maual trading skills. No matter for experienced trader or beginners. If we could find a short cut to make money and at the same time to learn the skill isn't it a good way to have a better life?
> 
> Ignored

Lyllia.. Please respond to my question at post #130. Really appreciate for your hard work and good system.  
  
Cheers  
Prea 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#133](/thread/post/2640093#post2640093 "Post Permalink")

  * Mar 31, 2009 5:45pm  Mar 31, 2009 5:45pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Are there any people come out to help those people who lost their money?  
  
Those people lost their money are crownded gambler? They are innocent aren't they?Do you know in this world there are many people call themselve street smart and screw those innecent people to lose money. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#134](/thread/post/2640099#post2640099 "Post Permalink")

  * Mar 31, 2009 5:46pm  Mar 31, 2009 5:46pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I know fx trading could never be easy.Same apply to those so called analysts,advisors etc. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#135](/thread/post/2640125#post2640125 "Post Permalink")

  * Mar 31, 2009 5:59pm  Mar 31, 2009 5:59pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting preawansyah](/thread/post/2640067#post2640067 "View Quoted Post")
> 
> Disliked
> 
> Lyllia..!! I put all the indicators and EA and Template that you posted in this thread into my Trading Platform but it did not execute the trades automatically. What is the problem. What trading platform (broker) is yours?   
>    
>  Could you please show and post the result of your trading here so that we may see visually how the sytem work?  
>    
>  Thanks much.  
>  Prea
> 
> Ignored

I couldn't understand your peoblem.It shouldn't happen if you download all the indicators to your trading platform properly,regardless which broker you use.  
Follow the following steps;  
  
1.download all the indicators into your indicator file & template into your template file:  
  
2.attach template to your chart;  
  
3.download EA to your expert file and attach it to your chart. When you attach it to your chart ,do not forget to tick the box allow Expert Adviser,and other boxes (anybody could help here give the name of other boxes and tick them all,my platform version is Chinese)  
  
4.click the icon Expert Adviser on your platform to enable EA function.  
  
Then EA should work on your trading platform 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#136](/thread/post/2640149#post2640149 "Post Permalink")

  * Mar 31, 2009 6:16pm  Mar 31, 2009 6:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar96656_4.gif) $aly]($aly)

  * | Commercial User  | Joined Mar 2009 | [183 Posts](/search?do=process&provider=Member&searchuser=96656)

> [Quoting jgadefelth](/thread/post/2640057#post2640057 "View Quoted Post")
> 
> Disliked
> 
> Saly why can i use it on 4h but not on 1h is there a speciel sort of arrows i shall follow ??   
>    
>  what did you have as a stopploss and target ?  
>    
>  best regards
> 
> Ignored

1-as i see hours and hours ,,, when up trend or down trend break and one candle form in opposite way and then it closes now arrows show ...it seems in 1H and lower arrows sometimes (20%) appear on entry point of previous arrow  
2-my entry points are after break the blue line (in buy position above the blue line and in sell position below the blue line) and i set my SL (below the blue line in buy and above the blue line in sell positions)  
3-i close my position when Fisher_Yur4ik chenge color (red to white or white to red) or before it change when it is going to change ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#137](/thread/post/2640153#post2640153 "Post Permalink")

  * Mar 31, 2009 6:17pm  Mar 31, 2009 6:17pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I perfer this method for 4hr+ TF and it is safe.  
  
Are there anybody here would like to do a test and then report it here:  
  
Attach the arrow to your chart: 4hr,daily,nad weekly for all the pairs you could get access to.  
  
1.Find out how many false signal could you find? eg, are there any open positions that could not be closed by the counter arrow.  
  
2.If you find any , please specify the symbol,TF,Time.  
  
3.make a suggestion how to handl such a peoblem.eg how could you manange the risk? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#138](/thread/post/2640157#post2640157 "Post Permalink")

  * Mar 31, 2009 6:20pm  Mar 31, 2009 6:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar96656_4.gif) $aly]($aly)

  * | Commercial User  | Joined Mar 2009 | [183 Posts](/search?do=process&provider=Member&searchuser=96656)

> [Quoting lyllia](/thread/post/2639991#post2639991 "View Quoted Post")
> 
> Disliked
> 
> Aud 0.7064-0.6592  
>  Nzd 0.5812-0.5450  
>  Cad 1.2784-1.2344  
>  Jpy 99.77-94.96  
>  Euro 1.3581-1.2842  
>  Gbp 1.4671-1.3841  
>  Chf 1.1618-1.1354
> 
> Ignored

it seems great lyllia  
i took over 300pips from GJ from last night...  
thanks a lot  
saly 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#139](/thread/post/2640167#post2640167 "Post Permalink")

  * Mar 31, 2009 6:23pm  Mar 31, 2009 6:23pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting $aly](/thread/post/2640149#post2640149 "View Quoted Post")
> 
> Disliked
> 
> 1-as i see hours and hours ,,, when up trend or down trend break and one candle form in opposite way and then it closes now arrows show ...it seems in 1H and lower arrows sometimes (20%) appear on entry point of previous arrow  
>  2-my entry points are after break the blue line (in buy position above the blue line and in sell position below the blue line) and i set my SL (below the blue line in buy and above the blue line in sell positions)  
>  3-i close my position when [color=magenta]Fisher_Yur4ik [color=black]chenge color (red to white or white to red)...
> 
> Ignored

could you please attch your chart here? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#140](/thread/post/2640170#post2640170 "Post Permalink")

  * Mar 31, 2009 6:24pm  Mar 31, 2009 6:24pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting $aly](/thread/post/2640157#post2640157 "View Quoted Post")
> 
> Disliked
> 
> it seems great lyllia  
>  i took over 300pips from GJ from last night...  
>  thanks a lot  
>  saly
> 
> Ignored

you did? so do I. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#141](/thread/post/2640180#post2640180 "Post Permalink")

  * Mar 31, 2009 6:26pm  Mar 31, 2009 6:26pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

it's a no brain trade ,isn't it? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#142](/thread/post/2640190#post2640190 "Post Permalink")

  * Mar 31, 2009 6:31pm  Mar 31, 2009 6:31pm 

  * [ preawansyah](preawansyah)

  * | Additional Username  | Joined Jan 2009 | [17 Posts](/search?do=process&provider=Member&searchuser=90826)

I attached all Indicators into: **C![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) rogram FilesSIGTraderexpertsindicators**, and I attached the Lyllia EA into **C![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) rogram FilesSIGTraderexperts**,   
I attached Template FX **into C![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) rogram FilesSIGTraderexpertstemplates**. However, the EA system has not execute any trade automatically.  
  
I also Turn on the Menu “ Expert Advisor” into Green Tick to enable the EA to work. Bt still, it did not work.  
  
Could you and anybody else direct me how to do it properly to enable the EA work automatically?  
  
Really Appreaciate for your kind help.  
  
Cheers,  
Prea

Attached Image (click to enlarge)

[![Click to Enlarge

Name: sample chart.gif_2.gif
Size: 59 KB](/attachment/image/226350/thumbnail?d=1365566699)](/attachment/image/226350?d=1238491860)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#143](/thread/post/2640204#post2640204 "Post Permalink")

  * Mar 31, 2009 6:37pm  Mar 31, 2009 6:37pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

When I test EA I made mistake:  
  
I did not let platform continually running. I shut them down. Then when I restart it I did not tick the icon enable EA.And I am wondering why the position could not be closed.That's how I get some good pips.But for test purpose it is not good.Because I want to know how many positions could not be closed in real time. if I exam the chart by eyes I see none.But there is no perfect system in this world .There must be something faulty for any system:  
  
For an example, this method when there is congestion area in lower TF >1hr there will be many arrows come out to closed each other frequently.That's something I do not like.So I avoid it.If anybody could solve that problem make it also tradable for lower time frame.it is vey helpful. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#144](/thread/post/2640212#post2640212 "Post Permalink")

  * Mar 31, 2009 6:42pm  Mar 31, 2009 6:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar96656_4.gif) $aly]($aly)

  * | Commercial User  | Joined Mar 2009 | [183 Posts](/search?do=process&provider=Member&searchuser=96656)

> [Quoting lyllia](/thread/post/2640167#post2640167 "View Quoted Post")
> 
> Disliked
> 
> could you please attch your chart here?
> 
> Ignored

my entry and exit point 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: gj.gif
Size: 51 KB](/attachment/image/226356/thumbnail?d=1365566699)](/attachment/image/226356?d=1238492511)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#145](/thread/post/2640217#post2640217 "Post Permalink")

  * Mar 31, 2009 6:42pm  Mar 31, 2009 6:42pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting preawansyah](/thread/post/2640190#post2640190 "View Quoted Post")
> 
> Disliked
> 
> I attached all Indicators into: **C![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) rogram FilesSIGTraderexpertsindicators**, and I attached the Lyllia EA into **C![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) rogram FilesSIGTraderexperts**,   
>  I attached Template FX **into C![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) rogram FilesSIGTraderexpertstemplates**. However, the EA system has not execute any trade automatically.  
>    
>  I also Turn on the Menu “ Expert Advisor” into Green Tick to enable the EA to work. Bt still, it did not work.  
>    
>  [FONT=Times...
> 
> Ignored

[/size][/font]   
When attach EA to your chart,there will be a dialoge box come out.You have tick all the box to make EA functional.and then click icon on your platform again to make it work. if you see on the right uphand corner of your platform there is smiling face which mean you attach it properly.otherwise No.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#146](/thread/post/2640240#post2640240 "Post Permalink")

  * Mar 31, 2009 6:55pm  Mar 31, 2009 6:55pm 

  * [ preawansyah](preawansyah)

  * | Additional Username  | Joined Jan 2009 | [17 Posts](/search?do=process&provider=Member&searchuser=90826)

> [Quoting lyllia](/thread/post/2640217#post2640217 "View Quoted Post")
> 
> Disliked
> 
> [/size][/font]   
>  When attach EA to your chart,there will be a dialoge box come out.You have tick all the box to make EA functional.and then click icon on your platform again to make it work. if you see on the right uphand corner of your platform there is smiling face which mean you attach it properly.otherwise No.
> 
> Ignored

Lyllia..! Could You please spell it out step by step on how to attach and enable the EA to Work? I am a newbie and just do not know much on the trading platform. Please advise it...  
  
I do not know where the smiling face coming up on the right of my uphand. Please show by illustrating it to me in picture.  
  
Really appreciate for your kind help and cheers. - PREA 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#147](/thread/post/2640256#post2640256 "Post Permalink")

  * Mar 31, 2009 7:01pm  Mar 31, 2009 7:01pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lyllia](/thread/post/2639991#post2639991 "View Quoted Post")
> 
> Disliked
> 
>   
>  Month End S & R  
>    
>  Aud 0.7064-0.6592  
>  Nzd 0.5812-0.5450  
>  Cad 1.2784-1.2344  
>  Jpy 99.77-94.96  
>  Euro 1.3581-1.2842  
>  Gbp 1.4671-1.3841  
>  Chf 1.1618-1.1354
> 
> Ignored

Tonight we could make good pips . 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#148](/thread/post/2640267#post2640267 "Post Permalink")

  * Mar 31, 2009 7:07pm  Mar 31, 2009 7:07pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting preawansyah](/thread/post/2640240#post2640240 "View Quoted Post")
> 
> Disliked
> 
> Lyllia..! Could You please spell it out step by step on how to attach and enable the EA to Work? I am a newbie and just do not know much on the trading platform. Please advise it...  
>    
>  I do not know where the smiling face coming up on the right of my uphand. Please show by illustrating it to me in picture.  
>    
>  Really appreciate for your kind help and cheers. - PREA
> 
> Ignored

please see my post 135 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#149](/thread/post/2640276#post2640276 "Post Permalink")

  * Mar 31, 2009 7:13pm  Mar 31, 2009 7:13pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

The most important thing in this system remember is to have your faith in this system:  
  
Once the arrow come out in 4hr chart ,play your trade.Like last night all the pairs turn around.According to my experiences,it is very rare that does not work. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#150](/thread/post/2640293#post2640293 "Post Permalink")

  * Mar 31, 2009 7:20pm  Mar 31, 2009 7:20pm 

  * [ preawansyah](preawansyah)

  * | Additional Username  | Joined Jan 2009 | [17 Posts](/search?do=process&provider=Member&searchuser=90826)

> [Quoting lyllia](/thread/post/2640125#post2640125 "View Quoted Post")
> 
> Disliked
> 
> I couldn't understand your peoblem.It shouldn't happen if you download all the indicators to your trading platform properly,regardless which broker you use.  
>  Follow the following steps;  
>    
>  1.download all the indicators into your indicator file & template into your template file:  
>    
>  2.attach template to your chart;  
>    
>  3.download EA to your expert file and attach it to your chart. When you attach it to your chart ,do not forget to tick the box allow Expert Adviser,and other boxes (anybody could help here give the name of other boxes and tick them all,my...
> 
> Ignored

Dear Lyllia..  
I have done it as you told above. But I do not understand when you said OTHER BOXES TO BE TICKED. What I have Ticked was Expert Advisor Box only. Please clarify it. Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#151](/thread/post/2640300#post2640300 "Post Permalink")

  * Mar 31, 2009 7:22pm  Mar 31, 2009 7:22pm 

  * [ preawansyah](preawansyah)

  * | Additional Username  | Joined Jan 2009 | [17 Posts](/search?do=process&provider=Member&searchuser=90826)

> [Quoting lyllia](/thread/post/2640276#post2640276 "View Quoted Post")
> 
> Disliked
> 
> The most important thing in this system remember is to have your faith in this system:  
>    
>  Once the arrow come out in 4hr chart ,play your trade.Like last night all the pairs turn around.According to my experiences,it is very rare that does not work.
> 
> Ignored

Why do you mind to shrare the result here by posting the chart and so on? Could you please post it...? We will learn quickly the through visualization  
  
Thanks  
Prea 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#152](/thread/post/2640430#post2640430 "Post Permalink")

  * Mar 31, 2009 8:11pm  Mar 31, 2009 8:11pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting preawansyah](/thread/post/2640240#post2640240 "View Quoted Post")
> 
> Disliked
> 
> Lyllia..! Could You please spell it out step by step on how to attach and enable the EA to Work? I am a newbie and just do not know much on the trading platform. Please advise it...  
>    
>  I do not know where the smiling face coming up on the right of my uphand. Please show by illustrating it to me in picture.  
>    
>  Really appreciate for your kind help and cheers. - PREA
> 
> Ignored

Follow thisi step:  
  
1.attach EA to your chart;  
2\. a dialogue box pops out ,go to the parameter section and tick all the   
boxes.then close it.  
3.then click your platform:enable EA trading fuction.  
4.you will see there is a smiling face on the right uphand of your platform. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: nzd4hr.gif
Size: 19 KB](/attachment/image/226405/thumbnail?d=1365566699)](/attachment/image/226405?d=1238497576)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#153](/thread/post/2640447#post2640447 "Post Permalink")

  * Mar 31, 2009 8:20pm  Mar 31, 2009 8:20pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting preawansyah](/thread/post/2640240#post2640240 "View Quoted Post")
> 
> Disliked
> 
> Lyllia..! Could You please spell it out step by step on how to attach and enable the EA to Work? I am a newbie and just do not know much on the trading platform. Please advise it...  
>    
>  I do not know where the smiling face coming up on the right of my uphand. Please show by illustrating it to me in picture.  
>    
>  Really appreciate for your kind help and cheers. - PREA
> 
> Ignored

this one might be more clearer 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: nzd4hr.gif
Size: 21 KB](/attachment/image/226413/thumbnail?d=1365566699)](/attachment/image/226413?d=1238498395)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#154](/thread/post/2640456#post2640456 "Post Permalink")

  * Mar 31, 2009 8:23pm  Mar 31, 2009 8:23pm 

  * [ preawansyah](preawansyah)

  * | Additional Username  | Joined Jan 2009 | [17 Posts](/search?do=process&provider=Member&searchuser=90826)

> [Quoting lyllia](/thread/post/2640430#post2640430 "View Quoted Post")
> 
> Disliked
> 
> Follow thisi step:  
>    
>  1.attach EA to your chart;  
>  2\. a dialogue box pops out ,go to the parameter section and tick all the   
>  boxes.then close it.  
>  3.then click your platform:enable EA trading fuction.  
>  4.you will see there is a smiling face on the right uphand of your platform.
> 
> Ignored

Lyllia,  
  
When I insert the EA by clicking at Menu 'Indicator - Custom', No pop-up box coming up.  
  
FYI, I saved and copied the EA in the Expert/Indicator Folder already. Am I doing right? If I am wrong, how should I pick up the EA from the Expert Indicator folder?  
  
Cheers and Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#155](/thread/post/2640466#post2640466 "Post Permalink")

  * Mar 31, 2009 8:28pm  Mar 31, 2009 8:28pm 

  * [ preawansyah](preawansyah)

  * | Additional Username  | Joined Jan 2009 | [17 Posts](/search?do=process&provider=Member&searchuser=90826)

Lyllia,,,  
  
I know now how to attach it. I should go to NAVIGATOR. Now smiling face is appearing. Thanks:-)  
  
Lyllia,, If I want to stop tarding, how and what should I do then? Do I have to turn off the EA or turn off the Platform trading..?  
  
Cheers  
Prea 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#156](/thread/post/2640542#post2640542 "Post Permalink")

  * Mar 31, 2009 9:06pm  Mar 31, 2009 9:06pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting preawansyah](/thread/post/2640466#post2640466 "View Quoted Post")
> 
> Disliked
> 
> Lyllia,,,  
>    
>  I know now how to attach it. I should go to NAVIGATOR. Now smiling face is appearing. Thanks:-)  
>    
>  Lyllia,, If I want to stop tarding, how and what should I do then? Do I have to turn off the EA or turn off the Platform trading..?  
>    
>  Cheers  
>  Prea
> 
> Ignored

just disable the EA function on your platform 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#157](/thread/post/2640587#post2640587 "Post Permalink")

  * Mar 31, 2009 9:21pm  Mar 31, 2009 9:21pm 

  * [ preawansyah](preawansyah)

  * | Additional Username  | Joined Jan 2009 | [17 Posts](/search?do=process&provider=Member&searchuser=90826)

Lyllia,,  
  
As I have set up the trading platform with all the lyllia template and activation of EA on 4H Time Frame, Do I just leave it to the EA to execute the trade automatically or Do I have to firstly initiate a trade from each pair? Please Advise.  
  
Thanks much, and have a nice pips.  
  
Thanks  
Prea 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#158](/thread/post/2640632#post2640632 "Post Permalink")

  * Mar 31, 2009 9:42pm  Mar 31, 2009 9:42pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Resistance 0.7064 for today 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: aud 4hr.gif
Size: 24 KB](/attachment/image/226448/thumbnail?d=1365566726)](/attachment/image/226448?d=1238503105)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#159](/thread/post/2640667#post2640667 "Post Permalink")

  * Mar 31, 2009 9:59pm  Mar 31, 2009 9:59pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

1.4671-1.3841 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: gbp 4hr.gif
Size: 25 KB](/attachment/image/226458/thumbnail?d=1365566726)](/attachment/image/226458?d=1238504381)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#160](/thread/post/2640678#post2640678 "Post Permalink")

  * Mar 31, 2009 10:06pm  Mar 31, 2009 10:06pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

1.3581-1.2842 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: euro 4hr.gif
Size: 25 KB](/attachment/image/226461/thumbnail?d=1365566726)](/attachment/image/226461?d=1238504784)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#161](/thread/post/2640683#post2640683 "Post Permalink")

  * Mar 31, 2009 10:09pm  Mar 31, 2009 10:09pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

1.1618-1.1354 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: chf 4hr.gif
Size: 27 KB](/attachment/image/226463/thumbnail?d=1365566726)](/attachment/image/226463?d=1238504933)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#162](/thread/post/2640692#post2640692 "Post Permalink")

  * Mar 31, 2009 10:14pm  Mar 31, 2009 10:14pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

99.77-94.96 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: jpy 4hr.gif
Size: 26 KB](/attachment/image/226465/thumbnail?d=1365566726)](/attachment/image/226465?d=1238505266)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#163](/thread/post/2640706#post2640706 "Post Permalink")

  * Mar 31, 2009 10:19pm  Mar 31, 2009 10:19pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

1.2784-1.2344 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: cad 4hr.gif
Size: 25 KB](/attachment/image/226474/thumbnail?d=1365566726)](/attachment/image/226474?d=1238505570)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#164](/thread/post/2640724#post2640724 "Post Permalink")

  * Mar 31, 2009 10:31pm  Mar 31, 2009 10:31pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting preawansyah](/thread/post/2640587#post2640587 "View Quoted Post")
> 
> Disliked
> 
> Lyllia,,  
>    
>  As I have set up the trading platform with all the lyllia template and activation of EA on 4H Time Frame, Do I just leave it to the EA to execute the trade automatically or Do I have to firstly initiate a trade from each pair? Please Advise.  
>    
>  Thanks much, and have a nice pips.  
>    
>  Thanks  
>  Prea
> 
> Ignored

Hi Prea,  
  
This EA is still in testing stage. You could run it with demo account if there is any position opened by EA, you could give it a second thought to open an live account position manually.If after trial of the EA,you are 100 % sure you have a faith in it,then you could run it with your living account. Please truthfully share your experience with the EA.  
  
You could apply it with only one chart and save it as a template.Then you could apply the template to any chart. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#165](/thread/post/2640738#post2640738 "Post Permalink")

  * Mar 31, 2009 10:35pm  Mar 31, 2009 10:35pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting preawansyah](/thread/post/2640456#post2640456 "View Quoted Post")
> 
> Disliked
> 
> Lyllia,  
>    
>  When I insert the EA by clicking at Menu 'Indicator - Custom', No pop-up box coming up.  
>    
>  FYI, I saved and copied the EA in the Expert/Indicator Folder already. Am I doing right? If I am wrong, how should I pick up the EA from the Expert Indicator folder?  
>    
>  Cheers and Thanks
> 
> Ignored

1.save indicator to indicator file;  
2.save EA into expert file;  
3.save template into template file. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#166](/thread/post/2640779#post2640779 "Post Permalink")

  * Mar 31, 2009 10:48pm  Mar 31, 2009 10:48pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting preawansyah](/thread/post/2640587#post2640587 "View Quoted Post")
> 
> Disliked
> 
> Lyllia,,  
>    
>  As I have set up the trading platform with all the lyllia template and activation of EA on 4H Time Frame, Do I just leave it to the EA to execute the trade automatically or Do I have to firstly initiate a trade from each pair? Please Advise.  
>    
>  Thanks much, and have a nice pips.  
>    
>  Thanks  
>  Prea
> 
> Ignored

Remember market is continuing, for testing purpose you have to leave your platform open during trading weekdays. you can apply EA to each chart seperately or just make an template including EA. Then apply this template to any chart.After you set up everything,click Enable EA icon on your trading platform. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#167](/thread/post/2640790#post2640790 "Post Permalink")

  * Mar 31, 2009 10:52pm  Mar 31, 2009 10:52pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting preawansyah](/thread/post/2640466#post2640466 "View Quoted Post")
> 
> Disliked
> 
> Lyllia,,,  
>    
>  I know now how to attach it. I should go to NAVIGATOR. Now smiling face is appearing. Thanks:-)  
>    
>  Lyllia,, If I want to stop tarding, how and what should I do then? Do I have to turn off the EA or turn off the Platform trading..?  
>    
>  Cheers  
>  Prea
> 
> Ignored

you could disable EA by clicking the EA icon .If you want to put it back you could enable it by clicking it again. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#168](/thread/post/2640862#post2640862 "Post Permalink")

  * Mar 31, 2009 11:18pm  Mar 31, 2009 11:18pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

When enable EA with 4hr chart Please do not switch that same chart to another TF.Because different TF has different arrow,that will ruin the trade opened with 4hr chart. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#169](/thread/post/2641001#post2641001 "Post Permalink")

  * Apr 1, 2009 12:09am  Apr 1, 2009 12:09am 

  * [ imanhadi](imanhadi)

  * | Joined Mar 2009  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=98533)

Hi Lyllia  
  
A great system that you have there.   
  
I was wondering how the abha center timing works. Care to explain further?  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#170](/thread/post/2641056#post2641056 "Post Permalink")

  * Apr 1, 2009 12:24am  Apr 1, 2009 12:24am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting imanhadi](/thread/post/2641001#post2641001 "View Quoted Post")
> 
> Disliked
> 
> Hi Lyllia  
>    
>  A great system that you have there.   
>    
>  I was wondering how the abha center timing works. Care to explain further?  
>    
>  Thanks
> 
> Ignored

It is a cycle identifier:Red signals top might in place,green signals bottom might in place.The indicator is medium reliable.It might repaint. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#171](/thread/post/2641484#post2641484 "Post Permalink")

  * Apr 1, 2009 3:00am  Apr 1, 2009 3:00am 

  * [ jgadefelth](jgadefelth)

  * | Joined Jan 2008  | Status: Trillion Dollar Man | [1,495 Posts](/search?do=process&provider=Member&searchuser=58861)

Any one hitting the 95% hit rate or how is it going ?   
  
  
best regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#172](/thread/post/2641719#post2641719 "Post Permalink")

  * Apr 1, 2009 4:29am  Apr 1, 2009 4:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar96656_4.gif) $aly]($aly)

  * | Commercial User  | Joined Mar 2009 | [183 Posts](/search?do=process&provider=Member&searchuser=96656)

> [Quoting jgadefelth](/thread/post/2641484#post2641484 "View Quoted Post")
> 
> Disliked
> 
> Any one hitting the 95% hit rate or how is it going ?   
>    
>    
>  best regards
> 
> Ignored

calcute 95% needs at least 10 trades ...we have to wait jgadefelth and see what happened....![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#173](/thread/post/2641757#post2641757 "Post Permalink")

  * Apr 1, 2009 4:41am  Apr 1, 2009 4:41am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Hi Peter,  
  
on EURO 4hr chart, There is sell arrow on top of the candle with a 100 pips 1.3338-1.3227.The sell postion opened at the end of the candle 1.3227.Then price go up to 133.Eurusd only has 2pips spread.Why the postion opened at the end of the candle?It will completly destroy this method.could you find reason? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#174](/thread/post/2641804#post2641804 "Post Permalink")

  * Apr 1, 2009 4:55am  Apr 1, 2009 4:55am 

  * [ VenomDraC](venomdrac)

  * | Joined Feb 2009  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=95060)

hi lilya,  
  
just curious with those circle (balls![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)) with numbers indicator, care to share what indi izit? can i have them please.  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
Drac. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#175](/thread/post/2641866#post2641866 "Post Permalink")

  * Apr 1, 2009 5:08am  Apr 1, 2009 5:08am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Could you help to find out what time the arrow appeared on euro 4hr chart?Are there any way to find out?tia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#176](/thread/post/2641871#post2641871 "Post Permalink")

  * Apr 1, 2009 5:10am  Apr 1, 2009 5:10am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting VenomDraC](/thread/post/2641804#post2641804 "View Quoted Post")
> 
> Disliked
> 
> hi lilya,  
>    
>  just curious with those circle (balls![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)) with numbers indicator, care to share what indi izit? can i have them please.  
>  ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
>  Drac.
> 
> Ignored

go to the start of this thread you will have them all 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#177](/thread/post/2641879#post2641879 "Post Permalink")

  * Apr 1, 2009 5:11am  Apr 1, 2009 5:11am 

  * [ bwk9087](bwk9087)

  * | Joined Nov 2006  | Status: Trader | [64 Posts](/search?do=process&provider=Member&searchuser=23733)

> [Quoting lyllia](/thread/post/2641757#post2641757 "View Quoted Post")
> 
> Disliked
> 
> Hi Peter,  
>    
>  on EURO 4hr chart, There is sell arrow on top of the candle with a 100 pips 1.3338-1.3227.The sell postion opened at the end of the candle 1.3227.Then price go up to 133.Eurusd only has 2pips spread.Why the postion opened at the end of the candle?It will completly destroy this method.could you find reason?
> 
> Ignored

  
on mine, A sell opened at 16:00 at beginning of a candle, and then a buy opened up, at the 20:00 candle, not closing the sell order. Perfect hedge at the moment, down $15 each. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#178](/thread/post/2641889#post2641889 "Post Permalink")

  * Apr 1, 2009 5:14am  Apr 1, 2009 5:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83209_5.gif) pitpiter](pitpiter)

  * | Joined Oct 2008  | Status: Trader | [300 Posts](/search?do=process&provider=Member&searchuser=83209)

> [Quoting lyllia](/thread/post/2641757#post2641757 "View Quoted Post")
> 
> Disliked
> 
> Hi Peter,  
>    
>  on EURO 4hr chart, There is sell arrow on top of the candle with a 100 pips 1.3338-1.3227.The sell postion opened at the end of the candle 1.3227.Then price go up to 133.Eurusd only has 2pips spread.Why the postion opened at the end of the candle?It will completly destroy this method.could you find reason?
> 
> Ignored

Hi again , I ask You about Your broker . Without that I can't do any analize or just post pic with situation about You asking. I program EA for open pos only with first tic for new bar. I will run EA today and share results tommorow.  
I'm sure about LWMA , just see code and You will sure too.  
And information for everybody : for working EA You need put EA file in expert folder , put indi IINWMARROWS to indikators folder , restart your platform , apply EA to chart , make it enable trade automaticaly . If You apply EA for couple pair the better way set every another magic number.  
I do not think the stoploss will be good for this system , but it just my opinion.  
Thats it.  
Regards  
Peter 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#179](/thread/post/2641896#post2641896 "Post Permalink")

  * Apr 1, 2009 5:18am  Apr 1, 2009 5:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar96656_4.gif) $aly]($aly)

  * | Commercial User  | Joined Mar 2009 | [183 Posts](/search?do=process&provider=Member&searchuser=96656)

> [Quoting lyllia](/thread/post/2641866#post2641866 "View Quoted Post")
> 
> Disliked
> 
> Could you help to find out what time the arrow appeared on euro 4hr chart?Are there any way to find out?tia
> 
> Ignored

the arrow appeared when one candle form in opposite of prier candle and break low of prier candle in sell position or high in buy position 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#180](/thread/post/2641901#post2641901 "Post Permalink")

  * Apr 1, 2009 5:18am  Apr 1, 2009 5:18am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

anyvody get good pips with all nzd pairs? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#181](/thread/post/2641931#post2641931 "Post Permalink")

  * Apr 1, 2009 5:26am  Apr 1, 2009 5:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar96656_4.gif) $aly]($aly)

  * | Commercial User  | Joined Mar 2009 | [183 Posts](/search?do=process&provider=Member&searchuser=96656)

> [Quoting $aly](/thread/post/2641896#post2641896 "View Quoted Post")
> 
> Disliked
> 
> the arrow appeared when one candle form in opposite of prier candle and break low of prier candle in sell position or high in buy position
> 
> Ignored

look at this 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: euro.gif
Size: 53 KB](/attachment/image/226744/thumbnail?d=1365566750)](/attachment/image/226744?d=1238531177)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#182](/thread/post/2641939#post2641939 "Post Permalink")

  * Apr 1, 2009 5:29am  Apr 1, 2009 5:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar96656_4.gif) $aly]($aly)

  * | Commercial User  | Joined Mar 2009 | [183 Posts](/search?do=process&provider=Member&searchuser=96656)

lyllia  
do U want to enter before arrows appeared???? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#183](/thread/post/2641972#post2641972 "Post Permalink")

  * Apr 1, 2009 5:39am  Apr 1, 2009 5:39am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lyllia](/thread/post/2641901#post2641901 "View Quoted Post")
> 
> Disliked
> 
> anyvody get good pips with all nzd pairs?
> 
> Ignored

  
nzdusd 90pips,enzd 250 pips,anzd230 pips. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#184](/thread/post/2641975#post2641975 "Post Permalink")

  * Apr 1, 2009 5:41am  Apr 1, 2009 5:41am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting $aly](/thread/post/2641931#post2641931 "View Quoted Post")
> 
> Disliked
> 
> look at this
> 
> Ignored

Let's see if the signal is valid 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#185](/thread/post/2641998#post2641998 "Post Permalink")

  * Apr 1, 2009 5:53am  Apr 1, 2009 5:53am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lyllia](/thread/post/2641972#post2641972 "View Quoted Post")
> 
> Disliked
> 
> nzdusd 90pips,enzd 250 pips,anzd230 pips.
> 
> Ignored

NZDUSD H&S formation? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#186](/thread/post/2642007#post2642007 "Post Permalink")

  * Apr 1, 2009 5:56am  Apr 1, 2009 5:56am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lyllia](/thread/post/2641998#post2641998 "View Quoted Post")
> 
> Disliked
> 
> NZDUSD H&S formation?
> 
> Ignored

Normally 4hr chart trend will last for a while. I have support for NZD for this week around 0.54 or lower area 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#187](/thread/post/2642043#post2642043 "Post Permalink")

  * Apr 1, 2009 6:11am  Apr 1, 2009 6:11am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting $aly](/thread/post/2641939#post2641939 "View Quoted Post")
> 
> Disliked
> 
> lyllia  
>  do U want to enter before arrows appeared????
> 
> Ignored

it is impossible.But it makes me nervious when it opened position 100 below the high. how do you think the NZD pairs today? Do we have to take profit manually or wait for the 4 hrs chart opposit signal come out to close them itself? What if the close position will be another 100 pips higher over the low ?That will eat all the pips.But if the trend will last, we could get more pips ahead.what's ous chioce? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#188](/thread/post/2642098#post2642098 "Post Permalink")

  * Apr 1, 2009 6:39am  Apr 1, 2009 6:39am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Enzd come down more than 100 pips from the high if we leave the position to the arrow to close it ,it might have a counter signal that opens the position 100 pips lower than the high.We have to be aware of this. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#189](/thread/post/2642113#post2642113 "Post Permalink")

  * Apr 1, 2009 6:46am  Apr 1, 2009 6:46am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I have two buy signals at JPY and CHFJPY 4hr chart.Again they opened almost 200 pips higher than where the arrow is.Worry me.Can we survive? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#190](/thread/post/2642136#post2642136 "Post Permalink")

  * Apr 1, 2009 6:56am  Apr 1, 2009 6:56am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

We have to study on the arrow appearing time on 4hr.It is critical.Before I did not notice arrow will only appear after breakout.If you see the first wave on floowing chart the arrow do not have to break out the previous one to generate signal.Anybody could give logic explanation? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: jpy 4hr.gif
Size: 25 KB](/attachment/image/226771/thumbnail?d=1365566776)](/attachment/image/226771?d=1238536595)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#191](/thread/post/2642149#post2642149 "Post Permalink")

  * Apr 1, 2009 7:04am  Apr 1, 2009 7:04am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I just read somebody's comments on NZD:Kiwi posting a nice H&S on the 4hr. Gotta go to bed now will catch the neckline test tomorrow.--Big Rider 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#192](/thread/post/2642204#post2642204 "Post Permalink")

  * Apr 1, 2009 7:44am  Apr 1, 2009 7:44am 

  * [ Mandl2007](mandl2007)

  * | Membership Revoked  | Joined Nov 2008 | [279 Posts](/search?do=process&provider=Member&searchuser=86165)

hmm .. may be RR (Ronald Raygun - EA programmer) and Swingman could help ? You find them in the AshFX II thread - they are great programmers ! The AshFx system is also a long term (4H + daily) one and a little bit similar. I think a dashboard (swingmans great idea !) would be very good for watching possible signals generated by your system. The dashboard is summerazing all generated signals for all pairs in one table at the given moment. So you can see at any moment what pairs are worth for trading. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#193](/thread/post/2642297#post2642297 "Post Permalink")

  * Apr 1, 2009 8:34am  Apr 1, 2009 8:34am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lyllia](/thread/post/2642149#post2642149 "View Quoted Post")
> 
> Disliked
> 
> I just read somebody's comments on NZD:Kiwi posting a nice H&S on the 4hr. Gotta go to bed now will catch the neckline test tomorrow.--Big Rider
> 
> Ignored

Good luck!pips are with you! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: nzd 4hr.gif
Size: 22 KB](/attachment/image/226818/thumbnail?d=1365566776)](/attachment/image/226818?d=1238542484)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#194](/thread/post/2642306#post2642306 "Post Permalink")

  * Apr 1, 2009 8:37am  Apr 1, 2009 8:37am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting Mandl2007](/thread/post/2642204#post2642204 "View Quoted Post")
> 
> Disliked
> 
> hmm .. may be RR (Ronald Raygun - EA programmer) and Swingman could help ? You find them in the AshFX II thread - they are great programmers ! The AshFx system is also a long term (4H + daily) one and a little bit similar. I think a dashboard (swingmans great idea !) would be very good for watching possible signals generated by your system. The dashboard is summerazing all generated signals for all pairs in one table at the given moment. So you can see at any moment what pairs are worth for trading.
> 
> Ignored

thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#195](/thread/post/2642410#post2642410 "Post Permalink")

  * Apr 1, 2009 9:20am  Apr 1, 2009 9:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar48267_23.gif) Oksana17](oksana17)

  * | Membership Revoked  | Joined Sep 2007 | [903 Posts](/search?do=process&provider=Member&searchuser=48267)

> [Quoting lyllia](/thread/post/2636854#post2636854 "View Quoted Post")
> 
> Disliked
> 
> Hi Mate,  
>    
>  why you laugh? Could you help to what happened to the EA trading since you are a programmer as well? Please read what I post about EA trading.You peomised to help yesterday.tia
> 
> Ignored

I never said I promised. I said that if nobody would have made an EA while I was taking a break, I would have made it. So there are errors in the EA that someone made? Write a PM if so. 

Request custom Expert Advisor or Indicator: dostapyuk "at" gmail . com

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#196](/thread/post/2642603#post2642603 "Post Permalink")

  * Apr 1, 2009 10:54am  Apr 1, 2009 10:54am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting Oksana17](/thread/post/2642410#post2642410 "View Quoted Post")
> 
> Disliked
> 
> I never said I promised. I said that if nobody would have made an EA while I was taking a break, I would have made it. So there are errors in the EA that someone made? Write a PM if so.
> 
> Ignored

'I would have made it' is a promise' Do not play your words. You are funny ,aren't you?  
  
I do not think it is an error.Maybe it is how it works.  
  
But I prefer as soon an arrow appears the position will be opened.The problem is I do not know when the arrow will appear.It seems they appear at the end of the candle bar.It is worry.How to improve it? make it working perfect. I do not have that experience that arrow only appears after it breaks the previous bar.But this time looks like it.4hr Euro opened 100 pips lower than the high.But later proves to be a valid signal 100 pips.GBP too opened position 100 pips lower.Still in negtive area.  
  
There are also some inside bar signals like first wave in 4hr JPY chart.they are perfect. they gice instant signals and position.  
  
Would you please have a look and help since you are also a good programmer.  
  
I saw you post here and there wondering around ,why should you spend sometime help us?tia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#197](/thread/post/2642606#post2642606 "Post Permalink")

  * Apr 1, 2009 10:55am  Apr 1, 2009 10:55am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

all positions are in profit except GBP. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#198](/thread/post/2642613#post2642613 "Post Permalink")

  * Apr 1, 2009 10:57am  Apr 1, 2009 10:57am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

This system is good because it is able to catch up the trend from the very begining.So I do not want to give up. Help please everybody ,give your hand here. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#199](/thread/post/2642639#post2642639 "Post Permalink")

  * Apr 1, 2009 11:11am  Apr 1, 2009 11:11am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

see the arrow appear long time but not position opened 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: ejpy 4hr.gif
Size: 24 KB](/attachment/image/226889/thumbnail?d=1365566776)](/attachment/image/226889?d=1238551889)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#200](/thread/post/2642646#post2642646 "Post Permalink")

  * Apr 1, 2009 11:14am  Apr 1, 2009 11:14am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lyllia](/thread/post/2642639#post2642639 "View Quoted Post")
> 
> Disliked
> 
> see the arrow appear long time but not position opened
> 
> Ignored

I take off the EA because in case a position opened it is too low. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#201](/thread/post/2642873#post2642873 "Post Permalink")

  * Apr 1, 2009 1:44pm  Apr 1, 2009 1:44pm 

  * [ piptiger](piptiger)

  * | Joined Jan 2009  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=91721)

Hi lillya,  
  
i was reading your started thread from the beginning. I would like to  
trade on the 4 hr. TF. Did you mention the arrows only appear, if the  
next candle breaks the price? So sometimes the entry would be far away,  
especially in volatile pairs or times?  
  
I also want the EA only to show entry and exit signals so in  
can trade them manually.  
  
I also was wondering what means "3 level zz" to what exactly does it refer?  
  
thanks for the good work done so far.  
  
piptiger 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#202](/thread/post/2642884#post2642884 "Post Permalink")

  * Apr 1, 2009 1:51pm  Apr 1, 2009 1:51pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting pitpiter](/thread/post/2641889#post2641889 "View Quoted Post")
> 
> Disliked
> 
> Hi again , I ask You about Your broker . Without that I can't do any analize or just post pic with situation about You asking. I program EA for open pos only with first tic for new bar. I will run EA today and share results tommorow.  
>  I'm sure about LWMA , just see code and You will sure too.  
>  And information for everybody : for working EA You need put EA file in expert folder , put indi IINWMARROWS to indikators folder , restart your platform , apply EA to chart , make it enable trade automaticaly . If You apply EA for couple pair the better way...
> 
> Ignored

Hi Peter,  
  
Thank you for this EA. It seems working well. except after the arrow appeared for a long time the position could not be opened.  
  
Take a look at the chart of EJPY my post befor this one. when I saw arrow appears and stay there for a long time and no position opened so I took off the EA. Because I am afraid if a position opened it might too low.But in fact the later the price did come down.  
Same happened to 4hr Euro and GBP chart. It opened the position 100 pips lower than the high.But euro signal is still valid into profit,GBP now 10 pips negtive.  
  
Could you please have a look at the original arrow code I post.They are fast EMA3 and have their rules to make arrow appear.Could you include them into EA start function.Do you think it might help to solve the problem?  
  
Before I am doing manual trading,there is no delayed arrow signal.If this problem could be solved that will be perfect.Tia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#203](/thread/post/2642892#post2642892 "Post Permalink")

  * Apr 1, 2009 1:55pm  Apr 1, 2009 1:55pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting piptiger](/thread/post/2642873#post2642873 "View Quoted Post")
> 
> Disliked
> 
> Hi lillya,  
>    
>  i was reading your started thread from the beginning. I would like to  
>  trade on the 4 hr. TF. Did you mention the arrows only appear, if the  
>  next candle breaks the price? So sometimes the entry would be far away,  
>  especially in volatile pairs or times?  
>    
>  I also want the EA only to show entry and exit signals so in  
>  can trade them manually.  
>    
>  I also was wondering what means "3 level zz" to what exactly does it refer?  
>    
>  thanks for the good work done so far.  
>    
>  piptiger
> 
> Ignored

3 level zz is not reliable,it repaint all the time with pA.I put there for count wave purpose. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#204](/thread/post/2642920#post2642920 "Post Permalink")

  * Apr 1, 2009 2:08pm  Apr 1, 2009 2:08pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting piptiger](/thread/post/2642873#post2642873 "View Quoted Post")
> 
> Disliked
> 
> Hi lillya,  
>    
>  i was reading your started thread from the beginning. I would like to  
>  trade on the 4 hr. TF. Did you mention the arrows only appear, if the  
>  next candle breaks the price? So sometimes the entry would be far away,  
>  especially in volatile pairs or times?  
>    
>  I also want the EA only to show entry and exit signals so in  
>  can trade them manually.  
>    
>  I also was wondering what means "3 level zz" to what exactly does it refer?  
>    
>  thanks for the good work done so far.  
>    
>  piptiger
> 
> Ignored

Peter,  
  
when I do manual trading as soon as the arrow appears I open the position .Because it is so reliable.I am not hesitating to take action.I know breakout is a good trading principle.But for me it is too late. I am not used to it.If you see the original code of the arrow I m sure you will understand how it works.I know you give a good reliable entry and exist points.If you could combined the two good points together .that will help to make it perfect. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#205](/thread/post/2642934#post2642934 "Post Permalink")

  * Apr 1, 2009 2:13pm  Apr 1, 2009 2:13pm 

  * [ piptiger](piptiger)

  * | Joined Jan 2009  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=91721)

lillya,  
  
thanks for explanation of "3 level zz".  
  
But could you also let me know what i asked:  
does the arrow only appear, if the price of the next bar is lower/higher  
as the forgoing bar?  
  
like i mentioned i am looking for a system/method for higher TF.  
best 4hr.  
  
It would be also an great help for fellow traders, if there would be an short  
manual who explains, how the indis itself and the whole system works.  
  
What is your preferred pair to trade with?  
  
thanks for your dedication to this thread  
  
piptiger 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#206](/thread/post/2642942#post2642942 "Post Permalink")

  * Apr 1, 2009 2:18pm  Apr 1, 2009 2:18pm 

  * [ piptiger](piptiger)

  * | Joined Jan 2009  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=91721)

illya,  
  
BTW, i am NOT PITPITER,  
  
but my membername is also very close and could be confused.  
  
greetings  
PIPTIGER 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#207](/thread/post/2643064#post2643064 "Post Permalink")

  * Apr 1, 2009 3:10pm  Apr 1, 2009 3:10pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting pitpiter](/thread/post/2635439#post2635439 "View Quoted Post")
> 
> Disliked
> 
> Try this one. It open trade after bar on which indi generate signal close.  
>  Good luck  
>  Peter  
>  edit look post 62 for correct version
> 
> Ignored

Hi Peter,  
  
Is it not too late to generate singnal after the bar close?  
  
This happened to some pairs yesterday. Euro ,GBP,both give the signal after the previous bar close .that's 100 pips under the high.It is too late.  
If you look at the original code : FASTEMA3,they are very efficient.as soon as the rule has been met the arrow appears. no delayed signal.Could you strickly follow that rule .Or it also might be helpful to include the original code into the  
EA,which might help to solve this problem? tia,hope you make soem adjustment according to th eoriginal code please. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#208](/thread/post/2643076#post2643076 "Post Permalink")

  * Apr 1, 2009 3:15pm  Apr 1, 2009 3:15pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting piptiger](/thread/post/2642873#post2642873 "View Quoted Post")
> 
> Disliked
> 
> Hi lillya,  
>    
>  i was reading your started thread from the beginning. I would like to  
>  trade on the 4 hr. TF. Did you mention the arrows only appear, if the  
>  next candle breaks the price? So sometimes the entry would be far away,  
>  especially in volatile pairs or times?  
>    
>  I also want the EA only to show entry and exit signals so in  
>  can trade them manually.  
>    
>  I also was wondering what means "3 level zz" to what exactly does it refer?  
>    
>  thanks for the good work done so far.  
>    
>  piptiger
> 
> Ignored

No I did not mention that. I prefer as soon as the arrow comes out the position could be opened. I just observe that the position is too far away from the time an arrow appeared. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#209](/thread/post/2643083#post2643083 "Post Permalink")

  * Apr 1, 2009 3:19pm  Apr 1, 2009 3:19pm 

  * [ fxxx](fxxx)

  * | Joined Dec 2007  | Status: Trader | [475 Posts](/search?do=process&provider=Member&searchuser=55426)

you guys gottobe kidding - what a waste of time an affords - your ma3 open/close cross repaints, solar wind (your fisher y4rik) - repaints as trooper - and you don't even know this...   
any EA under this circumstances would be complete waste - there is no reliable becktest - no point   
  
p.s. any another ind. would perform same or even better - and w/o lying 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#210](/thread/post/2643238#post2643238 "Post Permalink")

  * Apr 1, 2009 5:06pm  Apr 1, 2009 5:06pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting fxxx](/thread/post/2643083#post2643083 "View Quoted Post")
> 
> Disliked
> 
> you guys gottobe kidding - what a waste of time an affords - your ma3 open/close cross repaints, solar wind (your fisher y4rik) - repaints as trooper - and you don't even know this...   
>  any EA under this circumstances would be complete waste - there is no reliable becktest - no point   
>    
>  p.s. any another ind. would perform same or even better - and w/o lying
> 
> Ignored

Hi mate,  
  
Please be polite. if you read carefully from the begining you will know this system is only about the arrow.Other indicators are for reference.they are helpful even they are faulty. I do not know why you have to swere ,could you make some positive suggestion? Be happy ,it is good for you! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#211](/thread/post/2643391#post2643391 "Post Permalink")

  * Apr 1, 2009 6:32pm  Apr 1, 2009 6:32pm 

  * [ tentoerun](tentoerun)

  * | Joined Jan 2008  | Status: Trader | [45 Posts](/search?do=process&provider=Member&searchuser=58967)

Hi[ lyllia](http://www.forexfactory.com/member.php?u=67706)  
  
IINWMARROWS is no more than two 3-period LMA indicators(fast with PRICE_CLOSE, slow with PRICE_OPEN), it does repaint, sometimes frequently.  
  
Please have a look at the following two GJ 4H charts:  
  
The first one is a normal history chart, the second one comes from MT4 Tester. That is: you will meet 2 more up arrows on chart-2 when trading live, how do you handle it?  
  
Cheers,  
Simon 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 2.gif
Size: 6 KB](/attachment/image/227028/thumbnail?d=1365566802)](/attachment/image/227028?d=1238578157)   
[![Click to Enlarge

Name: 1.gif
Size: 6 KB](/attachment/image/227030/thumbnail?d=1365566826)](/attachment/image/227030?d=1238578293)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#212](/thread/post/2643523#post2643523 "Post Permalink")

  * Apr 1, 2009 7:35pm  Apr 1, 2009 7:35pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting suwuming](/thread/post/2643391#post2643391 "View Quoted Post")
> 
> Disliked
> 
> Hi[ lyllia](http://www.forexfactory.com/member.php?u=67706)  
>    
>  IINWMARROWS is no more than two 3-period LMA indicators(fast with PRICE_CLOSE, slow with PRICE_OPEN), it does repaint, sometimes frequently.  
>    
>  Please have a look at the following two GJ 4H charts:  
>    
>  The first one is a normal history chart, the second one comes from MT4 Tester. That is: you will meet 2 more up arrows on chart-2 when trading live, how do you handle it?  
>    
>  Cheers,  
>  Simon
> 
> Ignored

Somebody told me repaint means they are not stable ,move or disappear.  
  
I could confirm that they are stable,once they come out ,they remain.  
  
If there are more than one arrow appear in one time frame,in EA trading which means sevral positions opened,then the first opposite singal close them all. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#213](/thread/post/2645027#post2645027 "Post Permalink")

  * Apr 2, 2009 4:51am  Apr 2, 2009 4:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83209_5.gif) pitpiter](pitpiter)

  * | Joined Oct 2008  | Status: Trader | [300 Posts](/search?do=process&provider=Member&searchuser=83209)

Hi there.  
I have observe EA and indi on 5M TF. When bar 1 close arrow was apply on place when now I apply 1 , and latter it lose .  
As for me it looking that if we have aroow up and get arrow down and on next bar get arrow up again , it canceled arrow down , applied one bar before and in that case we have on chart second up arrow .  
As I see arrow always apply when bar close .  
Lyllia , You shoud observe indi and will say your opinie about thing , what I'm talk.  
Regards  
Peter 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 1.gif
Size: 26 KB](/attachment/image/227362/thumbnail?d=1365566884)](/attachment/image/227362?d=1238615499)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#214](/thread/post/2645444#post2645444 "Post Permalink")

  * Apr 2, 2009 8:59am  Apr 2, 2009 8:59am 

  * [ fxxx](fxxx)

  * | Joined Dec 2007  | Status: Trader | [475 Posts](/search?do=process&provider=Member&searchuser=55426)

Originally Posted by **fxxx** [](http://www.forexfactory.com/showthread.php?p=2643083#post2643083)<http://www.forexfactory.com/images/buttons/viewpost.gif>   
_you guys gottobe kidding - what a waste of time an affords - your ma3 open/close cross repaints, solar wind (your fisher y4rik) - repaints as trooper - and you don't even know this..._  
_any EA under this circumstances would be complete waste - there is no reliable becktest - no point_  
  
_p.s. any another ind. would perform same or even better - and w/o lying_  
[/quote]  

> [Quoting lyllia](/thread/post/2643238#post2643238 "View Quoted Post")
> 
> Disliked
> 
> Hi mate,Quote:  
>    
>  Please be polite. if you read carefully from the begining you will know this system is only about the arrow.Other indicators are for reference.they are helpful even they are faulty. I do not know why you have to swere ,could you make some positive suggestion? Be happy ,it is good for you!
> 
> Ignored

i was polite - i sayed you indicators are lying, and you didn't even knew about it (it's tells how good you know your system - positive part)   
p.s.your "arrow" - lwma 3 (open/close cross) ? (on such short per.(3) - can be any Ma) - ma cross _alone_ basically would kill any system on chopy/flat market  
cheers, mate 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#215](/thread/post/2645461#post2645461 "Post Permalink")

  * Apr 2, 2009 9:12am  Apr 2, 2009 9:12am 

  * [ forexisfx](forexisfx)

  * | Joined Nov 2008  | Status: Gold Member | [689 Posts](/search?do=process&provider=Member&searchuser=84687)

> [Quoting fxxx](/thread/post/2645444#post2645444 "View Quoted Post")
> 
> Disliked
> 
> i was polite - i sayed you indicators are lying, and you didn't even knew about it (it's tells how good you know your system - positive part)   
>  p.s.your "arrow" - lwma 3 (open/close cross) ? (on such short per.(3) - can be any Ma) - ma cross _alone_ basically would kill any system on chopy/flat market  
>  cheers, mate
> 
> Ignored

Hey, lyllia has 95% success rate. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#216](/thread/post/2646224#post2646224 "Post Permalink")

  * Apr 2, 2009 4:06pm  Apr 2, 2009 4:06pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting pitpiter](/thread/post/2645027#post2645027 "View Quoted Post")
> 
> Disliked
> 
> Hi there.  
>  I have observe EA and indi on 5M TF. When bar 1 close arrow was apply on place when now I apply 1 , and latter it lose .  
>  As for me it looking that if we have aroow up and get arrow down and on next bar get arrow up again , it canceled arrow down , applied one bar before and in that case we have on chart second up arrow .  
>  As I see arrow always apply when bar close .  
>  Lyllia , You shoud observe indi and will say your opinie about thing , what I'm talk.  
>  Regards  
>  Peter
> 
> Ignored

Ok I have another look.Try to find repaints.I have used it for a while,only come cross once.It moved a bit but not far from the original place ,maybe 4 or 5 pips away. It is very rare.I insist that it is reliable,usable for trading better than other arrow indicators.this is how I value this indicator.Nothing is perfect in this world.We should allow faulty in anything.For this indicator I have a high opinion of it.   
  
The following are the MA that form the indicator:not only LWMA,They are working together make this indicator efficient and reliable.  
  
FasterMode=3; //0=sma, 1=ema, 2=smma, 3=lwma  
FasterMA= 3;  
SlowerMode=3; //0=sma, 1=ema, 2=smma, 3=lwma  
SlowerMA= 3;  
  
if ((fasterMAnow > slowerMAnow) && (fasterMAprevious < slowerMAprevious) && (fasterMAafter > slowerMAafter))   
{  
CrossUp[i]=Low[i] - Range*0.5;  
}  
else if ((fasterMAnow < slowerMAnow) && (fasterMAprevious > slowerMAprevious) && (fasterMAafter < slowerMAafter))   
{  
CrossDown[i]=High[i] + Range*0.5; (additional filter here)  
  
This fuction works very efficient.As soon as the arrow comes out it stay.I give it 95% successful rate. Especially for High TF.  
  
If EA could includes the above function into its programming structure.that will be very promising.The only concern after I using the EA is the position opened sometimes too late after the arrow appears. If your guys could do something positive,that will be terrific.Do not kill this system even though it has faulty side .try to solve te problem.I think that's the way to make a perfect system. How do you think.Are there any way we could improve it? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#217](/thread/post/2646460#post2646460 "Post Permalink")

  * Apr 2, 2009 6:17pm  Apr 2, 2009 6:17pm 

  * [ jgadefelth](jgadefelth)

  * | Joined Jan 2008  | Status: Trillion Dollar Man | [1,495 Posts](/search?do=process&provider=Member&searchuser=58861)

Saly how are youdoing with this system ??  
  
  
Lylia are you still thinking 95% hit rate or was that little to mutch ?   
  
im not getting you buy signal and sell signals ?  
  
  
best regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#218](/thread/post/2646531#post2646531 "Post Permalink")

  * Apr 2, 2009 6:47pm  Apr 2, 2009 6:47pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

good news tonight:  
  
R & S:  
  
JPY 100.11-97.34  
GBP 1.4636-1.4216  
AUD 0.7084-0.6849  
EUR 1.3437-1.3058  
CHF 1.1590-1.1307  
NZD 0.5776-0.5539  
CAD1.2482-1.2448  
  
manage your own risk. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#219](/thread/post/2647491#post2647491 "Post Permalink")

  * Apr 3, 2009 12:40am  Apr 3, 2009 12:40am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting pitpiter](/thread/post/2645027#post2645027 "View Quoted Post")
> 
> Disliked
> 
> Hi there.  
>  I have observe EA and indi on 5M TF. When bar 1 close arrow was apply on place when now I apply 1 , and latter it lose .  
>  As for me it looking that if we have aroow up and get arrow down and on next bar get arrow up again , it canceled arrow down , applied one bar before and in that case we have on chart second up arrow .  
>  As I see arrow always apply when bar close .  
>  Lyllia , You shoud observe indi and will say your opinie about thing , what I'm talk.  
>  Regards  
>  Peter
> 
> Ignored

Hi Peter,  
  
I watched whole day and try to find repaint arrow,the result is none.  
  
When you give me this EA, you mentioned the signal generated at the close of the bar.I did not pay attention to what you say then.Today I understand what does it mean.  
  
Obviously this is not good for trading purpose.and the today 4hr CHF chart sell arrow comes out 1.1449 but the sell position opened after the next candle break out the low of the previous candle at 1.1338.also that's 3.5 hrs later opened this position.And the today's projected maximum low is 1.1309.So As a programmer you could see something wrong with this EA or it is not optimal. I have to tell everybody using this EA please make it optimal or do not use it.It will riun the profit.  
  
There is somebody here in this thread mentioned sometimes the entry and exit point is a bit far.I do not agree.Since we have already got a good indicator why shouldn't we have a good EA.  
  
This reminds me of some year's ago there is one person who talked to me online: people looking for fine things in life , that's an empty dream.This person played my best friend when he was talking to me as a role of an Expert Adviser. But behind me he also manupulated my situation to destroy me. His best skill is using different prople's name to do different things and nobody believe that's all done by one person.And he thought he played a smart role in life and dare not admit it.He said ' it is not me'.And He talked big and loud about integrity.  
  
This person did somethig good for me,I thought I want to know the other side of this person , I did a test . The person showed his teeth.Actually this person know me long time ago before contacting me.Because I am a sort of research target, they tried all means to keep me in the game.  
  
Ok just a story to have a fun. Are we a bit far from the entry of a good dream? or the exit is much nearer than the entry? when could we get a true and real Expert Adviser for a good dream? Or it is an empty dream? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#220](/thread/post/2647832#post2647832 "Post Permalink")

  * Edited 8:59am  Apr 3, 2009 2:59am | Edited 8:59am 

  * [ mitchp](mitchp)

  * | Joined Jul 2007  | Status: Trader | [262 Posts](/search?do=process&provider=Member&searchuser=44818)

Lyllia,   
  
I placed the EA on four charts: EU, GU, UJ, GJ on Tuesday night. When I awoke in the morning (6am CST) I was -$254 (.01 lots on a standard account). When I got home from work(6 pm CST) all of the lots had closed for -$258 and new lots had opened for +$138. This morning I looked at it again and I was +$749, so I closed out half of each position and let the rest ride. So from since Tuesday night I have a profit of $124 (give or take) and I'm in positive pips with my current trades.  
  
I will keep reporting.  
  
Thanks  
Mitch  
  
  
Ok, it's 7:00pm (CST) and my account is at +$500. The only bad part is the the EA opened a sell on EU at 1.3215. It did go down to 1.3192 but then a bar later a buy signal appeared (up arrow) but the EA did not close me out of the sell and open a buy. If it did I would have seen a profit of 225 pips (ouch). Not sure why it did work on that pair. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#221](/thread/post/2648540#post2648540 "Post Permalink")

  * Apr 3, 2009 9:40am  Apr 3, 2009 9:40am 

  * [ ataviano](ataviano)

  * | Joined Feb 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=60944)

> [Quoting lyllia](/thread/post/2643523#post2643523 "View Quoted Post")
> 
> Disliked
> 
> Somebody told me repaint means they are not stable ,move or disappear.  
>    
>  I could confirm that they are stable,once they come out ,they remain.  
>    
>  If there are more than one arrow appear in one time frame,in EA trading which means sevral positions opened,then the first opposite singal close them all.
> 
> Ignored

hi lillya ,   
believ in ur dream and you'll definitely get there.  
Ps. i demo traded only the arrows manually today and they seemed to give good result. I was shooting at anything between 15-20 pips 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#222](/thread/post/2648663#post2648663 "Post Permalink")

  * Apr 3, 2009 10:56am  Apr 3, 2009 10:56am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

a little problem here.I will attache two 4hr chart of ENZD in this page and next page.you will see the difference and could you guys give me the reason.In this chart there is a buy and sell signal.Buy singal at 2.3317 and then was cancelled at 2.2854.Five figues apart.is it rediculous?This Chart trading with EA. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: enzd 4hr.gif
Size: 24 KB](/attachment/image/228160/thumbnail?d=1365567054)](/attachment/image/228160?d=1238723771)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#223](/thread/post/2648680#post2648680 "Post Permalink")

  * Apr 3, 2009 11:05am  Apr 3, 2009 11:05am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

this chart same as above,but it from my live account.There is no buy and sell signals at all after the last sell arrow appears at 2.375 area.Which means the trend has been keeping continuing.Could you guys tell me why the same chart but different result? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: enzd 4hr.gif
Size: 24 KB](/attachment/image/228165/thumbnail?d=1365567054)](/attachment/image/228165?d=1238724316)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#224](/thread/post/2648689#post2648689 "Post Permalink")

  * Apr 3, 2009 11:09am  Apr 3, 2009 11:09am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

So I would say if you do manual trading with the arrow ,it is much safer.  
  
Only use this EA for testing purpose and a reference for live account trading. Until this EA problem could be solved. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#225](/thread/post/2649054#post2649054 "Post Permalink")

  * Apr 3, 2009 3:13pm  Apr 3, 2009 3:13pm 

  * [ ataviano](ataviano)

  * | Joined Feb 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=60944)

> [Quoting lyllia](/thread/post/2648689#post2648689 "View Quoted Post")
> 
> Disliked
> 
> So I would say if you do manual trading with the arrow ,it is much safer.  
>    
>  Only use this EA for testing purpose and a reference for live account trading. Until this EA problem could be solved.
> 
> Ignored

Hi Lillya  
How many pips do you make on average per day with this system(manually) and how many pairs do trade?   
Thanx it looks promising 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#226](/thread/post/2649441#post2649441 "Post Permalink")

  * Edited 7:23pm  Apr 3, 2009 7:01pm | Edited 7:23pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting ataviano](/thread/post/2649054#post2649054 "View Quoted Post")
> 
> Disliked
> 
> Hi Lillya  
>  How many pips do you make on average per day with this system(manually) and how many pairs do trade?   
>  Thanx it looks promising
> 
> Ignored

this system could work well on trending period.not side way period.it eats profit.For example,this morning asian session there is sell signal on euro.aud and also the cross.All in money .but you have to manually closed the position and lock in the profit. Then they go up again during european session there is buy signal appear at 8.pm sydney time that's 70 pips up for AUD until now 50 minutes past no position open. I got two conclusion:  
  
1\. This EA still depends on bar breaking out principle. that's the reason why there is buy arrow appearing but no position opened. But for higher time frame position will be opened a bit far away from the time arrow appears.Because the bigger the time frame , the larger the candle length, the far away the position will be opened.  
  
2.In sideway period no matter which time frame if they cancel each other all the time, the chance that making profit is very narrow. That will frustrate trader .So in such a market you have to help it manually closed the position. Now I realize that depending on arrows themselve to self-fulfil their own positions is just a dream.   
  
I still insist that this arrow is reliable.Tradable manually.If anybody have suggestion to improve it ,please give us your opinion here. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#227](/thread/post/2649474#post2649474 "Post Permalink")

  * Apr 3, 2009 7:19pm  Apr 3, 2009 7:19pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I have to be fair with this EA,it is based on good principle:Break out system.I appreciate Pitpiter's help.  
  
I am too greedy and ambitious.Always want something perfect. If there is a kind of way that will make arrows working more efficiently.That would be good. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#228](/thread/post/2650111#post2650111 "Post Permalink")

  * Apr 4, 2009 12:34am  Apr 4, 2009 12:34am 

  * [ lang48](lang48)

  * | Joined Jan 2008  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=59429)

hi lyllia  
  
started your system manually and ea demo. thks. may be ronald raygun is able to make another ea to try. where you are ronald? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#229](/thread/post/2650303#post2650303 "Post Permalink")

  * Edited 4:17am  Apr 4, 2009 2:30am | Edited 4:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83209_5.gif) pitpiter](pitpiter)

  * | Joined Oct 2008  | Status: Trader | [300 Posts](/search?do=process&provider=Member&searchuser=83209)

Hi everybody.  
I run EA on 8 pairs three days ago and it work good , I find just one place , when EA do not open trades on two pairs (GU and GY) in the same time it open trade on NU , it's marked on pic with red vertical line . I think it was problem with communication between terminal and brokers server . I fix problem and will test next week , if it will solwd I will put here new version.   
Regards  
Peter  
EDIT   
Sorry , It was not opened trades on 3 pairs , EG too , but in the same time 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#230](/thread/post/2650308#post2650308 "Post Permalink")

  * Apr 4, 2009 2:32am  Apr 4, 2009 2:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83209_5.gif) pitpiter](pitpiter)

  * | Joined Oct 2008  | Status: Trader | [300 Posts](/search?do=process&provider=Member&searchuser=83209)

Sorry , here is pic 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: ea.gif
Size: 79 KB](/attachment/image/228520/thumbnail?d=1365567141)](/attachment/image/228520?d=1238779922)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#231](/thread/post/2650350#post2650350 "Post Permalink")

  * Apr 4, 2009 2:52am  Apr 4, 2009 2:52am 

  * [ VenomDraC](venomdrac)

  * | Joined Feb 2009  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=95060)

> [Quoting lyllia](/thread/post/2635401#post2635401 "View Quoted Post")
> 
> Disliked
> 
> aud weekly,daily,4hrs
> 
> Ignored

Dear Lyllia,  
  
I must said, your indicator is the best i have found so far, its marvellous, i used it on 1 M TF during EST time, works marvellous on EURUSD. I have downloaded all the attachment provided but i cany get the bowling ball with number out, i have been searching it for months, i know that is one of the best indi, can you please email them to me, hope it is fine with you.. Thanx  
  
my email : [venomdrac@yahoo.co.uk](mailto:venomdrac@yahoo.co.uk)  
  
DraC 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#232](/thread/post/2650388#post2650388 "Post Permalink")

  * Edited 4:13am  Apr 4, 2009 3:21am | Edited 4:13am 

  * [ Mandl2007](mandl2007)

  * | Membership Revoked  | Joined Nov 2008 | [279 Posts](/search?do=process&provider=Member&searchuser=86165)

... or could you post this indi for all of us ? ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#233](/thread/post/2650466#post2650466 "Post Permalink")

  * Apr 4, 2009 4:18am  Apr 4, 2009 4:18am 

  * [ VenomDraC](venomdrac)

  * | Joined Feb 2009  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=95060)

> [Quoting Oksana17](/thread/post/2636420#post2636420 "View Quoted Post")
> 
> Disliked
> 
> Did anyone get luck in backtesting?
> 
> Ignored

i did... works marvellous.. just follow the arrows.. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) please see attached results. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: mzfx - llya.gif
Size: 61 KB](/attachment/image/228551/thumbnail?d=1365567141)](/attachment/image/228551?d=1238786055)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#234](/thread/post/2650635#post2650635 "Post Permalink")

  * Apr 4, 2009 6:28am  Apr 4, 2009 6:28am 

  * [ jgadefelth](jgadefelth)

  * | Joined Jan 2008  | Status: Trillion Dollar Man | [1,495 Posts](/search?do=process&provider=Member&searchuser=58861)

[VenomDraC](http://www.forexfactory.com/member.php?u=95060)   
Member  
Everyone else but you almost say it repaints badly and especiall y on timeframes lower than 4h. Repaints means the indicator change after it have an arrow after some time it moves the arrow so it will not be at the same place where it was the first time do you understand this and if so what have you done to prevent it if you think it is a great indicator ?   
  
  
best regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#235](/thread/post/2650671#post2650671 "Post Permalink")

  * Apr 4, 2009 6:54am  Apr 4, 2009 6:54am 

  * [ ataviano](ataviano)

  * | Joined Feb 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=60944)

hi lillya where is the Bowling balls Indicator? Post it here for all.  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#236](/thread/post/2650698#post2650698 "Post Permalink")

  * Apr 4, 2009 7:21am  Apr 4, 2009 7:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar43332_2.gif) willmalou](willmalou)

  * | Joined Jul 2007  | Status: Think before you act!!! | [113 Posts](/search?do=process&provider=Member&searchuser=43332)

> [Quoting pitpiter](/thread/post/2650308#post2650308 "View Quoted Post")
> 
> Disliked
> 
> Sorry , here is pic
> 
> Ignored

Pitpiter can you have and option for the ea to trade tickmode. That way it will take trades as soon as the arrow appears. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#237](/thread/post/2650737#post2650737 "Post Permalink")

  * Apr 4, 2009 8:20am  Apr 4, 2009 8:20am 

  * [ mitchp](mitchp)

  * | Joined Jul 2007  | Status: Trader | [262 Posts](/search?do=process&provider=Member&searchuser=44818)

I normally wouldn't trade today, but I decided to close out all of my trades this morning (all in profit) and let the EA run (4hr charts). At end of day I have 4 open trades in profit for $88.00. I'll take that anyday!  
  
Mitch 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#238](/thread/post/2650851#post2650851 "Post Permalink")

  * Apr 4, 2009 1:09pm  Apr 4, 2009 1:09pm 

  * [ preawansyah](preawansyah)

  * | Additional Username  | Joined Jan 2009 | [17 Posts](/search?do=process&provider=Member&searchuser=90826)

IF The INDICATOR/ARROW can work at H4 TF, Why Not We just use it at 4H TF then? I use it to trade manually and could make money even though in demo. Will be on live immediately. Let's trade due to the signal asking us to trade rather than our emotion saying to trade.  
  
Whatever Lyllia has put here is very fantastic, and let's improve it rather than we keep complaining. Cheers  
  
Lyllia and friends.... Thanks much for your hard work 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#239](/thread/post/2650859#post2650859 "Post Permalink")

  * Edited 2:29pm  Apr 4, 2009 1:39pm | Edited 2:29pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting VenomDraC](/thread/post/2650350#post2650350 "View Quoted Post")
> 
> Disliked
> 
> Dear Lyllia,  
>    
>  I must said, your indicator is the best i have found so far, its marvellous, i used it on 1 M TF during EST time, works marvellous on EURUSD. I have downloaded all the attachment provided but i cany get the bowling ball with number out, i have been searching it for months, i know that is one of the best indi, can you please email them to me, hope it is fine with you.. Thanx  
>    
>  my email : [venomdrac@yahoo.co.uk](mailto:venomdrac@yahoo.co.uk)  
>    
>  DraC
> 
> Ignored

Hi VenomDrac,  
  
Thanks! I couldn't say my indicator is the best.Actually it is not my indicator.I get it online and recommend it here.I would like everybody who have trouble with fx trading benifit from it. It is not perfect.Like some people found out that it has repaint problem.But according to my observation,very rare.So that's why I give it a 95 % seccessful rate. If we together do our best to perfect it,it will eventually become bowling ball indicator.But EA has to make it work flawless.That will save all the trader's trouble to look at the chart all day to pick up the position.Again I will thank Pitpiter for his efforts into this indicator's EA.  
  
I summerized its infinit potential for this indicator, based on the assumption:If it works flawless;  
  
  
1\. It picks up the peaks and bottoms on any time frame for any chart;  
2\. it save the trouble for trader to gauge the cycle,wave,OB,OS,fibonacci   
retracement/extention ect. parameters;  
3.it is a self-fufilled bowling ball indicator that combines all the merits of all   
the indicators and theory to trade in fx market or other other financial   
markets.  
  
If we could make it ,that's a big revolution of trading the fx market and it will change the life of all traders.  
  
So I hope everybody do your best to make a contribution to this trading system.To make it working perfect.  
  
In order to achieve this:we have to find out as much faulty points as possible to improve it.  
  
1\. Give us your observation here;  
2\. make suggestion;  
3\. if you are experienced trader,financial modelling person and   
programmer.please give this indicator a hand to to make it perfect to work   
for traders. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#240](/thread/post/2650883#post2650883 "Post Permalink")

  * Apr 4, 2009 2:36pm  Apr 4, 2009 2:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar92630_2.gif) abhilash](abhilash)

  * | Joined Jan 2009  | Status: Trader | [198 Posts](/search?do=process&provider=Member&searchuser=92630)

Helo I'am not getting the Buy and sell arrow .Somebody help me.What should i do .Here is my chart 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 01.gif
Size: 23 KB](/attachment/image/228646/thumbnail?d=1365567173)](/attachment/image/228646?d=1238823342)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#241](/thread/post/2650888#post2650888 "Post Permalink")

  * Apr 4, 2009 2:52pm  Apr 4, 2009 2:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar92630_2.gif) abhilash](abhilash)

  * | Joined Jan 2009  | Status: Trader | [198 Posts](/search?do=process&provider=Member&searchuser=92630)

Hii lyllia ,Should i follow the arrows or the dot ?what is the dot for? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#242](/thread/post/2650891#post2650891 "Post Permalink")

  * Apr 4, 2009 3:01pm  Apr 4, 2009 3:01pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting abhilash](/thread/post/2650883#post2650883 "View Quoted Post")
> 
> Disliked
> 
> Helo I'am not getting the Buy and sell arrow .Somebody help me.What should i do .Here is my chart
> 
> Ignored

Have you download all the indicators?Please go to the first few pages to download them and it is better you go through all the posts with this thread. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#243](/thread/post/2650893#post2650893 "Post Permalink")

  * Apr 4, 2009 3:02pm  Apr 4, 2009 3:02pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting abhilash](/thread/post/2650888#post2650888 "View Quoted Post")
> 
> Disliked
> 
> Hii lyllia ,Should i follow the arrows or the dot ?what is the dot for?
> 
> Ignored

the arrow not the dot.the dot give you the possibility. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#244](/thread/post/2651105#post2651105 "Post Permalink")

  * Apr 5, 2009 12:36am  Apr 5, 2009 12:36am 

  * [ preawansyah](preawansyah)

  * | Additional Username  | Joined Jan 2009 | [17 Posts](/search?do=process&provider=Member&searchuser=90826)

Great Work Pipiter and Lyllia... Keep doing good, and I thank you for wonderful Results that I have found out so far due to the EA and the Arrow Indicator. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#245](/thread/post/2651797#post2651797 "Post Permalink")

  * Apr 5, 2009 11:40pm  Apr 5, 2009 11:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83209_5.gif) pitpiter](pitpiter)

  * | Joined Oct 2008  | Status: Trader | [300 Posts](/search?do=process&provider=Member&searchuser=83209)

> [Quoting willmalou](/thread/post/2650698#post2650698 "View Quoted Post")
> 
> Disliked
> 
> Pitpiter can you have and option for the ea to trade tickmode. That way it will take trades as soon as the arrow appears.
> 
> Ignored

If I have observe indi applying on 5M chart , aways arrow appears after close bar and start next bar . If I'm wrong , please correct me . I tried make EA , which work on open bars value and it didn't opened any trade. As I said before I run EA on 8 pair and it opened all trades correctly with open price for next bar after bar when appear arrow. Now I propose wait on result working EA this week , if I sold problem , which I find - wrigt about in previouse post , I will post here new version for public testing.  
Regards  
Peter 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#246](/thread/post/2651918#post2651918 "Post Permalink")

  * Apr 6, 2009 2:01am  Apr 6, 2009 2:01am 

  * [ joes](joes)

  * | Joined Apr 2009  | Status: Trader | [29 Posts](/search?do=process&provider=Member&searchuser=98806)

Is It Possible To trade This System On 5 Min. Chart Manuley Just to Follow The Arroys It Looks Like Can Have A Lot Of Small Gains In Pips 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#247](/thread/post/2652000#post2652000 "Post Permalink")

  * Apr 6, 2009 3:30am  Apr 6, 2009 3:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar96656_4.gif) $aly]($aly)

  * | Commercial User  | Joined Mar 2009 | [183 Posts](/search?do=process&provider=Member&searchuser=96656)

> [Quoting joes](/thread/post/2651918#post2651918 "View Quoted Post")
> 
> Disliked
> 
> Is It Possible To trade This System On 5 Min. Chart Manuley Just to Follow The Arroys It Looks Like Can Have A Lot Of Small Gains In Pips
> 
> Ignored

Do it ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#248](/thread/post/2652009#post2652009 "Post Permalink")

  * Apr 6, 2009 3:41am  Apr 6, 2009 3:41am 

  * [ joes](joes)

  * | Joined Apr 2009  | Status: Trader | [29 Posts](/search?do=process&provider=Member&searchuser=98806)

> [Quoting $aly](/thread/post/2652000#post2652000 "View Quoted Post")
> 
> Disliked
> 
> Do it ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)
> 
> Ignored

Did You Try Thate? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#249](/thread/post/2652011#post2652011 "Post Permalink")

  * Apr 6, 2009 3:42am  Apr 6, 2009 3:42am 

  * [ joes](joes)

  * | Joined Apr 2009  | Status: Trader | [29 Posts](/search?do=process&provider=Member&searchuser=98806)

When Are The Arrows Forming At The Open Of The Bar Or Diffrent Time? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#250](/thread/post/2652017#post2652017 "Post Permalink")

  * Apr 6, 2009 3:51am  Apr 6, 2009 3:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar96656_4.gif) $aly]($aly)

  * | Commercial User  | Joined Mar 2009 | [183 Posts](/search?do=process&provider=Member&searchuser=96656)

> [Quoting joes](/thread/post/2652009#post2652009 "View Quoted Post")
> 
> Disliked
> 
> Did You Try Thate?
> 
> Ignored

yeah it seems very nice but Fisher is a repaint indicator and arrows appear at the end of bolish or bearish candle on the next candle i got 20 pips and lost 55pips in M5 in live account....

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#251](/thread/post/2652233#post2652233 "Post Permalink")

  * Apr 6, 2009 6:48am  Apr 6, 2009 6:48am 

  * [ perjo](perjo)

  * | Joined Nov 2008  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=86171)

hello Lyllia,  
  
first i want to thanks you for sharing the system.Then i have a question about ABHA center... how do you use this indicator? have you seen that if you just follow this indicator you have very big winner trade? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#252](/thread/post/2652299#post2652299 "Post Permalink")

  * Apr 6, 2009 7:58am  Apr 6, 2009 7:58am 

  * [ eforex3](eforex3)

  * | Joined Dec 2007  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=56139)

does this indi repaint? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#253](/thread/post/2652458#post2652458 "Post Permalink")

  * Apr 6, 2009 10:53am  Apr 6, 2009 10:53am 

  * [ mitchp](mitchp)

  * | Joined Jul 2007  | Status: Trader | [262 Posts](/search?do=process&provider=Member&searchuser=44818)

From Friday I had 4 open trades taken by the EA, positive $88. It's now almost 9pm and my trades are up to $428. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#254](/thread/post/2652563#post2652563 "Post Permalink")

  * Apr 6, 2009 11:52am  Apr 6, 2009 11:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar24851_3.gif) hayseed](hayseed)

  * Joined Nov 2006 | Status: Trader | [4,150 Posts](/search?do=process&provider=Member&searchuser=24851)

not tryin to change anything here but to be money reliable, the iinwmarrows needs to be rewritten slightly..... just slightly....  
  
also, small period ma cross systems can whack you pretty good unless filtered.... a filtering in this case would be taking buys only when a slower ma on a couple higher time frames supports the trade....  
  
as example, using the 15 minute chart, take every 3 ma coss buy but only when the 6 period ma's are confirming the buy on the 4 hour and daily charts....   
  
breakevens and trailing stops using lot weighted _average price_ might help to a small degree.... a total profit target would be a definite plus.....  
  
using small lots on small timeframes gives the action so often desired while the higher timeframes keep some reality......  
  
the charts included are lyllia's 3 ma cross system with sole exceptions of the 4 hour and day filters.... some losses are unavoidable.......h 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: llia1.gif
Size: 35 KB](/attachment/image/229133/thumbnail?d=1365567270)](/attachment/image/229133?d=1238986323)   
[![Click to Enlarge

Name: llia4.gif
Size: 40 KB](/attachment/image/229134/thumbnail?d=1365567270)](/attachment/image/229134?d=1238986323)   

to trade and code, keep both simple... no call to impress....h

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#255](/thread/post/2652667#post2652667 "Post Permalink")

  * Apr 6, 2009 1:04pm  Apr 6, 2009 1:04pm 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

The IINWMARROWS indicator does repaint!! I followed it all last week when an arrow appears showing either a reverse in trend or a continue in trend if the next candle goes the other way the arrow will disappear, if that fails the arrow will appear again. Sometimes it does not show on the chart unless you restart the platform or reload the indicator then you will see the repaint. I have the screen shots to prove it, as well as the back test that shows trades where arrows were painted but do not show on chart now.  
  
All of that being said I still think there may be something here, but I think the method used now will only work in trending markets like now (well sort of) but when you have range bound weeks arrows will be repainting like crazy but you still may able to pick up some pips if you do not wait for exit arrows. I will continue to watch and maybe pick up a trade or two but in no way do I think its near 95% success, sure if you look at a chart it seems that way but its hind sight 20/20 repaint thing its not possible unless you have a time machine, the only thing that is 95% success rate of is them blowing your account sooner or later.   
  
My 1 cent  
Have to save other cent 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#256](/thread/post/2653164#post2653164 "Post Permalink")

  * Apr 6, 2009 7:16pm  Apr 6, 2009 7:16pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting perjo](/thread/post/2652233#post2652233 "View Quoted Post")
> 
> Disliked
> 
> hello Lyllia,  
>    
>  first i want to thanks you for sharing the system.Then i have a question about ABHA center... how do you use this indicator? have you seen that if you just follow this indicator you have very big winner trade?
> 
> Ignored

Hi guys,  
  
Thanks for help.   
  
Like I said before for this system we focus on the arrow trading.Because it is more reliable than other indicators. It seldom repaint if it does repaint. Still give us good pips. I focus on 4 hr's trading because the trend could last longer and could produce more pips.Save us the time busy with more small trades with more risk.  
  
I use arrow for trading;  
  
Use other indicators as reference to confirm:  
the wave:3 levl zz;  
the cycle:Rads MACD, fisher & ABHA.(they do repaint but they help);  
the possibility:beginer alert;  
the OB & OS: Pivots.  
  
I hope after use this system for a while,you will learn to develope yor own logic.  
  
For day trading pivots are important to me .Once the OB & OS level has been reached,the arrow comes in to tell you to trade. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#257](/thread/post/2653180#post2653180 "Post Permalink")

  * Apr 6, 2009 7:34pm  Apr 6, 2009 7:34pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Weekly & Daily  
  
Euro 1.4187-1.2715, 1.3651-1.3294;  
  
Gbp 1.5732-1.3775, 1.5059-1.4568;  
  
Chf 1.1713-1.0973, 1.1438-1.1215;  
  
JPY 105.6-94.32, 101.87-98.64;  
  
Aud 0.7631-0.6590, 0.7290-0.7016;  
  
Nzd 0.6099-0.5678 , 0.5966-0.5747;  
  
Cad 1.2882-1.1843, 1.2503-1.2153; 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#258](/thread/post/2653195#post2653195 "Post Permalink")

  * Apr 6, 2009 7:47pm  Apr 6, 2009 7:47pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting abhilash](/thread/post/2650883#post2650883 "View Quoted Post")
> 
> Disliked
> 
> Helo I'am not getting the Buy and sell arrow .Somebody help me.What should i do .Here is my chart
> 
> Ignored

Did you download all the indicator? read first several page then you are able to do it properly. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#259](/thread/post/2653210#post2653210 "Post Permalink")

  * Apr 6, 2009 7:59pm  Apr 6, 2009 7:59pm 

  * [ shapitt09](shapitt09)

  * | Joined Mar 2009  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=98294)

Hi Lyllia.. are you used an EA in real trading? do you make more profit or lost since you use it? thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#260](/thread/post/2653259#post2653259 "Post Permalink")

  * Apr 6, 2009 8:32pm  Apr 6, 2009 8:32pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I do not recomment EA for live trading. We still struggle with EA testing. all the problems are discussed in the thread. I hope people could help to solved the problem and make it work.Please read the thread. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#261](/thread/post/2653369#post2653369 "Post Permalink")

  * Apr 6, 2009 9:29pm  Apr 6, 2009 9:29pm 

  * [ lang48](lang48)

  * | Joined Jan 2008  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=59429)

hi lyllia  
seems that your method and ea both work well on H4. i use shi channel mtf as support and resistance. thanks 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [SHI_Channel_MTF.ex4](/attachment/file/229340?d=1239020920) 10 KB | 449 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#262](/thread/post/2653372#post2653372 "Post Permalink")

  * Apr 6, 2009 9:31pm  Apr 6, 2009 9:31pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting hayseed](/thread/post/2652563#post2652563 "View Quoted Post")
> 
> Disliked
> 
> not tryin to change anything here but to be money reliable, the iinwmarrows needs to be rewritten slightly..... just slightly....  
>    
>  also, small period ma cross systems can whack you pretty good unless filtered.... a filtering in this case would be taking buys only when a slower ma on a couple higher time frames supports the trade....  
>    
>  as example, using the 15 minute chart, take every 3 ma coss buy but only when the 6 period ma's are confirming the buy on the 4 hour and daily charts....   
>    
>  breakevens and trailing stops using lot weighted [i]average...
> 
> Ignored

Thank you!  
  
Could you help to make tthis arrow more reliable? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#263](/thread/post/2653377#post2653377 "Post Permalink")

  * Apr 6, 2009 9:33pm  Apr 6, 2009 9:33pm 

  * [ senbanda](senbanda)

  * | Joined Nov 2005  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=4325)

Hi Lyllia  
Thanks for your great method. I have a small Q.   
When a thick red line occurs in Abha in H4 is it a trend change?  
Thanking in advance  
Senbanda 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#264](/thread/post/2653401#post2653401 "Post Permalink")

  * Apr 6, 2009 9:42pm  Apr 6, 2009 9:42pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lang48](/thread/post/2653369#post2653369 "View Quoted Post")
> 
> Disliked
> 
> hi lyllia  
>  seems that your method and ea both work well on H4. i use shi channel mtf as support and resistance. thanks
> 
> Ignored

have you got pips from 4hr trading start from NY session? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#265](/thread/post/2653402#post2653402 "Post Permalink")

  * Apr 6, 2009 9:44pm  Apr 6, 2009 9:44pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting senbanda](/thread/post/2653377#post2653377 "View Quoted Post")
> 
> Disliked
> 
> Hi Lyllia  
>  Thanks for your great method. I have a small Q.   
>  When a thick red line occurs in Abha in H4 is it a trend change?  
>  Thanking in advance  
>  Senbanda
> 
> Ignored

it indicate a possible cycle low or high in that TF is in place.But sometime it repaint with PA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#266](/thread/post/2653430#post2653430 "Post Permalink")

  * Apr 6, 2009 9:55pm  Apr 6, 2009 9:55pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lang48](/thread/post/2653369#post2653369 "View Quoted Post")
> 
> Disliked
> 
> hi lyllia  
>  seems that your method and ea both work well on H4. i use shi channel mtf as support and resistance. thanks
> 
> Ignored

Thanks for your indicator,is it solid? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#267](/thread/post/2653432#post2653432 "Post Permalink")

  * Apr 6, 2009 9:56pm  Apr 6, 2009 9:56pm 

  * [ lang48](lang48)

  * | Joined Jan 2008  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=59429)

> [Quoting lyllia](/thread/post/2653401#post2653401 "View Quoted Post")
> 
> Disliked
> 
> have you got pips from 4hr trading start from NY session?
> 
> Ignored

hi  
5 usd pairs opened around midday gmt now 170 pips plus (not yet closed) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#268](/thread/post/2653444#post2653444 "Post Permalink")

  * Apr 6, 2009 9:59pm  Apr 6, 2009 9:59pm 

  * [ senbanda](senbanda)

  * | Joined Nov 2005  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=4325)

Thank you Lyllia  
I will monitor it more  
Senbanda 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#269](/thread/post/2653452#post2653452 "Post Permalink")

  * Apr 6, 2009 10:02pm  Apr 6, 2009 10:02pm 

  * [ lang48](lang48)

  * | Joined Jan 2008  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=59429)

> [Quoting lyllia](/thread/post/2653430#post2653430 "View Quoted Post")
> 
> Disliked
> 
> Thanks for your indicator,is it solid?
> 
> Ignored

do not know yet, i have only 4 hours experience with this indicator. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#270](/thread/post/2653463#post2653463 "Post Permalink")

  * Apr 6, 2009 10:08pm  Apr 6, 2009 10:08pm 

  * [ lang48](lang48)

  * | Joined Jan 2008  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=59429)

one more 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [SHI_Channel_MTF_Mod.mq4](/attachment/file/229356?d=1239023313) 7 KB | 473 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#271](/thread/post/2653548#post2653548 "Post Permalink")

  * Apr 6, 2009 10:52pm  Apr 6, 2009 10:52pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lang48](/thread/post/2653463#post2653463 "View Quoted Post")
> 
> Disliked
> 
> one more
> 
> Ignored

are you a programmer?  
  
what's the diffrence between MTF indicator and normal mt4 indicators?tia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#272](/thread/post/2653577#post2653577 "Post Permalink")

  * Apr 6, 2009 11:03pm  Apr 6, 2009 11:03pm 

  * [ lang48](lang48)

  * | Joined Jan 2008  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=59429)

> [Quoting lyllia](/thread/post/2653548#post2653548 "View Quoted Post")
> 
> Disliked
> 
> are you a programmer?  
>    
>  what's the diffrence between MTF indicator and normal mt4 indicators?tia
> 
> Ignored

hi  
i am not programmer and i just found them this morning from FF forum and now trying myself to understand the difference. but i found them very useful to find support and resistance levels. for example put on H4 chart shi indicator with timeframe value 60 and another indicator with timeframe value 240 and this is some kind of filter for arrows (in case of manual trading). timeframe value 0 works on any timeframe according to this timefame. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#273](/thread/post/2653598#post2653598 "Post Permalink")

  * Apr 6, 2009 11:12pm  Apr 6, 2009 11:12pm 

  * [ lang48](lang48)

  * | Joined Jan 2008  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=59429)

hi lyllia  
  
todays trade with ea 5 usd pairs approx. 350 pips plus closed, 330 plus still opened. with todays market movement your method works well. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#274](/thread/post/2653613#post2653613 "Post Permalink")

  * Apr 6, 2009 11:18pm  Apr 6, 2009 11:18pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Do you use both indicators on the same 4 hr chart with different value 60 and 240? could not understand what do you mean? Do you mean you put shi mft on 1hr chart and shi mod on 4hr chart? I have not try them yet.Could you explain the difference or post your chart here. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#275](/thread/post/2653649#post2653649 "Post Permalink")

  * Apr 6, 2009 11:31pm  Apr 6, 2009 11:31pm 

  * [ lang48](lang48)

  * | Joined Jan 2008  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=59429)

> [Quoting lyllia](/thread/post/2653613#post2653613 "View Quoted Post")
> 
> Disliked
> 
> Do you use both indicators on the same 4 hr chart with different value 60 and 240? could not understand what do you mean? Do you mean you put shi mft on 1hr chart and shi mod on 4hr chart? I have not try them yet.Could you explain the difference or post your chart here.
> 
> Ignored

i put on H4 chart first shi indicator with timeframe value 60 and second shi indicator with timframe value 240 (if you like you may add third shi with 1440 daily value). then you can see 4 hours trend and inside 1 hour trend on your chart. sr levels are channel borders and center line. for example where H1 channel crosses H4 channel there is very strong sr level. it makes trading more simple. if you see arrow appears but this trade goes against the trend you can drop this trade and wait for next. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#276](/thread/post/2653663#post2653663 "Post Permalink")

  * Edited 11:52pm  Apr 6, 2009 11:37pm | Edited 11:52pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

It is working well in trending market.The good thing is it catches the trend from very begining.But not working so good in congestion area ,especially in small time frame.when we do manual trading,we have choice to choose when to trade.But working with EA, it is not that simple.  
  
When the position opened so late after the arrow appears, the position might be against you. With manaul trading there is no such a problem.As soon as the arrow appears, I could open the positions.  
  
Today I did not trade,cause my broker's server has problem,they have to redirect clients to other server which only allow clients to log in no more than 2 minutes,then disconnect it.It is all manupulated.  
  
I trade mony years ago,some brokers use this kind of method to do their own good.They make it like accident. In another word,the accident is not real.That's the way how they could benifit themselve by taking advantage of the client.So choose broker like choosing friend,if you go with the wrong one,you always get trouble.And they do this ruthless.They keep talking to you as if they provid good service to help you passing the time.At the same time they are using your money and method to make money for themselves.  
And they pretend to pity you. And you know what one of them is my best friend I talked about in my little story I posted before.They are not really your friends.They pretend to be, to keep you in the game. They play the game : who is the best cheater who could beat all other people to satisfy themselves. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#277](/thread/post/2653665#post2653665 "Post Permalink")

  * Apr 6, 2009 11:39pm  Apr 6, 2009 11:39pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lang48](/thread/post/2653649#post2653649 "View Quoted Post")
> 
> Disliked
> 
> i put on H4 chart first shi indicator with timeframe value 60 and second shi indicator with timframe value 240 (if you like you may add third shi with 1440 daily value). then you can see 4 hours trend and inside 1 hour trend on your chart. sr levels are channel borders and center line. for example where H1 channel crosses H4 channel there is very strong sr level. it makes trading more simple. if you see arrow appears but this trade goes against the trend you can drop this trade and wait for next.
> 
> Ignored

thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#278](/thread/post/2653677#post2653677 "Post Permalink")

  * Apr 6, 2009 11:44pm  Apr 6, 2009 11:44pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

did you see what I post about S & R ? it seems they will getting there.After they reach the weekly S & R, there will be big move ahead. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#279](/thread/post/2653680#post2653680 "Post Permalink")

  * Apr 6, 2009 11:46pm  Apr 6, 2009 11:46pm 

  * [ lang48](lang48)

  * | Joined Jan 2008  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=59429)

good system for manual trading on H4. ea trading is now 550 pips plus still opened. thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#280](/thread/post/2653773#post2653773 "Post Permalink")

  * Apr 7, 2009 12:21am  Apr 7, 2009 12:21am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lang48](/thread/post/2653680#post2653680 "View Quoted Post")
> 
> Disliked
> 
> good system for manual trading on H4. ea trading is now 550 pips plus still opened. thanks
> 
> Ignored

I saw you tried many system here.Could you recommend your favorite one so far pleas ?(do not include this one ). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#281](/thread/post/2653869#post2653869 "Post Permalink")

  * Apr 7, 2009 12:59am  Apr 7, 2009 12:59am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lang48](/thread/post/2653649#post2653649 "View Quoted Post")
> 
> Disliked
> 
> i put on H4 chart first shi indicator with timeframe value 60 and second shi indicator with timframe value 240 (if you like you may add third shi with 1440 daily value). then you can see 4 hours trend and inside 1 hour trend on your chart. sr levels are channel borders and center line. for example where H1 channel crosses H4 channel there is very strong sr level. it makes trading more simple. if you see arrow appears but this trade goes against the trend you can drop this trade and wait for next.
> 
> Ignored

I did what you said, but only shi mode appear on 4h,shi mft with 60 and 1440 value do not appear.what's the reason. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#282](/thread/post/2653971#post2653971 "Post Permalink")

  * Apr 7, 2009 1:40am  Apr 7, 2009 1:40am 

  * [ VenomDraC](venomdrac)

  * | Joined Feb 2009  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=95060)

Hi Lyllia,  
  
Can all of us here have the bowling ball indicator, tried the inmarrows today on the H4 chart, results were not that good compared to last week where i concentrated more on 15 M TF and 1 H TF, today the sell arrow on H4 TF appeared when market has started to go against me ( meaning i was still having buy position and waiting for the sell arrow to appear for me to close the buy position, when it started to go short the sell arrow did not appear, the sell arrow appeared after 2 hours of waiting.) left no choice but to hedge them.  
  
The bowling ball indicator instead is one of the finest, it tells us to standby when to get out from your position by number 1,2 or 3, so if number 3 comes out, it is the best time to close your position and wait for the buy or sell arrow to come out. This way it is safer, i dont have to close my position when the market has started to go against me.  
  
Please let us all have your bowling ball indicator, you will be blessed heaven and earth.![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)   
  
DraC 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#283](/thread/post/2654018#post2654018 "Post Permalink")

  * Edited 3:52am  Apr 7, 2009 1:57am | Edited 3:52am 

  * [ Mandl2007](mandl2007)

  * | Membership Revoked  | Joined Nov 2008 | [279 Posts](/search?do=process&provider=Member&searchuser=86165)

Looking onto Lyllias charts it seems to me the so called "ball indicator" may be the "ZZ semafor" ? Try to find it out in the "tsd" Forum - this forum contains a lot of modern (and older) useful indis. This forum houses a lot of programmers too. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#284](/thread/post/2654106#post2654106 "Post Permalink")

  * Apr 7, 2009 2:28am  Apr 7, 2009 2:28am 

  * [ lang48](lang48)

  * | Joined Jan 2008  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=59429)

> [Quoting lyllia](/thread/post/2653869#post2653869 "View Quoted Post")
> 
> Disliked
> 
> I did what you said, but only shi mode appear on 4h,shi mft with 60 and 1440 value do not appear.what's the reason.
> 
> Ignored

i do not know what is reason. you have to put on one chart three shi indicators each with different timeframe value: first with value 60, second with 240, third with 1440. try again. regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#285](/thread/post/2654222#post2654222 "Post Permalink")

  * Apr 7, 2009 3:17am  Apr 7, 2009 3:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar24851_3.gif) hayseed](hayseed)

  * Joined Nov 2006 | Status: Trader | [4,150 Posts](/search?do=process&provider=Member&searchuser=24851)

> [Quoting lyllia](/thread/post/2653372#post2653372 "View Quoted Post")
> 
> Disliked
> 
> Thank you!  
>    
>  Could you help to make tthis arrow more reliable?
> 
> Ignored

  
removing the forward looking code reduces it to the standard ma cross indicator..... also including **< = **and **> =** in the appropriate places strenghtens the logic.....  
  
keep in mind your settings for the 2 ma's ..... they are so close to being identical that sometimes the micro differences will be missed....h 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: no repaint.gif
Size: 28 KB](/attachment/image/229535/thumbnail?d=1365567351)](/attachment/image/229535?d=1239041821)   

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [arrows no repaint.mq4](/attachment/file/229536?d=1239041821) 4 KB | 3,146 downloads 

to trade and code, keep both simple... no call to impress....h

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#286](/thread/post/2654242#post2654242 "Post Permalink")

  * Apr 7, 2009 3:25am  Apr 7, 2009 3:25am 

  * [ VenomDraC](venomdrac)

  * | Joined Feb 2009  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=95060)

> [Quoting Mandl2007](/thread/post/2654018#post2654018 "View Quoted Post")
> 
> Disliked
> 
> Looking onto Lyllias charts it seems to me the so called "ball indicator" may be the "ZZ semafor" ? Try to find it out in the "tsd" Forum - this forum contains a lot of modern (and older) useful indis. This forum is houses a lot of programmers too.
> 
> Ignored

Got it!! Thanx Mandl2007, may God Bless you always... and May the pips be with you!!![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Drac 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [3_Level_ZZ_Semafor.mq4](/attachment/file/229549?d=1239042253) 8 KB | 1,038 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#287](/thread/post/2654283#post2654283 "Post Permalink")

  * Apr 7, 2009 3:57am  Apr 7, 2009 3:57am 

  * [ jamesfr](jamesfr)

  * | Joined Mar 2009  | Status: Trader | [76 Posts](/search?do=process&provider=Member&searchuser=95609)

Can someone explain the zz indicator please?  
  
Thanks for the thread 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#288](/thread/post/2654351#post2654351 "Post Permalink")

  * Apr 7, 2009 4:39am  Apr 7, 2009 4:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar24851_3.gif) hayseed](hayseed)

  * Joined Nov 2006 | Status: Trader | [4,150 Posts](/search?do=process&provider=Member&searchuser=24851)

hey james..... the zz indicator is basically 3 separate zigzag's in one.... the typical zigzag lines are replaced by numbered dots....  
  
the dots are labled 1, 2 and 3.....   
  
if only 1 of the three zigzags turns at that point it's labeled 1.....  
  
if 2 zigzags turn at that point it's labeled 2.....   
  
if all three turn at the same point it's labeled 3......  
  
zigzag, as you likely know, uses hindsight.... h 

to trade and code, keep both simple... no call to impress....h

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#289](/thread/post/2654530#post2654530 "Post Permalink")

  * Apr 7, 2009 6:08am  Apr 7, 2009 6:08am 

  * [ jgadefelth](jgadefelth)

  * | Joined Jan 2008  | Status: Trillion Dollar Man | [1,495 Posts](/search?do=process&provider=Member&searchuser=58861)

hayseed is that indicator also repainting or is it usefull ?   
  
how do you trade it ?   
  
  
best regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#290](/thread/post/2654668#post2654668 "Post Permalink")

  * Apr 7, 2009 7:53am  Apr 7, 2009 7:53am 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

USD/JPY 4HR TF at 00:00 or 21:00 gmt the candle ended with a arrow at the bottom the pair then fell 15 pips, reloaded the platform now arrow is gone, if you were running EA for that pair it should have taken the trade. How do you handle this in real time?????

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#291](/thread/post/2654681#post2654681 "Post Permalink")

  * Apr 7, 2009 8:07am  Apr 7, 2009 8:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar24851_3.gif) hayseed](hayseed)

  * Joined Nov 2006 | Status: Trader | [4,150 Posts](/search?do=process&provider=Member&searchuser=24851)

hey jgadefelth..... yes it can at times repaint......   
  
if any indicator marks turning points with such precision , it's reasonably safe to assume it repaints.... but depending on your use, repainting is not neccessarily a negative.....   
  
one of the best ways to know for sure is to scan the code for terms like,   
  
**Low[Lowest** and **High[Highest** ... by definition they are subject to change.....h 

to trade and code, keep both simple... no call to impress....h

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#292](/thread/post/2654745#post2654745 "Post Permalink")

  * Apr 7, 2009 9:04am  Apr 7, 2009 9:04am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lang48](/thread/post/2654106#post2654106 "View Quoted Post")
> 
> Disliked
> 
> i do not know what is reason. you have to put on one chart three shi indicators each with different timeframe value: first with value 60, second with 240, third with 1440. try again. regards
> 
> Ignored

Thanks. I got it .They look logic. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#293](/thread/post/2654776#post2654776 "Post Permalink")

  * Apr 7, 2009 9:21am  Apr 7, 2009 9:21am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting hayseed](/thread/post/2654681#post2654681 "View Quoted Post")
> 
> Disliked
> 
> hey jgadefelth..... yes it can at times repaint......   
>    
>  if any indicator marks turning points with such precision , it's reasonably safe to assume it repaints.... but depending on your use, repainting is not neccessarily a negative.....   
>    
>  one of the best ways to know for sure is to scan the code for terms like,   
>    
>  **Low[Lowest** and **High[Highest** ... by definition they are subject to change.....h
> 
> Ignored

could you explain how to can the code with MT. I want to learn.If you are programmer could you please help to solve the repaint problem? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#294](/thread/post/2654787#post2654787 "Post Permalink")

  * Apr 7, 2009 9:31am  Apr 7, 2009 9:31am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting VenomDraC](/thread/post/2653971#post2653971 "View Quoted Post")
> 
> Disliked
> 
> Hi Lyllia,  
>    
>  Can all of us here have the bowling ball indicator, tried the inmarrows today on the H4 chart, results were not that good compared to last week where i concentrated more on 15 M TF and 1 H TF, today the sell arrow on H4 TF appeared when market has started to go against me ( meaning i was still having buy position and waiting for the sell arrow to appear for me to close the buy position, when it started to go short the sell arrow did not appear, the sell arrow appeared after 2 hours of waiting.) left no choice but to hedge them.  
>    
>    
>  Please let us all have your bowling ball indicator, you will be blessed heaven and earth.![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)   
>  The...
> 
> Ignored

Which pair the arrow on 4hr disappeared? I have many pairs turned around.All the arrows come out and stay.make fantastic trades.  
use 3 level zz at your own risk,it repaint all the time.I only use it as reference.And use arrow to confirm it.that way gives a high possibility of the   
the trade set up. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#295](/thread/post/2654792#post2654792 "Post Permalink")

  * Apr 7, 2009 9:34am  Apr 7, 2009 9:34am 

  * [ alain1](alain1)

  * | Joined Nov 2007  | Status: Trader | [48 Posts](/search?do=process&provider=Member&searchuser=54059)

Your system is great! I want to thank you and contribute if I can but dont'have much time. so, here's my 2 cents:get rid of all the other indis and just use the arrows **_BUT_** to filtrate the trades add the "Laguerre " indi that you can find easily. It works great and filtrate all your signals. For me , the arrows + Laguerre is the perfect weapon.  
Hope that helps and thanks agaIn for that great system.  
Alain1 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#296](/thread/post/2654875#post2654875 "Post Permalink")

  * Apr 7, 2009 10:36am  Apr 7, 2009 10:36am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I attach some indicators to confirm the trade. Put them on your chart.You will get more confidence.  
  
Set shi mtf :TF 60  
Set shi mode: TF 240  
Wolfwave has its own trend lines to insect with each other to confirm R & S. Use it with Shi to get extra confirmation.  
ang_PR is turning point indicator.  
I-drprojection gives predicated S & R when price is in action.  
buy/sell confirm the trend 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [ang_PR (Din)-v1.mq4](/attachment/file/229713?d=1239067434) 4 KB | 1,024 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [i-DRProjections_v[1][1].0.1.mq4](/attachment/file/229714?d=1239067479) 4 KB | 1,056 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [WolfWave_nen.mq4](/attachment/file/229716?d=1239067513) 15 KB | 981 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [SHI_Channel_MTF.ex4](/attachment/file/229718?d=1239067570) 10 KB | 881 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [SHI_Channel_MTF_Mod.mq4](/attachment/file/229721?d=1239067591) 7 KB | 986 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [CandleTime.mq4](/attachment/file/229726?d=1239068107) 2 KB | 784 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [buy_sell.mq4](/attachment/file/229728?d=1239068136) 1 KB | 1,348 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#297](/thread/post/2654903#post2654903 "Post Permalink")

  * Apr 7, 2009 10:51am  Apr 7, 2009 10:51am 

  * [ riskyachtar](riskyachtar)

  * | Joined Jul 2008  | Status: Trade to Life, life to trade | [330 Posts](/search?do=process&provider=Member&searchuser=74044)

what tf u use in trade ?  
thank 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#298](/thread/post/2654912#post2654912 "Post Permalink")

  * Apr 7, 2009 10:54am  Apr 7, 2009 10:54am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

G macd signal  
G macd bars 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: gbp  4hr.gif
Size: 31 KB](/attachment/image/229742/thumbnail?d=1365567402)](/attachment/image/229742?d=1239069672)   

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [GMACD_Signals.mq4](/attachment/file/229732?d=1239068561) 19 KB | 1,204 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [G#MACD_Bars.mq4](/attachment/file/229734?d=1239068633) 3 KB | 1,175 downloads 

![File Type: tpl](https://assets.faireconomy.media/images/attach/tpl.gif) [template_lyllia system.tpl](/attachment/file/229743?d=1239069741) 27 KB | 1,049 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#299](/thread/post/2654934#post2654934 "Post Permalink")

  * Apr 7, 2009 11:08am  Apr 7, 2009 11:08am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting riskyachtar](/thread/post/2654903#post2654903 "View Quoted Post")
> 
> Disliked
> 
> what tf u use in trade ?  
>  thank
> 
> Ignored

4hr 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#300](/thread/post/2654968#post2654968 "Post Permalink")

  * Apr 7, 2009 11:29am  Apr 7, 2009 11:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar24851_3.gif) hayseed](hayseed)

  * Joined Nov 2006 | Status: Trader | [4,150 Posts](/search?do=process&provider=Member&searchuser=24851)

> [Quoting lyllia](/thread/post/2654776#post2654776 "View Quoted Post")
> 
> Disliked
> 
> could you explain how to can the code with MT. I want to learn.If you are programmer could you please help to solve the repaint problem?
> 
> Ignored

  
hey lyllia.... the _arrows no repaint_ posted eariler should solve it....  
  
if your refering to the _3 level ZZ semafor_ indicator, it needs to stay as is... to alter it's code will render it less useful.....  
  
some indicators will repaint due to poor coding.... such is not the case with zigzag..... it repaints by design and is coded correctly.....h 

to trade and code, keep both simple... no call to impress....h

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#301](/thread/post/2654970#post2654970 "Post Permalink")

  * Apr 7, 2009 11:29am  Apr 7, 2009 11:29am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting hayseed](/thread/post/2654222#post2654222 "View Quoted Post")
> 
> Disliked
> 
> removing the forward looking code reduces it to the standard ma cross indicator..... also including **< = **and **> =** in the appropriate places strenghtens the logic.....  
>    
>  keep in mind your settings for the 2 ma's ..... they are so close to being identical that sometimes the micro differences will be missed....h
> 
> Ignored

Thanks mate.Would you like help to optimal the EA as well?it will be highly appreciated from all traders. I try your arrow from today. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#302](/thread/post/2654978#post2654978 "Post Permalink")

  * Apr 7, 2009 11:33am  Apr 7, 2009 11:33am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Hi everybody,  
  
please try this arrow in the template and give your opinion here after you use it for several sessions. If it is more reliable why wouldn't we make another EA for it? your observation of test is highly appreciated .Please make your contribution to this thread. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#303](/thread/post/2654988#post2654988 "Post Permalink")

  * Apr 7, 2009 11:43am  Apr 7, 2009 11:43am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting hayseed](/thread/post/2654968#post2654968 "View Quoted Post")
> 
> Disliked
> 
> hey lyllia.... the _arrows no repaint_ posted eariler should solve it....  
>    
>  if your refering to the _3 level ZZ semafor_ indicator, it needs to stay as is... to alter it's code will render it less useful.....  
>    
>  some indicators will repaint due to poor coding.... such is not the case with zigzag..... it repaints by design and is coded correctly.....h
> 
> Ignored

could you optimate the 3 level zz as well make it more reliable? And also I want to make all the indicators used in this system more reliable .Could you please find their faulty points and correct them?like all the indicators in the sub section of the chart.tia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#304](/thread/post/2655041#post2655041 "Post Permalink")

  * Apr 7, 2009 12:36pm  Apr 7, 2009 12:36pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting hayseed](/thread/post/2654222#post2654222 "View Quoted Post")
> 
> Disliked
> 
> removing the forward looking code reduces it to the standard ma cross indicator..... also including **< = **and **> =** in the appropriate places strenghtens the logic.....  
>    
>  keep in mind your settings for the 2 ma's ..... they are so close to being identical that sometimes the micro differences will be missed....h
> 
> Ignored

Do we have to change the setting to 2MA when use this indicator? Because in the code it seems they all remain 3MA .could you explain please?  
  
And apply it to the 4hr chart.It seems it comes out one bar later than the old ones. is it a delayed singal than the old one?   
  
And there are more arrow come out which is uneccessary. I label them on the chart attached.  
  
And I saw only there is one place of the code you changed. Are you sure that will make it no repaint? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: jpy 4hr.gif
Size: 24 KB](/attachment/image/229771/thumbnail?d=1365567402)](/attachment/image/229771?d=1239075336)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#305](/thread/post/2655045#post2655045 "Post Permalink")

  * Apr 7, 2009 12:39pm  Apr 7, 2009 12:39pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

the label moved the place.there are three uneccessary signals on the chart compared with original arrow. they are pre matured signals. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#306](/thread/post/2655053#post2655053 "Post Permalink")

  * Apr 7, 2009 12:49pm  Apr 7, 2009 12:49pm 

  * [ riskyachtar](riskyachtar)

  * | Joined Jul 2008  | Status: Trade to Life, life to trade | [330 Posts](/search?do=process&provider=Member&searchuser=74044)

simple indicatror 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: aaa.JPG
Size: 136 KB](/attachment/image/229777/thumbnail?d=1365567402)](/attachment/image/229777?d=1239076168)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#307](/thread/post/2655066#post2655066 "Post Permalink")

  * Apr 7, 2009 12:59pm  Apr 7, 2009 12:59pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting riskyachtar](/thread/post/2655053#post2655053 "View Quoted Post")
> 
> Disliked
> 
> simple indicatror
> 
> Ignored

are you sure 3 level zz reliable? it repaint all the time .simple not reliable ,not useful. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: euro 4hr.gif
Size: 24 KB](/attachment/image/229781/thumbnail?d=1365567402)](/attachment/image/229781?d=1239076744)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#308](/thread/post/2655078#post2655078 "Post Permalink")

  * Apr 7, 2009 1:12pm  Apr 7, 2009 1:12pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

many arrows 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: gbp 1hr.gif
Size: 21 KB](/attachment/image/229786/thumbnail?d=1365567402)](/attachment/image/229786?d=1239077568)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#309](/thread/post/2655087#post2655087 "Post Permalink")

  * Apr 7, 2009 1:21pm  Apr 7, 2009 1:21pm 

  * [ riskyachtar](riskyachtar)

  * | Joined Jul 2008  | Status: Trade to Life, life to trade | [330 Posts](/search?do=process&provider=Member&searchuser=74044)

if we trade with trendline don't see arrow to open position.  
3 level zz is not repaint for me  
  
see my chart 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: aa.jpg
Size: 114 KB](/attachment/image/229792/thumbnail?d=1365567402)](/attachment/image/229792?d=1239078096)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#310](/thread/post/2655089#post2655089 "Post Permalink")

  * Apr 7, 2009 1:22pm  Apr 7, 2009 1:22pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

not so bad ,but some arrow prematural 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: gbp 4hr.gif
Size: 23 KB](/attachment/image/229794/thumbnail?d=1365567402)](/attachment/image/229794?d=1239078118)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#311](/thread/post/2655091#post2655091 "Post Permalink")

  * Apr 7, 2009 1:25pm  Apr 7, 2009 1:25pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting riskyachtar](/thread/post/2655087#post2655087 "View Quoted Post")
> 
> Disliked
> 
> if we trade with trendline don't see arrow to open position.  
>  3 level zz is not repaint for me  
>    
>  see my chart
> 
> Ignored

so I think shi is important.The two indicators are in harmony to confirm with each other.So the shi has to be reliable. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#312](/thread/post/2655408#post2655408 "Post Permalink")

  * Apr 7, 2009 5:40pm  Apr 7, 2009 5:40pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting alain1](/thread/post/2654792#post2654792 "View Quoted Post")
> 
> Disliked
> 
> Your system is great! I want to thank you and contribute if I can but dont'have much time. so, here's my 2 cents:get rid of all the other indis and just use the arrows **_BUT_** to filtrate the trades add the "Laguerre " indi that you can find easily. It works great and filtrate all your signals. For me , the arrows + Laguerre is the perfect weapon.  
>  Hope that helps and thanks agaIn for that great system.  
>  Alain1
> 
> Ignored

thanks! Alain 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#313](/thread/post/2655478#post2655478 "Post Permalink")

  * Edited 6:22pm  Apr 7, 2009 6:20pm | Edited 6:22pm 

  * [ niksan](niksan)

  * | Joined Jan 2009  | Status: Trader | [72 Posts](/search?do=process&provider=Member&searchuser=90478)

I've been reading the thread from page one and finally today I gave it a try. And guess what! I closed the trade with +807 pips ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) on the Daily chart.  
  
see the attached chart.  
  
Thank you very much for the system. I will be trying it more.  
  
niksan 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eurusd_daily.gif
Size: 48 KB](/attachment/image/229887/thumbnail?d=1365567431)](/attachment/image/229887?d=1239096143)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#314](/thread/post/2655615#post2655615 "Post Permalink")

  * Apr 7, 2009 7:39pm  Apr 7, 2009 7:39pm 

  * [ Corppu](corppu)

  * | Joined Jun 2008  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=72090)

Thanks to Lillya for the system and Pitpiter for the EA.  
  
After using the EA for a while I have one request. The EA currently does not open the trade if there is a requote or other error ("trade context is busy" I have encountered many times). Without a stop loss this will eventually ruine ones account if the EA cannot close a trade once the arrow appears in the other direction.  
  
Could it be programmed to overcome this. For example by placing the trade until it is eventually opened. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#315](/thread/post/2656128#post2656128 "Post Permalink")

  * Apr 8, 2009 12:09am  Apr 8, 2009 12:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar24851_3.gif) hayseed](hayseed)

  * Joined Nov 2006 | Status: Trader | [4,150 Posts](/search?do=process&provider=Member&searchuser=24851)

> [Quoting lyllia](/thread/post/2655041#post2655041 "View Quoted Post")
> 
> Disliked
> 
> Do we have to change the setting to **_2MA_** when use this indicator? Because in the code it seems they all remain 3MA .could you explain please?  
>    
>  And apply it to the 4hr chart.It seems it comes out one bar later than the old ones. is it a delayed singal than the old one?   
>    
>  And there are more arrow come out which is uneccessary. I label them on the chart attached.
> 
> Ignored

  
hey lyllia.... by _**2 ma's**_ i meant _both ma's ...._ that was a poor choice of words on my part, sorry....   
  
the arrows should mark the bar following the cross ..... at the first tick of the new bar the order is sent....   
  
the picture here shows the orders, each dead on the arrow.... it's common for some signals to be missed... either due to trade context issues, server issues and such..... or it could be protective coding in the ea, such as spread protection......  
  
in the picture can be seen one signal that did not produce a trade.....  
  
  
in this picture you can see the _arrows no repaint_ indicator.... also both ma's.... one is a 3 period linnear weighted on the open and the second is a 3 period linnear weighted on the close..... those settings are from your original indicator.....  
  
the arrows line up with the ma cross's, or at least they do here......h 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: no repaint ea.gif
Size: 28 KB](/attachment/image/230053/thumbnail?d=1365567461)](/attachment/image/230053?d=1239117035)   

to trade and code, keep both simple... no call to impress....h

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#316](/thread/post/2656710#post2656710 "Post Permalink")

  * Apr 8, 2009 5:34am  Apr 8, 2009 5:34am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting niksan](/thread/post/2655478#post2655478 "View Quoted Post")
> 
> Disliked
> 
> I've been reading the thread from page one and finally today I gave it a try. And guess what! I closed the trade with +807 pips ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) on the Daily chart.  
>    
>  see the attached chart.  
>    
>  Thank you very much for the system. I will be trying it more.  
>    
>  niksan
> 
> Ignored

God blessed you! Happy trading! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#317](/thread/post/2656723#post2656723 "Post Permalink")

  * Apr 8, 2009 5:43am  Apr 8, 2009 5:43am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lang48](/thread/post/2653577#post2653577 "View Quoted Post")
> 
> Disliked
> 
> hi  
>  i am not programmer and i just found them this morning from FF forum and now trying myself to understand the difference. but i found them very useful to find support and resistance levels. for example put on H4 chart shi indicator with timeframe value 60 and another indicator with timeframe value 240 and this is some kind of filter for arrows (in case of manual trading). timeframe value 0 works on any timeframe according to this timefame.
> 
> Ignored

Thank you Lang for your Shi.They are very good for short term and long term S & R. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#318](/thread/post/2656743#post2656743 "Post Permalink")

  * Apr 8, 2009 5:57am  Apr 8, 2009 5:57am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting hayseed](/thread/post/2656128#post2656128 "View Quoted Post")
> 
> Disliked
> 
> hey lyllia.... by _**2 ma's**_ i meant _both ma's ...._ that was a poor choice of words on my part, sorry....   
>    
>  the arrows should mark the bar following the cross ..... at the first tick of the new bar the order is sent....   
>    
>  the picture here shows the orders, each dead on the arrow.... it's common for some signals to be missed... either due to trade context issues, server issues and such..... or it could be protective coding in the ea, such as spread protection......  
>    
>  in the picture can be seen one signal that...
> 
> Ignored

could you write an new indicator using these setting? at least we should give it a try if they do not repaint and produce more reliable signal?thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#319](/thread/post/2656907#post2656907 "Post Permalink")

  * Apr 8, 2009 7:52am  Apr 8, 2009 7:52am 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

> [Quoting niksan](/thread/post/2655478#post2655478 "View Quoted Post")
> 
> Disliked
> 
> I've been reading the thread from page one and finally today I gave it a try. And guess what! I closed the trade with +807 pips ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) on the Daily chart.  
>    
>  see the attached chart.  
>    
>  Thank you very much for the system. I will be trying it more.  
>    
>  niksan
> 
> Ignored

  
Hi all, this is kind off the subject, but I see nicksan's chart shows the EUR/USD as having 5 places after the decimal, I have never seen this before but I am new to Forex. Are you sure you got 800+ pips and not 80+ pips? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#320](/thread/post/2656950#post2656950 "Post Permalink")

  * Apr 8, 2009 8:28am  Apr 8, 2009 8:28am 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

  
Hi all, I have been following this thread almost since the beginning although I have not gotten this to work for me I am still trying to follow along. I have been out of the loop for a day or two and now I am kinda lost. Are we still using the arrow as the primary trade setup? Is the file that Hayseed posted arrows no repaint a newer version of IINWMARROWS? The level ZZ indicator and the bowling ball indicator the same thing? Are they used as only secondary conformation or are they more important now? I would be so thank full to anyone that can catch me up.  
  
Sorry to ask so many questions. I will contribute in any way I can. I am not a programmer but I am pretty good at research and tracking things down, so Lyllia or anyone else do not hesitate to ask me for some grunt work…  
  
Have a great day….

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#321](/thread/post/2657006#post2657006 "Post Permalink")

  * Apr 8, 2009 9:24am  Apr 8, 2009 9:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar24851_3.gif) hayseed](hayseed)

  * Joined Nov 2006 | Status: Trader | [4,150 Posts](/search?do=process&provider=Member&searchuser=24851)

hey forextek..... the version i posted was a slightly edited version of the original.....   
  
using the no repaint version, the signals should stand and will only be seen after a confirmed cross.... both of which are more inline with a conventional ea's needs........h 

to trade and code, keep both simple... no call to impress....h

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#322](/thread/post/2657048#post2657048 "Post Permalink")

  * Apr 8, 2009 9:56am  Apr 8, 2009 9:56am 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

Thanks for the response hayseed its what I thought but the thread is going so fast makes my head spin. I noticed your chart showing no repaint, did you get a new Ea for that verson? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#323](/thread/post/2657075#post2657075 "Post Permalink")

  * Apr 8, 2009 10:11am  Apr 8, 2009 10:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar24851_3.gif) hayseed](hayseed)

  * Joined Nov 2006 | Status: Trader | [4,150 Posts](/search?do=process&provider=Member&searchuser=24851)

hey forextek..... anytime some posts an idea i'll write an ea just to run it through the paces.... nothing exposes strengths and flaws better ....  
  
and sometimes will add or subtract from the original posters idea just for general "what if's".....  
  
just habitual couriosty , nothing more.....h 

to trade and code, keep both simple... no call to impress....h

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#324](/thread/post/2657105#post2657105 "Post Permalink")

  * Apr 8, 2009 10:33am  Apr 8, 2009 10:33am 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

Must be nice to be able to do that and see pretty quick if its something that has worked in the past. I write simple formula programs for backtesting price stratagies with a diff app. but the programing for metatrade is way over my head. Just wondering what the results are with the new revised arrows backtester 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#325](/thread/post/2657742#post2657742 "Post Permalink")

  * Apr 8, 2009 5:21pm  Apr 8, 2009 5:21pm 

  * [ Mandl2007](mandl2007)

  * | Membership Revoked  | Joined Nov 2008 | [279 Posts](/search?do=process&provider=Member&searchuser=86165)

I used Lyllias template last night for EU and EJ and U/CHF - got at midnight signals with WHITE arrows for EU and EJ - LONG ! Got blue arrow for U/CHF - short. BUT: 9 hours later all these arrows disappeared ! The "balls" shiftting again in the old direction of Price Action. SO it repaints even on the 4H chart !  
@ hayseed - where did you post an other "no repainting" version ?  
  
So it seems to me it isn't enough to use onla the arrows - we have to use more filters ? Where are writen down detailed and CLEAR rules for this system ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#326](/thread/post/2657813#post2657813 "Post Permalink")

  * Apr 8, 2009 5:56pm  Apr 8, 2009 5:56pm 

  * [ niksan](niksan)

  * | Joined Jan 2009  | Status: Trader | [72 Posts](/search?do=process&provider=Member&searchuser=90478)

> [Quoting forextek](/thread/post/2656907#post2656907 "View Quoted Post")
> 
> Disliked
> 
> Hi all, this is kind off the subject, but I see nicksan's chart shows the EUR/USD as having 5 places after the decimal, I have never seen this before but I am new to Forex. Are you sure you got 800+ pips and not 80+ pips?
> 
> Ignored

  
forextek,  
  
I trade with [FxPro](/brokers/fxpro "View FxPro Broker Profile"). they have a 5 digit code after the decimal whereas many other systems have 4 digits.  
  
If you see the chart I posted, at the bottom of it you will see the trade details. I traded a 0.1 lot and made almost $80. For eur/usd 0.1 lot, 10 pips = $1. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#327](/thread/post/2657824#post2657824 "Post Permalink")

  * Apr 8, 2009 6:03pm  Apr 8, 2009 6:03pm 

  * [ niksan](niksan)

  * | Joined Jan 2009  | Status: Trader | [72 Posts](/search?do=process&provider=Member&searchuser=90478)

Hi,  
  
I attached lyllia's template to my chart yesterday and to when I started mt4 again, I started getting frequent signals like the attached pic shows. Any idea why its happening? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: signal_error.gif
Size: 19 KB](/attachment/image/230479/thumbnail?d=1365567563)](/attachment/image/230479?d=1239181408)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#328](/thread/post/2657882#post2657882 "Post Permalink")

  * Apr 8, 2009 6:39pm  Apr 8, 2009 6:39pm 

  * [ Mandl2007](mandl2007)

  * | Membership Revoked  | Joined Nov 2008 | [279 Posts](/search?do=process&provider=Member&searchuser=86165)

Yes this comes from one of the indis named "silver ..." - it happens some time ....  
  
Btw ... what about repainting ... as I described it above ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#329](/thread/post/2657970#post2657970 "Post Permalink")

  * Apr 8, 2009 7:27pm  Apr 8, 2009 7:27pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting forextek](/thread/post/2656950#post2656950 "View Quoted Post")
> 
> Disliked
> 
> [color=black] Hi all, I have been following this thread almost since the beginning although I have not gotten this to work for me I am still trying to follow along. I have been out of the loop for a day or two and now I am kinda lost. Are we still using the arrow as the primary trade setup? Is the file that Hayseed posted arrows no repaint a newer version of IINWMARROWS? The level ZZ indicator and the bowling ball indicator the same thing? Are they used as only secondary conformation or are they more important now? I would be so thank full to anyone...
> 
> Ignored

Hi Mate,  
  
as I said from very begining,in this system,we focus on arrow trading.If it is relaible and can be self fulfil the buy and sell positions as planned.It would be a simple and effective system for everybody to use. If it does have repaint problem,according to your observation,we try to fix the problem.My 4hr charts arrows all stay none of them disappear.All the other indicators for confirmation only like silver trend signal.sometimes it is very helpful.It does repaint with the PA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#330](/thread/post/2657982#post2657982 "Post Permalink")

  * Apr 8, 2009 7:32pm  Apr 8, 2009 7:32pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting niksan](/thread/post/2657824#post2657824 "View Quoted Post")
> 
> Disliked
> 
> Hi,  
>    
>  I attached lyllia's template to my chart yesterday and to when I started mt4 again, I started getting frequent signals like the attached pic shows. Any idea why its happening?
> 
> Ignored

which means you get buy signal from silver trend indicator which is a small pink arrow used to confirm the trend.It sometimes repaint.you could take it off if you like. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#331](/thread/post/2657990#post2657990 "Post Permalink")

  * Apr 8, 2009 7:37pm  Apr 8, 2009 7:37pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting hayseed](/thread/post/2657075#post2657075 "View Quoted Post")
> 
> Disliked
> 
> hey forextek..... anytime some posts an idea i'll write an ea just to run it through the paces.... nothing exposes strengths and flaws better ....  
>    
>  and sometimes will add or subtract from the original posters idea just for general "what if's".....  
>    
>  just habitual couriosty , nothing more.....h
> 
> Ignored

Could you make an new arrow indicator and rename it .Also EA let everybody test it please? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#332](/thread/post/2658000#post2658000 "Post Permalink")

  * Apr 8, 2009 7:41pm  Apr 8, 2009 7:41pm 

  * [ gutek04](gutek04)

  * | Joined Mar 2009  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=95989)

What You guys think about this kind of IINWMARROWS use? Thats mine template, and IINWMARROWS is used here only for comfirmation or as signal to reenter allready growing or falling trend.  
  
... Sry for OT, lets say its my version of lyllia trading sys it consist of trend follower, lyllia trading sys, RSI trader and some my addons. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: GB.JPG
Size: 146 KB](/attachment/image/230530/thumbnail?d=1365567563)](/attachment/image/230530?d=1239187280)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#333](/thread/post/2658005#post2658005 "Post Permalink")

  * Apr 8, 2009 7:46pm  Apr 8, 2009 7:46pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting hayseed](/thread/post/2657006#post2657006 "View Quoted Post")
> 
> Disliked
> 
> hey forextek..... the version i posted was a slightly edited version of the original.....   
>    
>  using the no repaint version, the signals should stand and will only be seen after a confirmed cross.... both of which are more inline with a conventional ea's needs........h
> 
> Ignored

Could you make an EA to open the position as soon as the arrow appear,it is critical. it means the pips. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#334](/thread/post/2658011#post2658011 "Post Permalink")

  * Apr 8, 2009 7:48pm  Apr 8, 2009 7:48pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting gutek04](/thread/post/2658000#post2658000 "View Quoted Post")
> 
> Disliked
> 
> What You guys think about this kind of IINWMARROWS use? Thats mine template, and IINWMARROWS is used here only for comfirmation or as signal to reenter allready growing or falling trend.
> 
> Ignored

could you please post your template here? let people try if it is good for use.  
do you have arrow repaint problem? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#335](/thread/post/2658017#post2658017 "Post Permalink")

  * Apr 8, 2009 7:52pm  Apr 8, 2009 7:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95485_4.gif) shilox](shilox)

  * | Joined Mar 2009  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=95485)

Your strategy is a very good one i must confess, I have followed it from the beginning. Very impressive!  
  
Please if you don't mind, check your arrows with fractals and zig zag indicators if they do about the same thing, let me know how it goes @ [sampsonzhiya@yahoo.com](mailto:sampsonzhiya@yahoo.com) then WE can figure something out.  
  
I am suggesting this because of 'THE NOISE'. When its all done then we can get back to the noise.  
  
See you soon. 

EVERY PIP COUNTS!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#336](/thread/post/2658028#post2658028 "Post Permalink")

  * Apr 8, 2009 8:00pm  Apr 8, 2009 8:00pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting pitpiter](/thread/post/2651797#post2651797 "View Quoted Post")
> 
> Disliked
> 
> If I have observe indi applying on 5M chart , aways arrow appears after close bar and start next bar . If I'm wrong , please correct me . I tried make EA , which work on open bars value and it didn't opened any trade. As I said before I run EA on 8 pair and it opened all trades correctly with open price for next bar after bar when appear arrow. Now I propose wait on result working EA this week , if I sold problem , which I find - wrigt about in previouse post , I will post here new version for public testing.  
>  Regards  
>  Peter
> 
> Ignored

Hi Peter,  
  
how is your EA going? fix the problem? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#337](/thread/post/2658034#post2658034 "Post Permalink")

  * Apr 8, 2009 8:03pm  Apr 8, 2009 8:03pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting shilox](/thread/post/2658017#post2658017 "View Quoted Post")
> 
> Disliked
> 
> Your strategy is a very good one i must confess, I have followed it from the beginning. Very impressive!  
>    
>  Please if you don't mind, check your arrows with fractals and zig zag indicators if they do about the same thing, let me know how it goes @ [sampsonzhiya@yahoo.com](mailto:sampsonzhiya@yahoo.com) then WE can figure something out.  
>    
>  I am suggesting this because of 'THE NOISE'. When its all done then we can get back to the noise.  
>    
>  See you soon.
> 
> Ignored

thank you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#338](/thread/post/2658072#post2658072 "Post Permalink")

  * Edited 8:40pm  Apr 8, 2009 8:19pm | Edited 8:40pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting Mandl2007](/thread/post/2657742#post2657742 "View Quoted Post")
> 
> Disliked
> 
> I used Lyllias template last night for EU and EJ and U/CHF - got at midnight signals with WHITE arrows for EU and EJ - LONG ! Got blue arrow for U/CHF - short. BUT: 9 hours later all these arrows disappeared ! The "balls" shiftting again in the old direction of Price Action. SO it repaints even on the 4H chart !  
>  @ hayseed - where did you post an other "no repainting" version ?  
>    
>  So it seems to me it isn't enough to use onla the arrows - we have to use more filters ? Where are writen down detailed and CLEAR rules for this system ?
> 
> Ignored

This system simple :trading the arrow. if it has problem ,fix it. Because it is the most reliable arrow I have come cross.If it works ,it is the most simple system to follow. I insist on using it as the main incator for this system.As I said it seldom repaint.I repeat point several times in this thread.And I do not want to reapeat again.  
  
Other indicators for confimation only.  
  
After try them you are flexible to decide what's the best combination of all these indicators as a good system for you to use. You could write you own rules of using it and test your rules to see whether they are working for you.If they are not you have to change the system that work for you.  
  
I list some indicator's function used in this system in the previous post.  
  
I like people to participate in providing a proven system that working in all market situations. If you have any please post here. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#339](/thread/post/2658110#post2658110 "Post Permalink")

  * Apr 8, 2009 8:30pm  Apr 8, 2009 8:30pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting shilox](/thread/post/2658017#post2658017 "View Quoted Post")
> 
> Disliked
> 
> Your strategy is a very good one i must confess, I have followed it from the beginning. Very impressive!  
>    
>  Please if you don't mind, check your arrows with fractals and zig zag indicators if they do about the same thing, let me know how it goes @ [sampsonzhiya@yahoo.com](mailto:sampsonzhiya@yahoo.com) then WE can figure something out.  
>    
>  I am suggesting this because of 'THE NOISE'. When its all done then we can get back to the noise.  
>    
>  See you soon.
> 
> Ignored

you are right.Fractal and arrow almost do the same thing. I put them together now for a test. As I remembered fractal is a laggin indicator.I haven't use if for a while. now I test it again.zigzag used with shi is a good combination to fogure out support and resistance. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#340](/thread/post/2658152#post2658152 "Post Permalink")

  * Apr 8, 2009 8:43pm  Apr 8, 2009 8:43pm 

  * [ gutek04](gutek04)

  * | Joined Mar 2009  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=95989)

Those are all indicators that I use, when m1 scalping I always check higher TF before going in. And YES, i have repaint problem too but as I wrote before I use IINWMARROWS only as a confirmation. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [Ind.zip](/attachment/file/230562?d=1239190981) 48 KB | 1,088 downloads 

![File Type: tpl](https://assets.faireconomy.media/images/attach/tpl.gif) [gootson.tpl](/attachment/file/230563?d=1239190989) 87 KB | 749 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#341](/thread/post/2658205#post2658205 "Post Permalink")

  * Apr 8, 2009 9:09pm  Apr 8, 2009 9:09pm 

  * [ jsj1970](jsj1970)

  * | Joined Feb 2009  | Status: Leaving stocks for FX | [30 Posts](/search?do=process&provider=Member&searchuser=93183)

Hello Lyllia. Great stuff!!!! So I have been following the thread from the begining and I think your system has great promise. I have had the EA up and running since fri. april 3 7 am cst. With the exception of 2 five hour periods, and the weekend, it has been running consistantly.I have tweaked my system a little from Lyllias'. I set my template up with three pairs(gbp/jyp,gbp/usd,eur/usd) on the one hour tf. I only have iinwmarrows running on this template otherwise it would be way to cluttered and noisy.I have lyllias full system up on another page for support and verification.So far since Friday, the EA has produced over 1000 pips with verry little involvement on my part. Ocasionally I would add a trailing s/l if I was in front of the computer but other than that, everything was auto generated.  
  
A couple of things I would change/improve if possible.  
  
1\. Instant execution of order when arrow paints instead of waiting for the candle to end.(we are missing too many pips due to the slow entry, and losing more due to the retracement of the candle.)  
  
2\. The application of a trailing stop to the EA. When using the EA on higher tf's a person could really get burned on a sudden heavy price swing.  
  
I plan on letting this run for a month and will post my results as the occur.  
  
Once again........ Great stuff lyllia, and thanks!! Jim 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: lyllia.gif
Size: 97 KB](/attachment/image/230550/thumbnail?d=1365567563)](/attachment/image/230550?d=1239190288)   

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [Statement 5469218 - James Jones.txt](/attachment/file/230560?d=1239190705) 7 KB | 486 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#342](/thread/post/2658302#post2658302 "Post Permalink")

  * Apr 8, 2009 10:02pm  Apr 8, 2009 10:02pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting jsj1970](/thread/post/2658205#post2658205 "View Quoted Post")
> 
> Disliked
> 
> Hello Lyllia. Great stuff!!!! So I have been following the thread from the begining and I think your system has great promise. I have had the EA up and running since fri. april 3 7 am cst. With the exception of 2 five hour periods, and the weekend, it has been running consistantly.I have tweaked my system a little from Lyllias'. I set my template up with three pairs(gbp/jyp,gbp/usd,eur/usd) on the one hour tf. I only have iinwmarrows running on this template otherwise it would be way to cluttered and noisy.I have lyllias full system up on another...
> 
> Ignored

Do you have any idea how many pips the trailing stop will be?  
If we could solve the slow entry peoblem, the opposite arrow appears and an instant opened order will close the previous position is my original plan.  
  
For this plane to be achieved:  
1.first we have to solve the arrow repaint problem if ther is any.  
2.Secondly, we have to let position to be opened when the arrow appeared.  
3\. there is no server and terminal connection problem. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#343](/thread/post/2658308#post2658308 "Post Permalink")

  * Apr 8, 2009 10:04pm  Apr 8, 2009 10:04pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting jsj1970](/thread/post/2658205#post2658205 "View Quoted Post")
> 
> Disliked
> 
> Hello Lyllia. Great stuff!!!! So I have been following the thread from the begining and I think your system has great promise. I have had the EA up and running since fri. april 3 7 am cst. With the exception of 2 five hour periods, and the weekend, it has been running consistantly.I have tweaked my system a little from Lyllias'. I set my template up with three pairs(gbp/jyp,gbp/usd,eur/usd) on the one hour tf. I only have iinwmarrows running on this template otherwise it would be way to cluttered and noisy.I have lyllias full system up on another...
> 
> Ignored

  
Which arrow are you using? the no repaint one? or the original one? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#344](/thread/post/2658339#post2658339 "Post Permalink")

  * Apr 8, 2009 10:15pm  Apr 8, 2009 10:15pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting gutek04](/thread/post/2658152#post2658152 "View Quoted Post")
> 
> Disliked
> 
> Those are all indicators that I use, when m1 scalping I always check higher TF before going in. And YES, i have repaint problem too but as I wrote before I use IINWMARROWS only as a confirmation.
> 
> Ignored

thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#345](/thread/post/2658362#post2658362 "Post Permalink")

  * Apr 8, 2009 10:28pm  Apr 8, 2009 10:28pm 

  * [ Corppu](corppu)

  * | Joined Jun 2008  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=72090)

> [Quoting lyllia](/thread/post/2658302#post2658302 "View Quoted Post")
> 
> Disliked
> 
> For this plane to be achieved:  
>  1.first we have to solve the arrow repaint problem if ther is any.  
>  2.Secondly, we have to let position to be opened when the arrow appeared.  
>  3\. there is no server and terminal connection problem.
> 
> Ignored

I have not seen the arrows repaint. I am using the original indicator, which gives good early signals. Points 2 and 3 are the main problems. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#346](/thread/post/2658399#post2658399 "Post Permalink")

  * Apr 8, 2009 10:44pm  Apr 8, 2009 10:44pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting Corppu](/thread/post/2658362#post2658362 "View Quoted Post")
> 
> Disliked
> 
> I have not seen the arrows repaint. I am using the original indicator, which gives good early signals. Points 2 and 3 are the main problems.
> 
> Ignored

trading is all about find support and resistance.Only use 3 level zz as a reference for the short term cycle for the TF chart to trade. Once arrow shows up in conjucture with other indicators showing the bottom or top and 3zz shows three.then the Top and Bottom is formed in that TF.hope this help. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#347](/thread/post/2658556#post2658556 "Post Permalink")

  * Apr 8, 2009 11:45pm  Apr 8, 2009 11:45pm 

  * [ jsj1970](jsj1970)

  * | Joined Feb 2009  | Status: Leaving stocks for FX | [30 Posts](/search?do=process&provider=Member&searchuser=93183)

> [Quoting lyllia](/thread/post/2658308#post2658308 "View Quoted Post")
> 
> Disliked
> 
> Which arrow are you using? the no repaint one? or the original one?
> 
> Ignored

I am still using the original one as I have not seem a modified one posted in this thread. As far as the trailing stop loss is concerned, I would say something in the range of 75 pips. It is mainly for protection on big reversal swings(like if some unexpected good or bad news was released). You still want the arrows to do the bulk of the work in closing positions. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#348](/thread/post/2658704#post2658704 "Post Permalink")

  * Apr 9, 2009 12:48am  Apr 9, 2009 12:48am 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

> [Quoting niksan](/thread/post/2657813#post2657813 "View Quoted Post")
> 
> Disliked
> 
> forextek,  
>    
>  I trade with FxPro. they have a 5 digit code after the decimal whereas many other systems have 4 digits.  
>    
>  If you see the chart I posted, at the bottom of it you will see the trade details. I traded a 0.1 lot and made almost $80. For eur/usd 0.1 lot, 10 pips = $1.
> 
> Ignored

I see, confussed me at first, so your 800 pips is same as my 4digit 80 pips,, .1 for 5 dig. same as .01 4 digit, thanks for shedding light on it.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#349](/thread/post/2658725#post2658725 "Post Permalink")

  * Apr 9, 2009 12:56am  Apr 9, 2009 12:56am 

  * [ perjo](perjo)

  * | Joined Nov 2008  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=86171)

sorry corppu,  
but i have seen last night 00.00gmt+3 eurusd arrow up to buy then this morning at 8gmt+3 there was an other arrows going down. then this afternoon no more arrow appearing.   
regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#350](/thread/post/2658744#post2658744 "Post Permalink")

  * Apr 9, 2009 1:01am  Apr 9, 2009 1:01am 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

> [Quoting lyllia](/thread/post/2657970#post2657970 "View Quoted Post")
> 
> Disliked
> 
> Hi Mate,  
>    
>  as I said from very begining,in this system,we focus on arrow trading.If it is relaible and can be self fulfil the buy and sell positions as planned.It would be a simple and effective system for everybody to use. If it does have repaint problem,according to your observation,we try to fix the problem.My 4hr charts arrows all stay none of them disappear.All the other indicators for confirmation only like silver trend signal.sometimes it is very helpful.It does repaint with the PA.
> 
> Ignored

Well it is strange it does not repaint on yours wonder if its a setting, I see it all the time on 4hr and daily, more on 4hr ofcourse. have you laid hayseeds arrows ontop of the other to see if hayseeds has arrows where the older one does not, that would show repainting? Sometimes if you restart your platform it forces the arrows to dissapear if a change in direction has occured. I wish we had a chat room where we could compare the arrows in real time...... notice the screen shot where there are places where hayseeds arrows are there but the older version is not they dissapeared including the usd/jpy long that I am in right now. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: test.JPG
Size: 285 KB](/attachment/image/230662/thumbnail?d=1365567584)](/attachment/image/230662?d=1239206491)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#351](/thread/post/2658860#post2658860 "Post Permalink")

  * Apr 9, 2009 1:36am  Apr 9, 2009 1:36am 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

> [Quoting lyllia](/thread/post/2658302#post2658302 "View Quoted Post")
> 
> Disliked
> 
> Do you have any idea how many pips the trailing stop will be?  
>  If we could solve the slow entry peoblem, the opposite arrow appears and an instant opened order will close the previous position is my original plan.  
>    
>  For this plane to be achieved:  
>  1.first we have to solve the arrow repaint problem if ther is any.  
>  2.Secondly, we have to let position to be opened when the arrow appeared.  
>  3\. there is no server and terminal connection problem.
> 
> Ignored

Would be great to have an audio alert for the arrows aswell... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#352](/thread/post/2658899#post2658899 "Post Permalink")

  * Apr 9, 2009 1:45am  Apr 9, 2009 1:45am 

  * [ lang48](lang48)

  * | Joined Jan 2008  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=59429)

you are welcome Lyllia  
  
when trading with ea you can use attached emergency ea,s. they close all you trades. put them on separate charts. at first try them on demo. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [CloseTrades_After_Account_Loss_TooMuch.ex4](/attachment/file/230681?d=1239209085) 2 KB | 507 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [CloseTrades_After_Account_Profit_Reached.mq4](/attachment/file/230682?d=1239209085) 3 KB | 638 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#353](/thread/post/2658913#post2658913 "Post Permalink")

  * Apr 9, 2009 1:49am  Apr 9, 2009 1:49am 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

I really think that we should get a live chat room and try to solve and see what going on with this repainting problem that some swear they do not see. The thought of this indy not repainting has my mouth watering. I think Hayseeds new indy shows the arrow on the bar that opens after the signal bar closes where the older one puts arrow on the current bar that produces singal as soon as singal is produced, therefore I think Hayseeds will only paint at the end of the bar not in middle as the old one does. Is this correct Hayseed?   
  
For any indy to produce a arrow in middle of a bar time, must take a risk of repaint if conditions change in same bar (highs get higher ect),   
  
AS I said at top we need a chat room, anyone else like this idea? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#354](/thread/post/2659009#post2659009 "Post Permalink")

  * Apr 9, 2009 2:29am  Apr 9, 2009 2:29am 

  * [ perjo](perjo)

  * | Joined Nov 2008  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=86171)

yes forextek i agree with you about chatroom even if i dont speak good english . it will be great to have a sonor alert when the arrows appears. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#355](/thread/post/2659018#post2659018 "Post Permalink")

  * Apr 9, 2009 2:34am  Apr 9, 2009 2:34am 

  * [ perjo](perjo)

  * | Joined Nov 2008  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=86171)

and i would like to know the exact price when one arrow comes so if we are late we always could enter the trade at that price. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#356](/thread/post/2659533#post2659533 "Post Permalink")

  * Apr 9, 2009 8:31am  Apr 9, 2009 8:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar24851_3.gif) hayseed](hayseed)

  * Joined Nov 2006 | Status: Trader | [4,150 Posts](/search?do=process&provider=Member&searchuser=24851)

> [Quoting forextek](/thread/post/2658913#post2658913 "View Quoted Post")
> 
> Disliked
> 
> I think Hayseeds new indy shows the arrow on the bar that opens after the signal bar closes where the older one puts arrow on the current bar that produces singal as soon as singal is produced, therefore I think Hayseeds will only paint at the end of the bar not in middle as the old one does. Is this correct Hayseed?
> 
> Ignored

hey forextek...... yes your correct..... it will show the first tick of a new bar after a confirmed cross...   
  
that's not saying it's a beter/worse signal.... it's common to focus on getting in quick at the earilest possible signal hopeing for the optimum entry....  
  
many times the signal is far from optimum..... the energy, movement, money, required to produce the signal, in this case a moving average cross, can fade quickly.... as it fades the price falls below the initial signals price.....  
  
delaying your entry a few bars after the signal can be worthwhile...... or perhaps using limit orders or a combination of both......   
  
run a backtest on most any ea but delay your entry a fews bars...... it's quite rare for the exact signal bar to be the best available entry.......h 

to trade and code, keep both simple... no call to impress....h

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#357](/thread/post/2659556#post2659556 "Post Permalink")

  * Apr 9, 2009 8:54am  Apr 9, 2009 8:54am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lang48](/thread/post/2658899#post2658899 "View Quoted Post")
> 
> Disliked
> 
> you are welcome Lyllia  
>    
>  when trading with ea you can use attached emergency ea,s. they close all you trades. put them on separate charts. at first try them on demo.
> 
> Ignored

Thanks! Lang 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#358](/thread/post/2659562#post2659562 "Post Permalink")

  * Apr 9, 2009 8:57am  Apr 9, 2009 8:57am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting forextek](/thread/post/2658860#post2658860 "View Quoted Post")
> 
> Disliked
> 
> Would be great to have an audio alert for the arrows aswell...
> 
> Ignored

I agree with this idea, could anybody make it? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#359](/thread/post/2659571#post2659571 "Post Permalink")

  * Apr 9, 2009 9:02am  Apr 9, 2009 9:02am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting forextek](/thread/post/2658744#post2658744 "View Quoted Post")
> 
> Disliked
> 
> Well it is strange it does not repaint on yours wonder if its a setting, I see it all the time on 4hr and daily, more on 4hr ofcourse. have you laid hayseeds arrows ontop of the other to see if hayseeds has arrows where the older one does not, that would show repainting? Sometimes if you restart your platform it forces the arrows to dissapear if a change in direction has occured. I wish we had a chat room where we could compare the arrows in real time...... notice the screen shot where there are places where hayseeds arrows are there but the older...
> 
> Ignored

I do not agree.If the old one is not there,it is not supposed to be there.It does not disappear. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#360](/thread/post/2659573#post2659573 "Post Permalink")

  * Apr 9, 2009 9:03am  Apr 9, 2009 9:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar16896_7.gif) sirwolf](sirwolf)

  * Joined Aug 2006 | Status: Believe and Achieve Proverbs 16:3 | [731 Posts](/search?do=process&provider=Member&searchuser=16896)

> [Quoting lyllia](/thread/post/2659562#post2659562 "View Quoted Post")
> 
> Disliked
> 
> I agree with this idea, could anybody make it?
> 
> Ignored

An email alert would also be great since it is a 4 hr chart. This allows for trading via a smartphone etc. 

Believe and Achieve!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#361](/thread/post/2659587#post2659587 "Post Permalink")

  * Apr 9, 2009 9:16am  Apr 9, 2009 9:16am 

  * [ ataviano](ataviano)

  * | Joined Feb 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=60944)

> [Quoting gutek04](/thread/post/2658000#post2658000 "View Quoted Post")
> 
> Disliked
> 
> What You guys think about this kind of IINWMARROWS use? Thats mine template, and IINWMARROWS is used here only for comfirmation or as signal to reenter allready growing or falling trend.  
>    
>  ... Sry for OT, lets say its my version of lyllia trading sys it consist of trend follower, lyllia trading sys, RSI trader and some my addons.
> 
> Ignored

Hi bro please can you post the indi that showes the news time and impact on u chart?  
Thanx  
  
__Succes is not an event. It is a process__

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#362](/thread/post/2659617#post2659617 "Post Permalink")

  * Apr 9, 2009 9:35am  Apr 9, 2009 9:35am 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

> [Quoting lyllia](/thread/post/2659571#post2659571 "View Quoted Post")
> 
> Disliked
> 
> I do not agree.If the old one is not there,it is not supposed to be there.It does not disappear.
> 
> Ignored

I wish I could see what you see. Check out the two attachments, they are from last week. the second screen shot was taken 5 mins. later after I restrated the platform, I suspected that they may dissapear because of the 2 direction changes in the 4 TF.  
  
If you run the backtester you will see where it did do the buy and sell at those times....  
  
Hope we can figure it out... 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: eur show.jpg
Size: 240 KB](/attachment/image/230869/thumbnail?d=1365567643)](/attachment/image/230869?d=1239237290)   
[![Click to Enlarge

Name: eur gone.jpg
Size: 243 KB](/attachment/image/230870/thumbnail?d=1365567643)](/attachment/image/230870?d=1239237290)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#363](/thread/post/2659952#post2659952 "Post Permalink")

  * Apr 9, 2009 3:30pm  Apr 9, 2009 3:30pm 

  * [ sholmes9000](sholmes9000)

  * | Joined Mar 2009  | Status: Trader | [87 Posts](/search?do=process&provider=Member&searchuser=98152)

hi lyllia, downloaded your file template_fx.tpl onto my metaforex. but i'm not able to see any arrows....can advise what shld i do? tks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#364](/thread/post/2660242#post2660242 "Post Permalink")

  * Apr 9, 2009 6:25pm  Apr 9, 2009 6:25pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

you have to download all the indicators to your indicator file.  
  
Template to template file.  
  
EA to EA file. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#365](/thread/post/2660261#post2660261 "Post Permalink")

  * Apr 9, 2009 6:34pm  Apr 9, 2009 6:34pm 

  * [ sholmes9000](sholmes9000)

  * | Joined Mar 2009  | Status: Trader | [87 Posts](/search?do=process&provider=Member&searchuser=98152)

> [Quoting lyllia](/thread/post/2660242#post2660242 "View Quoted Post")
> 
> Disliked
> 
> you have to download all the indicators to your indicator file.  
>    
>  Template to template file.  
>    
>  EA to EA file.
> 
> Ignored

tks lyllia 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#366](/thread/post/2660993#post2660993 "Post Permalink")

  * Apr 10, 2009 12:38am  Apr 10, 2009 12:38am 

  * [ gutek04](gutek04)

  * | Joined Mar 2009  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=95989)

> [Quoting ataviano](/thread/post/2659587#post2659587 "View Quoted Post")
> 
> Disliked
> 
> Hi bro please can you post the indi that showes the news time and impact on u chart?  
>  Thanx  
>    
>  __Succes is not an event. It is a process__
> 
> Ignored

  
Hi, sure its FFcal. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [FFCal.mq4](/attachment/file/231196?d=1239291494) 47 KB | 560 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#367](/thread/post/2662405#post2662405 "Post Permalink")

  * Apr 10, 2009 5:54pm  Apr 10, 2009 5:54pm 

  * [ jamesfr](jamesfr)

  * | Joined Mar 2009  | Status: Trader | [76 Posts](/search?do=process&provider=Member&searchuser=95609)

> [Quoting jsj1970](/thread/post/2658205#post2658205 "View Quoted Post")
> 
> Disliked
> 
> Hello Lyllia. Great stuff!!!! So I have been following the thread from the begining and I think your system has great promise. I have had the EA up and running since fri. april 3 7 am cst. With the exception of 2 five hour periods, and the weekend, it has been running consistantly.I have tweaked my system a little from Lyllias'. I set my template up with three pairs(gbp/jyp,gbp/usd,eur/usd) on the one hour tf. I only have iinwmarrows running on this template otherwise it would be way to cluttered and noisy.I have lyllias full system up on another...
> 
> Ignored

  
Hi Jim  
  
Any chance you could post your exact setup (template) TF etc,as I have tried the EA and it just produces loss after loss.  
This is indeed a great system as I have used it manually if I could get the EA working as you have it would be excellent.  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#368](/thread/post/2662576#post2662576 "Post Permalink")

  * Apr 10, 2009 9:36pm  Apr 10, 2009 9:36pm 

  * [ rayhalvey](rayhalvey)

  * | Joined Jul 2008  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=74411)

> [Quoting lyllia](/thread/post/2635312#post2635312 "View Quoted Post")
> 
> Disliked
> 
> I start this trading thread to share with fellow traders my trading system.See template_fx attached.Apply it to your chart, any time frame .I prefer one hour ++. Hope you enjoy and try it on Monday.  
>    
>  All the indicators included from the internet published resources.The most reliable indicator is IINWMARROWS.mq4.It is the core of this system. It has 95% + successful rate.In another word, if you only trade this arrow. you could be able to make pips.....;  
>    
>  Other indicators are used as reference.They are together make a complet system.After you used...
> 
> Ignored

I am sorry to be a pain,Lyllia but can you tell me where to get hold of your indicater 11NWMARROWS.mq4 ......I cant find it !!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#369](/thread/post/2662580#post2662580 "Post Permalink")

  * Apr 10, 2009 9:43pm  Apr 10, 2009 9:43pm 

  * [ webicknell](webicknell)

  * | Joined Mar 2006  | Status: Trader | [129 Posts](/search?do=process&provider=Member&searchuser=7494)

The indicator you are looking for is included in the zip file posted by guek04 on post # 340  
  
With the other indicators.... tpl file is on the same post 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#370](/thread/post/2662621#post2662621 "Post Permalink")

  * Apr 10, 2009 10:19pm  Apr 10, 2009 10:19pm 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

> [Quoting gutek04](/thread/post/2658000#post2658000 "View Quoted Post")
> 
> Disliked
> 
> What You guys think about this kind of IINWMARROWS use? Thats mine template, and IINWMARROWS is used here only for comfirmation or as signal to reenter allready growing or falling trend.  
>    
>  ... Sry for OT, lets say its my version of lyllia trading sys it consist of trend follower, lyllia trading sys, RSI trader and some my addons.
> 
> Ignored

Hey qutek04  
  
Can you give an example of how you would set up a trade using this template, entry/sl/ect  
  
Thanks  

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#371](/thread/post/2662686#post2662686 "Post Permalink")

  * Apr 10, 2009 11:15pm  Apr 10, 2009 11:15pm 

  * [ gutek04](gutek04)

  * | Joined Mar 2009  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=95989)

> [Quoting forextek](/thread/post/2662621#post2662621 "View Quoted Post")
> 
> Disliked
> 
> Hey qutek04  
>    
>  Can you give an example of how you would set up a trade using this template, entry/sl/ect  
>    
>  Thanks
> 
> Ignored

It would be hard to explain You how exactly Im opening positions with it because beside of M1 I use m5, m30 and h1 timeframe, where Im working with trend lines, fibonacci, divergences, support and resistances and sometimes candle patterns. My m5 after whole day looks like that in attachments. m1 timeframe Im using only to confirmation.  
  
check those systems:  
<http://www.forexfactory.com/showthread.php?t=148902>  
<http://www.forexfactory.com/showthread.php?t=40325>  
mine is based on them.  
  
The most important for me is technical analize on higher TF. Without strong signal on higher TF I dont even look at m1.   
  
My TP is 40 on GBP/JPY  
20-30 on GBP/USD  
Sometimes I determine my TP by fibonacci retracement and expansion.  
  
Im not a pro trader, still im more a student than a teacher so if You wanna use it first check it on demo. Have a nice pips! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: GB2.jpg
Size: 389 KB](/attachment/image/231548/thumbnail?d=1365567765)](/attachment/image/231548?d=1239372728)   
[![Click to Enlarge

Name: BG3.jpg
Size: 424 KB](/attachment/image/231549/thumbnail?d=1365567765)](/attachment/image/231549?d=1239372752)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#372](/thread/post/2662688#post2662688 "Post Permalink")

  * Apr 10, 2009 11:16pm  Apr 10, 2009 11:16pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting rayhalvey](/thread/post/2662576#post2662576 "View Quoted Post")
> 
> Disliked
> 
> I am sorry to be a pain,Lyllia but can you tell me where to get hold of your indicater 11NWMARROWS.mq4 ......I cant find it !!!
> 
> Ignored

post 18 & 19\. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#373](/thread/post/2662786#post2662786 "Post Permalink")

  * Apr 11, 2009 12:16am  Apr 11, 2009 12:16am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting gutek04](/thread/post/2662686#post2662686 "View Quoted Post")
> 
> Disliked
> 
> It would be hard to explain You how exactly Im opening positions with it because beside of M1 I use m5, m30 and h1 timeframe, where Im working with trend lines, fibonacci, divergences, support and resistances and sometimes candle patterns. My m5 after whole day looks like that in attachments. m1 timeframe Im using only to confirmation.  
>    
>  check those systems:  
>  <http://www.forexfactory.com/showthread.php?t=148902>  
>  <http://www.forexfactory.com/showthread.php?t=40325>  
>  mine is based on them.  
>    
>  The most important for me is technical analize...
> 
> Ignored

thanks for posting the chart here. Could you please post the template and indicators here? It is handy for learn. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#374](/thread/post/2662809#post2662809 "Post Permalink")

  * Apr 11, 2009 12:35am  Apr 11, 2009 12:35am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting jsj1970](/thread/post/2658205#post2658205 "View Quoted Post")
> 
> Disliked
> 
> Hello Lyllia. Great stuff!!!! So I have been following the thread from the begining and I think your system has great promise. I have had the EA up and running since fri. april 3 7 am cst. With the exception of 2 five hour periods, and the weekend, it has been running consistantly.I have tweaked my system a little from Lyllias'. I set my template up with three pairs(gbp/jyp,gbp/usd,eur/usd) on the one hour tf. I only have iinwmarrows running on this template otherwise it would be way to cluttered and noisy.I have lyllias full system up on another...
> 
> Ignored

  
Are you a programmer yourself?could you do something about it?Please let me [know.lyllia45@yahoo.com.au](mailto:know.lyllia45@yahoo.com.au)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#375](/thread/post/2662834#post2662834 "Post Permalink")

  * Edited 1:21am  Apr 11, 2009 1:01am | Edited 1:21am 

  * [ gutek04](gutek04)

  * | Joined Mar 2009  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=95989)

M1  
_[http://www.forexfactory.com/showpost...&postcount=340](http://www.forexfactory.com/showpost.php?p=2658152&postcount=340)_  
M5, m30 and h1 templates and indicators are in attachments. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [Templates and Indicators.zip](/attachment/file/231577?d=1239379253) 115 KB | 1,309 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#376](/thread/post/2663442#post2663442 "Post Permalink")

  * Apr 11, 2009 4:33pm  Apr 11, 2009 4:33pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting gutek04](/thread/post/2662834#post2662834 "View Quoted Post")
> 
> Disliked
> 
> M1  
>  _[http://www.forexfactory.com/showpost...&postcount=340](http://www.forexfactory.com/showpost.php?p=2658152&postcount=340)_  
>  M5, m30 and h1 templates and indicators are in attachments.
> 
> Ignored

  
thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#377](/thread/post/2663505#post2663505 "Post Permalink")

  * Apr 11, 2009 7:00pm  Apr 11, 2009 7:00pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting jamesfr](/thread/post/2662405#post2662405 "View Quoted Post")
> 
> Disliked
> 
> Hi Jim  
>    
>  Any chance you could post your exact setup (template) TF etc,as I have tried the EA and it just produces loss after loss.  
>  This is indeed a great system as I have used it manually if I could get the EA working as you have it would be excellent.  
>  Thanks
> 
> Ignored

Anybody could help to solve the EA problem? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#378](/thread/post/2663506#post2663506 "Post Permalink")

  * Apr 11, 2009 7:03pm  Apr 11, 2009 7:03pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting gutek04](/thread/post/2662834#post2662834 "View Quoted Post")
> 
> Disliked
> 
> M1  
>  _[http://www.forexfactory.com/showpost...&postcount=340](http://www.forexfactory.com/showpost.php?p=2658152&postcount=340)_  
>  M5, m30 and h1 templates and indicators are in attachments.
> 
> Ignored

it is great. I also put lang's Shi on the template,they are togethere to give out sort of R & S projection. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#379](/thread/post/2663566#post2663566 "Post Permalink")

  * Apr 11, 2009 9:31pm  Apr 11, 2009 9:31pm 

  * [ gutek04](gutek04)

  * | Joined Mar 2009  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=95989)

> [Quoting lyllia](/thread/post/2663506#post2663506 "View Quoted Post")
> 
> Disliked
> 
> it is great. I also put lang's Shi on the template,they are togethere to give out sort of R & S projection.
> 
> Ignored

lang's Shi? havent heard about it... is that indicator? Could You show it? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#380](/thread/post/2665617#post2665617 "Post Permalink")

  * Apr 13, 2009 10:32pm  Apr 13, 2009 10:32pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting lang48](/thread/post/2653463#post2653463 "View Quoted Post")
> 
> Disliked
> 
> one more
> 
> Ignored

have a look at post 261 & 270\. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#381](/thread/post/2665679#post2665679 "Post Permalink")

  * Apr 13, 2009 11:05pm  Apr 13, 2009 11:05pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

To Peter,  
  
[quote]   
I have tested the EA during the weekend on euro.The following is what I find out:  
  
1\. The ea open position at the end of the bar.This is in line with many EA' s method around.It seems nothing wrong with it.But for trading purpose,sometime it seems like a delayed entry.I have not compared the the time of arrow appearance on EA chart to the arrow on non EA chart.By logic they should appear on the same time. If anybody could help to exam it ,it will be appreciated.  
  
2\. If there are more than two opened positions,when an opposite singal appears it only close one position with the other one left unclosed.Then the situation will carry on, there will be always a position unclosed.Which contribute loss of the testing.Because when the PA changes its direction,the unclosed position will be closed in a negative figure and all trade since after will suffer the same.could you help to make EA close all the position?  
  
3.did not find any repaint arrow. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#382](/thread/post/2665872#post2665872 "Post Permalink")

  * Apr 14, 2009 12:13am  Apr 14, 2009 12:13am 

  * [ perjo](perjo)

  * | Joined Nov 2008  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=86171)

hello   
i just wanna say something for the EA, in fact the problem is not that it repaint or not. The EA must only buy or sell one time, the first time arrow appear and after that the problem Lyllia talk dont exist anymore. (sorry for english) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#383](/thread/post/2666080#post2666080 "Post Permalink")

  * Apr 14, 2009 1:46am  Apr 14, 2009 1:46am 

  * [ Corppu](corppu)

  * | Joined Jun 2008  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=72090)

[quote=lyllia;2665679]To Peter,  
  

> Quote
> 
> Disliked
> 
> I have tested the EA during the weekend on euro.The following is what I find out:  
>    
>  1\. The ea open position at the end of the bar.This is in line with many EA' s method around.It seems nothing wrong with it.But for trading purpose,sometime it seems like a delayed entry.I have...

  
I have noticed the same problems. There should only be one trade opened in one direction at a time and the signals (trades) should be forced through in order to close/open trades and avoid missed/unclosed trades. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#384](/thread/post/2666290#post2666290 "Post Permalink")

  * Apr 14, 2009 3:09am  Apr 14, 2009 3:09am 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

I would like to see someone post a screen shot showing a backtest on any pair showing buys/sells along with the IINWMARROWS indy, showing an arrow for every trade. (proving there is norepaint  
  
Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#385](/thread/post/2666328#post2666328 "Post Permalink")

  * Apr 14, 2009 3:28am  Apr 14, 2009 3:28am 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

[quote=lyllia;2665679]To Peter,  
  
[quote]   
I have tested the EA during the weekend on euro.The following is what I find out:  
  
1\. The ea open position at the end of the bar.This is in line with many EA' s method around.It seems nothing wrong with it.But for trading purpose,sometime it seems like a delayed entry.I have not compared the the time of arrow appearance on EA chart to the arrow on non EA chart.By logic they should appear on the same time. If anybody could help to exam it ,it will be appreciated.  
  
I may be wrong, but I think when an EA is being run (or any program), the code says take a long position if condition "X" is true, when the bar opens it looks to see if condition "X" is true if so it takes the position, if not it waits for the next bar to try again, if condition "X" becomes true in the middle of the current bar the EA will not look at it till beginning of next bar, that’s how it reads bar by bar. I am not sure if tick by tick can be used or not if so I bet would be quite a task to code, the only other thing is somehow run the EA on a smaller TF but have the code read off the larger TF that way the EA would take a trade when the smaller TF bar was complete and the Lager TF condition was true. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#386](/thread/post/2666345#post2666345 "Post Permalink")

  * Apr 14, 2009 3:36am  Apr 14, 2009 3:36am 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

Here is a challenge, open Stratgey tester load LyliaEa as advisor set Tf to 4 hours, check use data, and visual mode, uncheck optimization, and press start, after it opens the chart add the IINWMARROWS indy and the arrows no repaint indy. Run it for several days turn up the speed so it gos trough rather quickly , IINWMARROWS should appear second to last bar and arrows no repaint appear at new bar, see if both indys create same arrows, see where Ea took positions from.  
  
Love to see what you get.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#387](/thread/post/2666804#post2666804 "Post Permalink")

  * Apr 14, 2009 8:26am  Apr 14, 2009 8:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar43332_2.gif) willmalou](willmalou)

  * | Joined Jul 2007  | Status: Think before you act!!! | [113 Posts](/search?do=process&provider=Member&searchuser=43332)

Lyllia please try this ea. It buys or sells on the closing of the new arrow. I think this is what you were looking for. It still opens the first time on the next bar, but after that whenever the arrows show it opens a new trade. I am not a coder just a cut and paste guy. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [LyliaMod.mq4](/attachment/file/232465?d=1239665054) 9 KB | 1,237 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#388](/thread/post/2667740#post2667740 "Post Permalink")

  * Edited 8:18pm  Apr 14, 2009 8:05pm | Edited 8:18pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting willmalou](/thread/post/2666804#post2666804 "View Quoted Post")
> 
> Disliked
> 
> Lyllia please try this ea. It buys or sells on the closing of the new arrow. I think this is what you were looking for. It still opens the first time on the next bar, but after that whenever the arrows show it opens a new trade. I am not a coder just a cut and paste guy.
> 
> Ignored

ok I have a try. thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#389](/thread/post/2669589#post2669589 "Post Permalink")

  * Apr 15, 2009 11:59am  Apr 15, 2009 11:59am 

  * [ yzzack](yzzack)

  * | Joined Jul 2008  | Status: Trader | [23 Posts](/search?do=process&provider=Member&searchuser=75218)

Thank you Lyllia for your system.   
  
I borrowed your arrows indicator and now making serious pips(more than 950 in 3 days). I got to have consistency for a few months before I go live.   
  
Thank you again. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#390](/thread/post/2670127#post2670127 "Post Permalink")

  * Apr 15, 2009 6:00pm  Apr 15, 2009 6:00pm 

  * [ gutek04](gutek04)

  * | Joined Mar 2009  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=95989)

> [Quoting yzzack](/thread/post/2669589#post2669589 "View Quoted Post")
> 
> Disliked
> 
> Thank you Lyllia for your system.   
>    
>  I borrowed your arrows indicator and now making serious pips(more than 950 in 3 days). I got to have consistency for a few months before I go live.   
>    
>  Thank you again.
> 
> Ignored

Will You share Youre method to us? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#391](/thread/post/2671988#post2671988 "Post Permalink")

  * Apr 16, 2009 7:58am  Apr 16, 2009 7:58am 

  * [ Silenthunter](silenthunter)

  * | Joined Dec 2008  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=89159)

> [Quoting yzzack](/thread/post/2669589#post2669589 "View Quoted Post")
> 
> Disliked
> 
> Thank you Lyllia for your system.   
>    
>  I borrowed your arrows indicator and now making serious pips(more than 950 in 3 days). I got to have consistency for a few months before I go live.   
>    
>  Thank you again.
> 
> Ignored

How do you use it? what time frame ? template please.  
thanks a lot. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#392](/thread/post/2672517#post2672517 "Post Permalink")

  * Edited 4:26pm  Apr 16, 2009 2:19pm | Edited 4:26pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting willmalou](/thread/post/2666804#post2666804 "View Quoted Post")
> 
> Disliked
> 
> Lyllia please try this ea. It buys or sells on the closing of the new arrow. I think this is what you were looking for. It still opens the first time on the next bar, but after that whenever the arrows show it opens a new trade. I am not a coder just a cut and paste guy.
> 
> Ignored

Thanks willmalou.  
I test only one pair: Euro at the weekend.Now the position will be buy/sell at the close of the bar (not end). When I was doing the test it seems the quick the speed sometimes the remote the position buy/sell.Anybody have the same problem?Maybe in real situation is not same.  
  
anybody tried the new EA? and what's the result?any suggestions.  
  
I really appreciate perjo and Corppu's suggestion that open one position at one directon. I assum it is on 4hr chart.So the entry(buy/sell) should be determined by the collective comfirmation of all the indicators used in the system like manual trading.That way will get rid of the noise and make consistant profitable pips.  
  
If anybody could work out the plan please post here. And let peter and willmalow help us again.Appreciate your help. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#393](/thread/post/2677504#post2677504 "Post Permalink")

  * Apr 18, 2009 2:12pm  Apr 18, 2009 2:12pm 

  * [ Rascalz](rascalz)

  * | Joined Apr 2009  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=99916)

Hi Lyllia and everyone,  
  
Would someone be able to elaborate when does the arrow appears? At the start of a new candle after the last closed candle or at the close of a candle?  
  
Thanks.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#394](/thread/post/2677817#post2677817 "Post Permalink")

  * Apr 19, 2009 12:49am  Apr 19, 2009 12:49am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting Rascalz](/thread/post/2677504#post2677504 "View Quoted Post")
> 
> Disliked
> 
> Hi Lyllia and everyone,  
>    
>  Would someone be able to elaborate when does the arrow appears? At the start of a new candle after the last closed candle or at the close of a candle?  
>    
>  Thanks..
> 
> Ignored

The arrow appears when the cross up /down conditions have been met.See the coding of the indicator (post2).I assum it could be anywhere during the bar formation in any TF. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#395](/thread/post/2677968#post2677968 "Post Permalink")

  * Apr 19, 2009 4:06am  Apr 19, 2009 4:06am 

  * [ yzzack](yzzack)

  * | Joined Jul 2008  | Status: Trader | [23 Posts](/search?do=process&provider=Member&searchuser=75218)

For those who asked me about my system and template. I have to admit that after gaining those pips I lost more than half. so I still have to adjust my system , but the basic principle is there . This is the template and it's self explanatory. I trade on the 4 hr TF 8 different pairs, lot size is .05 and I put a stop loss of 200 pips. I open two orders. On one the take profit is 20 to 25 pips, the other when it reaches that many (20,25) pips the stop loss is moved to break-even and I let it ride. Suggestions are appreciated. I only check the charts every four hours and its less stressful but I do use the help of an EA to move to break-even. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: usdcad23.gif
Size: 62 KB](/attachment/image/234858/thumbnail?d=1365568453)](/attachment/image/234858?d=1240081550)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#396](/thread/post/2678708#post2678708 "Post Permalink")

  * Apr 20, 2009 12:55am  Apr 20, 2009 12:55am 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

I delete last few posts.Because it does not work.So I take it back. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#397](/thread/post/2678901#post2678901 "Post Permalink")

  * Apr 20, 2009 3:27am  Apr 20, 2009 3:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar96656_4.gif) $aly]($aly)

  * | Commercial User  | Joined Mar 2009 | [183 Posts](/search?do=process&provider=Member&searchuser=96656)

> [Quoting yzzack](/thread/post/2677968#post2677968 "View Quoted Post")
> 
> Disliked
> 
> For those who asked me about my system and template....
> 
> Ignored

hi there  
  
i have all of your indicators and your template.... it's different from Lyllia's trading system ...if anyone want to try it i will post them here .....  
by the way what's your wins percentage till now my friend????  
  
be happy 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#398](/thread/post/2679359#post2679359 "Post Permalink")

  * Apr 20, 2009 8:45am  Apr 20, 2009 8:45am 

  * [ Rascalz](rascalz)

  * | Joined Apr 2009  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=99916)

Why not let's us try them out ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#399](/thread/post/2679851#post2679851 "Post Permalink")

  * Apr 20, 2009 1:27pm  Apr 20, 2009 1:27pm 

  * [ yzzack](yzzack)

  * | Joined Jul 2008  | Status: Trader | [23 Posts](/search?do=process&provider=Member&searchuser=75218)

My winning percentage is about 80% the 20% really gets me. Actually the template I posted is I think an improved version and will try it out. I also think that If I have a loser trade I should get out sooner and lose little instead of losing a lot and that is what happened when I lost more than half of the pips I had already made. One more thing the aqua line on the chart is Mama but I erased the slow line and posted the xpma at (9) instead. Of course this is my main indicator, the arrows and the rest of the indicators are for confirmation only.   
  
I made trades this Sunday and banked 60 pips right away and then another 20.   
  
This is the template with the trades that were active at this moment. I initiated these trades based on the fact that the trend was down and on the audusd the lines were crossing. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: picture.gif
Size: 94 KB](/attachment/image/235224/thumbnail?d=1365568537)](/attachment/image/235224?d=1240201572)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#400](/thread/post/2680492#post2680492 "Post Permalink")

  * Apr 20, 2009 6:41pm  Apr 20, 2009 6:41pm 

  * [ olachico](olachico)

  * | Joined Apr 2009  | Status: Trader | [45 Posts](/search?do=process&provider=Member&searchuser=99080)

> [Quoting yzzack](/thread/post/2679851#post2679851 "View Quoted Post")
> 
> Disliked
> 
> My winning percentage is about 80% the 20%...
> 
> Ignored

  
can you post the indicator, please? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#401](/thread/post/2681020#post2681020 "Post Permalink")

  * Apr 20, 2009 10:18pm  Apr 20, 2009 10:18pm 

  * [ yzzack](yzzack)

  * | Joined Jul 2008  | Status: Trader | [23 Posts](/search?do=process&provider=Member&searchuser=75218)

Here is another shot at how my trades developed this morning. I already have a little bit more than 100 pips banked and making more than 250 pips this morning, but I am letting it ride and to see what happenes. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: picture2.gif
Size: 70 KB](/attachment/image/235483/thumbnail?d=1365568588)](/attachment/image/235483?d=1240233465)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#402](/thread/post/2681125#post2681125 "Post Permalink")

  * Apr 20, 2009 11:02pm  Apr 20, 2009 11:02pm 

  * [ yzzack](yzzack)

  * | Joined Jul 2008  | Status: Trader | [23 Posts](/search?do=process&provider=Member&searchuser=75218)

Sorry I added wrong since each pip is worth $.50 cents then I have already banked more than 200 pips, as you can see by the balance. This is a brand new account that I started with a $5000.00 dollars.   
  
I think this is a pretty good trading system it is just that some of the rules and indicators have to be defined clearly. I wont be this lucky always you know making all of my trades 100% winners, well I am not going to lose any of the trades that are active since the EA has already moved the stop loss to break even, but the percentage is high. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#403](/thread/post/2681570#post2681570 "Post Permalink")

  * Apr 21, 2009 1:16am  Apr 21, 2009 1:16am 

  * [ yzzack](yzzack)

  * | Joined Jul 2008  | Status: Trader | [23 Posts](/search?do=process&provider=Member&searchuser=75218)

The trades that I placed yesterday progressed nicely.   
  
But I still sometimes have trouble understanding the EA that breaks even. Because sometimes it does not breakeven and the order to break even is missed. Then I have a loser trade that I have to close out manually.   
  
Can somebody explain the proper way to prepare the EA for breaking even. I might be doing something wrong.  
  
Anyways at the moment I am making more than 400 pips. Plus 200 already banked for a total of more than 600 pips in less than a day. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: picture3.gif
Size: 69 KB](/attachment/image/235569/thumbnail?d=1365568615)](/attachment/image/235569?d=1240244178)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#404](/thread/post/2685358#post2685358 "Post Permalink")

  * Apr 22, 2009 5:57am  Apr 22, 2009 5:57am 

  * [ forextek](forextek)

  * | Joined Apr 2009  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=98929)

> [Quoting yzzack](/thread/post/2679851#post2679851 "View Quoted Post")
> 
> Disliked
> 
> My winning percentage is about 80% the 20% really gets me. Actually the template I posted is I think an improved version and will try it out. I also think that If I have a loser trade I should get out sooner and lose little instead of losing a lot and that is what happened when I lost more than half of the pips I had already made. One more thing the aqua line on the chart is Mama but I erased the slow line and posted the xpma at (9) instead. Of course this is my main indicator, the arrows and the rest of the indicators are for confirmation only....
> 
> Ignored

  
where is this template I do not see it? was it removed? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#405](/thread/post/2685934#post2685934 "Post Permalink")

  * Apr 22, 2009 10:55am  Apr 22, 2009 10:55am 

  * [ yzzack](yzzack)

  * | Joined Jul 2008  | Status: Trader | [23 Posts](/search?do=process&provider=Member&searchuser=75218)

I am getting killed right now but adjusted the XpMa to (7) . I think this change will prevent this from happening again. Still holding on to the trades but they are all losers. I am losing about $600 dollars at this moment. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#406](/thread/post/2686436#post2686436 "Post Permalink")

  * Apr 22, 2009 4:48pm  Apr 22, 2009 4:48pm 

  * [ jamesfr](jamesfr)

  * | Joined Mar 2009  | Status: Trader | [76 Posts](/search?do=process&provider=Member&searchuser=95609)

Looks like this thread is sidetracking.  
  
Is anyone working on an EA for Lyllia's original system? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#407](/thread/post/2693702#post2693702 "Post Permalink")

  * Apr 25, 2009 2:28am  Apr 25, 2009 2:28am 

  * [ yzzack](yzzack)

  * | Joined Jul 2008  | Status: Trader | [23 Posts](/search?do=process&provider=Member&searchuser=75218)

I had not posted for a while, I was collecting myself after I saw how the last trades were developing. so I bailed out losing about $900.00 dollars. If I had waited because my SL was 200 pip it would have never hit it, and today I would have been $900.00 dollars ahead. Anyways just wanted to give you guys an update. Nobody has posted nothing so I think I will stop posting.   
  
About the EA, I really would like to trust them but I have not found a consist ant EA. If it is profitable I think I would test it first for three month or so. Up to know I have tested FXproadvisors trend catcher and in two weeks it has made close to $2000.00 on a $5000.00 demo account. I also bought the other one called scalper HR1 but that one has lost $3000.00 dollars on 5000.00 demo account. Anyways good bye. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#408](/thread/post/2694327#post2694327 "Post Permalink")

  * Apr 25, 2009 6:24pm  Apr 25, 2009 6:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar12384_5.gif) mxb](mxb)

  * | Joined Jun 2006  | Status: Trader | [241 Posts](/search?do=process&provider=Member&searchuser=12384)

can we get a alert on this IINWMARROWS.mq4? You have to be glued to the chart to catch them...  
thx ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#409](/thread/post/2696634#post2696634 "Post Permalink")

  * Apr 27, 2009 5:36pm  Apr 27, 2009 5:36pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

> [Quoting jamesfr](/thread/post/2686436#post2686436 "View Quoted Post")
> 
> Disliked
> 
> Looks like this thread is sidetracking.  
>    
>  Is anyone working on an EA for Lyllia's original system?
> 
> Ignored

Hi everyone,  
  
I have not post for a while. I tried to solve the problem about this system Ea.Until now getting no where.I am not a programmer myself.but I could read code .Both version of EA are good basically.I think the problem part comes from the Arrow.sometimes it appears very late, but signal is still valid.So that cause the delayed signal of the positon opening.   
  
Both EA could not close all the postions opened in one TF.  
  
For an example, it there are two selling arrows before a buying arrow,the buying arrow should close the previous two sell positions and open a new buy position as well. Now the real situation is if there are two selling arrows appear one after another. the second sell arrow doesl not SELL instead it closes the previous sell arrow and opens a BUY position. This is definitely wrong about this system.then the buy arrow appears it close the buy position by the second sell arrow and opens a SELL position.then every position after will close each other in red.Do you see what I mean.  
  
Anyone could help solve this problem with EA. Like I said I still want to work out better way for EA to trade.Any suggestons? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#410](/thread/post/2709875#post2709875 "Post Permalink")

  * May 3, 2009 11:46pm  May 3, 2009 11:46pm 

  * [ bobcat275](bobcat275)

  * | Joined Sep 2008  | Status: Trader | [24 Posts](/search?do=process&provider=Member&searchuser=79479)

Hi,  
  
Can you post the alpha center timesignal indicator from post 209 # 15  
  
Thanks [topcat275@yahoo.com](mailto:topcat275@yahoo.com)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#411](/thread/post/2808145#post2808145 "Post Permalink")

  * Jun 17, 2009 11:17am  Jun 17, 2009 11:17am 

  * [ BobHall](bobhall)

  * | Membership Revoked  | Joined Jun 2009 | [557 Posts](/search?do=process&provider=Member&searchuser=106294)

Thank you for sharing your strategy Lyllia.  
  
The Beginners Alert indicator doesn't update itself properly. I have to switch to different time frames all the time to see it plot it self on the chart again.  
  
  
The arrow one is ok, but only for 1H time frames or above during trending markets, or it'll cause false signals, or very small gains.  
  
I tried your EA and it never worked for me.  
  
Best of luck 

PM Me If You Need Help!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#412](/thread/post/2808146#post2808146 "Post Permalink")

  * Jun 17, 2009 11:18am  Jun 17, 2009 11:18am 

  * [ BobHall](bobhall)

  * | Membership Revoked  | Joined Jun 2009 | [557 Posts](/search?do=process&provider=Member&searchuser=106294)

That indicator repaints itself, I would not use it.  
  

> [Quoting bobcat275](/thread/post/2709875#post2709875 "View Quoted Post")
> 
> Disliked
> 
> Hi,  
>    
>  Can you post the alpha center timesignal indicator from post 209 # 15  
>    
>  Thanks [topcat275@yahoo.com](mailto:topcat275@yahoo.com)
> 
> Ignored

PM Me If You Need Help!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#413](/thread/post/2883409#post2883409 "Post Permalink")

  * Jul 18, 2009 10:37pm  Jul 18, 2009 10:37pm 

  * [ NormBo](normbo)

  * | Joined Dec 2008  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=88678)

> [Quoting lyllia](/thread/post/2696634#post2696634 "View Quoted Post")
> 
> Disliked
> 
> Hi everyone,  
>    
>  I have not post for a while. I tried to solve the problem about this system Ea.Until now getting no where.I am not a programmer myself.but I could read code .Both version of EA are good basically.I think the problem part comes from the Arrow.sometimes it appears very late, but signal is still valid.So that cause the delayed signal of the positon opening.   
>    
>  Both EA could not close all the postions opened in one TF.  
>    
>  For an example, it there are two selling arrows before a buying arrow,the buying arrow should close the previous two...
> 
> Ignored

I have just discovered this thread and am very impressed with your manual system. There is a guy named findmanu <http://www.forexfactory.com/member.php?u=102657> who has a thread that says he will code an EA for free. I did a search on his thread for "Lyllia" and it seems that no one has ever requested his assistance. Check out his thread, it appears that he has had pretty good success in the past. It would be awesome to get this working as an EA. THANKS FOR ALL YOUR POST. Blessings!!![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#414](/thread/post/2975561#post2975561 "Post Permalink")

  * Aug 21, 2009 11:34pm  Aug 21, 2009 11:34pm 

  * [ Traderdf](traderdf)

  * | Joined Aug 2009  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=113348)

Can anyone tell me how to trigger the trailing stop. The EA doesn't seem to do that automatically 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#415](/thread/post/3270613#post3270613 "Post Permalink")

  * Dec 1, 2009 12:18am  Dec 1, 2009 12:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar103015_1.gif) dancingphil](dancingphil)

  * Joined May 2009 | Status: Trader | [667 Posts](/search?do=process&provider=Member&searchuser=103015)

> [Quoting pitpiter](/thread/post/2635535#post2635535 "View Quoted Post")
> 
> Disliked
> 
> I find bug , here is workable version
> 
> Ignored

Hey Pitpiter, I am interested in this EA of yours, but I would like to use dynamic money-management.  
  
I notice in the scalping FX Prime EA you built that you have dynamic code for it.  
  
I was wondering what code I should/could add to your Lyllia EA?  
  
In fact I would love to have dynamic money-management code that I could cut and past into any and all EA's I test. But for now would be very happy if you can help with the Lyllia EA.  
  
Thx  
  
DancingPhil 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#416](/thread/post/3501319#post3501319 "Post Permalink")

  * Feb 26, 2010 5:27pm  Feb 26, 2010 5:27pm 

  * [ unclek6](unclek6)

  * | Joined Jul 2009  | Status: Trader | [29 Posts](/search?do=process&provider=Member&searchuser=108612)

> [Quoting lyllia](/thread/post/2635430#post2635430 "View Quoted Post")
> 
> Disliked
> 
> weekly new high ahead.daily and 4hrs new low need to be confirmed
> 
> Ignored

Iyllia, thanks for sharing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#417](/thread/post/3932903#post3932903 "Post Permalink")

  * Aug 10, 2010 3:35am  Aug 10, 2010 3:35am 

  * [ kneal](kneal)

  * | Joined Jul 2010  | Status: Trader | [24 Posts](/search?do=process&provider=Member&searchuser=148457)

Did anyone perfect this EA? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#418](/thread/post/5549589#post5549589 "Post Permalink")

  * Apr 7, 2012 2:20am  Apr 7, 2012 2:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar28987_1.gif) charvo](charvo)

  * Joined Dec 2006 | Status: Backtest is meaningless (to me) | [2,176 Posts](/search?do=process&provider=Member&searchuser=28987)

Why is the only valuable post in the early development of this confusing yet crappy system ignored?  
  
noobs are incredible......  
  

> [Quoting hemantaims](/thread/post/2636782#post2636782 "View Quoted Post")
> 
> Disliked
> 
> Hey guys i have just backtested lyliaEA Posted on post no 62. Results are no so promising. date of backtesting is from 1-1-2007 to 30-3-1009.just have a look.   
>    
>  May be some modification is required in EA.![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#419](/thread/post/6184355#post6184355 "Post Permalink")

  * Nov 12, 2012 5:16am  Nov 12, 2012 5:16am 

  * [ fuctuations](fuctuations)

  * | Joined Jul 2012  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=268823)

> [Quoting kneal](/thread/post/3932903#post3932903 "View Quoted Post")
> 
> Disliked
> 
> Did anyone perfect this EA?
> 
> Ignored

if this strategy really can make money, i can code for it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#420](/thread/post/12336919#post12336919 "Post Permalink")

  * Jun 19, 2019 5:01am  Jun 19, 2019 5:01am 

  * [ Mitchwakahn](mitchwakahn)

  * | Joined Jun 2019  | Status: Trader | [44 Posts](/search?do=process&provider=Member&searchuser=819435)

I cloned the triple arrow system from Super EZ Forex.. Pretty damn good job if i do say so myself. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: tripplearrow.PNG
Size: 39 KB](/attachment/image/3364657/thumbnail?d=1560888074)](/attachment/image/3364657?d=1560888074)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#421](/thread/post/12347419#post12347419 "Post Permalink")

  * Jun 25, 2019 12:17am  Jun 25, 2019 12:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar141121_8.gif) Hutch](hutch)

  * Joined Apr 2010 | Status: Lazy trader on D1 charts | [5,906 Posts](/search?do=process&provider=Member&searchuser=141121)

> [Quoting Wavegarrick](/thread/post/12345449#post12345449 "View Quoted Post")
> 
> Disliked
> 
> {quote} Always a good cause, well done.
> 
> Ignored

Thank you but successful traders should always give time and/or money to those that are not as well off as they are.   
  
A few traders wanted the indicators to the system I posted yesterday so here they are with the template. Good luck with your trades. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [EMA Trading.zip](/attachment/file/3369476?d=1561389380) 87 KB | 1,592 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#422](/thread/post/12395904#post12395904 "Post Permalink")

  * Jul 22, 2019 10:18pm  Jul 22, 2019 10:18pm 

  * [ lyllia](lyllia)

  * | Joined Apr 2008  | Status: Trader | [215 Posts](/search?do=process&provider=Member&searchuser=67706)

Hi everybody, how things are going? welcome to continually contribute to this thread. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#423](/thread/post/12396058#post12396058 "Post Permalink")

  * Jul 22, 2019 11:32pm  Jul 22, 2019 11:32pm 

  * [ Azz1](azz1)

  * | Joined Dec 2018  | Status: Trader | [18 Posts](/search?do=process&provider=Member&searchuser=741800)

> [Quoting lyllia](/thread/post/12395904#post12395904 "View Quoted Post")
> 
> Disliked
> 
> Hi everybody, how things are going? welcome to continually contribute to this thread.
> 
> Ignored

Hello, you still use this system? How is it going? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#424](/thread/post/12410866#post12410866 "Post Permalink")

  * Jul 30, 2019 7:06pm  Jul 30, 2019 7:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar290066_1.gif) scubemedia1](scubemedia1)

  * | Joined Sep 2012  | Status: Trader | [99 Posts](/search?do=process&provider=Member&searchuser=290066)

> [Quoting lyllia](/thread/post/12395904#post12395904 "View Quoted Post")
> 
> Disliked
> 
> hi everybody, how things are going? Welcome to continually contribute to this thread.
> 
> Ignored

any chnace to get ea for this indicators? 

5-20% withadraw daily

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#425](/thread/post/12412561#post12412561 "Post Permalink")

  * Jul 31, 2019 3:04pm  Jul 31, 2019 3:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar834516_1.gif) BTM](btm)

  * | Additional Username  | Joined Jul 2019 | [577 Posts](/search?do=process&provider=Member&searchuser=834516)

> [Quoting yzzack](/thread/post/2681570#post2681570 "View Quoted Post")
> 
> Disliked
> 
> The trades that I placed yesterday progressed nicely. But I still sometimes have trouble understanding the EA that breaks even. Because sometimes it does not breakeven and the order to break even is missed. Then I have a loser trade that I have to close out manually. Can somebody explain the proper way to prepare the EA for breaking even. I might be doing something wrong. Anyways at the moment I am making more than 400 pips. Plus 200 already banked for a total of more than 600 pips in less than a day. {image}
> 
> Ignored

does i_trend indicator makes repaint ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#426](/thread/post/12543460#post12543460 "Post Permalink")

  * Oct 7, 2019 4:12am  Oct 7, 2019 4:12am 

  * [ bluedocfx191](bluedocfx191)

  * | Joined Aug 2019  | Status: Trader | [48 Posts](/search?do=process&provider=Member&searchuser=843330)

> [Quoting Mitchwakahn](/thread/post/12336919#post12336919 "View Quoted Post")
> 
> Disliked
> 
> I cloned the triple arrow system from Super EZ Forex.. Pretty damn good job if i do say so myself. {image}
> 
> Ignored

what indicators make this up? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#427](/thread/post/12545159#post12545159 "Post Permalink")

  * Oct 8, 2019 1:57am  Oct 8, 2019 1:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar141121_8.gif) Hutch](hutch)

  * Joined Apr 2010 | Status: Lazy trader on D1 charts | [5,906 Posts](/search?do=process&provider=Member&searchuser=141121)

> [Quoting BTM](/thread/post/12412561#post12412561 "View Quoted Post")
> 
> Disliked
> 
> {quote} does i_trend indicator makes repaint ?
> 
> Ignored

I_trend is the same as the ADX indicator and doesn't repaint but you should re-compute it when there is a MT4 update. Here is the .mq4 file. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [i_Trend.mq4](/attachment/file/3458310?d=1570467395) 3 KB | 743 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#428](/thread/post/12573904#post12573904 "Post Permalink")

  * Oct 22, 2019 6:07am  Oct 22, 2019 6:07am 

  * [ rcrane](rcrane)

  * | Joined Oct 2019  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=867369)

This is the original creator of the Triple Arrow system not Super EZ Forex  

Inserted Video

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#429](/thread/post/12573913#post12573913 "Post Permalink")

  * Oct 22, 2019 6:12am  Oct 22, 2019 6:12am 

  * [ rcrane](rcrane)

  * | Joined Oct 2019  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=867369)

Triple Arrow indis 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [auto trend lines.ex4](/attachment/file/3470224?d=1571692207) 7 KB | 1,162 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [big arrow.ex4](/attachment/file/3470225?d=1571692207) 4 KB | 1,298 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [entry arrow.ex4](/attachment/file/3470226?d=1571692207) 10 KB | 1,323 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [fibonacci-retracement.ex4](/attachment/file/3470227?d=1571692208) 14 KB | 1,041 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Little Arrow.v2.ex4](/attachment/file/3470228?d=1571692208) 18 KB | 1,317 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [MACD TRUE COLOR.ex4](/attachment/file/3470229?d=1571692208) 13 KB | 1,038 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [support-and-resistance-mtf.ex4](/attachment/file/3470230?d=1571692208) 83 KB | 1,145 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Symbol changer 1.1 separate (2).ex4](/attachment/file/3470231?d=1571692208) 15 KB | 968 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [yellow arrow.ex4](/attachment/file/3470232?d=1571692209) 5 KB | 1,259 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#430](/thread/post/12573914#post12573914 "Post Permalink")

  * Oct 22, 2019 6:12am  Oct 22, 2019 6:12am 

  * [ rcrane](rcrane)

  * | Joined Oct 2019  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=867369)

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Buy-Sell.ex4](/attachment/file/3470234?d=1571692358) 3 KB | 1,011 downloads 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [C-BIRD.ex4](/attachment/file/3470235?d=1571692358) 10 KB | 876 downloads 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [HelpLine.ex4](/attachment/file/3470236?d=1571692358) 11 KB | 824 downloads 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Info Plus.ex4](/attachment/file/3470237?d=1571692358) 49 KB | 837 downloads 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [TMA-1 (1).ex4](/attachment/file/3470238?d=1571692359) 10 KB | 766 downloads 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [trend filter.ex4](/attachment/file/3470239?d=1571692359) 13 KB | 873 downloads 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Trum Amazing Bar Chart.ex4](/attachment/file/3470240?d=1571692359) 284 KB | 893 downloads 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#431](/thread/post/12581170#post12581170 "Post Permalink")

  * Oct 25, 2019 5:17am  Oct 25, 2019 5:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar141121_8.gif) Hutch](hutch)

  * Joined Apr 2010 | Status: Lazy trader on D1 charts | [5,906 Posts](/search?do=process&provider=Member&searchuser=141121)

> [Quoting rcrane](/thread/post/12573913#post12573913 "View Quoted Post")
> 
> Disliked
> 
> Triple Arrow indis {file} {file} {file} {file} {file} {file} {file} {file} {file}
> 
> Ignored

Thank you rcrane. Triple Arrow looks like a complex system compared to the simple system I use but there is always added value in trying a new system.   
The attached chart shows RENKO 10 pips with EMA Cross 5/8. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: GBPNZD-4M2.png
Size: 36 KB](/attachment/image/3473213/thumbnail?d=1571948241)](/attachment/image/3473213?d=1571948241)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#432](/thread/post/12678401#post12678401 "Post Permalink")

  * Dec 28, 2019 12:37am  Dec 28, 2019 12:37am 

  * [ Mitchwakahn](mitchwakahn)

  * | Joined Jun 2019  | Status: Trader | [44 Posts](/search?do=process&provider=Member&searchuser=819435)

Inserted Video

  
  
Working well 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#433](/thread/post/12698241#post12698241 "Post Permalink")

  * Jan 11, 2020 5:50pm  Jan 11, 2020 5:50pm 

  * [ daughtry](daughtry)

  * | Joined Jul 2019  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=830460)

> [Quoting rcrane](/thread/post/12573913#post12573913 "View Quoted Post")
> 
> Disliked
> 
> Triple Arrow indis {file} {file} {file} {file} {file} {file} {file} {file} {file}
> 
> Ignored

Hi bro,  
Please could you assist with a template.  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#434](/thread/post/12698690#post12698690 "Post Permalink")

  * Jan 12, 2020 11:07am  Jan 12, 2020 11:07am 

  * [ rcrane](rcrane)

  * | Joined Oct 2019  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=867369)

> [Quoting Mitchwakahn](/thread/post/12336919#post12336919 "View Quoted Post")
> 
> Disliked
> 
> I cloned the triple arrow system from Super EZ Forex.. Pretty damn good job if i do say so myself. {image}
> 
> Ignored

Why would you want to? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#435](/thread/post/12720358#post12720358 "Post Permalink")

  * Jan 25, 2020 4:53am  Jan 25, 2020 4:53am 

  * [ Mitchwakahn](mitchwakahn)

  * | Joined Jun 2019  | Status: Trader | [44 Posts](/search?do=process&provider=Member&searchuser=819435)

> [Quoting rcrane](/thread/post/12698690#post12698690 "View Quoted Post")
> 
> Disliked
> 
> {quote} why would you want to?
> 
> Ignored

just because i can. Making good profits too. What about you? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#436](/thread/post/12958461#post12958461 "Post Permalink")

  * May 22, 2020 11:03pm  May 22, 2020 11:03pm 

  * [ mikep1](mikep1)

  * | Joined May 2020  | Status: Trader | [18 Posts](/search?do=process&provider=Member&searchuser=949437)

> [Quoting Mitchwakahn](/thread/post/12336919#post12336919 "View Quoted Post")
> 
> Disliked
> 
> I cloned the triple arrow system from Super EZ Forex.. Pretty damn good job if i do say so myself. {image}
> 
> Ignored

Hi Mitchwakahn  
Please see if possible ...please upload template of the chart and all indicators you used. That will help us all.  
thanks a lot. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#437](/thread/post/12959932#post12959932 "Post Permalink")

  * Edited 6:11am  May 24, 2020 6:01am | Edited 6:11am 

  * [ Mactormind](mactormind)

  * | Joined Jan 2019  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=752754)

Good luck to any and all of you that think youll make any money using x3arrow system. Yes, it has some great runs but long term your losers will outweigh the winners very quickly. But at least you guys didnt pay the $300 Pat(owner) charged for the indicators in this system that you can find free online. I was in the SuperEZ group for over a year and quickly realized that Pat (owner) was nothing more than a lier and highly manipulative individual. Trust me guys theres waaaay better systems out ther you can invest your time in. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#438](/thread/post/13285603#post13285603 "Post Permalink")

  * Edited Nov 28, 2020 2:03am  Nov 27, 2020 11:17pm | Edited Nov 28, 2020 2:03am 

  * [ nxvz](nxvz)

  * | Joined Nov 2020  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=1032773)

Sir, i am a newbe here i was asking if someone could please mod this lyllia's EA into exponential buying/selling lot size (martingale), please sir do consider , sorry for my eng if any wrong, thnx please reply.  
  
[https://www.forexfactory.com/attachm...3&d=1238332687](https://www.forexfactory.com/attachment.php/225363?attachmentid=225363&d=1238332687)

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [lyliaEA.mq4](/attachment/file/3799678?d=1606496574) 3 KB | 341 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#439](/thread/post/13286153#post13286153 "Post Permalink")

  * Nov 28, 2020 8:37am  Nov 28, 2020 8:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar141121_8.gif) Hutch](hutch)

  * Joined Apr 2010 | Status: Lazy trader on D1 charts | [5,906 Posts](/search?do=process&provider=Member&searchuser=141121)

> [Quoting nxvz](/thread/post/13285603#post13285603 "View Quoted Post")
> 
> Disliked
> 
> Sir, i am a newbe here i was asking if someone could please mod this lyllia's EA into exponential buying/selling lot size (martingale), please sir do consider , sorry for my eng if any wrong, thnx please reply. [https://www.forexfactory.com/attachm...3&d=1238332687](https://www.forexfactory.com/attachment.php/225363?attachmentid=225363&d=1238332687) {file}
> 
> Ignored

Please ask the coders in the "**I will code your EAs and Indicators for no charge"** thread. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#440](/thread/post/13289563#post13289563 "Post Permalink")

  * Dec 1, 2020 11:56am  Dec 1, 2020 11:56am 

  * [ BTS0301](bts0301)

  * | Joined Jun 2020  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=966984)

> [Quoting Hutch](/thread/post/12347419#post12347419 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thank you but successful traders should always give time and/or money to those that are not as well off as they are. A few traders wanted the indicators to the system I posted yesterday so here they are with the template. Good luck with your trades. {file}
> 
> Ignored

Hi Hutch.  
I'm having trouble with the Infoboard as it's only showing the data you entered manually into it. Is there a way to change this so that the info displayed reflects the chart its on?  
Thanks heaps 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

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

[HYBRID: trading system within a trading system](/thread/302279-hybrid-trading-system-within-a-trading-system "No man can capture all the fluctuations.....Jesse Livermore..... 
 
FRACTALS/HYBRID:trading system within a trading system 
 
Generally,...") 31 replies

[Please suggest a simple & effective Method/System of "Trading System" Forum to newbie](/thread/35860-please-suggest-a-simple-effective-methodsystem-of "Dear Friends in FF, 
  
I have read most threads of 5 stars trading strategys and methods form &quot;Trading System&quot; Forums of FF, but certain...") 180 replies

[WatchMyZone trading system - WMZ system](/thread/1107590-watchmyzone-trading-system-wmz-system "Welcome to WatchMyZone trading system - WMZ system 
  
Hello dear traders this is Anjan, My username is watchmyzone. I don’t know why I...") 7 replies

[Day Trading system - Simple system to make money](/thread/1002782-day-trading-system-simple-system-to-make "Hi to all, 
  
I am testing this system. i had attached the beta version of two indicators.Both are simple indicators. one indicator used...") 51 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)
  * Subscribe
  * [136](javascript:void\(0\);)

Attachments: lyllia's trading system

Tags: lyllia's trading system

#  [](/thread/160639-lyllias-trading-system)lyllia's trading system 

  * 

  * [#441](/thread/post/13291520#post13291520 "Post Permalink")

  * Dec 2, 2020 5:56am  Dec 2, 2020 5:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar141121_8.gif) Hutch](hutch)

  * Joined Apr 2010 | Status: Lazy trader on D1 charts | [5,906 Posts](/search?do=process&provider=Member&searchuser=141121)

> [Quoting BTS0301](/thread/post/13289563#post13289563 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Hutch. I'm having trouble with the Infoboard as it's only showing the data you entered manually into it. Is there a way to change this so that the info displayed reflects the chart its on? Thanks heaps
> 
> Ignored

This is totally new to me since I never had any problem with that indicator since it exclusively works on the chart it is on. The most likely error I can think of is that you did not click the "Allow DLL import" on the "Common" tab. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#442](/thread/post/13301783#post13301783 "Post Permalink")

  * Dec 8, 2020 10:51am  Dec 8, 2020 10:51am 

  * [ Slingshots1](slingshots1)

  * Joined Feb 2012 | Status: Trader | [1,709 Posts](/search?do=process&provider=Member&searchuser=225036)

> [Quoting Mitchwakahn](/thread/post/12678401#post12678401 "View Quoted Post")
> 
> Disliked
> 
> <https://youtu.be/tqr6yqZG72s> Working well
> 
> Ignored

Hy pls can you gimme the link to that background song on youtube THANKS 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#443](/thread/post/13326298#post13326298 "Post Permalink")

  * Dec 23, 2020 2:17am  Dec 23, 2020 2:17am 

  * [ slayerofpips](slayerofpips)

  * | Joined May 2019  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=805366)

> [Quoting rcrane](/thread/post/12573913#post12573913 "View Quoted Post")
> 
> Disliked
> 
> Triple Arrow indis {file} {file} {file} {file} {file} {file} {file} {file} {file}
> 
> Ignored

Do you by chance have an alert for the Little Arrow v2.ex4 indicator? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#444](/thread/post/13398937#post13398937 "Post Permalink")

  * Last Post: Feb 8, 2021 4:29pm  Feb 8, 2021 4:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar869316_2.gif) theonewalker](theonewalker)

  * | Joined Oct 2019  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=869316)

> [Quoting rcrane](/thread/post/12573914#post12573914 "View Quoted Post")
> 
> Disliked
> 
> {file}{file}{file}{file}{file}{file}{file}
> 
> Ignored

i need help if you can guid me using this indicator Trum Amazing Bar Chart..... the previous one not working on me at all, you dont mine to share with me the new one? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * lyllia's trading system
  *   * [ **Reply to Thread** ](/thread/160639-lyllias-trading-system/reply#reply)

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)
