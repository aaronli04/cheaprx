import { Medication } from "@/utils/types/medication";

const parseMedications = (medications: any[]): Medication[] => {
    const parsedMedications: Medication[] = [];
    
    for (const medication of medications) {
        const parsedMedication: Medication = {
            name: medication.name,
            generic: medication.generic,
            link: medication.link,
            price: medication.price,
            prescriptionNeeded: medication.prescription_needed,
            strength: medication.strength,
            count: medication.count
        }
        parsedMedications.push(parsedMedication);
    }

    return parsedMedications
}

export const getMatchingMedications = async (medicationName: string): Promise<Medication[] | null> => {
    try {
        const response = await fetch(process.env.NEXT_PUBLIC_API_URL + '/api/medication', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: medicationName,
            }),
        })

        if (!response.ok) {
            const errorMessage = await response.json();
            console.error('Server error:', errorMessage.error);
            throw new Error(errorMessage.error);
        }
        const data = await response.json()
        const medications = parseMedications(data.medications)
        return medications

    } catch (error) {
        console.log(error)
    }

    return null
}