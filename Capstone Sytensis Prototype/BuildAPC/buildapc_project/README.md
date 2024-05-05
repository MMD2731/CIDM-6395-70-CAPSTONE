# BuildAPC Application

BuildAPC’s is a dynamic web application with a goal to revolutionize how individuals approach buying and building personal computers. Our platform will allow users to select, customize and purchase computer components based on compatibility and user preference. BuildAPC will have the ability to track prices for saved "wishlisted" components and alert users with real-time pricing alerts for their components. This functionality allows consumers to move away from overpriced, under-optimized pre-built options.

BuildAPC also wants to help small businesses and integrate our Configuration Builds and Wishlist builds with System Integrator API's to allow users to have a small business build their PC for them (if they so choose to.) Why is this important? We would work directly with other System Integrators to help them grow their business and become direct partners with BuildAPC which would help them go to market and build market share for their client base. The goal? System Integrators (SI) will work directly with BuildAPC to have their customer's components upgraded through our website and have the SI help with either the upgrade or a whole new build. 


## Features

- **User Authentication**: Secure login system for users and administrators.
- **Component Customization**: Users can choose components like CPU, GPU, RAM, etc., with options for customization.
- **Price Calculation**: Real-time price updates as components are selected or customized.
- **Wishlist and Save Configuration**: Users can save their configurations for later or add them to a wishlist.
- **Admin Panel**: Administrators can manage product listings, user data, and view analytics.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8 or higher
- pip (Python package installer)
- Review the requirements.txt file to identify all necessary packages that need to be installed.

## Administrator Role
- Login as admin/superuser with the following credentials:
 - username - admin123
 - password - gobuild1

### PC Component Admin View

Admin homepage will be displayed on screen "PC Component Admin View"
With the list of all PC Components:
- CPU
- Cooler
- Motherboard
- RAM
- GPU 
- Storage
- PowerSupply
- Tower
- OperatingSystem
- Monitor
- Q - Selecting "Q" will allow the logged in account to quit out of the menu they are in (in all sub menus)

Once a selection is made the following sub menu will appear "Select a component to manage or Q to Quit"
Sub menu will have the following options 
- A (Add) - Addition of new component into database
- D (Delete) - Deletion of an existing component in database
- E (Edit) - Edit of an existing component in database
- V (View) - View existing component in database
- Q (Quit) - Quit to previous sub menu

After selection an option the user will need to input product specific data for the PC Component selected:
- Component_id - This is the custom ID that BuildAPC will be assigning to its class (component) will drive which specific item it is, i.e. cpu_id is for CPU, gpu_id is for GPU, os_id is for OperatingSystem.
- vendor_sku_id - This vendor sku will come directly from the Amazon API webservice. This initial release of BuildAPC will not be able to have integrations with Amazon, therefore an manual input of vendor_sku_id is required. 
- Name - The name of the component you are doing.
- Item Price - Price of component
- Once the user presses "Enter" depending on the Sub menu option selected A,D,E or V. The system will proceed to the next component. 

## Future Sprint Considerations

- BuildAPC will feature a compatibility checker in a future sprint that will identify if specific components are compatible with one another. I.E. - When selecting a specific Tower for your PC Build the BuildAPC Config menu for a user will display a compatibility checkmark (if compatible) or X (if not compatible). It will also display which components have compatibility issues and make recommendations.
- Down the road, Artificial Intelligence (AI) considerations will be added to BuildAPC to help users select the appropriate build for the appropriate use case and within the budget they are trying to achieve. By simply asking the AI a question, it will formulate a build in the config menu to display a build that best fits the customers use case. The customer will then be able to edit or purchase the components as they see fit. 

*BuildAPC is a Minimum Viable Product state.* 
- It's intention is to build a foundational framework create a fully functioning webpage to reflect my project for CIDM-6330. A fully functioning application for a domain and initiative of this scale would potentially take years to develop but the problem domain and use case is viable for considerations of a future build. 

 The MSCISBA program provided by West Texas A&M University has proven to be invaluable in both my career and also my professional development. My future goals will be to continue to enhance my Software Design and Engineering skils by attending coding bootcamps and continuous software development learning events. 

Regards,

Miguel Sanchez

West Texas A&M University

