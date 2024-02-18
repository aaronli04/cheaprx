'use client'
import React, { useState, useEffect } from 'react'
import classes from './SearchSection.module.css'
import { Input, Button } from '@mantine/core'
import { CiSearch } from "react-icons/ci"
import { Medication } from '@/utils/types/medication'
import useMedications from '../../../hooks/medication/useMedications'
import ResultCard from '../ResultCard/ResultCard'

const SearchSection = () => {
    const { getMedications } = useMedications()
    const [medication, setMedication] = useState('')
    const [medications, setMedications] = useState<Medication[]>([])

    const fetchData = async () => {
        const medicationsData = await getMedications(medication)
        console.log(medicationsData)
        if (medicationsData) {
            setMedications(medicationsData)
        }
    }

    const handleSearch = () => {
        fetchData()
    }

    const handleKeyPress = (event: any) => {
        if (event.key === 'Enter') {
            fetchData()
        }
    }

    const handleChange = (event: any) => {
        setMedication(event.target.value)
    }

    return (
        <div className={classes.liner}>
            <div className={classes.searchSection}>
                <Input
                    leftSection={<CiSearch size={20} color="black" />}
                    classNames={{
                        wrapper: classes.wrapper,
                        input: classes.input,
                    }}
                    placeholder="Enter a medication"
                    onChange={handleChange}
                    onKeyPress={handleKeyPress}
                />
                <Button
                    classNames={{
                        root: classes.buttonRoot,
                    }}
                    onClick={handleSearch}
                >
                    Search
                </Button>
            </div>
            <div className={classes.resultsSection}>
                {medications.map((medicationItem, index) => (
                    <div key={index}>
                        <ResultCard {...medicationItem} />
                    </div>
                ))}
            </div>
        </div>
    )
}

export default SearchSection