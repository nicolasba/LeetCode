class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
    
        # First attempt with assumption that first val in original is 0
        # Deduce all following original values from this assumption
        # At the end, the last deduction, should come back to the initial value
        # Otherwise contradiction
        original_val_at_i = 0
        original_val_at_0 = 0

        for i in range(len(derived)):
            # Using fact that derived[i] = original[i] ⊕ original[i + 1] -> original[i + 1] = derived[i] ⊕ original[i]
            original_val_at_i_plus_1 = derived[i] ^ original_val_at_i
            original_val_at_i = original_val_at_i_plus_1

            if i == len(derived) - 1:
                if original_val_at_i_plus_1 == original_val_at_0:
                    return True
        
        # Second attempt with assumption that first val in original is 1
        original_val_at_i = 1
        original_val_at_0 = 1
        for i in range(len(derived)):
            original_val_at_i_plus_1 = derived[i] ^ original_val_at_i
            original_val_at_i = original_val_at_i_plus_1

            if i == len(derived) - 1:
                if original_val_at_i_plus_1 == original_val_at_0:
                    return True

        return False
