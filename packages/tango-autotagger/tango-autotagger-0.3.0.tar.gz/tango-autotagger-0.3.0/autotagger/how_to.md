##Autotagger

The autotagger app helps establish relationships between objects in the database with little or no human intervention.
Essentially, you tell it what to look for and where to look, and it will automatically create links.
For example, I might tell it to watch for venue names in articles, and it would then start cross-referencing those tables and to find matches and create links.

It can also be used to automatically group stories together, creating groupings of content on the fly.

###Automatically creating links within articles or other content to other objects
* First, decide what should be linked. Note that to avoid false positives, the name of the thing being auto-linked must be very specific. For example, if we were to attempting to auto-tag cities, we would end up creating links in articles wherever that city name is found: New York's Finest Delivery Service, for example, would end up linked to New York.
* Once you know what you're attempting to link to and where you intend to have the links show up, a developer will add a few lines to the site settings and it will begin working with no further intervention. If you are the developer, consult the project README.

###Automatically grouping articles
You can create micro-sections of related articles on the fly by specifying a given phrase to watch for. From then onany articles with that phrase would be related to one another. To do so...

* Go to "Autotagger > Auto tags"
* Click "Add Auto Tag" in the upper right
* Give it a phrase to watch for. Again, to avoid false positives, be specific. For example, "Turtle" would probably be too broad. "Teenage Mutant Ninja Turtle" would work better.
* Save. The system will now watch for your phrase in articles, relate articles in which it is found to one another, and show the related articles.
