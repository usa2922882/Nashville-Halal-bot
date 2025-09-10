from telegram.ext import ApplicationBuilder
application = ApplicationBuilder().token("8210249353:AAFvDJZgX2O-aSVLaxKjbp9Sg0J3pT770uo").build()
print("Bot ishga tushdi ✅")
application.run_polling()
