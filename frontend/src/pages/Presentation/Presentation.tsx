import React from 'react';
import { Grid, Paper, Typography } from "@mui/material";

const FeirouPage: React.FC = () => {
    return (
        <Paper style={{ padding: '20px' }}>
            <Grid container spacing={3}>
                <Grid item xs={12}>
                    <Typography variant="h1">Feirou</Typography>
                    <Typography>
                        Introducing Feirou, a free and open-source platform designed to facilitate direct connections between consumers and producers, particularly rural and local producers. Feirou is based on the creation of communities encompassing both consumers and producers, simplifying and organizing the buying and selling processes in a fairer and more beneficial manner for everyone.
                    </Typography>
                </Grid>

                <Grid item xs={12}>
                    <Typography variant="h3">Communities</Typography>
                    <ul>
                        <li>Create sustainable communities: Feirou facilitates the creation and management of communities, allowing consumers to connect with producers who share their interests and values.</li>
                        <li>Buy and sell without intermediaries: The platform eliminates middlemen, reducing costs and promoting fair and direct relationships between consumers and producers.</li>
                        <li>Strengthen bonds beyond commerce: Besides the commercialization of products, Feirou facilitates meaningful connections and mutual support within communities.</li>
                        <li>Collectively determine the rules and norms of participation: Communities have the autonomy to define their own regulations, schedules, and places of delivery, prices, and payment methods.</li>
                    </ul>
                </Grid>

                <Grid item xs={12}>
                    <Typography variant="h3">Producer</Typography>
                    <ul>
                        <li>Optimize your sales: Feirou organizes the offer and distribution of products in a fair and efficient manner through smart association methods.</li>
                        <li>Offer to multiple communities: Producers can offer their products to multiple communities without the need to separate specific stocks for each.</li>
                    </ul>
                </Grid>

                <Grid item xs={12}>
                    <Typography variant="h3">Consumer</Typography>
                    <ul>
                        <li>Strengthen local production: By purchasing directly from local producers, you support your region's economy and promote sustainability.</li>
                        <li>Expand your access: Participate in various communities, allowing flexibility and variety in your purchases.</li>
                    </ul>
                </Grid>

                <Grid item xs={12}>
                    <Typography variant="h2">Objectives</Typography>
                    <ul>
                        <li>Enhance Local Supply Chains: Eliminate intermediaries; reduce the cost of products and allow a non-competitive distribution logic, i.e., ensure equal opportunities for producers and consumers.</li>
                        <li>Increase Food Security and Nutrition: Ensure that more people have continuous access to locally produced food and encourage the consumption of surplus production.</li>
                        <li>Promote Agroecology: Enable consumer awareness of production processes, promoting sustainable choices through the closeness between consumers and producers.</li>
                    </ul>
                </Grid>

                <Grid item xs={12}>
                    <Typography variant="h2">How It Works</Typography>
                    <Typography variant="h3">Step 1: Formation of Communities</Typography>
                    <Typography>Producers and consumers freely register on the platform, while administrators create communities and invite producers and consumers to join. Administrators, producers, and consumers are allowed to participate in several communities at the same time.</Typography>

                    <Typography variant="h3">Step 2: Community Management</Typography>
                    <Typography>Each community, with the aid of Feirou for organization, defines its own rules of participation, deadlines, and places of delivery, price lists, and payment methods.</Typography>

                    <Typography variant="h3">Step 3: Product Offerings</Typography>
                    <Typography>Producers freely offer their products, setting a validity period for the offer. Feirou organizes all offers and automatically manages the distribution of stock.</Typography>

                    <Typography variant="h3">Step 4: Placement of Orders</Typography>
                    <Typography>Feirou organizes a catalog of offers for each community. Consumers place individual orders, choosing specific products or allowing for an automatic selection, which encourages the consumption of surplus products.</Typography>

                    <Typography variant="h3">Step 5: Order Determination</Typography>
                    <Typography>Feirou determines which producer will fulfill each order item, through a simple and auditable distribution algorithm, ensuring transparency in the product selection and distribution process.</Typography>

                    <Typography variant="h3">Step 6: Logistics of Delivery</Typography>
                    <Typography>Producers harvest and deliver fresh food on the defined day, time, and place. Options for consumers to pick up the food on-site or receive it at home are set according to community rules.</Typography>
                </Grid>

                <Grid item xs={12}>
                    <Typography variant="h2">About Feirou</Typography>
                    <Typography>Feirou has been developed over several years with both direct and indirect collaboration from many people. The idea for the platform was inspired by the Community-Supported Agriculture (CSA) model and experiences of this type in São Carlos-Brazil, in the CSA São Carlos/Abirú and Assis-Brasil in the Curihorta/APROA projects.</Typography>
                    <Typography>The platform is being developed by:</Typography>
                    <ul>
                        <li>Luiz Henrique B. Bertolucci (Brazil): Principal creator of the project and systems programmer.</li>
                        <li>Nicolás Hatcher (Germany): Programmer and technology coordinator of the project.</li>
                        <li>Carlos Andreassa (Brazil): Responsible for the development of the interface (UI/UX).</li>
                    </ul>
                </Grid>

                <Grid item xs={12}>
                    <Typography variant="h2">Contact</Typography>
                    <Typography>Contact us through the email contact@feirou.org.</Typography>
                </Grid>
            </Grid>
        </Paper>
    );
};

export default FeirouPage;