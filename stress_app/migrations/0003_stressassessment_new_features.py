from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [('stress_app', '0002_psychologist')]
    operations = [
        migrations.AddField(model_name='stressassessment', name='screen_time', field=models.IntegerField(default=0)),
        migrations.AddField(model_name='stressassessment', name='deadline_pressure', field=models.IntegerField(default=0)),
        migrations.AddField(model_name='stressassessment', name='mood_level', field=models.IntegerField(default=5)),
        migrations.AddField(model_name='stressassessment', name='anxiety_level', field=models.IntegerField(default=0)),
        migrations.AddField(model_name='stressassessment', name='concentration_difficulty', field=models.IntegerField(default=0)),
        migrations.AddField(model_name='stressassessment', name='attendance_percentage', field=models.IntegerField(default=0)),
        migrations.AddField(model_name='stressassessment', name='study_life_balance', field=models.IntegerField(default=5)),
        migrations.AddField(model_name='stressassessment', name='emotional_support', field=models.IntegerField(default=5)),
        migrations.AddField(model_name='stressassessment', name='fatigue_level', field=models.IntegerField(default=0)),
        migrations.AddField(model_name='stressassessment', name='relaxation_time', field=models.IntegerField(default=0)),
        migrations.AddField(model_name='stressassessment', name='stress_score', field=models.FloatField(default=0)),
    ]
