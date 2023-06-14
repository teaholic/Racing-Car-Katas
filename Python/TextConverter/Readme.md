# Text Converter

SOLID principles practiced:
* Single responsibility
* Interface Segregation

## My Approach

This approach is reflected in the commit history.

Task description:
> Write the unit tests for the UnicodeFileToHtmlTextConverter class. The UnicodeFileToHtmlTextConverter class is designed to reformat a plain text file for display in a browser. There is an additional class "HtmlPagesConverter" which is slightly harder to get under test. It not only converts text in a file to html, it also supports pagination. It's meant as a follow up exercise.

### Understanding the problem
* I read the html_pages description:
 >  It not only converts text in a file to html, it also supports pagination
 
* From the description, I found two scopes of needed behavior:
  1. converts text in a file to html
  2. supports pagination
 
### Iteration #1
* These two scopes need to be tested. I started adding (failing) tests for these scopes.

### Iteration #2
> I'm thinking:
> 
> `HtmlPagesConverter` is dependent from an external systems (filesystem to read files). I need to extract this responsibility to separate the pagination and text conversion responsibilities.

* I created a `FileRepository` class and I moved there the responsibility of reading files from filesystem and getting page breaks.
* I injected `FileRepository` as a dependency of `HtmlPagesConverter`.

> I'm thinking:
> 
>The only responsibility left in `HtmlPagesConverter` is to return an html page and to delegate to `FileRepository` to retrieve the lines given a filename and a page number. 
* 
* I iterated on the test of `HtmlPagesConverter` using a stubbed `FileRepository` to return a list of lines.

### Iteration #3
* I iterated on testing `UnicodeFileToHtmlTextConverter`. 
* Also here I had to externalize the behavior of opening the file and inject the client that escapes lines.
* `UnicodeFileToHtmlTextConverter` is left with the only responsibility of orchestrating these two services interfacing with external systems.
* As a possible improvement, a facade layer could be added to initialize and inject to `UnicodeFileToHtmlTextConverter` the needed html_converter_client at runtime.