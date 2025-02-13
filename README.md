# Argentum-tg-bot-sample

aiogram-base telegram bot arch sample.

Implemented: 
- Gino DB, 
- custom event system, 
- referal system, 
- error handling,
- logging, 
- anti-spam system, 
- blacklist, 
- role system
- docker setup

It is worth noting that a special approach is used when working with database models. We wrap them in Classes that implement the interface for interacting with that entities.
There are no direct work with Gino's models fields
