1. **Identification of the problem you are trying to solve by building this particular app.**  
- The problem I'm trying to solve with this app is a language barrier problem. Swahili is widely spoken language in East Africa. Recently, East Africa has been attracting a lot of foreigners in terms of tourism and business. This is where my app comes into play, it would be useful for these foreigners to have a Swahili translator while they go about their business.  
2. **Why is it a problem that needs solving?**  
- It is a problem that needs solving because there would be no proper way for people to connect with a language barrier in place. People understand each other better if there is good communication. Solving the problem would bring along a lot of benefits such as, better communication, efficient business dealings and better connections between people.  
3. **Why have you chosen this database system. What are the drawbacks compared to others?**  
- For this app I have chosen a RDMS, PostgreSQL for these reasons; It provides a reliable and structured way to store and retrieve data, making it a suitable option for complex data models and relationships. PostgreSQL can handle large amounts of data and and high concurrent user access efficiently. Another reason why I chose it, is because it allows the creation of custom data types, functions and extensions.  
- However, PostgreSQL can be more complex to set up and manage compared to light-weight databases like SQLite. It requires more configuration including user management and permissions settings.Another drawback is that PostgreSQL may require more system resources in terms of memory and processing power.  
4. **Identify and discuss the key functionalities and benefits of an ORM**  
- Object-Relational Mapping(ORM) is a programming technique that allows developers to interact with a relational database using object-oriented paradigms.
- **Object-Oriented Paradigm**- ORM bridges the gap between object-oriented programming languages and relational databases. It makes it easier to model and manipulate data.  
- **Data Modelling and Relationships**- ORM frameworks provide tools to define data models and relationships between entities in the database. A benefit of this is developers can define classes and their attributes and entity relationships.  
- **Querying Language**- ORM frameworks provide query languages that allow developers to retrieve data from the database using high-level, object-oriented syntax.  
- **Perfomance Optimization**- Many ORM frameworks include features for performance optimization, such as lazy loading, eager loading and caching.  
5. **Document all endpoints for your API**  
A. **Endpoint:** **'/translate'**  
- **Method:** POST  
- **Description:** Translates the provided text from the source language to the target language.  
- **Request Body:** {  
  "source_text": "Text to be translated",  
  "source_language": "en",  
  "target_language": "sw"  
}  
- **Response:** {  
  "translated_text": "Translated text"  
}  
B. **Endpoint:** **'/languages'**  
- **Method:** GET  
- **Description:** Retrieves the list of supported languages for translation.  
- **Response:** {  
  "languages:" [  
    {  
      "language_id": "en",  
      "language_id": "sw"  
    }  
  ]  
}  
6. **An ERD for your app**  
![ERD for the app](./docs/ERD.drawio.png)  
7. **Detail any third party services that your app will use**