import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from dotenv import load_dotenv
from gpiozero import LED
from time import sleep

led1 = LED(18)
led2 = LED(14)
led3 = LED(15)
led4 = LED(23)


load_dotenv()


# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])


@app.command("/on")
def on(ack, body, logger):
    ack()
    logger.info(body)
    led1.on()
    sleep(1)
    led2.on()
    sleep(1)
    led3.on()
    sleep(1)
    led4.on()
   
@app.command("/off")
def close_light(ack, body, logger): 
    ack()
    logger.info(body)
    led1.off() 
    led1.off()
    sleep(1)
    led2.off()
    sleep(1)
    led3.off()
    sleep(1)
    led4.off()
    sleep(1)


@app.event("app_home_opened")
def update_home_tab(client, event, logger):
  try:
    # views.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
      # the user that opened your app's app home
      user_id=event["user"],
      # the view object that appears in the app home
      view={
        "type": "home",
        "callback_id": "home_view",

        # body of the view
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "*Welcome to Meeting Bot!* :tada:"
            }
          },
          {
            "type": "divider"
          },
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "Meeting bot let's the office know when you are on an important call. Use the command `/on` to let people know you are in meeting. When you are finished, `/off` will let people know you have finished."
            }
          }
        ]
      }
    )
  
  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")



if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()


