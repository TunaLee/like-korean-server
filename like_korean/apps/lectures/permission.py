from rest_framework.permissions import BasePermission



class UnitsPermission(BasePermission):
    def has_permission(self, request, view):
        grade, profile = Profile.objects.get_grade_profile(club_id=obj.club.id, user=request.user)

        if view.action in ['board_group_board']:
            return profile.club_board_permission

        elif view.action in ['board_group_merge']:
            return obj.merge_permission <= grade

        elif view.action in ['board_group_order']:
            return True
        # Todo 나머지 로직 추가
        return True


class BoardPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        grade, profile = Profile.objects.get_grade_profile(club_id=obj.club.id, user=request.user)

        if view.action in ['board_post']:
            return obj.write_permission <= grade

        elif view.action in ['partial_update']:
            return profile.club_board_permission

        elif view.action in ['board_merge']:
            return obj.merge_permission <= grade
        # Todo 나머지 로직 추가
        return True
