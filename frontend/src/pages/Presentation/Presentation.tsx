import React from 'react';

const FeirouPage: React.FC = () => {
    return (
        <div style={{ fontFamily: 'Arial, sans-serif', backgroundColor: '#f4f4f4', color: '#333', margin: '0', padding: '20px' }}>
            <div style={{ maxWidth: '800px', margin: 'auto', background: '#fff', padding: '20px', boxShadow: '0 0 10px rgba(0,0,0,0.1)' }}>
                <h1 style={{ color: '#444' }}>Feirou</h1>
                <p style={{ lineHeight: '1.9' }}>
                    Introducing Feirou, a free and open-source platform designed to facilitate direct connections between consumers and producers, particularly rural and local producers. Feirou is based on the creation of communities encompassing both consumers and producers, simplifying and organizing the buying and selling processes in a fairer and more beneficial manner for everyone.
                </p>
                
                <h3 style={{ color: '#444' }}>Communities</h3>
                <ul style={{ lineHeight: '1.9' }}>
                    <li><strong>Create sustainable communities:</strong> Feirou facilitates the creation and management of communities, allowing consumers to connect with producers who share their interests and values.</li>
                    <li><strong>Buy and sell without intermediaries:</strong> The platform eliminates intermediaries, reducing costs and promoting fair and direct relationships between consumers and producers.</li>
                    <li><strong>Strengthen bonds beyond commerce:</strong> Besides the commercialization of products, Feirou facilitates meaningful connections and mutual support within communities.</li>
                    <li><strong>Collectively determine the rules and norms of participation:</strong> Communities have the autonomy to define their own regulations, schedules and places for delivery, prices and payment methods.</li>
                </ul>

                <h3 style={{ color: '#444' }}>Producer</h3>
                <ul style={{ lineHeight: '1.9' }}>
                    <li><strong>Optimize your sales:</strong> Feirou organizes the offer and distribution of products in a fair and efficient manner through smart association methods.</li>
                    <li><strong>Offer to multiple communities:</strong> Producers can offer their products to multiple communities without the need to separate specific stocks for each.</li>
                </ul>

                <h3 style={{ color: '#444' }}>Consumer</h3>
                <ul style={{ lineHeight: '1.9' }}>
                    <li><strong>Strengthen local production:</strong> By purchasing directly from local producers, you support your region's economy and promote sustainability.</li>
                    <li><strong>Expand your access:</strong> Participate in various communities, allowing flexibility and variety in your purchases.</li>
                </ul>

                <h2 style={{ color: '#444' }}>Objectives</h2>
                <ul style={{ lineHeight: '1.9' }}>
                    <li><strong>Enhance Local Supply Chains:</strong> Eliminate intermediaries; reduce the cost of products and allow a non-competitive distribution logic, i.e., ensure equal opportunities between producers and for consumers.</li>
                    <li><strong>Increase Food Security and Nutrition:</strong> Ensure that more people have continuous access to locally produced food and encourage the consumption of surplus production.</li>
                    <li><strong>Promote Agroecology:</strong> Enable consumer awareness of production processes, promoting sustainable choices through the closeness between consumers and producers.</li>
                </ul>

                <h2 style={{ color: '#444' }}>How It Works</h2>
                <h3 style={{ color: '#555' }}>Step 1: Communities Formation</h3>
                <p style={{ lineHeight: '1.9' }}>
                    Producers and consumers freely register on the platform, while administrators create communities and invite producers and consumers to join. Administrators, producers, and consumers are allowed to participate in as many communities as they want.
                </p>
                <h3 style={{ color: '#555' }}>Step 2: Community Management</h3>
                <p style={{ lineHeight: '1.9' }}>
                    Each community, with the aid of Feirou for organization, defines its own rules of participation, deadlines, and places of delivery, price lists, and payment methods.
                </p>
                <h3 style={{ color: '#555' }}>Step 3: Product Offerings</h3>
                <p style={{ lineHeight: '1.9' }}>
                    Producers freely offer their products, setting a validity period for the offer. Feirou organizes all offers and automatically manages the distribution of stock.
                </p>
                <h3 style={{ color: '#555' }}>Step 4: Placement of Orders</h3>
                <p style={{ lineHeight: '1.9' }}>
                    Feirou organizes a catalog of offers for each community. Consumers place individual orders, choosing specific products or allowing for an automatic selection, which encourages the consumption of surplus products.
                </p>
                <h3 style={{ color: '#555' }}>Step 5: Order Determination</h3>
                <p style={{ lineHeight: '1.9' }}>
                    Feirou determines which producer will fulfill each order item, through a simple and auditable distribution algorithm, ensuring transparency in the product selection and distribution process.
                </p>
                <h3 style={{ color: '#555' }}>Step 6: Logistics of Delivery</h3>
                <p style={{ lineHeight: '1.9' }}>
                    Producers harvest and deliver fresh food on the defined day, time, and place. Options for consumers to pick up the food on-site or receive it at home are set according to community rules.
                </p>

                <h2 style={{ color: '#444' }}>About Feirou</h2>
                <p style={{ lineHeight: '1.9' }}>
                    Feirou has been developed over several years with both direct and indirect collaboration from many people. The idea for the platform was inspired by the Community-Supported Agriculture (CSA) model and experiences of this type in São Carlos-Brazil, in the CSA São Carlos/Abirú and Assis-Brasil in the Curihorta/APROA projects.
                </p>
                <p style={{ lineHeight: '1.9' }}>
                    The platform is being developed by:
                </p>
                <ul style={{ lineHeight: '1.9' }}>
                    <li>Luiz Henrique B. Bertolucci (Brazil): Main creator of Feirou concept and programmer.</li>
                    <li>Nicolás Hatcher (Germany): Programmer and technology coordinator of the project.</li>
                    <li>Carlos Andreassa (Brazil): Responsible for the development of the interface (UI/UX).</li>
                </ul>

                <p style={{ lineHeight: '1.9' }}>
                Development can be followed through our platform at https://app.feirou.org and our repository at https://github.com/nhatcher/feirou.
                </p>

                <h2 style={{ color: '#444' }}>Contact</h2>
                <p style={{ lineHeight: '1.9' }}>
                    Contact us through the email contact@feirou.org.
                </p>
            </div>
        </div>
    );
};

export default FeirouPage;
