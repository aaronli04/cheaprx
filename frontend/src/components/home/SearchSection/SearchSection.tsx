'use client'
import React, { useState, useEffect } from 'react'
import classes from './SearchSection.module.css'
import { Input } from '@mantine/core'
import { CiSearch } from "react-icons/ci"

const SearchSection = () => {
    const [medication, setMedication] = useState('')

    useEffect(() => {
        console.log(medication)
    })

    return (
        <div className={classes.liner}>
            <div className={classes.searchSection}>
                <Input
                    leftSection={<CiSearch size={20} color="black"/>}
                    classNames={{
                        wrapper: classes.wrapper,
                        input: classes.input,
                    }}
                    placeholder="Enter a medication"
                    onChange={(event) => setMedication(event.target.value)}
                />
            </div>
        </div>
    )
}

export default SearchSection