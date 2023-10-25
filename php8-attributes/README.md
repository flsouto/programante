# Feature Attributes do PHP 8

No PHP 8, a feature "Attributes" permite adicionar metadados a classes, métodos, propriedades, parâmetros de métodos e funções. Esses metadados podem ser usados para documentação, anotações ou para criar comportamentos personalizados em sua aplicação. Aqui está um exemplo simples de como usar Attributes em PHP 8:

```php

#[Author("John Doe")]
class Book {
    private string $title;
    private string $author;

    public function __construct(string $title, string $author) {
        $this->title = $title;
        $this->author = $author;
    }

    #[Description("Get the book's title")]
    public function getTitle(): string {
        return $this->title;
    }

    #[Description("Get the book's author")]
    public function getAuthor(): string {
        return $this->author;
    }
}

class Author {
    public function __construct(public string $name) {}
}

class Description {
    public function __construct(public string $text) {}
}

// Obtendo atributos e seus valores
$bookReflection = new ReflectionClass(Book::class);

$authorAttribute = $bookReflection->getAttributes("Author")[0];
$author = $authorAttribute->newInstance();
echo "Author: " . $author->name . "\n";

$titleMethod = $bookReflection->getMethod("getTitle");
$descriptionAttribute = $titleMethod->getAttributes("Description")[0];
$description = $descriptionAttribute->newInstance();
echo "Description: " . $description->text . "\n";

```

Neste exemplo, usamos Attributes para adicionar metadados a uma classe Book e seus métodos. Os Attributes Author e Description são usados para adicionar informações sobre o autor do livro e descrições dos métodos getTitle e getAuthor.

Em seguida, usamos a classe Reflection para obter os atributos e seus valores associados à classe Book e ao método getTitle. Isso nos permite acessar as informações de autor e descrição que foram adicionadas como metadados usando Attributes.

Observe que os Attributes são personalizados, ou seja, você precisa criar as classes Author e Description para representar os atributos. Em uma aplicação real, você pode usar Attributes para fins de documentação, mapeamento ORM, injeção de dependência e outras finalidades que requerem metadados em seus objetos.

