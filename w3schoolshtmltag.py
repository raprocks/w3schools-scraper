from helpers import get_soup, write_dict_to_json
from bs4 import BeautifulSoup


def scrape_tag(tagurl: str):
    soup = get_soup(tagurl)
    main_div = soup.find('div', 'id')
    # identifier = tagurl.split('/')[-1].split('tag_')[1].split('.asp')[0]
    soup = get_soup(tagurl)
    main_div = soup.find('div', id="main")
    br_tag = BeautifulSoup().new_tag(name='br')
    hr_tag = BeautifulSoup().new_tag(name='hr')
    # replace target tree with tree after first <br/> tag
    main_div_list = list(main_div)
    br_tag_index = main_div_list.index(br_tag)
    main_div_list = main_div_list[br_tag_index:]
    main_div = BeautifulSoup("".join(map(str, main_div_list)))
    # get table of compatibility
    # compatability_table = main_div.find('table')
    parts = []
    for i in len(main_div.find_all('hr')):
        hr_index = main_div_list.index(hr_tag)
        parts.append(main_div_list[:hr_index+1])
        main_div_list = main_div_list[hr_index:]
    parts.append(main_div_list)
    return main_div

# # <div class="w3-col l10 m12" id="main">
# # <div id="mainLeaderboard" style="overflow:hidden;">
# # <!-- MainLeaderboard-->
# # <!--<pre>main_leaderboard, all: [728,90][970,90][320,50][468,60]</pre>-->
# # <div id="snhb-main_leaderboard-0"></div>
# # <!-- adspace leaderboard -->
# # </div>
# # <h1>HTML <span class="color_h1">&lt;!--...--&gt;</span> Tag</h1>
# # <div class="w3-clear w3-center nextprev">
# # <a class="w3-left w3-btn" href="ref_keyboardshortcuts.asp">❮<span class="w3-hide-small"> Previous</span></a>
# # <a class="w3-btn" href="default.asp"><span class="w3-hide-small">Complete HTML </span>Reference</a>
# # <a class="w3-right w3-btn" href="tag_doctype.asp"><span class="w3-hide-small">Next </span>❯</a>
# # </div>
# first br # <br/>
# <div class="w3-example">
# <h3>Example</h3>
# <p>An HTML comment:</p>
# <div class="w3-code notranslate htmlHigh">
# &lt;!--This is a comment. Comments are not displayed in the browser--&gt;<br/><br/>
# &lt;p&gt;This is a paragraph.&lt;/p&gt;
# </div>
# <a class="w3-btn w3-margin-bottom" href="tryit.asp?filename=tryhtml_comment" target="_blank">Try it Yourself »</a>
# </div>
# <hr/>
# <h2>Definition and Usage</h2>
# <p>The comment tag is used to insert comments in the source code. Comments are not displayed in the browsers.</p>
# <p>You can use comments to explain your code, which can help you when you edit the source code at a later date. This is
# especially useful if you have a lot of code.</p>
# <hr/>
# <h2>Browser Support</h2>
# <table class="browserref notranslate">
# <tr>
# <th style="width:20%;font-size:16px;text-align:left;">Element</th>
# <th class="bsChrome" style="width:16%;" title="Chrome"></th>
# <th class="bsEdge" style="width:16%;" title="Internet Explorer / Edge"></th>
# <th class="bsFirefox" style="width:16%;" title="Firefox"></th>
# <th class="bsSafari" style="width:16%;" title="Safari"></th>
# <th class="bsOpera" style="width:16%;" title="Opera"></th>
# </tr>
# <tr>
# <td style="text-align:left;">&lt;!--...--&gt;</td>
# <td>Yes</td>
# <td>Yes</td>
# <td>Yes</td>
# <td>Yes</td>
# <td>Yes</td>
# </tr>
# </table>
# <hr/>
# <h2>Tips and Notes</h2>
# <p>You can use the comment tag to "hide" scripts from
# browsers without support for scripts (so they don't show them as plain text):</p>
# <div class="w3-code w3-border notranslate htmlHigh">
# <div>
# &lt;script type="text/javascript"&gt;<br/>
# &lt;!--<br/>
# function displayMsg()
# {<br/>
#   alert("Hello World!")<br/>
# }<br/>
# //--&gt;<br/>
# &lt;/script&gt;
# </div></div>
# <p><b>Note:</b> The two forward slashes at the end of comment line (//) is the
# JavaScript comment symbol. This prevents JavaScript from executing the --&gt; tag.</p>
# <hr/>
# <h2>Standard Attributes</h2>
# <p>The comment tag does not support any standard attributes.</p>
# <p>More information about <a href="ref_standardattributes.asp">Standard Attributes</a>.</p>
# <hr/>
# <h2>Event Attributes</h2>
# <p>The comment tag does not support any event attributes.</p>
# <p>More information about <a href="ref_eventattributes.asp">Event Attributes</a>.</p>
# <br/>
# <div class="w3-clear w3-center nextprev">
# <a class="w3-left w3-btn" href="ref_keyboardshortcuts.asp">❮<span class="w3-hide-small"> Previous</span></a>
# <a class="w3-btn" href="default.asp"><span class="w3-hide-small">Complete HTML </span>Reference</a>
# <a class="w3-right w3-btn" href="tag_doctype.asp"><span class="w3-hide-small">Next </span>❯</a>
# </div>
# <div id="mypagediv2" style="position:relative;text-align:center;"></div>
# <br/>
# </div>
