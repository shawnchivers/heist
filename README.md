
# Heist

## What?

`Heist` is a language I made up to learn by stealings ideas from other programming languages primary BASIC and Scheme.

It needed a vaguely lawless name: Scheme, Swindle, Racket.

Or what BASIC would be without goto / gosub but with addition of:
- first-class functions
- anonymous functions
- lexical closure
- support for tail recusion optimization
- dynamic type system (piggie backs on Python)


## Expression

Use infix notation for expressions

| Operation       |                                                                                 |
| --------------- | ------------------------------------------------------------------------------- |
| Constant        | `pi` `e`                                                                        |
| Unary Minus     | `-`                                                                             |
| Unary           | `sin` `cos` `tan` `abs` `sqrt` `ln` `log` `log10` `log2` `str` `factorial` `int` `float` `tab`             |
| Power           | `^`                                                                             |
| Multiplication  | `*` `/`  `%` `mod`                                                              |
| Addition        | `+` `-`                                                                         |
| Paren           | `( )`                                                                           |
| Concatenate     | `;`  `&`                                                                        |
| BOOLEAN         | `true` `false`                                                                  |
| INT             |                                                                                 |
| DOUBLE          |                                                                                 |
| VAR             |                                                                                 |
| STRING          | `"` `"`                                                                         |
| `<statement>`   |                                                                                 |
| null            |                                                                                 |


## Statements

### Print


```
print <expression>
```

Expression must resolve to printable

### Conditionals

```
if <expression> then
    <if-body>
end if
```

```
if <expression> then
    <if-body>
else
    <else-body>
end if
```

### Loops

``` 
do while
    <loop-body>
loop
```

```
for <variable> = <start> to <end>
    <loop-body>
next
```

Optional: step-amount allowing negative steps in situations where start is greater than start
```
for <variable> = <start> to <end> step? <step-amount>?
    <loop-body>
next
```

### Function

```
function <tail-recurse>? <function-name>? (<parameter-list>?)
    <function-body>
end function
```

### Invoking Function

```
call? <function-name> (<expression-list>?)
```

### Input

```
input <variable-name>
```

## Variable Assignment

```
<variable-name> = <expression>
```

### Array

creating an array
```
<array-name> as Array ( <numeric-expression> )
```

assign value
```
<array-name> ( <numeric-expression> ) = <expression>
```

retrieve value
```
<array-name> ( <numeric-expression> )
```

ubound / upperbound
```
ubound(<array-name>)

upperbound(<array-name>)
```

# Build Grammar

```
antlr4 -Dlanguage=Python3 heist.g4 -visitor
```

# Run Heist

```
python3 ./heist.py <inputfile>
```


