# curl the page and save content to tmp_file
# curl -H "Accept-Charset: utf-8" "https://www.lemon64.com/news/" > tmp_file
# All below commands will have as result "The content i want"
# Simple tag (within other tags)
# <ul class="list"><li class="specific_class"><span>The content i want</span></li><div>...
# cat tmp_file | grep "id=\"rnd_review\"" | cut -d'>' -f4 | cut -d'<' -f1
#sed -n '/<div id=\"rnd_review\">/,/<\/div>/p' tmp_file
python3 c64game.py
