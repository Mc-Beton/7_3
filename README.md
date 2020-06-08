# Fake Business Card Generator:

It's a simple program which generates random business cards with fake information.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Fisrt of all download or clone this program to Your pc.
You need a proper version of Faker. You can get it by this link: https://github.com/joke2k/faker.


### Prerequisites

Install Faker

```
>pip install faker
```
more information you will recive in the faker readme file.

### List of available commands

- help_me - print out all available commands
- make base cards- generate random cards with personal data, it will ask for the amount of cards You want to generate
- make business cards - generate random business cards, it will ask for the amount of cards You want to generate
- show - print out generated personal or business cards
- call - print out who you are calling by what number
- exit - quit program

## Getting started/Examples

First of all, this is currently a project which doesn't store information for later use (doesn't save the given information in a file), so it's only to check whether all the given commands really work.

### Examples

Lets turn it on in **cmd**, starting in the files location:
```
>python Zadanie.py
```
And there we get greetings from the program and a small assist how get started.
```
>Hello! I am a simple program to do some stuff. Wanna check me out? Type in help_me for commands ;)
>What would you like to do?
```

Well, we don't have any cards in our base, so lets start by generating some:
```
>What would you like to do? *make base cards*
>How many random base cards would you like to create? *6*
```

Lets check it out, whether they were made:
```
>What would you like to do? *show*
>Which cards would you like to see? 
 base cards
 business cards
>*base cards*
Margaret Phillips donna37@example.org
Tracy Avery nguyenjulie@example.com
Jeffery Burgess christopherhudson@example.com
Jose Rios jeffrey98@example.net
Tyler Holmes donald53@example.org
Monica Rogers bgolden@example.net

```
It works. Thanks to Faker, it generated totally random cards. It all works the same for business cards.
Lest say we want to try to call someone from the list? Goes like this:
```
>What would you like to do? *call*
>From which list of contacts would you like to call? 
 base cards
 business cards
```
After choosing from which list we would like to call someone it will print out all available people:
```
>*base cards*
Margaret Phillips donna37@example.org
Tracy Avery nguyenjulie@example.com
Jeffery Burgess christopherhudson@example.com
Jose Rios jeffrey98@example.net
Tyler Holmes donald53@example.org
Monica Rogers bgolden@example.net
Type in the persons first name you would like to contact?
```
Lest choose "Jose"
```
>*Jose*
Dailing +48 669-035-7260 and calling to Jose Rios
```

And that's all folk's.

## Later updates.
Well, maybe, somewhere, in the future. For now I need to keep up with the course. 
Thanks

## Authors
Filip Gabrys - Initial work With help from his mentor from the Kodilla course.
