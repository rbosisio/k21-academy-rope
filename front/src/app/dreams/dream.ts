export interface Dream {
    dreamer_name: string;
    dreamer_age: string;
    dreamer_address: string;
    dreamer_health_conditions: string;
    contact_name: string;
    contact_email: string;
    contact_phone: string;
    contact_liason: string;
    inmate: boolean;
    local: string;
    local_name: string;
    local_address: string;
    local_phone: string;
    medical_approved: boolean;
    parental_approved: boolean;
    description: string;
    planning_description: string;
    dream_needs: string;
    needs_attended: string;
    status?: string;
    category?: string;
    dream_nickname: string;
    dream_short_description: string;
}

