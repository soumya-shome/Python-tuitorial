# Python tuitorial

# Python
<p>
Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language. It was created by Guido van Rossum during 1985- 1990. Like Perl, Python source code is also available under the GNU General Public License (GPL). This tutorial gives enough understanding on Python programming language.
</p>

### Features of Python
<p>
- Easy-to-learn </br>
- Easy-to-read </br>
- Easy-to-maintain </br>
- A broad standard library </br>
- Interactive Mode </br>
- Portable </br>
- Extendable </br>
- Databases </br>
- GUI Programming </br>
- Scalable </br>
</p>

### Applications of Python
<p>
- GUI based desktop applications </br>
- Image processing and graphic design applications </br>
- Web frameworks and applications </br>
- Enterprise and business applications </br>
- Operating systems </br>
- Language development </br>
- Prototyping </br>
</p>

## Basics  [ basics.py ](basics.py)

Literals / Datatypes<br>
|-- Integer => int => int()<br>
|-- Float => float => float()<br>
|-- String => str => str()<br>
|-- Boolean => bool => bool()<br>


|  | Description |
| --- | --- |
| print() | 1. using end and sep <br> 2. using format <br> 3. using f-string <br> 3. using %  |
| input() | 1. using input() <br> 2. using eval() |
| type() | 1. using type()  |
| Operators | <br> 1. Arithmetic Operators <br> 2. Assignment Operators <br> 3. Comparison Operators <br> 4. Logical Operators <br> 5. Identity Operators <br> 6. Membership Operators <br> 7. Bitwise Operators |
| Control Flow | <br> 1. If-else <br> 2. For <br> 3. While <br> 4. Break <br> 5. Continue <br> 6. Pass|
| range() |  <br> 2. using range() <br> 2. using range() with step  <br> 2. using range() with start, stop and step |
| List Comprehension | <br> 1. using List Comprehension <br> 2. >using List Comprehension with if <br> 3. using List Comprehension with if-else <br> 4. using List Comprehension with nested if <br> 5. using List Comprehension with nested if-else |
|Concatenation and Replication |  <br> 2. Concatenation <br> 2. Replication |

## DSA and OOPs 

| | Create| Add| Remove  | Modify  | Access | Others  |
| --- | --- | --- | --- | --- | --- | --- |
| [**List**](list.py)            | - using [ ]<br>- using list() constructor | - using append( element )<br>- using insert( index, element )<br>- using extend( iterable ) | - using pop()<br>- using pop( index )<br>- using remove( element )<br>- using clear() | - using index<br>- using slice<br>- using slice with step | - using index<br>- using slice<br>- using slice with step | - Iteration<br>- len()<br>- count( element )<br>- sort()<br>- reverse()<br>- copy()<br>- max()<br>- min()<br>- sum()<br>- any()<br>- all()<br>- enumerate()<br>- zip()<br>- list( iterable )<br>- cmp()<br>- filter()<br>- map()<br>- reduce()<br>- List Comprehension |
| [**Tuple**](tuple.py)           | - using ( )<br>- using tuple() constructor | It is immutable | It is immutable | It is immutable | - using index<br>- using slice<br>- using slice with step<br>- using stride | - Iteration<br> -all()<br>- any()<br>- enumerate()<br>- len()<br>- max()<br>- min()<br>- sorted()<br>-sum()<br>-zip()<br> -count( element )<br>- using index( element )<br>- cmp()<br>- filter()<br>- map()<br>- reduce()<br>- reversed()<br>- Tuple Comprehension |
| [**Set**](set.py)             | - using { }<br>- using set() constructor | - using add( element )<br>- using update( iterable ) | - using pop()<br>- using remove( element )<br>- using discard( element )<br>- using clear() | -using update() | - It is unordered | - Iteration<br>- all()<br>- any()<br>- enumerate()<br>- len()<br>- max()<br>- min()<br>- sum()<br>- sorted()<br>- set()<br>- zip()<br>- copy()<br>- cmp()<br>- filter()<br>- map()<br>- reduce()<br>- reverse()- isdisjoint(); -issubset(); -issuperset(); -difference(); -intersection(); -union(); -symmetric_difference()<br>- Set Comprehension |
| [**Dictionary**](dictionary.py)     | - using { }<br>- using dict() constructor | - using update( key=value )<br> | - using pop( key )<br>- using popitem()<br>- using clear() | - using update( key=value )<br>- using update( { key:value } ) | -using get()<br>- using keys()<br>- using values()<br>- using items() |  -len()<br> -type()<br> -setdefault()<br> -all()<br> -any()<br> -sorted()<br> -reversed()<br> -enumerate()<br> -copy()<br> -fromkeys()<br> -haskeys()<br> -cmp()<br> -iter()<br> -max()<br> -min()<br> -sum()<br> -filter()<br> -map()<br> -reduce()<br> -zip()<br> -Dictionary Comprehension |   

|  | Description |
| --- | --- |
|Functions | 1.Function</br> 2.Function Arguments </br>3.Default Arguments </br>4.Keyword Arguments </br>5.Variable Length Arguments </br>6.Anonymous Function </br>7.Recursion |
|Lambda | 1. using lambda </br> 2. using lambda with filter() </br> 3. using lambda with map() </br> 4. using lambda with reduce() |
|Map | 1. using map() </br> 2. using map() with lambda </br> 3. using map() with multiple iterables |
|Filter | 1. using filter() </br> 2. using filter() with lambda </br> 3. using filter() with multiple iterables |
|Reduce | 1. using reduce() </br> 2. using reduce() with lambda </br> 3. using reduce() with multiple iterables |
|Decorators | 1. using @decorator </br> 2. using @decorator with arguments </br> 3. using @decorator with arguments and return value </br> 4. using @decorator with arguments and return value |
|Generators | 1. using yield </br> 2. using yield with arguments </br> 3. using yield with arguments and return value </br> 4. using yield with arguments and return value |
|Closures | 1. using nested function </br> 2. using nested function with arguments </br> 3. using nested function with arguments and return value </br> 4. using nested function with arguments and return value |
|Iterators | 1. using iter() </br> 2. using iter() with arguments </br> 3. using iter() with arguments and return value </br> 4. using iter() with arguments and return value |
|Classes and Objects | 1. Class </br> 2. Object </br> 3. Constructor </br> 4. Self </br> 5. Instance Variables </br> 6. Class Variables </br> 7. Static Methods </br> 8. Inheritance </br> 9. Overriding Methods </br> 10. Data Hiding |
|Modules | 1. Importing Modules </br> 2. Importing from Modules </br> 3. Importing Specific Items </br> 4. Importing with Alias </br> 5. Importing Everything |
|File Handling | 1. Opening a File </br> 2. Reading a File </br> 3. Writing to a File </br> 4. Appending to a File </br> 5. Closing a File |
|Exception Handling | 1. Try </br> 2. Except </br> 3. Finally </br> 4. Raise </br> 5. Assert |
|Regular Expressions | 1. Match </br> 2. Search </br> 3. Sub </br> 4. Subn </br> 5. Group </br> 6. Flags |
|Multithreading | 1. Thread </br> 2. Starting a Thread </br> 3. Starting a Thread with Arguments </br> 4. Starting a Thread with Keyword Arguments </br> 5. Starting a Thread with Both Arguments and Keyword Arguments |
|Networking | 1. Client </br> 2. Server |
|Database | 1. Connecting to a Database </br> 2. Creating a Table </br> 3. Inserting Data </br> 4. Selecting Data </br> 5. Updating Data </br> 6. Deleting Data |
|GUI | 1. Label </br> 2. Button </br> 3. Entry </br> 4. Text </br> 5. Frame </br> 6. Checkbutton </br> 7. Radiobutton </br> 8. Listbox </br> 9. Menu </br> 10. Message </br> 11. OptionMenu </br> 12. Scale </br> 13. Scrollbar </br> 14. Toplevel |
|Web Scraping | 1. BeautifulSoup </br> 2. Scraping a Webpage </br> 3. Scraping Multiple Webpages |
|Sending Emails | 1. SMTP </br> 2. Sending a Plain Text Email </br> 3. Sending an HTML Email </br> 4. Sending an Email with Attachment |
|Python - MySQL | 1. Connecting to MySQL </br> 2. Creating a Table </br> 3. Inserting Data </br> 4. Selecting Data |
|Python - MongoDB | 1. Connecting to MongoDB </br> 2. Creating a Collection </br> 3. Inserting Data </br> 4. Selecting Data |
|Python - SQLite | 1. Connecting to SQLite </br> 2. Creating a Table </br> 3. Inserting Data </br> 4. Selecting Data |
|Python - PostgreSQL | 1. Connecting to PostgreSQL </br> 2. Creating a Table </br> 3. Inserting Data </br> 4. Selecting Data |
|Python - XML | 1. Parsing XML </br> 2. Creating XML </br> 3. Modifying XML </br> 4. Deleting XML |
|Python - JSON | 1. Parsing JSON </br> 2. Creating JSON </br> 3. Modifying JSON </br> 4. Deleting JSON |
|Python - YAML | 1. Parsing YAML </br> 2. Creating YAML </br> 3. Modifying YAML </br> 4. Deleting YAML |
|Python - CSV | 1. Reading CSV </br> 2. Writing to CSV </br> 3. Appending to CSV </br> 4. Deleting CSV |
|Python - Excel | 1. Reading Excel </br> 2. Writing to Excel </br> 3. Appending to Excel </br> 4. Deleting Excel |

