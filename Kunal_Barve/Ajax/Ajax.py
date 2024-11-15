xml_content = """
<?xml version="1.0" encoding="UTF-8"?>
<movies>
    <movie>
        <title>The Shawshank Redemption</title>
        <release_date>1994-09-23</release_date>
        <gross_profit>$58,500,000</gross_profit>
    </movie>
    <movie>
        <title>The Godfather</title>
        <release_date>1972-03-24</release_date>
        <gross_profit>$245,066,411</gross_profit>
    </movie>
    <movie>
        <title>Forrest Gump</title>
        <release_date>1994-07-06</release_date>
        <gross_profit>$678,226,805</gross_profit>
    </movie>
    <movie>
        <title>The Dark Knight</title>
        <release_date>2008-07-18</release_date>
        <gross_profit>$1,005,457,016</gross_profit>
    </movie>
    <movie>
        <title>Pulp Fiction</title>
        <release_date>1994-10-14</release_date>
        <gross_profit>$213,928,762</gross_profit>
    </movie>
    <movie>
        <title>The Lord of the Rings: The Return of the King</title>
        <release_date>2003-12-17</release_date>
        <gross_profit>$1,142,219,401</gross_profit>
    </movie>
    <movie>
        <title>Star Wars: Episode V - The Empire Strikes Back</title>
        <release_date>1980-06-20</release_date>
        <gross_profit>$538,375,067</gross_profit>
    </movie>
    <movie>
        <title>The Matrix</title>
        <release_date>1999-03-31</release_date>
        <gross_profit>$463,517,383</gross_profit>
    </movie>
    <movie>
        <title>Goodfellas</title>
        <release_date>1990-09-19</release_date>
        <gross_profit>$46,836,214</gross_profit>
    </movie>
    <movie>
        <title>Interstellar</title>
        <release_date>2014-11-07</release_date>
        <gross_profit>$677,545,589</gross_profit>
    </movie>
    <movie>
        <title>The Silence of the Lambs</title>
        <release_date>1991-02-14</release_date>
        <gross_profit>$272,742,922</gross_profit>
    </movie>
    <movie>
        <title>Gladiator</title>
        <release_date>2000-05-05</release_date>
        <gross_profit>$457,640,427</gross_profit>
    </movie>
    <movie>
        <title>The Lion King</title>
        <release_date>1994-06-24</release_date>
        <gross_profit>$968,511,805</gross_profit>
    </movie>
    <movie>
        <title>The Dark Knight Rises</title>
        <release_date>2012-07-20</release_date>
        <gross_profit>$1,081,041,287</gross_profit>
    </movie>
    <movie>
        <title>Avatar</title>
        <release_date>2009-12-18</release_date>
        <gross_profit>$2,847,246,203</gross_profit>
    </movie>
    <movie>
        <title>Inception</title>
        <release_date>2010-07-16</release_date>
        <gross_profit>$829,895,144</gross_profit>
    </movie>
    <movie>
        <title>Shrek 2</title>
        <release_date>2004-05-19</release_date>
        <gross_profit>$928,760,770</gross_profit>
    </movie>
    <movie>
        <title>Jurassic Park</title>
        <release_date>1993-06-11</release_date>
        <gross_profit>$1,038,812,584</gross_profit>
    </movie>
    <movie>
        <title>Harry Potter and the Philosopher's Stone</title>
        <release_date>2001-11-16</release_date>
        <gross_profit>$974,755,371</gross_profit>
    </movie>
</movies>

"""

# Save XML content to a file
with open('movies.xml', 'w') as xml_file:
    xml_file.write(xml_content)

print("XML file saved successfully.")
