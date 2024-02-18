import { Medication } from "@/utils/types/medication";
import { getMatchingMedications } from "./medicationApi";

const useMedications = () => {

    const getMedications = async (medicationName: string): Promise<Medication[] | null> => {
        if (!medicationName) { return null }
        const medications = await getMatchingMedications(medicationName)
        return medications
    }

    return {
        getMedications
    }

}

export default useMedications