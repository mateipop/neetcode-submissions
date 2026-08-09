# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Inițializăm variabila start cu capul listei
        start = head
        # Variabila current primește valoarea lui start
        current = start
        
        # Creăm dicționarul pentru a stoca nodurile vizitate
        visited_nodes = {}

        # Bucla care iterează prin listă
        while current is not None:
            # Verificăm dacă nodul (obiectul în sine) este deja în dicționar
            if current in visited_nodes:
                return True
            
            # Stocăm nodul în dicționar (folosim nodul ca cheie)
            visited_nodes[current] = current.val
            
            # Trecem la următorul nod
            current = current.next
            
        # Dacă am ajuns la finalul listei (None), nu există ciclu
        return False

        