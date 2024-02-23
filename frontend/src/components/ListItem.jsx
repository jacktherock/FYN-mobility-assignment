import React from 'react'

const ListItem = ({ itemName, itemValue }) => {
    return (
        <div className='flex items-center justify-between mb-1'>
            <span> {itemName} </span>
            <p className='font-semibold shadow-inner shadow-[#ED7D31]-300 rounded-md px-5 max-w-40 w-36 text-end bg-[#F4EEFF] break-words capitalize'>{itemValue}</p>
        </div>
    )
}

export default ListItem