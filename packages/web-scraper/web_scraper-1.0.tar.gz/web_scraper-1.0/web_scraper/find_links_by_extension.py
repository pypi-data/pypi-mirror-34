import requests
from bs4 import BeautifulSoup

def find_links_by_extension(url, extension, restricted=False, recursive=True, depth=2, MAXnumberOfLinksPerPage=50, maxNumberOfLinksToFind=30, sorted=False):
  """Return a list of links to files with the given extension in the webpage and its children. It uses two methods: one based on Google search, and one direct method. 
  
  Keyword arguments:
  url -- The webpage's url
  extension -- The file extension. Do not include dot.
  restricted -- (used only in the direct method) Whether to search only for files that their link is superset of the url given (default False).
  recursive -- (used only in the direct method) Whether to look in child-pages (default True).
  depth -- (used only in the direct method) How deep follow the links. Is considered only if recursive=True (default 2, minimum 0).
  MAXnumberOfLinksPerPage -- (used only in the direct method) This is in case execution gets stuck in a webpage for unforseen reasons (default 50).
  maxNumberOfLinksToFind -- (default 30).
  sorted -- Whether to sort the output list.
  """
  def get_links_using_Google_search(url, extension, maxNumberOfLinksToFind=30):
    """Use Google search engine to find links to files with a specific extension in a given webpage and its children.
    
    Keyword arguments:
    url -- (string) The url to look for files in it and its children.
    extension -- (string) The type of file to look for. Do NOT include the dot (as in .pdf).
    maxNumofFilesToFind -- (int) The max number of files to find (default 30).
    """
    flag = False  # to check if maxNumberOfLinksToFind has been reached
    startingResultNum = 0  # to build the address to other pages of search results
    output = set()  # set of found links so far
    
    while True:
      searchUrl = 'https://www.google.com/search?q=site:'+ url + '+filetype:' + extension + '&start=' + str(startingResultNum)
      # Packages the request, send the request and catch the response: r
      r = requests.get(searchUrl)
      # Extract the response
      html = r.text
      soup = BeautifulSoup(html, 'html5lib')
      
      # checking to see if there is no more search-result pages
      if 'did not match any document' in soup.text: 
        break

      # checking to see if Google has blocked access becuase of too many requests
      checkForCaptcha = soup.find_all('div', class_ = 'g-recaptcha')
      if checkForCaptcha != []:
        msg = "***** Google blocked access by requiring CAPTCHA solving! This is because many requests has been sent in a short period of time. Either wait for a while, or use a different ip to overcome this problem. You can also use the 'get_links_directly' module (from the same package) which does not rely on Google services *****"
        output.add(msg)
        break

      # accessing tags that include links
      h3Tags = soup.find_all('h3', class_ = 'r')  # this specific class is because of the way Google shows search results
      for h3Tag in h3Tags:
        dirtyLink = h3Tag.a.get('href')  # this has some extra characters at the beginning and end which need to be striped, thus 'dirty'.
        
        # Some links to desired files do not contain the extension in them although they are of the requested type.
        # So we check to see if the extension appears. If so then do the regular cleaning. If not, use & as indicator for cleaning
        try:
          link = dirtyLink[dirtyLink.lower().index('http') : dirtyLink.lower().index('.' + extension) + len(extension) + 1]
        except:
          link = dirtyLink[dirtyLink.index('http') : dirtyLink.index('&')]
        output.add(link)
        if len(output) >= maxNumberOfLinksToFind:
          flag = True
          # get out of for loop
          break
      if flag:
        # get out of while loop
        break
      startingResultNum += 10
    
    return output

  def get_links_directly(url, extension, restricted=False, recursive=True, depth=2, MAXnumberOfLinksPerPage=50, maxNumberOfLinksToFind=35, output=set()):
    """Return set of links to files with the given extension in the webpage with the given url and its children.
    
    Keyword arguments:
    url -- The webpage's url
    extension -- The file extension. Do not include dot.
    restricted -- Wether to search only for files that their link is superset of the url given (default False).
    recursive -- Whether to look in child-pages (default True).
    depth -- How deep follow the links. Is considered only if recursive=True (default 2).
    MAXnumberOfLinksPerPage -- This is to overcome cases where execution gets stuck in a webpage for unforseen reasons (default 50).
    maxNumberOfLinksToFind -- The max number of files to find (default 30).
    """
    global flag  # to check if maxNumberOfLinksToFind has been reached
    flag = False
    # The following is the list of extensions that getting urls from links ending at them takes too long. It is used in the _page_urls method.
    extensionsDict = {'2':['.db', '.gz'], 
                      '3':['.gif', '.png', '.ico', '.htm', '.jpg', '.bmp', '.pdf', '.mp3', 'mp4', '.ogg', '.wav', '.wma', '.wmv', '.3gp', '.avi', '.bin', '.exe', '.iso', '.ppt', '.rar', '.zip', '.tar', '.tif', '.mkv', '.mov', ], 
                      '4':['.jpeg', '.gzip', '.html']
                    }
    try:
      # removing the provided extension from the extensions blacklist (above)
      extensionsDict.get(str(len(extension))).remove('.'+ extension)
    except:
      pass

    def _page_urls(url, extension, restricted, MAXnumberOfLinksPerPage, extensionsDict):
      """Return the urls in the webpage as a set."""
      length = len(extension)
      try:
        # Packages the request, send the request and catch the response: r
        r = requests.get(url)
        # Extract the response
        html = r.text
      except:
        html = ''

      soup = BeautifulSoup(html, 'html5lib')
      
      # adding / at the end of url if it is an indexing page and doesn't already have / at the end
      if url[-1] != '/' and soup.title != None and 'Index' in soup.title.text:
        url += '/'
      
      # making an illegal list of those links in index pages that go to parent directory or sort by name, modified time, ...
      illegal = ['?C=N;O=D', '?C=N;O=A', '?C=M;O=D', '?C=M;O=A', '?C=S;O=A', '?C=S;O=D', '?C=D;O=A', '?C=D;O=D', '/', '']
      
      urls = []
      for tag_element in soup.find_all('a'):
        href = tag_element.get('href', '')
        # exclude links that refer to different parts of the website, or are 'mailto' links or include 'javascript:'
        if '#' in href or 'mailto:' in href or 'javascript:' in href:
          continue
        if href not in illegal:
          newUrl = url + href

          if newUrl[-3:] in extensionsDict['2'] or newUrl[-4:] in extensionsDict['3'] or newUrl[-5:] in extensionsDict['4']:
            continue
          # excluding urls that have // but not as a part of the beggining http(s)://
          if '//' in newUrl[7:] and newUrl[-(length + 1) :] != '.' + extension:
            continue
          if restricted:
            # checks whether there is another http(s):// in the url other than the one at the beginning
            if '://' in item[7:]: # item[7:] exclude the http(s):// part from the url
              continue
          if 'html' in newUrl[:-4]:
            continue
          urls.append(newUrl)
          if len(urls) >= MAXnumberOfLinksPerPage:
            break
      return urls

    def _find_by_extension(url, extension, restricted, recursive, depth, MAXnumberOfLinksPerPage, maxNumberOfLinksToFind, output, extensionsDict):
      global flag
      if flag:  # if maxNumberOfLinksToFind has been reached
        return
      if depth > -1:
        length = len(extension)
        urls = _page_urls(url, extension, restricted, MAXnumberOfLinksPerPage, extensionsDict)
        for item in urls:
          depth_copy = depth
          if item[-(length + 1) :] == '.' + extension: # if the extension is matched
            if not restricted:
              if 'http' in item[7:]:  # starting from index 7 guarantees the first http(s) is excluded
                output.add(item[item[7:].index('http') +7:])
              else:
                output.add(item)
            else: # if restricted
              if 'http' not in item[7:]:
                output.add(item)
            if len(output) >= maxNumberOfLinksToFind:
              flag = True
              break
            continue  # this replaces 'else' (which is more expensive) for the next to lines 
          # the following lines get executed only if the extension is not matched
          depth_copy -= 1
          _find_by_extension(item, extension, restricted, recursive, depth_copy, MAXnumberOfLinksPerPage, maxNumberOfLinksToFind, output, extensionsDict)
      else:
        return

    _find_by_extension(url, extension, restricted, recursive, depth, MAXnumberOfLinksPerPage, maxNumberOfLinksToFind, output, extensionsDict)
    return output

  google_search_res = get_links_using_Google_search(url, extension, maxNumberOfLinksToFind)
  count = len(google_search_res)
  if count >= maxNumberOfLinksToFind:
    res = list(google_search_res)
    if sorted:
      res.sort()
    return res
  direct_method_res = get_links_directly(url, extension, restricted, recursive, depth, MAXnumberOfLinksPerPage, maxNumberOfLinksToFind, google_search_res)
  res = list(google_search_res.union(direct_method_res))
  if sorted:
    res.sort()
  return res