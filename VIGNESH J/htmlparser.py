from html.parser import HTMLParser
class Parser(HTMLParser):
  # list start_tags.
  def handle_starttag(self, tag, attrs):
    global start_tags
    start_tags.append(tag)
    # list end_tags.
  def handle_endtag(self, tag):
    global end_tags
    end_tags.append(tag)
  #  list all_data.
  def handle_data(self, data):
    global all_data
    all_data.append(data)
  #  list comments.
  def handle_comment(self, data):
    global comments
    comments.append(data)
start_tags = []
end_tags = []
all_data = []
comments = []

parser = Parser()
# input.
parser.feed('<html><title>Desserts</title><body><p>'
            'HI,HELLO,HOW ARE YOU? .</p><'
            '/body><!--My Comment--></html>')
print("start tags:", start_tags)
print("end tags:", end_tags)
print("data:", all_data)
print("comments", comments)