import React from 'react';
import ListItem from './ListItem';

const PricingList = ({ pricingConfigurations }) => {

    const formatTimestamp = (timestamp) => {
        const date = new Date(timestamp);
        const formattedDate = date.toLocaleDateString('en-GB');
        const formattedTime = date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
        return `${formattedDate} ${formattedTime}`;
    };

    return (
        <div>
            <h2 className='font-bold text-3xl text-center pb-5'>Pricing Configurations</h2>
            <div className='grid grid-cols-4 gap-5 mx-4'>
                {pricingConfigurations.map((item) => (
                    <div key={item.id} className='border shadow-lg p-4 rounded-xl bg-[#DCD6F7]'>
                        <ListItem itemName="Distance Base Price" itemValue={item.distance_base_price} />
                        <ListItem itemName="Distance Additional Price" itemValue={item.distance_additional_price} />
                        <ListItem itemName="Time Multiplier Factor" itemValue={item.time_multiplier_factor} />
                        <ListItem itemName="Waiting Charges" itemValue={item.waiting_charges} />
                        <ListItem itemName="Day of Week" itemValue={item.day_of_week} />
                        <ListItem itemName="Min Distance" itemValue={item.min_distance} />
                        <ListItem itemName="Max Distance" itemValue={item.max_distance} />
                        <ListItem itemName="Price" itemValue={item.calculated_price} />
                        <ListItem itemName="User" itemValue={item.created_by} />
                        <ListItem itemName="Timestamp" itemValue={formatTimestamp(item.created_at)} />
                    </div>
                ))}
            </div>
        </div>
    );
};

export default PricingList;
