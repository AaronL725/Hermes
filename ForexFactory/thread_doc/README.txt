26/02/2011

This Project started from Forex Factory Forum:
http://www.forexfactory.com/showthread.php?t=281832

Thanks to Ronnierott for share his System!

If you Like my Work pleas quote me on ForexFactory.

For any question my MSN/Email: eacoder@hotmail.it

Use this EA at your own risk!

Happy Pipping!



In this Package:
Ronnie EA, Some Libraries, Indicator and a Template.





SETTINGS INFO:

AutoTrading  = TRUE: will open pos - FALSE: it will NOT trade
Retracement_Alert = TRUE: when all the condition are meet it will alert on the  retracement

FixedLot = The Lotisize. If = 0 it will use Percent Money Menageent
Risk = The risk in percent of your capital per any trade
StopLoss = Stop Loss Distance in Pips (OK for 4 and 5 Digits )
TakeProfit = Take Profit Distance in Pips (OK for 4 and 5 Digits )

RetracementDistance = It will lookinig for retracement only if the price will touch this distance from the retracement EMA
EmaDistance = Min. Distance for Retracement EMA with Channel EMA
OrderDistance = Distance of the Sell/Buy Stop Order from HIGH/LOW

UseTrailingStop = Want to use Trailing Stop?
TrailingAfter = Start using TS after X pips
TrailingDistance = Distance of the new SL
TrailingStep = Trailing Stop Step

// SETTINGS OF THE INDICATOR IN ATTACHMENT
extern   string   Macd_With_Ema = "-------Settings-------";
extern   int      FastEMA = 35;
extern   int      SlowEMA = 70;
extern   int      SignalEMA = 1;
extern   int      MAofSignalPer = 12;

//SETTINGS OF THE RETRACEMENT EMA AND THE CHANNEL EMA
extern   string   Ema_Settings = "-------Settings-------";
extern   int      RetracementEMA = 15;
extern   int      ChannelEMA = 50;

extern   color    Text_Color = TEXT COLOR
extern   int      Magic = Magic Number