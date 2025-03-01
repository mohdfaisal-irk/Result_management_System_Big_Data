from mrjob.job import MRJob
from mrjob.step import MRStep

class MarksProcessing(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_marks,
                   reducer=self.reducer_calculate_averages)
        ]
    
    def mapper_get_marks(self, _, line):
        if line.startswith("Student_ID"):
            return

        data = line.split(',')
        student_id = data[0]
        marks = list(map(int, data[4:]))  
        
        yield student_id, marks

    def reducer_calculate_averages(self, student_id, marks_list):
        total_marks = [sum(marks) for marks in marks_list]
        avg_marks = sum(total_marks) / len(total_marks)
        
        yield student_id, (sum(total_marks), avg_marks)

if __name__ == '__main__':
    MarksProcessing.run()
