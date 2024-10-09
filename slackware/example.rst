My Project Documentation
========================

This is the official documentation for **My Project**, a simple and effective tool for managing tasks.

Table of Contents
-----------------
.. contents:: Table of Contents
   :depth: 2

1. Introduction
---------------
My Project is designed to help you manage your tasks efficiently. 

2. Features
-----------
- Simple and intuitive user interface
- Supports task prioritization
- Ability to categorize tasks
- Synchronization with cloud storage

3. Installation
---------------
To install My Project, use the following command:

.. code-block:: bash
   pip install my_project

4. Usage
--------
To start using My Project, follow these steps:

1. Import the library in your Python script:
   .. code-block:: python
      import my_project

2. Create a new task:
   .. code-block:: python
      task = my_project.Task("Buy groceries")
      task.set_priority(1)

3. Save your tasks:
   .. code-block:: python
      my_project.save_tasks()

5. Example
----------
Here’s a complete example of how to use My Project:

.. code-block:: python
   # Import the library
   import my_project

   # Create a new task
   task = my_project.Task("Complete the report")
   task.set_priority(2)
   
   # Add a category
   task.add_category("Work")
   
   # Save the task
   my_project.save_tasks()

6. Configuration
----------------
You can configure My Project using a configuration file. Below is an example of a configuration file in YAML format:

.. code-block:: yaml
   # config.yaml
   task_management:
     default_priority: 3
     cloud_sync: true

7. FAQs
-------
**Q: Can I use My Project offline?**  
A: Yes, My Project can be used offline. However, synchronization features will only be available when online.

**Q: Is there a mobile version?**  
A: Currently, My Project is only available on desktop, but a mobile version is planned for future releases.

8. Troubleshooting
------------------
If you encounter issues while using My Project, here are some common solutions:

- **Problem**: Installation errors  
  **Solution**: Ensure that you have the latest version of Python and pip.

- **Problem**: Task not saving  
  **Solution**: Check your permissions for the save directory.

9. Links
--------
For more information, check the following resources:
- Official Documentation: `https://example.com/docs`_
- GitHub Repository: `https://github.com/my_project`_

10. Images
----------
Here’s an example of how the user interface looks:

.. image:: images/ui_screenshot.png
   :alt: User Interface Screenshot
   :width: 600px
   :align: center

This image illustrates the main dashboard of My Project.

11. More Images
----------------
You can include multiple images in your documentation. Below is another screenshot that shows task management in action:

.. image:: images/task_management_screenshot.png
   :alt: Task Management Screenshot
   :width: 600px
   :align: center

This image shows how to create and manage tasks within the application.

12. Tables
----------
Here’s a summary of features:

.. table:: Features Summary
   :widths: auto
   :header-rows: 1

   | Feature                   | Description                                      |
   |---------------------------|--------------------------------------------------|
   | Simple Interface          | Easy to navigate and use.                        |
   | Task Prioritization       | Set priority levels for tasks.                   |
   | Cloud Synchronization      | Sync tasks with your cloud account.              |

13. Footnotes
-------------
You can add footnotes for additional information. Here’s a reference to the installation method [#install]_.

.. [#install] Installation can also be done using a direct download from the website.

Conclusion
----------
Thank you for using **My Project**! For more detailed information, please refer to the official documentation.
